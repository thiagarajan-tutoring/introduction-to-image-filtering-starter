import numpy as np
from scipy import signal

FAST = True


def get_mean_filter(kernel_size):
    """Computes a mean filter for the given `kernel_size`.

    Args:
        kernel_size (Tuple[int]): a tuple of integers describing the filter size

    Returns:
        np.ndarray: A NumPy array with the corresponding mean filter
    """
    return NotImplementedError('Function isnt implemented yet.')


def get_gaussian_filter(kernel_size, sigma=1.0):
    """Computes a Gaussian (Normal) filter for the given `kernel_size` and `sigma` value.

    Args:
        kernel_size (Tuple[int]): a tuple of integers describing the filter size
        sigma (float, optional): the sigma parameter for the Gaussian distribution. Defaults to 1.0.
    """
    return NotImplementedError('Function isnt implemented yet.')


def pad(image, filter):
    """Returns a padded version of `image` so that cross-correlating with `filter` will return the
    same size image.

    Args:
        image (np.ndarray): a NumPy array corresponding to the image to be padded
        filter (np.ndarray): the filter to be used for cross-correlation

    Returns:
        np.ndarray: a padded image to properly cross-correlate with `filter` and return the same
            size as the original image
    """
    return NotImplementedError('Function isnt implemented yet.')

def cross_correlate_2d(image, filter):
    """Performs a 2D cross-correlation.

    Args:
        image (np.ndarray): the image to be used for cross-correlation
        filter (np.ndarray): the filter to be used for cross-correlation

    Returns:
        np.ndarray: the result of the cross-correlation. The output should be the same size as
            `image`.

    Hint:
        Look into the scipy.signal library.
    """
    return NotImplementedError('Function isnt implemented yet.')


def cross_correlate(image, filter):
    """Cross-correlates and RGB `image` with `filter`.

    Args:
        image (np.ndarray): a NumPy array for the RGB image - it must be 3D
        filter (np.ndarray): a 2D NumPy array corresponding to the filter to be used

    Returns:
        np.ndarray: the cross-correlated output. It should be the same size as `image`.

    Hint:
        Use your `cross_correlate_2d` function in a loop.
    """
    return NotImplementedError('Function isnt implemented yet.')


def mean_filter_transform(image, filter_size):
    """Performs the mean-filter transformation.

    Args:
        image (np.ndarray): the image to be cross-correlated. It must be 3D.
        filter_size (Tuple[int]): the size of the mean filter to use.

    Returns:
        np.ndarray: the mean-filtered image. It must be the same shape as the input `image`.
    """
    return cross_correlate(image, get_mean_filter(filter_size))


def gaussian_filter_transform(image, filter_size, sigma=1.0):
    """Performs the Gaussian filter transformation.

    Args:
        image (np.ndarray): the image to be cross-correlated. It must be 3D.
        filter_size (Tuple[int]): the size of the Gaussian filter to use.
        sigma (float, optional): the sigma parameter for the Gaussian distribution. Defaults to 1.0.

    Returns:
        np.ndarray: the Gaussian-filtered image. It must be the same shape as the input `image`.
    """
    return cross_correlate(image, get_gaussian_filter(filter_size, sigma=sigma))


def sharpen_transform(image, filter_size, sigma=1.0, alpha=0.2):
    """Performs the sharpening transformation.

    Args:
        image (np.ndarray): the image to be sharpened. It must be 3D
        filter_size (Tuple[int]): the size of the Gaussian filter to use for blur
        sigma (float, optional): the sigma parameter for the Gaussian distribution. Defaults to 1.0.
        alpha (float, optional): the sharpening factor. Defaults to 0.2.

    Returns:
        np.ndarray: the sharpened image. It must be the same shape as the input `image`.

    Hint:
        Recall the formula: if the Gaussian filter transform gives us a blurred image B, then we
        want S in the following formulation:
            D = I - B
            S = I + alpha * (D)
        where I corresponds to the input image
    """
    blurred_image = gaussian_filter_transform(image, filter_size, sigma=sigma)
    return NotImplementedError('Function isnt completed yet.')
