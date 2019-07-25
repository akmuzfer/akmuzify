#!/usr/bin/env python3
from io import BytesIO

from PIL import Image

from flask import Flask, request, send_file

LOGO_WIDTH_SCALE_FACTOR = 0.1

app = Flask(__name__)
logo = Image.open("images/logo.png", "r")
logo_width, logo_height = logo.size

@app.route("/api/create", methods=["POST"])
def create():
    image_file = request.files["image"]
    image = Image.open(image_file)

    image_width, image_height = image.size
    image_longer_side = max(image_width, image_height)

    resized_logo_width = int(LOGO_WIDTH_SCALE_FACTOR * image_longer_side)
    resized_logo_height = int((resized_logo_width * logo_height) / logo_width)

    resized_logo = logo.resize((resized_logo_width, resized_logo_height))

    horizontal_offset = int(image_width - resized_logo_width - 0.25 * resized_logo_width)
    vertical_offset = int(image_height - resized_logo_height - 0.25 * resized_logo_width)

    image.paste(resized_logo, (horizontal_offset, vertical_offset), mask=resized_logo)

    image_bytes = BytesIO()
    image.save(image_bytes, image.format.lower())
    image_bytes.seek(0)

    return send_file(image_bytes, mimetype=image_file.mimetype)