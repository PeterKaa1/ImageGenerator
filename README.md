# Image Generator 1.0.0
# Copyright ©2023 PeterKaa, all rights reserved.

This Python script utilizes the PIL (Pillow) library to generate images based on user input. Here's a breakdown of the code:

1. The program continuously prompts the user with a yes/no question, asking if they want to generate an image.

2. If the user responds with 'no', the program exits. If the response is 'yes', the script proceeds to gather information about the desired image.

3. The user is prompted to enter the image format (PNG or JPG), and the input is converted to uppercase for validation.

4. If the chosen format is not PNG or JPG, an error message is displayed, and the user is prompted again.

5. The script then attempts to gather numeric input for width, height, compression level, and a filename (without extension). If the input is invalid, an error message is displayed, and the user is prompted again.

6. Using the Pillow library, an RGB image is created with the specified dimensions and background color (given in HEX format).

7. The script saves the generated image with the specified filename, format, and compression level.

8. The program provides feedback on the successful generation of the image, including the filename and format.

9. If the user enters an invalid response (neither 'yes' nor 'no') during the initial prompt, an error message is displayed.

10. The `if __name__ == "__main__":` block ensures that the `generate_image()` function is called when the script is executed.

In summary, this code creates a simple image generator that interacts with the user to gather specifications for image generation, creates the image accordingly, and provides feedback on the process.
