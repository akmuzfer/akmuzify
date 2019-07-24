#!/usr/bin/env python3
import PIL.Image
import sys

LOGO_WIDTH_SCALE_FACTOR = 0.1

if __name__ == "__main__":
    logo = PIL.Image.open("./images/logo.png", "r")
    logo_width, logo_height = logo.size

    image = PIL.Image.open(sys.argv[1], "r")
    image_width, image_height = image.size
    image_longer_side = max(image_width, image_height)

    resized_logo_width = int(LOGO_WIDTH_SCALE_FACTOR * image_longer_side)
    resized_logo_height = int((resized_logo_width * logo_height) / logo_width)

    resized_logo = logo.resize((resized_logo_width, resized_logo_height))

    horizontal_offset = int(image_width - resized_logo_width - 0.25 * resized_logo_width)
    vertical_offset = int(image_height - resized_logo_height - 0.25 * resized_logo_width)

    image.paste(resized_logo, (horizontal_offset, vertical_offset), mask=resized_logo)
    image.save("result." + image.format.lower())
