import base64
from PIL import Image
import io

def decode_base64_to_image(encoded_data):
    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(encoded_data)
        # Converting binary data to an image using Pillow
        image = Image.open(io.BytesIO(decoded_data))
        return image
    except Exception as e:
        return f"Error: {e}"

def main():
    # Specify the path to the file with encoded data
    input_file_path = "IMG_8563.txt"

    try:
        # Reading encoded data from a file
        with open(input_file_path, "r") as input_file:
            encoded_data = input_file.read()

        # Decoding the data and displaying the image
        decoded_image = decode_base64_to_image(encoded_data)

        # Displaying an Image Using Pillow
        decoded_image.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
