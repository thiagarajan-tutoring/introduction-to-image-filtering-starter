import matplotlib.pyplot as plt
import numpy as np


def save_image(image, output_fp):
    """Saves `image` to file at location `output_fp`.

    Args:
        image (np.ndarray): a NumPy array corresponding to the image
        output_fp (str): a file path to save the image at

    Hint:
        When saving the image, you'll find the following functions useful:
            1. plt.imsave in Matplotlib
            2. np.clip in NumPy, especially after using the sharpening transform

    """
    plt.figure(figsize=(10, 10))
    return NotImplementedError('Function isnt completed yet.')
