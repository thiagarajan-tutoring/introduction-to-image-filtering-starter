# import cv2
import numpy as np

def cross_correlation_2d_helper(channel, kernel):
    def get_pixel(channel, x, y):
        if x >= 0 and x < channel.shape[0]:
            if y >= 0 and y < channel.shape[1]:
                return channel[x][y]
        return 0

    newImg = np.zeros(channel.shape)
    kernelXOff = kernel.shape[0]/2
    kernelYOff = kernel.shape[1]/2

    for i in range(channel.shape[0]):
        for j in range(channel.shape[1]):
            # print("PROCESSING " + str(i) + " " + str(j))

            for x in range(kernel.shape[0]):
                for y in range(kernel.shape[1]):
                    # print('using coord:', i-(kernel.shape[0]//2)+x, j-(kernel.shape[1]//2)+y, 'with weight', kernel[x][y], 'value', get_pixel(channel, i - (kernel.shape[0]//2)+x, j-(kernel.shape[1]//2)+y))
                    #TODO: CHANGE TO PYTHON2
                    newImg[i][j] += kernel[x][y] * get_pixel(channel, i - (kernel.shape[0]//2)+x, j-(kernel.shape[1]//2)+y)
                    # print('ASSIGNED', newImg[i][j])
            if newImg[i][j] < 0:
                newImg[i][j] = 0
            if newImg[i][j] > 255:
                newImg[i][j] = 255

    return newImg


def cross_correlation_2d(img, kernel):
    '''Given a kernel of arbitrary m x n dimensions, with both m and n being
    odd, compute the cross correlation of the given image with the given
    kernel, such that the output is of the same dimensions as the image and that
    you assume the pixels out of the bounds of the image to be zero. Note that
    you need to apply the kernel to each channel separately, if the given image
    is an RGB image.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    if len(img.shape) == 3:
	output = np.zeros(img.shape)
	for chan in range(3):
		output[:,:,chan] = cross_correlation_2d_helper(img[:,:,chan], kernel)
        return output
    else:
#	print('in else')
	output = cross_correlation_2d_helper(img, kernel)
#	print('returning', output)
	return output


    # TODO-BLOCK-END


def convolve_2d(img, kernel):
    '''Use cross_correlation_2d() to carry out a 2D convolution.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    kernel = np.flipud(kernel)
    kernel = np.fliplr(kernel)
    return cross_correlation_2d(img, kernel)
    # TODO-BLOCK-END

def gaussian_blur_kernel_2d(sigma, width, height):
    '''Return a Gaussian blur kernel of the given dimensions and with the given
    sigma. Note that width and height are different.

    Input:
        sigma:  The parameter that controls the radius of the Gaussian blur.
                Note that, in our case, it is a circular Gaussian (symmetric
                across height and width).
        width:  The width of the kernel.
        height: The height of the kernel.

    Output:
        Return a kernel of dimensions width x height such that convolving it
        with an image results in a Gaussian-blurred image.
    '''
    # TODO-BLOCK-BEGIN
    ''' Computes the Gaussian kernel function for x (zero-indexed).

    Input:
        x: zero-indexed coordinate for kernel
        sigma: Gaussian blur radius parameter
    Returns:
        RBF(x; sigma)
    '''
    def kernel_fun(x, sigma):
        return np.exp(-((x**2.0)) / (2.0 * (sigma ** 2.0)))

    if ((height % 2 == 0) or (width % 2 == 0)): 
        print "Either height or width is even, returning zeros."
        return np.zeros((width, height))


    height_incr_max = (height - 1) / 2
    width_incr_max = (width - 1) / 2
    u = np.zeros([width, 1])
    v = np.zeros([height, 1])
    for dx in range(width_incr_max + 1):
        u[width_incr_max + dx] = kernel_fun(dx, sigma)
        u[width_incr_max - dx] = kernel_fun(dx, sigma)
    for dy in range(height_incr_max + 1):
        v[height_incr_max + dy] = kernel_fun(dy, sigma)
        v[height_incr_max - dy] = kernel_fun(dy, sigma)
    kernel =  (1 / (2 * np.pi * (sigma ** 2))) * np.outer(u, v)
    return kernel / kernel.sum()

def low_pass(img, sigma, size):
    '''Filter the image as if its filtered with a low pass filter of the given
    sigma and a square kernel of the given size. A low pass filter supresses
    the higher frequency components (finer details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    gbk = gaussian_blur_kernel_2d(sigma, size, size)
    return convolve_2d(img, gbk)
    # TODO-BLOCK-END

def high_pass(img, sigma, size):
    '''Filter the image as if its filtered with a high pass filter of the given
    sigma and a square kernel of the given size. A high pass filter suppresses
    the lower frequency components (coarse details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    low_pass_img = low_pass(img, sigma, size)
    return img - low_pass_img
    # TODO-BLOCK-END

def create_hybrid_image(img1, img2, sigma1, size1, high_low1, sigma2, size2,
        high_low2, mixin_ratio):
    '''This function adds two images to create a hybrid image, based on
    parameters specified by the user.'''
    high_low1 = high_low1.lower()
    high_low2 = high_low2.lower()

    if img1.dtype == np.uint8:
        img1 = img1.astype(np.float32) / 255.0
        img2 = img2.astype(np.float32) / 255.0

    if high_low1 == 'low':
        img1 = low_pass(img1, sigma1, size1)
    else:
        img1 = high_pass(img1, sigma1, size1)

    if high_low2 == 'low':
        img2 = low_pass(img2, sigma2, size2)
    else:
        img2 = high_pass(img2, sigma2, size2)

    img1 *= 2 * (1 - mixin_ratio)
    img2 *= 2 * mixin_ratio
    hybrid_img = (img1 + img2)
    return (hybrid_img * 255).clip(0, 255).astype(np.uint8)


