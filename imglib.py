import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle


def color_as_gray_scale(image: np.ndarray) -> np.ndarray:
    luminance = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] \
                + 0.114 * image[:, :, 2]

    image = np.zeros(image.shape)
    image[:, :, 0] = luminance
    image[:, :, 1] = luminance
    image[:, :, 2] = luminance

    return image.astype(np.uint8)


def transform_h_flip(image: np.ndarray) -> np.ndarray:
    return np.flip(image, 1).copy().astype(np.uint8)


def transform_v_flip(image: np.ndarray) -> np.ndarray:
    return np.flip(image, 0).copy().astype(np.uint8)


def quantization_random(image: np.ndarray, n_colors: int) -> np.ndarray:
    width, height, depth = image.shape
    reshaped = np.reshape(image, (width * height, depth))

    palette = shuffle(reshaped)[:n_colors]
    labels = pairwise_distances_argmin(reshaped, palette)

    return np.reshape(palette[labels], (width, height, palette.shape[1])).astype(np.uint8)


def quantization_kmeans(image: np.ndarray, n_colors: int, sample_size: float = 0.5) -> np.ndarray:
    width, height, channels = image.shape
    reshaped = np.reshape(image, (width * height, channels))

    model = KMeans(n_clusters=n_colors)
    labels = model.fit_predict(reshaped)
    palette = model.cluster_centers_

    return np.reshape(palette[labels], (width, height, palette.shape[1])).astype(np.uint8)

