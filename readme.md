# Image to Base64 Converter

This project provides a simple Python script to convert image files to Base64 encoding and another script to decode the Base64 data back into an image. The scripts support various image formats, including .jpg, .png, and .webp.

## Requirements

Make sure you have the following dependencies installed before running the scripts:

- Python 3
- Pillow (PIL)

You can install Pillow using the following command:

```bash
pip install Pillow
```

## Usage

### 1. Encoding an Image to Base64

Run the `app.py` script to encode an image to Base64. Update the `image_path` variable in the `main()` function to point to the image you want to encode.

```bash
python app.py
```

The Base64-encoded data will be saved to a text file (specified by `output_file_path`).

### 2. Decoding Base64 to Image

Run the `decode.py` script to decode the Base64 data back into an image. Update the `input_file_path` variable in the `main()` function to point to the file containing the Base64 data.

```bash
python decode.py
```

The decoded image will be displayed using the Pillow library.

## Example

For demonstration purposes, the project includes an example image (`IMG_8563.JPG`). You can replace this image with your own.

## Notes

- Ensure that the image file path is correct and that you have read permissions for the file.
- The scripts have been tested with .jpg, .png, and .webp image formats. If you encounter any issues, please make sure your Pillow installation is up-to-date.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.