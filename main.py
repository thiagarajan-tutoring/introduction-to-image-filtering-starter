#!/usr/bin/python3
import argparse
from typing import Tuple, Union

from data import load_numpy_image
from processing import gaussian_filter_transform, mean_filter_transform, sharpen_transform
from visualization import save_image


def parse_args():
    parser = argparse.ArgumentParser(description='Introduction to Image Filtering')
    parser.add_argument('--image', required=True, type=str, help='Path to the image to process.')
    parser.add_argument(
        '--transformation', required=True, type=str, help='Transformation to apply.',
        choices=['mean', 'gaussian', 'sharpen']
    )
    parser.add_argument(
        '--output', required=True, type=str, help='Where to store the processed image.'
    )
    parser.add_argument(
        '--size', required=False, type=Union[int, Tuple[int, int]], default=3,
        help='Specification of the filter size. Defaults to 3 (i.e. 3 by 3).'
    )
    parser.add_argument(
        '--sigma', required=False, type=float, default=1.0,
        help=(
            'Specification of the sigma for any Gaussian filter used in the transformation.'
            'Defaults to 1.0.'
        )
    )
    parser.add_argument(
        '--alpha', required=False, type=float, default=0.1,
        help=(
            'Specification of the alpha for the sharpening transformation (see the formula).'
            'Defaults to 0.1.'
        )
    )
    args = parser.parse_args()
    return args


def main(args):
    input_image = load_numpy_image(args.image)

    if type(args.size) is int:
        assert args.size % 2 == 1, 'Filter size must be odd.'
        fh, fw = args.size, args.size
    else:
        assert len(args.size) == 2, 'Filter size must be 2D.'
        fh, fw = args.size
        assert fh % 2 == 1 and fw % 2 == 1, 'Filter dimensions must be odd.'

    if args.transformation == 'mean':
        output_image = mean_filter_transform(input_image, (fh, fw))
    elif args.transformation == 'gaussian':
        output_image = gaussian_filter_transform(input_image, (fh, fw), sigma=args.sigma)
    elif args.transformation == 'sharpen':
        output_image = sharpen_transform(input_image, (fh, fw), sigma=args.sigma, alpha=args.alpha)
    else:
        raise ValueError(f'Transformation {args.transformation} is invalid.')

    save_image(output_image, args.output)


if __name__ == '__main__':
    args = parse_args()
    main(args)
