import logging

from adaptive_huffman_coding import compress, extract
from adaptive_huffman_coding.utils import show_raw_img


logging.basicConfig(level=logging.INFO)


def main():
    for filename in ('tests/images/lena_b.raw','tests/images/lena_halftone.raw','tests/images/lena.raw',
                     'tests/images/baboon_b.raw','tests/images/baboon_halftone.raw','tests/images/baboon.raw',):
        alphabet_range = (0, 255)
        dpcm = False
        compress(filename, 'compressed',
                 alphabet_range=alphabet_range, dpcm=dpcm)
        extract('compressed', 'extracted.raw',
                alphabet_range=alphabet_range, dpcm=dpcm)
        show_raw_img(filename, 'extracted.raw', size=(256, 256))


if __name__ == '__main__':
    main()
