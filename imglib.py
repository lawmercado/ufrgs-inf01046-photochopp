import numpy as np
from skimage import io
from skimage import color
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle

kernels_3x3 = {
    "gaussian": np.array(
        [[0.0625, 0.125, 0.0625],
         [ 0.125,  0.25,  0.125],
         [0.0625, 0.125, 0.0625]]
    ),
    "laplacian": np.array(
        [[ 0, -1,  0],
         [-1,  4, -1],
         [ 0, -1,  0]]
    ),
    "highpass": np.array(
        [[-1, -1, -1],
         [-1,  8, -1],
         [-1, -1, -1]]
    ),
    "prewitt_hx": np.array(
        [[-1, 0, 1],
         [-1, 0, 1],
         [-1, 0, 1]]
    ),
    "prewitt_hy": np.array(
        [[-1, -1, -1],
         [ 0,  0,  0],
         [ 1,  1,  1]]
    ),
    "sobel_hx": np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
    ),
    "sobel_hy": np.array(
        [[-1, -2, -1],
         [ 0,  0,  0],
         [ 1,  2,  1]]
    ),
}


def read(file_name: str) -> np.ndarray:
    return io.imread(file_name)


def save(file_name: str, image: np.ndarray):
    return io.imsave(file_name, image)


def is_gray_scale_image(image: np.ndarray) -> bool:
    return len(image.shape) == 2


def color_as_gray_scale(image: np.ndarray) -> np.ndarray:
    if not is_gray_scale_image(image):
        luminance = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]

        return luminance.astype(np.uint8)
    else:
        return image


def transform_h_flip(image: np.ndarray) -> np.ndarray:
    return image[:, ::-1].astype(np.uint8)


def transform_v_flip(image: np.ndarray) -> np.ndarray:
    return image[::-1].astype(np.uint8)


def quantization_random(image: np.ndarray, n_colors: int) -> np.ndarray:
    height, width, depth = image.shape
    reshaped = np.reshape(image, (width * height, depth))

    palette = shuffle(reshaped)[:n_colors]
    labels = pairwise_distances_argmin(reshaped, palette)

    return np.reshape(palette[labels], (height, width, palette.shape[1])).astype(np.uint8)


def quantization_kmeans(image: np.ndarray, n_colors: int) -> np.ndarray:
    height, width, channels = image.shape
    reshaped = np.reshape(image, (width * height, channels))

    model = KMeans(n_clusters=n_colors)
    labels = model.fit_predict(reshaped)
    palette = model.cluster_centers_

    return np.reshape(palette[labels], (height, width, palette.shape[1])).astype(np.uint8)


def get_negative(image: np.ndarray) -> np.ndarray:
    return (255 - image).astype(np.uint8)


def adjust_brightness(image: np.ndarray, brightness: int) -> np.ndarray:
    brightened_image = image.astype(np.int) + brightness
    
    brightened_image[brightened_image > 255] = 255
    brightened_image[brightened_image < 0] = 0

    return brightened_image.astype(np.uint8)


def adjust_contrast(image: np.ndarray, contrast: float) -> np.ndarray:
    contrasted_image = image.astype(np.int) * contrast

    contrasted_image[contrasted_image > 255] = 255
    contrasted_image[contrasted_image < 0] = 0

    return contrasted_image.astype(np.uint8)


def get_histogram(image: np.ndarray) -> np.ndarray:
    histogram = np.zeros(256)

    luminance = image if is_gray_scale_image(image) else color_as_gray_scale(image)

    for x in range(0, luminance.shape[0]):
        for y in range(0, luminance.shape[1]):
            histogram[luminance[x][y]] += 1

    return histogram


