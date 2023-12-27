import base64
from PIL import Image
import io

def encode_image_to_base64(image_path):
    try:
        # Opening an image using Pillow
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_data = base64.b64encode(image_data).decode('utf-8')
            return encoded_data
    except Exception as e:
        return f"Error: {e}"

def save_base64_to_file(encoded_data, output_file_path):
    try:
        # We write the encoded data to a file
        with open(output_file_path, "w") as output_file:
            output_file.write(encoded_data)
        print(f"Base64 data saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    # Specify the path to your image
    image_path = "IMG_8563.JPG"

    # We encode the image in base64
    encoded_image = encode_image_to_base64(image_path)

    if "Error" in encoded_image:
        print(encoded_image)
    else:
        # Specify the path to save the encoded data
        output_file_path = "IMG_8563.txt"
        save_base64_to_file(encoded_image, output_file_path)

if __name__ == "__main__":
    main()
