# # from pydrive.auth import GoogleAuth
# # from pydrive.drive import GoogleDrive
# # import os
# #
# # def authenticate_and_upload(folder_path, email, password, folder_id):
# #     # Authenticate using email and password
# #     gauth = GoogleAuth()
# #     gauth.LocalWebserverAuth()  # Creates local webserver and handles authentication.
# #     gauth.CommandLineAuth(email=email, password=password)  # Alternative: Authenticate with email and password
# #
# #     # Create GoogleDrive instance with authenticated GoogleAuth instance
# #     drive = GoogleDrive(gauth)
# #
# #     # Upload files from the given folder
# #     for file_name in os.listdir(folder_path):
# #         file_path = os.path.join(folder_path, file_name)
# #
# #         # Create a GoogleDriveFile instance with the name and folder ID
# #         drive_file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
# #
# #         # Set content of the file from local file
# #         drive_file.UploadFile(file_path)
# #
# #         print(f"File '{file_name}' uploaded successfully.")
# #
# # if __name__ == "__main__":
# #     # Get user inputs
# #     folder_path = "E:\\report_store"
# #     email = "rishii4kumar4@gmail.com"
# #     password = "IAmRish9i"
# #     folder_id = "1HI5eCpR9HLBT-eQI0hZE6H_8QpKKNwPI"
# #
# #     # Authenticate and upload
# #     authenticate_and_upload(folder_path, email, password, folder_id)
#
# # from twilio.rest import Client
# #
# # # Twilio credentials
# # account_sid = 'your_account_sid'
# # auth_token = 'your_auth_token'
# # twilio_phone_number = 'your_twilio_phone_number'
# # recipient_phone_number = 'recipient_phone_number'
# #
# # # Function to send SMS using Twilio
# # def send_sms(message):
# #     client = Client(account_sid, auth_token)
# #
# #     message = client.messages.create(
# #         body=message,
# #         from_=twilio_phone_number,
# #         to=recipient_phone_number
# #     )
# #
# #     print(f"SMS sent with SID: {message.sid}")
# #
# # # Function to check if elements in the list are integers
# # def check_elements_for_integers(lst):
# #     non_integer_elements = [str(element) for element in lst if not isinstance(element, int)]
# #
# #     if non_integer_elements:
# #         message = f"Non-integer elements found in the list: {', '.join(non_integer_elements)}"
# #         send_sms(message)
# #
# # # Example list
# # example_list = [1, 2, 'three', 4, 5]
# #
# # # Check elements for integers
# # check_elements_for_integers(example_list)
#
#
# # import datetime
# # import time
# #
# # def check_and_print():
# #     while True:
# #         current_time = datetime.datetime.now().time()
# #         if datetime.time(2, 33) <= current_time <= datetime.time(2, 34):
# #             print("Completed")
# #             break
# #         time.sleep(4)
# #
# # if __name__ == "__main__":
# #     check_and_print()
#
#
# import os
# import PyPDF4
#
#
# def add_white_page_with_name(pdf_writer, pdf_name):
#     # Create a blank white page
#     white_page = PyPDF4.pdf.PageObject.createBlankPage(width=612,
#                                                        height=792)  # Standard US Letter size (8.5 x 11 inches)
#
#     # Add the PDF name to the white page
#     white_page.mergeScaledTranslatedPage(pdf_writer.getPage(0), scale=1.5, tx=100, ty=300)
#     white_page.mergeScaledTranslatedPage(pdf_writer.getPage(0), scale=1.5, tx=100, ty=400)
#     white_page.mergeScaledTranslatedPage(pdf_writer.getPage(0), scale=1.5, tx=100, ty=500)
#
#     # Add the white page to the merged PDF
#     pdf_writer.addPage(white_page)
#
#
# def merge_pdfs(input_directory, output_filename):
#     pdf_files = [file for file in os.listdir(input_directory) if file.lower().endswith(".pdf")]
#
#     pdf_merger = PyPDF4.PdfFileMerger()
#
#     for pdf_file in pdf_files:
#         with open(os.path.join(input_directory, pdf_file), "rb") as pdf:
#             pdf_reader = PyPDF4.PdfReader(pdf)
#             add_white_page_with_name(pdf_merger, pdf_file)
#             pdf_merger.append(pdf_reader)
#
#     with open(output_filename, "wb") as output_pdf:
#         pdf_merger.write(output_pdf)
#
#
# # if __name__ == "__main__":
# #     input_dir = r"E:\pdffols"
# #     output_file = "Merged.pdf"
# #     merge_pdfs(input_dir, output_file)
# #     print(f"PDF files merged successfully into {output_file}")
#
#
# # Import the required modules
# import os
# import PyPDF2
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#
# # Define a function to create a white page with the pdf name
# def create_white_page(pdf_name):
#     # Create a canvas object
#     c = canvas.Canvas(pdf_name + "_white.pdf", pagesize=letter)
#     # Set the font and size
#     c.setFont("Helvetica", 28)
#     # Draw the pdf name at the center of the page
#     c.drawCentredString(300, 400, pdf_name)
#     # Save the canvas
#     c.save()
#
# # Define a function to merge all pdf files in a directory
# def merge_pdf_files(directory):
#     # Create a pdf writer object
#     pdf_writer = PyPDF2.PdfWriter()
#     # Loop through the files in the directory
#     for filename in os.listdir(directory):
#         # Check if the file is a pdf file
#         if filename.endswith(".pdf"):
#             # Create a white page with the pdf name
#             create_white_page(filename)
#             # Open the white page and append it to the pdf writer
#             white_page = open(filename + "_white.pdf", "rb")
#             pdf_writer.append_pages_from_reader(PyPDF2.PdfReader(white_page))
#             # Close the white page
#             white_page.close()
#             # Open the original pdf file and append it to the pdf writer
#             pdf_file = open(os.path.join(directory, filename), "rb")
#             pdf_writer.append_pages_from_reader(PyPDF2.PdfReader(pdf_file))
#             # Close the original pdf file
#             pdf_file.close()
#     # Write the merged pdf to a new file
#     with open("Merged.pdf", "wb") as output:
#         pdf_writer.write(output)
#
# # Ask the user for the directory of the pdf files
# # directory = r"E:\pdffols"
# # # Call the merge function
# # merge_pdf_files(directory)
# # # Print a success message
# # print("Merged all pdf files into Merged.pdf")
#
# import os
#
# def remove_hyphen(folder_path):
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         if os.path.isfile(file_path) and '-' in filename:
#             new_filename = filename.split('-')[0].strip() + os.path.splitext(filename)[1]
#             new_file_path = os.path.join(folder_path, new_filename)
#
#             os.rename(file_path, new_file_path)
#             print(f'Renamed: {filename} to {new_filename}')
#
# # if __name__ == "__main__":
# #     folder_path = directory
# #
# #     remove_hyphen(folder_path)
# #     print("File renaming completed.")
# import keyboard
#
# # def turn_off_capslock():
# import pyautogui
# import win32api
# import time
#
#
# def is_capslock_on():
#     # Check the state of the Caps Lock key
#     return win32api.GetKeyState(0x14) & 1
#
#
# def turn_off_capslock():
#     capslock_state = win32api.GetKeyState(0x14) & 1
#
#     if capslock_state:
#         # Press the Caps Lock key to toggle it off
#         pyautogui.press('capslock')
#         print("Caps Lock turned off")
#     else:
#         print("Caps Lock is already off")
#
#
# # Call the function
# turn_off_capslock()

