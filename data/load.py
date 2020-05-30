import numpy as np
from PIL import Image


def load_image(image_fp):
    """Loads an image from a specified file path.

    Args:
        image_fp (str): Path to image file to load

    Returns:
        PIL.Image: Image loaded from file using PIL.Image class

    Hint:
        Use PIL.Image.open
    """
    return NotImplementedError('Function isnt implemented yet.')


def load_numpy_image(image_fp):
    """Loads an image from a specified file path, as a NumPy array.

    Args:
        image_fp (str): Path to image file to load

    Returns:
        np.ndarray: Image loaded from file as a NumPy array

    Hint:
        Use your implementation of `load_image` above, and find out how you can construct a NumPy
        array from a PIL Image
    """
    return NotImplementedError('Function isnt implemented yet.')
