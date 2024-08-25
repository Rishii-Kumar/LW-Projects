# from Det_img import det_img
# from PIL import Image, ImageGrab
# import pytesseract
# import pyautogui
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # Determine the correct image paths based on detection results
#
# def read_below(path_list, sleep_time, text_type):
#     # Function to check if an image is present on the screen
#     def img_loc(file_path):
#         # Search for the target image on the screen
#         location = det_img(file_path, kt=4)
#         return location
#     def find_first_present_image(image_paths):
#         for image_path in image_paths:
#             result = det_img(image_path, code_string="print('Image Not Found')", kt=0)
#             if result is not None:
#                 print("Found Image:")
#                 print(image_path)
#                 return image_path
#         print("No image found on screen!")
#         return None
#
#     def read():
#         path = find_first_present_image(path_list)
#         print(path)
#
#         # Pause briefly
#         pyautogui.sleep(sleep_time / 2)
#
#         # Check if the image is present on the screen
#         image_location = img_loc(path)
#
#         if image_location:
#             # Get the dimensions of the detected image
#             image = Image.open(path)
#             image_width, image_height = image.size
#
#             # Capture the area just below the detected image with the same dimensions
#             screenshot = ImageGrab.grab(bbox=(
#                 image_location[0], image_location[1] + image_height, image_location[0] + image_width,
#                 image_location[1] + 2 * image_height))
#             screenshot.save(r"C:\Users\Rishi\Desktop\Python\CD Pro\screenshottt.pdf")
#             # Use Tesseract to extract text from the captured image
#             extracted_text = pytesseract.image_to_string(screenshot)
#             print(extracted_text)
#
#             # Print the extracted text
#             text = extracted_text
#             print(str(text_type))
#             print("Text: - ", text)
#             return text
#     reading_result = read()
#     return reading_result


from Det_img import det_img
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter
import pytesseract
import pyautogui
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Determine the correct image paths based on detection results

def read_below(path_list, sleep_time, text_type):
    # Function to check if an image is present on the screen
    def img_loc(file_path):
        # Search for the target image on the screen
        location = det_img(file_path, kt=4)
        return location
    def find_first_present_image(image_paths):
        for image_path in image_paths:
            result = det_img(image_path, code_string="print('Image Not Found')", kt=0)
            if result is not None:
                print("Found Image:")
                print(image_path)
                return image_path
        print("No image found on screen!")
        return None

    def read():
        path = find_first_present_image(path_list)
        print(path)

        # Pause briefly
        pyautogui.sleep(sleep_time / 2)

        # Check if the image is present on the screen
        image_location = img_loc(path)

        if image_location:
            # Get the dimensions of the detected image
            image = Image.open(path)
            image_width, image_height = image.size

            # Capture the area just below the detected image with the same dimensions
            screenshot = ImageGrab.grab(bbox=(
                image_location[0], image_location[1] + image_height, image_location[0] + image_width,
                image_location[1] + 2 * image_height))
            # Use Tesseract to extract text from the captured image
            enhancer = ImageEnhance.Contrast(screenshot)
            screenshot = enhancer.enhance(2.0)

            # Perform OCR
            extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
            print(extracted_text)

            # Print the extracted text
            text = extracted_text
            print(str(text_type))
            print("Text: - ", text)
            return text
    reading_result = read()
    return reading_result