def render_histogram(histogram: np.ndarray) -> np.ndarray:
    import matplotlib.pyplot as plt

    figure = plt.figure(figsize=(5, 3), dpi=100)
    plt.bar(x=list(range(0, 256)), height=histogram/np.max(histogram), color="blue")
    plt.xlim((-10, 265))
    plt.xlabel("Value", fontsize="small")
    plt.ylabel("Number of pixels\n(1:%d)" % np.max(histogram), fontsize="small")
    plt.xticks([0, 50, 100, 150, 200, 250, 255], [0, 50, 100, 150, 200, 250, ""])
    plt.tight_layout()

    figure.canvas.draw()

    data = np.fromstring(figure.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(figure.canvas.get_width_height()[::-1] + (3,))

    plt.close()

    return data


def cumulative_histogram(image: np.ndarray) -> np.ndarray:
    cum_histogram = np.zeros(256)
    alpha = 255 / (image.shape[0] * image.shape[1])

    # Computes the cumulative histogram, also normalizes it again
    histogram = get_histogram(image)
    cum_histogram[0] = alpha * histogram[0]
    for i in range(1, 256):
        cum_histogram[i] = cum_histogram[i - 1] + alpha * histogram[i]

    return cum_histogram


def histogram_equalization(image: np.ndarray) -> np.ndarray:
    equalized_image = np.zeros(image.shape)

    cum_histogram = cumulative_histogram(image)

    # Use the cumulative histogram as eq. function
    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            # If we are dealing with colored images, another loop must be done (to access the channel)
            if not is_gray_scale_image(image):
                for c in range(0, image.shape[2]):
                    equalized_image[x][y][c] = cum_histogram[image[x][y][c]]
            else:
                equalized_image[x][y] = cum_histogram[image[x][y]]

    return equalized_image.astype(np.uint8)


def lab_histogram_equalization(rgb_image: np.ndarray) -> np.ndarray:
    lab_image = color.rgb2lab(rgb_image)

    # Scaling to be in range of 0-255, original is 0-100
    lab_image[:, :, 0] = lab_image[:, :, 0] * 255/100
    lab_image[:, :, 1] = lab_image[:, :, 1] + 128
    lab_image[:, :, 2] = lab_image[:, :, 2] + 128
    lab_image = lab_image.astype(np.uint8)

    lab_equalized_image = np.copy(lab_image).astype(np.float64)

    cum_histogram = cumulative_histogram(lab_image[:, :, 0].reshape((lab_image.shape[0], lab_image.shape[1])))

    # Use the cumulative histogram as eq. function
    for x in range(0, lab_image.shape[0]):
        for y in range(0, lab_image.shape[1]):
            lab_equalized_image[x][y][0] = cum_histogram[lab_image[x][y][0]]

    lab_equalized_image[:, :, 0] = lab_equalized_image[:, :, 0] * 100 / 255
    lab_equalized_image[:, :, 1] = lab_equalized_image[:, :, 1] - 128
    lab_equalized_image[:, :, 2] = lab_equalized_image[:, :, 2] - 128

    return (color.lab2rgb(lab_equalized_image) * 255).astype(np.uint8)


def histogram_match(image: np.ndarray, reference: np.ndarray) -> np.ndarray:
    image = color_as_gray_scale(image)
    reference = color_as_gray_scale(reference)

    matched = np.zeros(image.shape)

    cum_histogram_image = cumulative_histogram(image)
    cum_histogram_ref = cumulative_histogram(reference)

    hm = np.zeros(256)

    for i in range(0, 256):
        closest = 0
        difference = np.abs(cum_histogram_ref[0] - cum_histogram_image[i])

        for j in range(1, 256):
            if np.abs(cum_histogram_ref[j] - cum_histogram_image[i]) < difference:
                closest = j
                difference = np.abs(cum_histogram_ref[j] - cum_histogram_image[i])

        hm[i] = closest

    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            matched[x][y] = hm[image[x][y]]

    return matched.astype(np.uint8)


def zoom_out(image: np.ndarray, sx: int, sy: int) -> np.ndarray:
    zoomed_image = np.zeros((np.ceil(image.shape[0] / sy).astype(np.int),
                             np.ceil(image.shape[1] / sx).astype(np.int),
                             image.shape[2]))

    i = j = 0

    for x in range(0, image.shape[1], sx):
        for y in range(0, image.shape[0], sy):
            zoomed_image[j][i] = np.mean(image[y:y+sy, x:x+sx], axis=(0, 1))
            j += 1

        i += 1
        j = 0

    return zoomed_image.astype(np.uint8)


def zoom_in(image: np.ndarray) -> np.ndarray:
    zoomed_image = np.zeros((image.shape[0] + image.shape[0] - 1,
                             image.shape[1] + image.shape[1] - 1,
                             image.shape[2]))

    i = j = 0

    # Zoomed image will have blank lines/columns between them
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            zoomed_image[j][i] = image[y][x]
            j += 2

        i += 2
        j = 0

    for y in range(0, zoomed_image.shape[0], 2):
        for x in range(0, zoomed_image.shape[1] - 2, 2):
            mean = (zoomed_image[y][x] + zoomed_image[y][x + 2])/2
            zoomed_image[y][x + 1] = mean

    for x in range(0, zoomed_image.shape[1]):
        for y in range(0, zoomed_image.shape[0] - 2, 2):
            mean = (zoomed_image[y][x] + zoomed_image[y + 2][x])/2
            zoomed_image[y + 1][x] = mean

    return zoomed_image.astype(np.uint8)


def rotate_cw(image: np.ndarray) -> np.ndarray:
    rotated_image = np.zeros((image.shape[1], image.shape[0], image.shape[2]))

    for x in range(0, image.shape[1]):
        rotated_image[x] = image[::-1, x]

    return rotated_image.astype(np.uint8)


def rotate_ccw(image: np.ndarray) -> np.ndarray:
    rotated_image = np.zeros((image.shape[1], image.shape[0], image.shape[2]))

    for y in range(0, image.shape[0]):
        rotated_image[:, y] = image[y, ::-1]

    return rotated_image.astype(np.uint8)


def convolute(image: np.ndarray, kernel: np.ndarray, add=0):
    image = image if is_gray_scale_image(image) else color_as_gray_scale(image)

    convoluted_image = np.zeros(image.shape)

    kh = np.floor(kernel.shape[0] / 2).astype(np.int)
    kw = np.floor(kernel.shape[1] / 2).astype(np.int)

    for y in range(kh, image.shape[0] - kh):
        for x in range(kw, image.shape[1] - kw):
            result = 0

            for i in range(-kh, kh + 1):
                for j in range(-kw, kw + 1):
                    result += kernel[kh + i][kw + j] * image[y - i][x - j]

            convoluted_image[y][x] = result

    convoluted_image = convoluted_image + add
    convoluted_image[convoluted_image > 255] = 255
    convoluted_image[convoluted_image < 0] = 0

    return convoluted_image.astype(np.uint8)

