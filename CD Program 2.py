# pip install opencv-python
# pip install numpy
# pip install pyautogui
# pip install pyinputplus
# pip install pyperclip
# pip install colorama
# pip install traceback
# pip install pygetwindow
# pip install Pillow
# pip install PyPDF2
# pip install pygame
# pip install sys
# pip install win32gui
# pip install pywin32
# pip install reportlab
# pip install datetime
# pip install shutil
# pip install os
# pip install pytesserac

# from reportlab.lib import colors
# import datetime
# import shutil
# import pyinputplus as pyip
# import os
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# import PyPDF2
# import cv2
# import numpy as np
# import pyperclip
import random
import pyautogui
from colorama import Fore, Style
import traceback
import pygetwindow as gw
from PIL import Image, ImageGrab
from ShutDown import shutdown_computer
import sys
import win32gui
import win32con
import time
import datetime
import pytesseract
from Report_PDF import create_pdf, add_screenshot_to_pdf, add_account_page_to_pdf
from copy_delete import copy_files, delete_all_files_in_directory, open_directory_in_explorer
from Power import shutdown_computer
from Routine_run import Routine_run
from txt_file import read_last_line
from Det_img import det_img
from txt_testing import Bunch_img_det
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pyautogui.FAILSAFE = False
start_time = time.time()
final_report = ""
tab_times = 0
first = 1

def file_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            formatted_content = '{' + file_content.strip() + '}'
            result_dict = eval(formatted_content)
            return result_dict
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Replace 'your_file.txt' with the path to your file containing the dictionary
file_path = "E:\\Det_img\\TXT Files\\Accounts.txt"
All_accounts = file_to_dict(file_path)

#Accounts Management
def Manage_account(work):
    input_dict = All_accounts
    if work == "IS":    #Input Taking String
        output_strings = []
        for key, value in input_dict.items():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) else key
                val = value.split("\\")[2]
                val = val.split(".")[0]
                if num < 10:
                    output_strings.append(f'\n{num} - {val}')
                else:
                    char = chr(ord('A') + num - 10)
                    output_strings.append(f'\n{char.upper()}/{char.lower()} - {val}')
            else:
                output_strings.append(f'Invalid input: {key}')
        return ''.join(output_strings)

    elif work == "RS":  #Registered account string
        output_strings = []
        for key in input_dict.keys():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) and key.isdigit() else key
                if num < 10:
                    output_strings.append(f'{num}')
                else:
                    char = chr(ord('A') + num - 10)
                    output_strings.append(f'{char.upper()}{char.lower()}')
            else:
                output_strings.append(f'Invalid input: {key}')
        return ''.join(output_strings) + "#@*"

    elif work == "RA": #Registered Accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) and key.isdigit() else key
                output_list.append(num)
            else:
                output_list.append(f'Invalid input: {key}')
        return output_list

    elif work == "SLA": #Second level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, int):
                output_list.append(key)
        return output_list

    elif work == "FLA": #First level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, str):
                output_list.append(int(key))
        return output_list

    elif work == "ANIP": #Accounts name image path
        return list(input_dict.values())

#Shut Down
Ask_Shut_Down = None


# Report File
# Specify the directory where you want to save the PDF file
pdf_directory = "G:\\My Drive\\Report Files"
pdf_direct = "G:\\My Drive\\Completed_Points"

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time as "2023-10-13__12/01"
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H;%M")

pdf_file_path = pdf_directory + f"\\report_file-({str(formatted_datetime)}).pdf"
completed_account_pdf = pdf_direct + f"\\complete_report-({str(formatted_datetime)}).pdf"
# def create():
#     copy_files()
#     delete_all_files_in_directory()
#     create_pdf(pdf_file_path)