# from Reading import read_below
# import pyautogui
# pyautogui.sleep(2)
# with open(r"E:\Det_img\TXT Files\Total-points.txt", 'r') as file:
#     # Read all lines from the file, strip any leading or trailing whitespace characters,
#     # and format each line as a raw string literal
#     lines = [rf'{line.strip()}' for line in file.readlines()]
# total_points = read_below(path_list=lines, sleep_time=1, text_type="Total Points")
#
#
# def convert_to_numeric(string_with_comma_and_newline):
#     # Remove comma and newline characters from the input string
#     cleaned_string = string_with_comma_and_newline.replace(',', '').replace('\n', '')
#     # Return the cleaned string
#     return cleaned_string
# print(total_points, "\n\n")
# print(convert_to_numeric(total_points), "\n\n")

import pyautogui
# from Report_PDF import add_account_page_to_pdf
# add_account_page_to_pdf(r"G:\My Drive\Completed_Points\complete_report-(2024-03-17 11;47).pdf", account_number=None, rep=1, hed="Summary", strng="ugyivifdsgy\nyfgwavhdjx\nyafcewghd\ngaewyshbd")
#
# pyautogui.sleep(2)
# print(pyautogui.position())
import time

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        mins, secs = divmod(remaining_time, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        print("\rTime Remaining:", time_display, end="", flush=True)
        time.sleep(1)

    print("\nTimer finished!")

# if __name__ == "__main__":
#     try:
#         seconds = int(input("Enter the number of seconds for the timer: "))
#         timer(seconds)
#     except ValueError:
#         print("Please enter a valid number of seconds.")

import time

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        hours, remainder = divmod(remaining_time, 3600)
        mins, secs = divmod(remainder, 60)
        time_display = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print("\rTime Remaining:", time_display, end="", flush=True)
        time.sleep(1)

    print("\nTimer finished!")

# if __name__ == "__main__":
#     try:
#         seconds = int(input("Enter the number of seconds for the timer: "))
#         timer(seconds)
#     except ValueError:
#         print("Please enter a valid number of seconds.")

import time

# ANSI escape code for blue color
BLUE = '\033[94m'
# ANSI escape code to reset color
RESET = '\033[0m'

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        hours, remainder = divmod(remaining_time, 3600)
        mins, secs = divmod(remainder, 60)
        time_display = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print("\rTime Remaining:", BLUE + time_display + RESET, end="", flush=True)
        time.sleep(1)

    print("\nTimer finished!")

# if __name__ == "__main__":
#     try:
#         seconds = int(input("Enter the number of seconds for the timer: "))
#         timer(seconds)
#     except ValueError:
#         print("Please enter a valid number of seconds.")


import time
from colorama import init, Fore, Style


def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = max(0, int(end_time - time.time()))
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        # Initialize Colorama
        init()
        def format_time(hours, minutes, seconds):
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        time_display = format_time(hours, minutes, seconds)
        colored_time_display = f"{Fore.BLUE}{Style.BRIGHT}{time_display}{Style.RESET_ALL}"
        print("\rTime Remaining:", colored_time_display, end="", flush=True)
        time.sleep(1)

    print("\nTimer finished!")

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the number of seconds for the timer: "))
        timer(seconds)
    except ValueError:
        print("Please enter a valid number of seconds.")

