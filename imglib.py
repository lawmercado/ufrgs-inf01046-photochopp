import numpy as np
from skimage import io
from skimage import color
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle


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
    width, height, depth = image.shape
    reshaped = np.reshape(image, (width * height, depth))

    palette = shuffle(reshaped)[:n_colors]
    labels = pairwise_distances_argmin(reshaped, palette)

    return np.reshape(palette[labels], (width, height, palette.shape[1])).astype(np.uint8)


def quantization_kmeans(image: np.ndarray, n_colors: int) -> np.ndarray:
    width, height, channels = image.shape
    reshaped = np.reshape(image, (width * height, channels))

    model = KMeans(n_clusters=n_colors)
    labels = model.fit_predict(reshaped)
    palette = model.cluster_centers_

    return np.reshape(palette[labels], (width, height, palette.shape[1])).astype(np.uint8)


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


def convolute(image: np.ndarray, kernel: np.ndarray):
    convoluted_image = np.zeros(image.shape)

    kw = np.floor(kernel.shape[0] / 2)
    kh = np.floor(kernel.shape[1] / 2)

    for y in range(kh, image.shape[1] - kh - 1):
        for x in range(kw, image.shape[0] - kw - 1):
            result = 0

            for i in range(-kh, kh + 1):
                for j in range(-kw, kw + 1):
                    result += kernel[kw + j][kh + i] * image[x - j][y - i]

            convoluted_image[x][y] = result

    return convoluted_image.astype(np.uint8)

