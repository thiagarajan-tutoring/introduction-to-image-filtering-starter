#!/usr/bin/env python3


def test_load_image():
    from .load import load_image
    face_image = load_image('./images/face.jpg')
    assert face_image is not None, './images/face.jpg was not loaded properly.'


def test_load_numpy_image():
    from .load import load_numpy_image
    import numpy as np
    face_image = load_numpy_image('./images/face.jpg')
    assert face_image is not None, './images/face.jpg was not loaded properly.'
    assert type(face_image) == np.ndarray, \
        './images/face.jpg was not loaded properly as Numpy array using load_numpy_image'
    assert face_image.shape == (300, 300, 3), \
        './images/face.jpg was not loaded properly - shape mismatch.'
