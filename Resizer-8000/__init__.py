import logging
import io
from PIL import Image, UnidentifiedImageError
import azure.functions as func

def main(myblob: func.InputStream, outputblob: func.Out[bytes]):
    try:
        # Define the maximum size for the resized image
        max_size = (800, 800)

        # Load the image from the blob
        image = Image.open(myblob)

        # Check if image format is JPEG
        if image.format not in ['JPEG', 'PNG']:
            logging.info(f"Skipping non-JPEG/PNG file: {myblob.name}")
            return

        # Resize the image while maintaining aspect ratio
        image.thumbnail(max_size)

        # Save the image to a byte stream
        byte_stream = io.BytesIO()
        image.save(byte_stream, format='JPEG')

        # Set the stream position to the start
        byte_stream.seek(0)

        # Write the stream to the output blob
        outputblob.set(byte_stream.read())

    except UnidentifiedImageError:
        logging.info(f"Invalid image file: {myblob.name}")