# Laptop search program
Cooldown_acc = []
Completed = 0
def my_program():
    try:
        #Tools
        def eliminate_duplicates(input_list):
            # Create an empty set to store unique elements
            unique_set = set()

            # Create a new list to store the elements without duplicates
            result_list = []

            # Iterate through the input list
            for item in input_list:
                # If the item is not in the set, it's unique
                if item not in unique_set:
                    # Add it to the set to mark it as seen
                    unique_set.add(item)

                    # Add it to the result list
                    result_list.append(item)

            return result_list

        def check_rewards_tab():
            rewards_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\rewards_tab_Hi.txt",
                                                      code_string="print('Rewards tab Hi button not found!')", img_name="Rewards tab")
            while rewards_tab_open_checking is None:
                time.sleep(sleep_time)
                rewards_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\rewards_tab_Hi.txt",
                                                          code_string="print('Rewards tab Hi button not found!')",
                                                          img_name="Rewards tab")
            return rewards_tab_open_checking

        def check_pointsbreakdown_tab(account_number):
            PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                      code_string="print('Points Breakdown Tab not found!')", img_name="Points Breakdown tab")
            titt = 0
            while PB_tab_open_checking is None:
                time.sleep(sleep_time)
                PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                          code_string="print('Points Breakdown Tab not found!')",
                                                          img_name="Points Breakdown tab")
                titt += 1
                if titt % 5 == 0:
                    etab = det_etab()
                    if etab is not None:
                        open_pointsbreakdown(account_number)
                        PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                             code_string="print('Points Breakdown Tab not found!')",
                                                             img_name="Points Breakdown tab")
            return PB_tab_open_checking

        # def check_points_breakdown():
        #     points_breakdown = det_img("E:\\Det_img\\points_breakdown.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown0.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown1.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown2.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown3.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown4.png",code_string='print("Points breakdown button not found!")',
        #                                img_name="Points breakdown")
        #     return points_breakdown

        def maximize_win():
            pyautogui.sleep(1)
            pyautogui.hotkey("win","up")

        def generate_random_meaningful_lines():
            try:
                import random
                import nltk
                from nltk.corpus import words

                # Get the list of English words from the NLTK corpus
                english_words = words.words()

                def generate_random_word():
                    return random.choice(english_words)

                def generate_random_words(num_words):
                    return [generate_random_word() for _ in range(num_words)]

                num_words = random.randint(1, 5)
                random_words = generate_random_words(num_words)
                ret = ""
                for word in random_words:
                    if ret == "":
                        ret = word
                    else:
                        ret = ret + " " + word
                return ret
            except Exception as e:
                generate_random_meaningful_lines()

        #Account edge profile opening
        def profile(given_account_number):
            print(Fore.BLUE + Style.BRIGHT + f"Accont Number {given_account_number}" + Style.RESET_ALL)
            # List of registered account numbers
            registered_accounts = Manage_account("RA")

            # Check if the given account number is valid
            while given_account_number not in registered_accounts:
                print("Invalid input!")
                given_account_number = int(input("Enter Number: - "))

            # Check if the account number is not 1
            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
            print(time.time())
            pyautogui.hotkey("win", "r")
            time.sleep(sleep_time/2)
            if given_account_number != 1:
                pyautogui.write(f'msedge.exe --profile-directory="Profile {str(int(given_account_number)-1)}"')
            elif given_account_number == 1:
                pyautogui.write(f'msedge.exe --profile-directory="Default"')
            time.sleep(sleep_time/4)
            pyautogui.press("enter")
            maximize_win()
            set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later2.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                        code_string="pass", img_name="Set Later Button")

        #PC Browsing
        def pc_search():
            # Generate a random search input
            search_input = generate_random_meaningful_lines()

            # Open a new browser tab
            pyautogui.hotkey("ctrl", "t")

            # Pause for a short delay
            time.sleep(sleep_time/4)

            # Type the generated search input with a random typing interval
            pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))

            # Press the 'Enter' key to initiate the search
            pyautogui.press("enter")
            pyautogui.sleep(sleep_time/2)
            # Detect if the search results have loaded by looking for specific images
            check_search = Bunch_img_det("E:\\Det_img\\TXT Files\\PC_search.txt",
                                         code_string="pass", kt=0)

            # Continue checking for search results until they are detected
            wwt = 0
            while check_search is None:
                wwt+=1
                time.sleep(sleep_time)
                check_search = Bunch_img_det("E:\\Det_img\\TXT Files\\PC_search.txt",
                                             code_string="pass", kt=0)
                etab = det_etab()
                if wwt % 5 == 0 and etab is not None and check_search is None:
                    pc_search()
                    return
                else:
                    continue
            # Wait for a short delay
            time.sleep(2)

            # Close the current browser tab
            pyautogui.hotkey("ctrl", "w")

            # Wait for a brief moment
            time.sleep(sleep_time)


        #Android Works
        #repeating image detections
        def find_searchbar():
            clk_on_srch_bar = Bunch_img_det("E:\\Det_img\\TXT Files\\Searchbar.txt", code_string="pass")
            return clk_on_srch_bar

        def find_dimensions():
            dimensions = Bunch_img_det("E:\\Det_img\\TXT Files\\Dimensions.txt",
                         code_string="print('Finding Dimension button')", img_name="Dimension Button")
            return dimensions

        def det_and_visuals():
            # Check for various visual cues indicating Android visuals are not found
            check_visual = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_visuals.txt",
                                         code_string="print('Android Visuals not found!')", kt=0,img_name=0)
            return check_visual

        def det_searched():
            check_searched = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_searched.txt",
                                           code_string="pass", kt=0, img_name="Android searched")
            return check_searched

        # Android search program
        def Open_android_visuals(account_number):
            Close_tabs()
            pyautogui.hotkey("win", "d")
            profile(account_number)
            # Display a message indicating the start of the process
            print("Opening Android Visuals...")

            # Open a new tab in the web browser
            pyautogui.hotkey("ctrl", "t")  # New tab

            # Pause briefly
            time.sleep(sleep_time/2)
            set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later2.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                        code_string="pass", img_name="Set Later Button")

            # Open the browser's element inspector (F12)
            pyautogui.press("f12")  # Inspect element

            # Pause to allow the element inspector to load
            time.sleep(sleep_time/2)

            # Find the dimensions of the web page
            dimensions = find_dimensions()

            # If dimensions are not found, keep trying until they are or until a timeout occurs
            if dimensions is None:
                while dimensions is None:
                    pyautogui.sleep(sleep_time)
                    rem_decision = Bunch_img_det("E:\\Det_img\\TXT Files\\Rem_Decision.txt",
                                                 code_string="pass", img_name="Remember my decision")
                    if rem_decision is not None:
                        rem_dec_tick = Bunch_img_det("E:\\Det_img\\TXT Files\\Remember_tick.txt",
                                                 code_string="print('Remember Decision Tick NOT FOUND!')", kt=0, img_name="Remember my decision tick")
                        while rem_dec_tick is None:
                            rem_dec_tick = Bunch_img_det("E:\\Det_img\\TXT Files\\Remember_tick.txt",
                                                 code_string="print('Remember Decision Tick NOT FOUND!')", img_name="Remember my decision tick")
                        if rem_dec_tick is not None:
                            Open_DevTools = Bunch_img_det("E:\\Det_img\\TXT Files\\Open_DevTools.txt",
                                                 code_string="print('Open DevTools Button NOT FOUND!')", img_name="Open DevTools")
                            while Open_DevTools is None:
                                Open_DevTools = Bunch_img_det("E:\\Det_img\\TXT Files\\Open_DevTools.txt",
                                                 code_string="print('Open DevTools Button NOT FOUND!')", img_name="Open DevTools")
                            if Open_DevTools is not None:
                                Android_view = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_view.txt",
                                                 code_string="print('Android View Button NOT FOUND!')", img_name="Android View Button")
                                while Android_view is None:
                                    Android_view = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_view.txt",
                                                 code_string="print('Android View Button NOT FOUND!')", img_name="Android View Button")
                    dimensions = find_dimensions()

                    # If dimensions are still not found, check if the Edge browser is open
                    if dimensions is None:
                        check_edge = det_etab()
                        Android_view = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_view.txt",
                                                     code_string="print('Android View Button NOT FOUND!')",
                                                     img_name="Android View Button")
                        # If Edge is not open, keep waiting until it is detected
                        if check_edge is None:
                            while check_edge is None:
                                pyautogui.sleep(sleep_time)
                                check_edge = det_etab()


            # Pause briefly
            pyautogui.sleep(sleep_time/2)

            # Detect the presence of an image (Samsung Galaxy S20 in this case)
            Bunch_img_det("E:\\Det_img\\TXT Files\\Samsung S20.txt", code_string="print('Image: Samsung Galaxy S20 (Not Found)')",
                            img_name="Samsung Galaxy S20")

            # Reload the web page
            # Not_now = det_img("E:\\Det_img\\Not_now.png", code_string="print('Not Now button not popped!')", img_name="Not Now Button")
            # if Not_now != None:
            #     print("Pop up closed!")
            pyautogui.hotkey("ctrl", "r")  # Reload

        def search_in_android(account_number):
            # Attempt to find the search bar element
            clk_on_srch_bar = find_searchbar()

            # Initialize a wait counter
            wait = 0

            # Print a message indicating that the search bar is being searched for
            print("Finding Searchbar...")

            # Continue searching for the search bar until it's found or a timeout occurs
            while clk_on_srch_bar is None:
                pyautogui.sleep(sleep_time)
                clk_on_srch_bar = find_searchbar()

                # If the search bar is still not found, check for specific visual cues
                if clk_on_srch_bar is None:
                    print("Checking Visuals...")

                    # Check for various visual cues indicating Android visuals are not found
                    check_visual = det_and_visuals()

                    # If specific visual cues are detected, proceed with further actions
                    if check_visual is not None:
                        wait = wait + 1
                        # Simulate clicking on specific coordinates
                        pyautogui.click(x=142, y=722)
                        pyautogui.sleep(sleep_time/2)
                        pyautogui.moveTo(x=621, y=814)
                        pyautogui.sleep(sleep_time/2)
                        pyautogui.scroll(10000)
                        time.sleep(sleep_time)

                        # Attempt to find the search bar again
                        clk_on_srch_bar = find_searchbar()

                        # If the search bar is found, break out of the loop
                        if clk_on_srch_bar is not None:
                            break
                        # If no search bar is found and the wait condition is not met, reset the wait counter
                    elif check_visual is None:
                        wait = wait - wait

                        # If no search bar is found, and we've waited for a certain number of times, proceed with reopening Android visuals
                    if wait % 3 == 0:
                        print("Reopening Android visuals...")
                        time.sleep(sleep_time)
                        Open_android_visuals(account_number)
                        pyautogui.sleep(sleep_time)
                        clk_on_srch_bar = find_searchbar()

                            # If the search bar is found after reopening Android visuals, break out of the loop
                elif clk_on_srch_bar is not None:
                    break

            # Generate a random search input
            search_input = generate_random_meaningful_lines()

            # Simulate typing the search input with random typing intervals
            pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))  # type search

            # Pause briefly
            pyautogui.sleep(sleep_time/4)

            # Simulate pressing the Enter key to perform the search
            pyautogui.press("enter")  # search
            # Pause for a duration
            time.sleep(sleep_time)
            pyautogui.moveTo(x=621, y=814)
            pyautogui.sleep(0.2)
            pyautogui.scroll(10000)
            # Simulate clicking on specific coordinates
            pyautogui.click(x=142, y=722)

            # Check for specific images to verify if the search was successful
            check_searched = det_searched()

            # Continue checking for the presence of specific images until they are detected
            check_freq = 1
            while check_searched is None:
                check_searched = det_searched()

                # If the specific images are detected, break out of the loop
                if check_searched is not None:
                    break

                # If the specific images are not detected, check for visual cues again
                elif check_searched is None:
                    print(f"Checking Visuals...{check_freq}")
                    check_freq += 1

                    # Check for specific visual cues indicating Android visuals are not found
                    check_visual = det_and_visuals()

                    # If specific visual cues are detected, proceed with further actions
                    if check_visual is not None:
                        clk_on_srch_bar = find_searchbar()

                        # If the search bar is found after checking visual cues, proceed with typing the search input and performing the search
                        if clk_on_srch_bar is not None:
                            pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))  # type search
                            pyautogui.sleep(0.25)
                            pyautogui.press("enter")  # search
                            time.sleep(sleep_time/2)
                            pyautogui.click(x=142, y=722)
                            time.sleep(sleep_time/2)
                            pyautogui.moveTo(x=621, y=814)
                            pyautogui.sleep(0.2)
                            pyautogui.scroll(10000)
                            check_searched = det_searched()
                            # If the search is successful, break out of the loop
                            if check_searched is not None:
                                break

            # Check for the presence of a "Back" button image
            back_button = Bunch_img_det("E:\\Det_img\\TXT Files\\Back_button.txt",
                          code_string="print('Back button not found!')", img_name=0)

            # Continue checking for the "Back" button until it is detected
            while back_button is None:
                back_button = Bunch_img_det("E:\\Det_img\\TXT Files\\Back_button.txt",
                              code_string="print('Back button not found!')", img_name=0)

            # Pause briefly
            pyautogui.sleep(0.25)

            # Simulate clicking on specific coordinates
            pyautogui.click(x=142, y=722)
            pyautogui.sleep(sleep_time)
            pyautogui.moveTo(x=621, y=814)
            pyautogui.sleep(0.2)
            pyautogui.scroll(10000)


        #Closing programs
        #frequent image detections
        def det_new_tab(clk=0):
            new_tab = Bunch_img_det("E:\\Det_img\\TXT Files\\New_tab.txt", code_string="pass", kt=clk)
            return new_tab

        def det_rewards_tab(clk=0):
            rewards_tab = Bunch_img_det("E:\\Det_img\\TXT Files\\Rewards_tab.txt", code_string="pass", kt=clk)
            return rewards_tab

        def det_etab():
            etab = Bunch_img_det("E:\\Det_img\\TXT Files\\Edge_tab.txt", code_string="pass", kt=0)
            return etab

        # def points_check():
        #     print("Finding Points Breakdown button...")
        #     pyautogui.moveTo(x=77, y=371)
        #     points_breakdown = check_points_breakdown()
        #     while points_breakdown is None:
        #         pyautogui.sleep(0.75)
        #         points_breakdown = check_points_breakdown()
        #     pyautogui.moveTo(x=77, y=371)

        def Points_Breakdown_Info(account_number):
            pyautogui.sleep(sleep_time)
            set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later2.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                        code_string="pass", img_name="Set Later Button")
            open_pointsbreakdown(account_number)
            pyautogui.sleep(sleep_time)
            check_pointsbreakdown_tab(account_number)
            pyautogui.sleep(sleep_time)
            print("Analysing Points Breakdown...")

            # Define file paths for point images
            pc_path_list = ["E:\\Det_img\\PC_points.png", "E:\\Det_img\\PC_points1.png", "E:\\Det_img\\PC_points2.png", "E:\\Det_img\\PC_points3.png", "E:\\Det_img\\PC_points4.png"]
            android_path_list = ["E:\\Det_img\\Android_points.png", "E:\\Det_img\\Android_points1.png", "E:\\Det_img\\Android_points3.png"]

            # Determine the correct image paths based on detection results
            def find_first_present_image(image_paths):
                for image_path in image_paths:
                    result = det_img(image_path, code_string="print('Image Not Found')", kt=0)
                    if result is not None:
                        print("Found Image:")
                        print(image_path)
                        return image_path
                print("No image found on screen!")
                return None

            # Function to check if an image is present on the screen
            def img_loc(file_path):
                # Search for the target image on the screen
                location = det_img(file_path, kt=4)
                return location
            def pc_points_first_img():
                pc_points_path = find_first_present_image(pc_path_list)
                if pc_points_path == None:
                    wait_path = 0
                    while pc_points_path is None:
                        pyautogui.sleep(sleep_time/2)
                        if wait_path > 10:
                            print("\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                            return
                        if wait_path % 5 == 0:
                            etab = det_etab()
                            if etab is None:
                                profile(account_number)
                                pyautogui.sleep(sleep_time)
                                set_later = det_img("E:\\Det_img\\Set_later1.png",
                                                    code_string="pass", img_name="Set Later Button") or det_img(
                                    "E:\\Det_img\\Set_later2.png",
                                    code_string="pass", img_name="Set Later Button") or det_img(
                                    "E:\\Det_img\\Set_later3.png",
                                    code_string="pass", img_name="Set Later Button")
                                open_pointsbreakdown(account_number)
                                check_pointsbreakdown_tab(account_number)
                                time.sleep(sleep_time/2)
                            elif etab is not None:
                                pyautogui.sleep(sleep_time/2)
                                open_pointsbreakdown(account_number)
                                check_pointsbreakdown_tab(account_number)
                                time.sleep(sleep_time/2)
                        pc_points_path = find_first_present_image(pc_path_list)
                        if pc_points_path is not None:
                            break
                        wait_path += 1
                return pc_points_path


            global prev_pc_remain, prev_and_remain, and_rep, pc_rep
            prev_pc_remain = None
            prev_and_remain = None
            and_rep = 0
            pc_rep = 0
            if account_number in Second_level_accounts:
                def and_points_first_img():
                    and_points_path = find_first_present_image(android_path_list)
                    if and_points_path == None:
                        wait_path = 0
                        while and_points_path is None:
                            pyautogui.sleep(sleep_time/2)
                            if wait_path > 10:
                                print("\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                                return
                            if wait_path % 5 == 0:
                                etab = det_etab()
                                if etab is None:
                                    profile(account_number)
                                    pyautogui.sleep(sleep_time)
                                    set_later = det_img("E:\\Det_img\\Set_later1.png",
                                                code_string="pass", img_name="Set Later Button") or det_img(
                                                "E:\\Det_img\\Set_later2.png", code_string="pass", img_name="Set Later Button") or det_img(
                                                "E:\\Det_img\\Set_later3.png", code_string="pass", img_name="Set Later Button")
                                    open_pointsbreakdown(account_number)
                                    check_pointsbreakdown_tab(account_number)
                                    time.sleep(sleep_time / 2)
                                elif etab is not None:
                                    pyautogui.sleep(sleep_time / 2)
                                    open_pointsbreakdown(account_number)
                                    check_pointsbreakdown_tab(account_number)
                                    time.sleep(sleep_time / 2)
                            and_points_path = find_first_present_image(android_path_list)
                            if and_points_path is not None:
                                break
                            wait_path += 1
                    return and_points_path
                pyautogui.sleep(sleep_time/2)

                def read():
                    global prev_pc_remain, prev_and_remain, and_rep, pc_rep, Completed
                    pc_points_path = pc_points_first_img()

                    # Pause briefly
                    pyautogui.sleep(sleep_time/2)
                    pc_points_left, android_points_left, pc_search_freq_left, android_search_freq_left = 0, 0, 0, 0

                    # Check if the image is present on the screen
                    image_location = img_loc(pc_points_path)
                    failed_pc = 0

                    if image_location:
                        # Get the dimensions of the detected image
                        image = Image.open(pc_points_path)
                        image_width, image_height = image.size

                        # Capture the area just below the detected image with the same dimensions
                        screenshot = ImageGrab.grab(bbox=(
                        image_location[0], image_location[1] + image_height, image_location[0] + image_width,
                        image_location[1] + 2 * image_height))

                        # Use Tesseract to extract text from the captured image
                        extracted_text = pytesseract.image_to_string(screenshot)
                        print(extracted_text)

                        # Print the extracted text
                        text = extracted_text
                        print("PC points details: - ")
                        print("Text: - ", text)
                        lst = text.split("/")
                        print(lst)
                        try:
                            if Server==0:
                                pc_points_left += 150 - int(lst[0])
                            elif Server==1:
                                pc_points_left += 90 - int(lst[0])
                        except:
                            print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                            pc_points_left = 0
                            failed_pc = 1

                        while pc_points_left > 0:
                            if prev_pc_remain == pc_points_left:
                                pc_rep += 1
                                if Server == 1:
                                    if pc_points_left == 90:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                    else:
                                        if pc_rep >= 2:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                elif Server == 0:
                                    if pc_points_left == 150:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                    else:
                                        if pc_rep >= 2:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                            elif prev_pc_remain != pc_points_left:
                                pc_rep = 0
                            prev_pc_remain = pc_points_left
                            pc_search()
                            #Read again
                            pc_points_path = pc_points_first_img()
                            # Check if the image is present on the screen
                            image_location = img_loc(pc_points_path)
                            failed_pc = 0
                            if image_location:
                                # Get the dimensions of the detected image
                                image = Image.open(pc_points_path)
                                image_width, image_height = image.size

                                # Capture the area just below the detected image with the same dimensions
                                screenshot = ImageGrab.grab(bbox=(
                                    image_location[0], image_location[1] + image_height,
                                    image_location[0] + image_width,
                                    image_location[1] + 2 * image_height))

                                # Use Tesseract to extract text from the captured image
                                extracted_text = pytesseract.image_to_string(screenshot)
                                print(extracted_text)
                                # Print the extracted text
                                text = extracted_text
                                print("PC points details: - ")
                                print("Text: - ", text)
                                lst = text.split("/")
                                print(lst)
                                pc_points_earned = lst[0]
                                try:
                                    if Server == 0:
                                        pc_points_left = 150 - int(lst[0])
                                    elif Server == 1:
                                        pc_points_left = 90 - int(lst[0])
                                except:
                                    print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                                    failed_pc += 1
                                    if failed_pc >= 3:
                                        failed_pc=1
                                        break
                                if pc_points_left == 0:
                                    break
                        if failed_pc == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)


                    # Check if the image is present on the screen
                    and_points_path = and_points_first_img()
                    image_location = img_loc(and_points_path)
                    failed_and = 0
                    if image_location:
                        # Get the dimensions of the detected image
                        image = Image.open(and_points_path)
                        image_width, image_height = image.size

                        # Capture the area just below the detected image with the same dimensions
                        screenshot = ImageGrab.grab(bbox=(
                        image_location[0], image_location[1] + image_height, image_location[0] + image_width,
                        image_location[1] + 2 * image_height))

                        # Use Tesseract to extract text from the captured image
                        extracted_text = pytesseract.image_to_string(screenshot)

                        print(extracted_text)
                        text = extracted_text
                        print("Android pints details: - ")
                        print(text)
                        lst = text.split("/")
                        print(lst)
                        try:
                            if Server == 0:
                                android_points_left += 100 - int(lst[0])
                            if Server == 1:
                                android_points_left += 60 - int(lst[0])
                        except:
                            print(Fore.RED + Style.BRIGHT + "Failed to read android points details!" + Style.RESET_ALL)
                            android_points_left = 0
                            failed_and = 1
                        if android_points_left == 0:
                            time.sleep(sleep_time/2)
                            add_screenshot_to_pdf(pdf_file_path)
                            add_account_page_to_pdf(completed_account_pdf, account_number)
                            add_screenshot_to_pdf(completed_account_pdf)
                            Completed = 1
                            time.sleep(sleep_time)
                        if android_points_left > 0:
                            print("Opening Android Visuals...")
                            pyautogui.sleep(sleep_time/3)
                            Open_android_visuals(account_number)
                            pyautogui.sleep(sleep_time/2)
                            open_pointsbreakdown(account_number)
                            check_pointsbreakdown_tab(account_number)
                            time.sleep(sleep_time/2)
                        while android_points_left > 0:
                            if prev_and_remain == android_points_left:
                                and_rep += 1
                                if and_rep >= 2:
                                    time_value = time.time()
                                    cool_account = [account_number, time_value]
                                    pyautogui.hotkey("ctrl", "w")
                                    for account in Cooldown_acc:
                                        if account[0] == account_number:
                                            return
                                    Cooldown_acc.append(cool_account)
                                    print(Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                    print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                    return
                            elif prev_and_remain != android_points_left:
                                and_rep = 0
                            prev_and_remain = android_points_left
                            pyautogui.hotkey('ctrl', 'shift', 'tab')
                            time.sleep(sleep_time/2)
                            search_in_android(account_number)
                            time.sleep(sleep_time/2)
                            pyautogui.hotkey('ctrl', 'tab')
                            time.sleep(sleep_time/2)
                            # Check if the image is present on the screen
                            and_points_path = and_points_first_img()
                            image_location = img_loc(and_points_path)
                            failed_and = 0
                            if image_location:
                                # Get the dimensions of the detected image
                                image = Image.open(and_points_path)
                                image_width, image_height = image.size

                                # Capture the area just below the detected image with the same dimensions
                                screenshot = ImageGrab.grab(bbox=(
                                    image_location[0], image_location[1] + image_height,
                                    image_location[0] + image_width,
                                    image_location[1] + 2 * image_height))

                                # Use Tesseract to extract text from the captured image
                                extracted_text = pytesseract.image_to_string(screenshot)
                                print(extracted_text)
                                text = extracted_text
                                print("Android pints details: - ")
                                print(text)
                                lst = text.split("/")
                                print(lst)
                                try:
                                    if Server == 0:
                                        android_points_left = 100 - int(lst[0])
                                    if Server == 1:
                                        android_points_left = 60 - int(lst[0])
                                except:
                                    print(
                                        Fore.RED + Style.BRIGHT + "Failed to read android points details!" + Style.RESET_ALL)
                                    failed_and += 1
                                    if failed_pc >= 3:
                                        failed_and = 1
                                        break
                                if android_points_left == 0:
                                    time.sleep(sleep_time/2)
                                    add_screenshot_to_pdf(pdf_file_path)
                                    add_account_page_to_pdf(completed_account_pdf, account_number)
                                    add_screenshot_to_pdf(completed_account_pdf)
                                    Completed = 1
                                    time.sleep(sleep_time)
                                    break

                        if failed_and == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)
                    return "Done"

                read()

            elif account_number in First_level_accounts:
                pyautogui.sleep(sleep_time/2)
                def read():
                    global prev_pc_remain, prev_and_remain, and_rep, pc_rep
                    pc_points_path = pc_points_first_img()

                    # Pause briefly
                    pyautogui.sleep(sleep_time/2)
                    pc_points_left, android_points_left, pc_search_freq_left, android_search_freq_left = 0, 0, 0, 0

                    # Check if the image is present on the screen
                    image_location = img_loc(pc_points_path)
                    failed_pc = 0

                    if image_location:
                        # Get the dimensions of the detected image
                        image = Image.open(pc_points_path)
                        image_width, image_height = image.size

                        # Capture the area just below the detected image with the same dimensions
                        screenshot = ImageGrab.grab(bbox=(
                        image_location[0], image_location[1] + image_height, image_location[0] + image_width,
                        image_location[1] + 2 * image_height))

                        # Use Tesseract to extract text from the captured image
                        extracted_text = pytesseract.image_to_string(screenshot)
                        print(extracted_text)

                        # Print the extracted text
                        text = extracted_text
                        print("PC points details: - ")
                        print("Text: - ", text)
                        lst = text.split("/")
                        print(lst)
                        pc_points_earned = lst[0]
                        try:
                            if Server==0:
                                pc_points_left += 50 - int(lst[0])
                            elif Server==1:
                                pc_points_left += 30 - int(lst[0])

                        except:
                            print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                            pc_points_left = 0
                            failed_pc = 1
                        if pc_points_left == 0:
                            time.sleep(sleep_time/2)
                            add_screenshot_to_pdf(pdf_file_path)
                            add_account_page_to_pdf(completed_account_pdf, account_number)
                            add_screenshot_to_pdf(completed_account_pdf)
                            Completed = 1
                            time.sleep(sleep_time/2)
                        while pc_points_left > 0:
                            if prev_pc_remain == pc_points_left:
                                pc_rep += 1
                                if Server == 1:
                                    if pc_points_left == 30:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                    else:
                                        if pc_rep >= 2:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                elif Server == 0:
                                    if pc_points_left == 50:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                    else:
                                        if pc_rep >= 2:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                            elif prev_pc_remain != pc_points_left:
                                pc_rep = 0
                            prev_pc_remain = pc_points_left
                            pc_search()
                            #Read again
                            pc_points_path = pc_points_first_img()
                            # Check if the image is present on the screen
                            image_location = img_loc(pc_points_path)
                            failed_pc = 0
                            if image_location:
                                # Get the dimensions of the detected image
                                image = Image.open(pc_points_path)
                                image_width, image_height = image.size

                                # Capture the area just below the detected image with the same dimensions
                                screenshot = ImageGrab.grab(bbox=(
                                    image_location[0], image_location[1] + image_height,
                                    image_location[0] + image_width,
                                    image_location[1] + 2 * image_height))

                                # Use Tesseract to extract text from the captured image
                                extracted_text = pytesseract.image_to_string(screenshot)
                                print(extracted_text)
                                # Print the extracted text
                                text = extracted_text
                                print("PC points details: - ")
                                print("Text: - ", text)
                                lst = text.split("/")
                                print(lst)
                                pc_points_earned =lst[0]
                                try:
                                    if Server == 0:
                                        pc_points_left = 50 - int(lst[0])
                                    elif Server == 1:
                                        pc_points_left = 30 - int(lst[0])
                                except:
                                    print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                                    failed_pc += 1
                                    if failed_pc >= 3:
                                        failed_pc=1
                                        break
                                if pc_points_left == 0:
                                    time.sleep(sleep_time/2)
                                    add_screenshot_to_pdf(pdf_file_path)
                                    add_account_page_to_pdf(completed_account_pdf, account_number)
                                    add_screenshot_to_pdf(completed_account_pdf)
                                    Completed = 1
                                    time.sleep(sleep_time/2)
                                    break
                        if failed_pc == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)

                read()

            report = "Done"
            return report

        def open_rewards_tab():
            # Close the current tab in the web browser
            pyautogui.hotkey("ctrl", "t")

            # Pause briefly
            time.sleep(sleep_time)

            # Navigate to the Bing Rewards page
            pyautogui.write("https://rewards.bing.com/  ")

            # Pause briefly
            time.sleep(sleep_time/5)

            # Press Enter to visit the URL
            pyautogui.press("enter")

            # Pause for a specified duration
            if Server==0:
                time.sleep(3)
            time.sleep(sleep_time*3)

            # Check if the rewards tab is open
            rewards_tab_open_check = check_rewards_tab()

            # Initialize a variable to track waiting time
            wait_time = 0

            # Wait until the rewards tab is detected or a timeout occurs
            while rewards_tab_open_check is None:
                time.sleep(1)
                wait_time += 1
                rewards_tab_open_check = check_rewards_tab()

                # If rewards tab is not found and a timeout occurs, perform additional checks
                if rewards_tab_open_check is None and wait_time % 8 == 0:
                    # Check if other tabs (e.g., Edge browser) are open
                    check_edge_tab = det_etab()

                    # If other tabs are detected, open the rewards tab again
                    if check_edge_tab is not None:
                        pyautogui.hotkey("ctrl", "t")
                        time.sleep(0.5)
                        pyautogui.write("https://rewards.bing.com")
                        time.sleep(0.5)
                        pyautogui.press("enter")
                        time.sleep(sleep_time*3)
                        rewards_tab_open_check = check_rewards_tab()

        def open_pointsbreakdown(account_number):
            check_edge = det_etab()
            # If Edge is not open, keep waiting until it is detected
            waits = 0
            while check_edge is None:
                waits += 1
                pyautogui.sleep(sleep_time)
                check_edge = det_etab()
                if waits % 5 == 0:
                    print(Fore.RED + Style.BRIGHT + f"Please open profile of account numbe: {account_number}" + Style.RESET_ALL)
            pyautogui.hotkey("ctrl", "t")
            pyautogui.sleep(sleep_time/4)
            pyautogui.write("https://rewards.bing.com/pointsbreakdown ")
            pyautogui.sleep(sleep_time/4)
            pyautogui.press("enter")
            pyautogui.sleep(sleep_time*3)

        def end(account_number, rep = 1):
            # Pause briefly
            time.sleep(sleep_time/ 2)

            #Add account page in pdf
            add_account_page_to_pdf(pdf_file_path, account_number, rep=rep)

            # Detailed Points Breakdown Information
            Points_Breakdown_Info(account_number)
            pyautogui.sleep(sleep_time/4)

            # Not_now = det_img("E:\\Det_img\\Not_now.png", code_string="print('Not Now button not popped!')", img_name="Not Now Button")
            # if Not_now != None:
            #     print("Pop up closed!")
            # Function to check for and collect extra points
            def extra_points():
                time.sleep(sleep_time)
                pyautogui.hotkey("ctrl", "w")
                pyautogui.sleep(sleep_time / 2)
                open_rewards_tab()
                check_rewards_tab()

                # Scroll down to check for extra points
                if Server==0:
                    for i in range(8):
                        pyautogui.scroll(-250)
                for i in range(12):
                    pyautogui.scroll(-450)
                    points_detection = Bunch_img_det("E:\\Det_img\\TXT Files\\Plus_sign.txt",
                                               code_string="print('No points available!')", img_name="Plus Sign")

                    # Wait for a specified time if sleep_time > 3, else sleep for 3 seconds
                    clk_plus = 1
                    while points_detection is not None:
                        clk_plus += 1
                        if sleep_time > 3:
                            pyautogui.sleep(sleep_time)
                        else:
                            pyautogui.sleep(3)
                        pyautogui.hotkey('ctrl', 'w')
                        if Server==0:
                            time.sleep(2)
                        time.sleep(1)
                        if clk_plus >= 10:
                            add_screenshot_to_pdf(pdf_file_path)
                            break
                        points_detection = Bunch_img_det("E:\\Det_img\\TXT Files\\Plus_sign.txt",
                                               code_string="print('No points available!')", img_name="Plus Sign")

                # Scroll up to reset scroll position
                for i in range(16):
                    pyautogui.scroll(500)

            global Completed
            if Completed == 1:
                extra_points()
                add_screenshot_to_pdf(completed_account_pdf)
                end_time = time.time()
                runtime = end_time - start_time
                runtime = float("{:.2f}".format(runtime))
                strng1 = "\n" + str(runtime) + " seconds"
                minutes = float("{:.2f}".format(runtime / 60))
                strng2 = "\n" + str(minutes) + " minutes"
                hours = float("{:.2f}".format(minutes / 60))
                strng3 = "\n" + str(hours) + " hours"
                strng = strng1 + strng2 + strng3
                add_account_page_to_pdf(completed_account_pdf, account_number=None, strng=strng, hed=f"Time Taken for Account Number: {account_number}")
            Completed = 0

            try:
                pyautogui.sleep(slp)
            except:
                pass

            # Close the new tab in the web browser
            if ask_for_tab_closing == 0:
                Close_new_tab()

        def Close_tabs():
            def close_edge_tabs():
                # Get all window titles
                window_titles = gw.getAllTitles()

                # Iterate through window titles and close Microsoft Edge tabs
                for title in window_titles:
                    if "Edge" in title:

                        # Find the window handle (hwnd) associated with the Edge tab
                        hwnd = win32gui.FindWindow(None, title)

                        # If a window handle is found
                        if hwnd:
                            # Restore the window if minimized and bring it to the foreground
                            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                            win32gui.SetForegroundWindow(hwnd)  # Activate the window
                            time.sleep(0.5)

                            # Simulate pressing Ctrl+W to close the current tab
                            pyautogui.hotkey('ctrl', 'w')
                            time.sleep(0.5)  # Wait for a moment to ensure the tab is closed

                # After closing Edge tabs, check for any remaining Edge tabs and close them recursively
                window_titles = gw.getAllTitles()
                for title in window_titles:
                    if "Edge" in title:
                        close_edge_tabs()

            def end_edge_processes():
                import psutil

                def terminate_edge_processes():
                    try:
                        for process in psutil.process_iter(['pid', 'name']):
                            if 'msedge.exe' in process.info['name'].lower():
                                print(f"Terminating Edge process with PID {process.info['pid']}")
                                psutil.Process(process.info['pid']).terminate()

                        print("All Edge processes terminated.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                if __name__ == "__main__":
                    terminate_edge_processes()

            # Call the close_edge_tabs function to close Microsoft Edge tabs
            close_edge_tabs()
            # end_edge_processes()

        def Close_new_tab():
            # Detect images to check if a new tab and rewards tab are open
            new_tab = det_new_tab(clk=0)

            rewards_tab = det_rewards_tab(clk=0)

            # Continue loop as long as both new tab and rewards tab are open
            while new_tab is not None and rewards_tab is not None:
                # If a new tab is detected, simulate closing it
                new_tab = det_new_tab(clk=1)
                if new_tab is not None:
                    pyautogui.sleep(0.1)
                    pyautogui.hotkey("ctrl", "w")  # Close the current tab
                    pyautogui.sleep(0.1)

                # Check for rewards tab again
                new_tab = det_new_tab(clk=0)

                rewards_tab = det_rewards_tab(clk=0)

        def play_music():
            import pygame
            def play_mp3(filename):
                pygame.init()
                pygame.mixer.init()
                try:
                    pygame.mixer.music.load(filename)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                except pygame.error as e:
                    print(f"Error playing {filename}: {e}")
                finally:
                    pygame.mixer.music.stop()
                    pygame.quit()

            mp3_file = "E:\\Alarm Ringtones\\beep_alarm.mp3"  # Replace with the path to your MP3 file
            # play_mp3(mp3_file)

            x = 2
            while x < -1 and x > 1:
                print(x)

        def alphabet_to_integer(char):
            if char.isalpha() and len(char) == 1:
                char = char.lower()
                return ord(char) - ord('a') + 10
            else:
                return "Invalid input: Please enter a single alphabet character."

        # Create a list to store the selected accounts
        provided_list_of_account = list(want_to_run_for_accounts)
        # Parse the selected accounts and store them in the provided_list_of_accounts list
        def account_list(input):
            output = []
            for i in input:
                if i in Manage_account("RS"):
                    try:
                        i = int(i)
                    except Exception as e:
                        i = i
                    typ = type(i)
                    if typ == int:
                        if int(i) not in output:
                            output.append(int(i))
                    elif typ == str:
                        if i in "*#@":
                            if i in "@":
                                for i in Second_level_accounts:
                                    output.append(i)
                            elif i in "#":
                                for i in First_level_accounts:
                                    output.append(i)
                            elif i in "*":
                                for i in Manage_account("RA"):
                                    output.append(i)
                        else:
                            output.append(alphabet_to_integer(i))
                else:
                    pass
            return output

        provided_list_of_accounts = account_list(provided_list_of_account)

        # Eliminate duplicates from the provided list of accounts
        provided_list_of_accounts = eliminate_duplicates(provided_list_of_accounts)

        global account_numbers_to_remove
        if account_numbers_to_remove:
            account_numbers_to_remove = list(account_numbers_to_remove)
            account_numbers_to_remove = account_list(account_numbers_to_remove)
            account_numbers_to_remove = eliminate_duplicates(account_numbers_to_remove)
            for i in account_numbers_to_remove:
                if i in provided_list_of_accounts:
                    provided_list_of_accounts.remove(i)

        print(provided_list_of_accounts)  # Print the final list of selected accounts

        a = input("Want to continue?")

        # Create a new list of customised account numbers
        list_of_customised_account_numbers = []

        # Validate the provided account numbers and add them to the list
        for i in provided_list_of_accounts:
            integer_of_provided_account = int(i)
            list_of_customised_account_numbers.append(integer_of_provided_account)

        for i in list_of_customised_account_numbers:
            profile(i)
            end(i)
            if i == 1:
                pyautogui.hotkey("win", "d")
            else:
                if ask_for_tab_closing == 1:
                    pyautogui.hotkey("alt", "f4")
                else:
                    pyautogui.hotkey("win", "d")

        def format_time(seconds):
            seconds = float("{:.2f}".format(seconds))
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60

            if hours > 0 or minutes > 0:
                return f"time remaining {int(hours)} hours {int(minutes)} minutes {int(remaining_seconds)} seconds"
            else:
                return f"time remaining {int(remaining_seconds)} seconds"

        while Cooldown_acc:
            first_cooldwon_acc = Cooldown_acc[0]
            print(Fore.MAGENTA + Style.BRIGHT + f"First Cool Down Account : {first_cooldwon_acc}" + Style.RESET_ALL)
            first_cooldwon_time = first_cooldwon_acc[1]
            print(Fore.CYAN + Style.BRIGHT + f"Time passed : {time.time() - first_cooldwon_time}")

            #Pausing if cool down time is not completed
            while time.time() - first_cooldwon_time <= cooldown_time:
                print(format_time(time.time() - first_cooldwon_time))
                time.sleep(5)

            #Creating Duplicate list Of Acoounts Having Points cooldown
            Cooldown_acc_copy = list(Cooldown_acc)

            #Extracting Account numbers from the list of lists of account number and cooldown time start time
            run_acc = []
            for acs in Cooldown_acc_copy:
                run_acc.append(acs[0]) #Adding account number to a new list
                Cooldown_acc.remove(acs) #Removing Account from main Cooldwon list
                print(Fore.LIGHTCYAN_EX + Style.NORMAL + f"{acs} removed from Cooldown Accounts list!" + Style.RESET_ALL)
            #Arranging Account numbers in ascending order
            run_acc = sorted(run_acc)
            print(Fore.BLUE + Style.BRIGHT + "Running for accounts : " + str(run_acc) + Style.RESET_ALL)
            #Starting Points collection after cool down
            for i in run_acc:
                print(run_acc)
                profile(i)
                time.sleep(sleep_time * 2)
                end(i, rep=2)
                time.sleep(sleep_time)
                if i == 1:
                    pyautogui.hotkey("win", "d")
                else:
                    if ask_for_tab_closing == 1:
                        pyautogui.hotkey("alt", "f4")
                    else:
                        pyautogui.hotkey("win", "d")
                time.sleep(sleep_time)



        # Tab Closing
        if ask_for_tab_closing == 1:
            pyautogui.sleep(sleep_time)
            Close_tabs()
        play_music()

    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error on line:", exc_tb.tb_lineno)
        sstt = str(e) + "\n" + "Error on line:" + str(exc_tb.tb_lineno)
        add_account_page_to_pdf(pdf_file_path, rep=0, account_number=None, strng=sstt)
        traceback.print_exc()
        if error_hand == 1:
            my_program()


#Work starts from here
# Define a list of second-level accounts
Second_level_accounts = Manage_account("SLA")

# Initialize an empty list for first-level accounts
First_level_accounts = Manage_account("FLA")

intruc = str("Instructions: \nPress '1' for YES & '0' for NO")
print(Fore.GREEN + Style.BRIGHT + intruc + Style.RESET_ALL)
try:
    # Ask the user for customizations (default or custom)
    Ask_Shut_Down = int(input("Want to shut down Computer after completion? (default = 0): - "))
except:
    # If input is not valid, default to running in default mode
    Ask_Shut_Down = None

#Choosing Server to run
try:
    Server = int(input("0 - USA\n1 - Indian\nChoose Server (Default-Indian): - "))
except:
    Server = 1
while Server!=1 and Server!=0:
    Server = int(input("Invalid Input!\nPlease Choose a Valid Server: - "))

if Server == 1:
    global cooldown_time
    try:
        # Ask for the time gap in search (default = 0.2 seconds)
        cooldown_time = int(input("Enter time for points cooldown (default: 900):- "))
    except Exception as e:
        # If input is not valid, use the default time gap
        cooldown_time = 900

try:
    error_hand = int(input("Want to restart after any error? (Default: 1): -"))
except:
    error_hand = 1

try:
    # Ask for the time gap in search (default = 0.2 seconds)
    sleep_time = int(input("Enter time gap in search (default = 1):- "))
except Exception as e:
    # If input is not valid, use the default time gap
    sleep_time = 1

#Profile tab closing syntax
try:
    # Ask if the user wants tianism
    # o close all tabs (default = 1, Yes)
    ask_for_tab_closing = int(input("Want to close all TABS? (default = 1): - "))
    if ask_for_tab_closing > 1:
        ask_for_tab_closing = 1
        try:
            global slp
            slp = int(input("Enter time to pause after checking extra points: - "))
        except:
            slp = 0
except Exception as e:
    # If input is not valid, default to closing all tabs
    ask_for_tab_closing = 1

# Ask the user to choose the account(s) to run the program for
IS = "Choose ACCOUNT :" + f"\n@ - All 2nd level accounts {Second_level_accounts}" + f"\n# - All 1st level Accounts {First_level_accounts}" + Manage_account("IS") + "\nEnter: - "
want_to_run_for_accounts = input(IS)
# Check if no accounts are provided
while not want_to_run_for_accounts:
    want_to_run_for_accounts = input("Please Select Accounts:-")
account_numbers_to_remove = None
if "-" in want_to_run_for_accounts:
    new_IS = want_to_run_for_accounts.split("-")
    want_to_run_for_accounts = new_IS[0]
    account_numbers_to_remove = new_IS[1]

try:
    ask_routine = int(input("Want to specify time to start in future? (Default: No): -"))
except:
    ask_routine = 0
create_pdf(pdf_file_path)
create_pdf(completed_account_pdf)
if ask_routine == 1:
    Routine_run()

my_program()

print("\n\n")

#Run time report
end_time = time.time()
runtime = end_time-start_time
runtime = float("{:.2f}".format(runtime))
print("Runtime:- ", runtime, "seconds")
strng1 = "\n" + str(runtime) + " seconds"
minutes = float("{:.2f}".format(runtime/60))
print("Runtime:- ", minutes, "minutes")
strng2 = "\n" + str(minutes) + " minutes"
hours = float("{:.2f}".format(minutes/60))
print("Runtime:- ", hours, "hours")
strng3 = "\n" + str(hours) + " hours"
strng = strng1 + strng2 + strng3
add_account_page_to_pdf(pdf_file_path, account_number=None, strng=strng)
if Ask_Shut_Down:
    shutdown_computer()