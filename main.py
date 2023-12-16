# Image Generator 1.0.0
# Copyright ©2023 PeterKaa, all rights reserved.

from PIL import Image

def generate_image():
    while True:
        user_response = input("Do you want to generate an image? (yes/no): ").lower()

        if user_response == 'no':
            print("Exiting the program.")
            break
        elif user_response == 'yes':
            format_choice = input("Enter the image format (e.g., PNG, JPG): ").upper()

            if format_choice not in ['PNG', 'JPG']:
                print("Invalid format choice. Supported formats: PNG, JPG.")
                continue

            try:
                width = int(input("Enter the width in pixels: "))
                height = int(input("Enter the height in pixels: "))
                filename = input("Enter the filename (without extension): ")
                compression_level = int(input("Enter the compression level (0-9): "))
                color_hex = input("Enter the color of the image (HEX format): ")
            except ValueError:
                print("Invalid input. Please enter valid numeric values for width, height, and compression level.")
                continue

            image = Image.new('RGB', (width, height), color_hex)
            save_format = format_choice.lower()

            if format_choice == 'JPG':
                save_format = 'jpg'

            image.save(f"{filename}.{save_format}", quality=compression_level)
            print(f"Image generated successfully as {filename}.{save_format}")
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    generate_image()
