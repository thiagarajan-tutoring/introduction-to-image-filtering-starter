#!/usr/bin/env python3


def test_save_image():
    from .output_image import save_image
    import numpy as np

    test_image = np.random.randint(low=0, high=255, size=(100, 100, 3))
    save_image(test_image, './test_image.jpg')
