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
# from ShutDown import shutdown_computer
# from txt_file import read_last_line
# from copy_delete import copy_files, delete_all_files_in_directory, open_directory_in_explorer

import random
import pyautogui
from colorama import Fore, Style, init
import traceback
import pygetwindow as gw
from PIL import Image, ImageGrab, ImageEnhance
import sys
import win32gui
import win32con
import win32api
import time
import datetime
import pytesseract
from Report_PDF import create_pdf, add_screenshot_to_pdf, add_account_page_to_pdf
from Power import shutdown_computer
from Routine_run import Routine_run
from Det_img import det_img, Bunch_img_det
from Managing_accounts import Manage_account
from Android import Open_android_visuals, search_in_android
from Profile import profile
from Random_Meaningful_Lines import generate_random_meaningful_lines
from Reading import read_below
from Bunch_Search import det_new_tab, det_etab, det_rewards_tab, det_searched, det_and_visuals, find_searchbar

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pyautogui.FAILSAFE = False
start_time = time.time()
final_report = ""
tab_times = 0
first = 1

# Shut Down
Ask_Shut_Down = None

# Specify the directory where you want to save the PDF file
pdf_directory = "G:\\My Drive\\Report Files"
pdf_direct = "G:\\My Drive\\Completed_Points"

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time as "2023-10-13__12/01"
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H;%M")

pdf_file_path = pdf_directory + f"\\report_file-({str(formatted_datetime)}).pdf"
completed_account_pdf = pdf_direct + f"\\complete_report-({str(formatted_datetime)}).pdf"

Cooldown_acc = []
Account_dictionary = {}
initial_list = Manage_account('RA')
Completed = 0

# Work starts from here
# Define a list of second-level accounts
Second_level_accounts = Manage_account("SLA")

# Initialize an empty list for first-level accounts
First_level_accounts = Manage_account("FLA")

instructions = str("Instructions: \nPress '1' for YES & '0' for NO")
print(Fore.GREEN + Style.BRIGHT + instructions + Style.RESET_ALL)
try:
    # Ask the user for customizations (default or custom)
    Ask_Shut_Down = int(input("Want to shut down Computer after completion? (default = 0): - "))
except Exception as e:
    Ask_Shut_Down = None

global Server, cooldown_time, error_hand, sleep_time, ask_for_tab_closing, want_to_run_for_accounts, ask_routine, account_numbers_to_remove
if Ask_Shut_Down != 9:
    # Choosing Server to run
    try:
        Server = int(input("0 - USA\n1 - Indian\nChoose Server (Default-Indian): - "))
    except:
        Server = 1
    while Server != 1 and Server != 0:
        Server = int(input("Invalid Input!\nPlease Choose a Valid Server: - "))

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

    # Profile tab closing syntax
    slp = None
    try:
        # o close all tabs (default = 1, Yes)
        ask_for_tab_closing = int(input("Want to close all TABS? (default = 1): - "))
        if ask_for_tab_closing > 1:
            ask_for_tab_closing = 1
            try:
                slp = int(input("Enter time to pause after checking extra points: - "))
            except:
                pass
    except Exception as e:
        # If input is not valid, default to closing all tabs
        ask_for_tab_closing = 1

    # Ask the user to choose the account(s) to run the program for
    IS = ("Choose ACCOUNT: " + f"\n@ - All 2nd level accounts {Second_level_accounts}" + f"\n# - All 1st level Accounts {First_level_accounts}" +
          Manage_account("IS") + "\nEnter: - ")
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
elif Ask_Shut_Down == 9:
    Server = 1
    cooldown_time = 900
    error_hand = 1
    sleep_time = 1
    ask_for_tab_closing = 1
    ask_routine = 0
    want_to_run_for_accounts = ["*"]
    account_numbers_to_remove = []
    slp = None


loop = 0


create_pdf(pdf_file_path)
create_pdf(completed_account_pdf)

def my_program():
    global error_hand
    try:
        # Tools
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

        def check_glitch(account_number):
            Glitch = Bunch_img_det(r"E:\Det_img\TXT Files\Glitch.txt", kt=0,
                                                    img_name="Glitch Tab", code_string="pass")
            if Glitch is not None:
                Close_all_edge_tabs()
                Close_all_edge_tabs(cnd=2)
                profile(account_number, sleep_time=sleep_time, Cooldown_acc=Cooldown_acc)
                open_rewards_tab(account_number)
            return Glitch
        def check_internet(account_number):
            Internet = Bunch_img_det(r"E:\Det_img\TXT Files\check_internet.txt", kt=0,
                                     img_name="Glitch Tab", code_string="pass")
            loop = 0
            while Internet is not None:
                time.sleep(sleep_time*4)
                pyautogui.hotkey('ctrl', 'r')
                Internet = Bunch_img_det(r"E:\Det_img\TXT Files\check_internet.txt", kt=0,
                                         img_name="Glitch Tab", code_string="pass")
                if Internet is None:
                    break
                loop += 1
                if loop % 5 ==0:
                    Close_all_edge_tabs()
                    Close_all_edge_tabs(cnd=2)
                    profile(account_number, sleep_time=sleep_time, Cooldown_acc=Cooldown_acc)
                    open_rewards_tab(account_number)
            return Internet

        def check_signin_tab():
            Check_signin_option = Bunch_img_det("E:\\Det_img\\TXT Files\\Signin.txt", kt=0,
                                                img_name="Sign-in Tab", code_string="Already Signed-in")
            if Check_signin_option is not None:
                print(Fore.RED + Style.BRIGHT + "Please Sign-in to the account to continue..." + Style.RESET_ALL)
                play_music(play=not None)
                a = input("press enter to continue after signing in:")
            return Check_signin_option

        def check_Suspension():
            for i in range(3):
                Check_suspension = Bunch_img_det("E:\\Det_img\\TXT Files\\Suspended.txt", kt=0,
                                                img_name="Sign-in Tab", code_string="Account Suspended!!!!!!!!!!!")
            if Check_suspension is not None:
                add_screenshot_to_pdf(completed_account_pdf)
                play_music(play=not None)
            return Check_suspension

        def check_rewards_tab(account_number, force=None):
            rewards_tab_open_check = Bunch_img_det("E:\\Det_img\\TXT Files\\rewards_tab_Hi.txt",
                                                      code_string="print('Rewards tab Hi button not found!')",
                                                      img_name="Rewards tab")
            loop = 0
            while rewards_tab_open_check is None:
                loop += 1
                time.sleep(sleep_time)
                rewards_tab_open_check = Bunch_img_det("E:\\Det_img\\TXT Files\\rewards_tab_Hi.txt",
                                                          code_string="print('Rewards tab Hi button not found!')",
                                                          img_name="Rewards tab")
                if loop%5 == 0:
                    check_glitch(account_number=account_number)
                    check_signin_tab()
                    check_internet(account_number=account_number)
                    if force:
                        open_rewards_tab(account_number=account_number)
            return rewards_tab_open_check

        def check_pointsbreakdown_tab(account_number):
            PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                 code_string="print('Points Breakdown Tab not found!')",
                                                 img_name="Points Breakdown tab")
            loop = 0
            while PB_tab_open_checking is None:
                time.sleep(sleep_time)
                PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                     code_string="print('Points Breakdown Tab not found!')",
                                                     img_name="Points Breakdown tab")
                loop += 1
                if loop % 3 == 0:
                    glitch = check_glitch(account_number)
                    if glitch is None:
                        etab = det_etab()
                        if etab is not None:
                            Suspension = check_Suspension()
                            if Suspension is not None:
                                return Suspension
                            check_signin_tab()
                            if loop % 12 == 0:
                                Close_all_edge_tabs()
                                Close_all_edge_tabs(2)
                                profile(account_number)
                            open_pointsbreakdown(account_number)
                            PB_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\points_breakdown_tab.txt",
                                                                 code_string="print('Points Breakdown Tab not found!')",
                                                                 img_name="Points Breakdown tab")
                        else:
                            pass
            return None
        
        # PC Browsing
        def pc_search():
            # Generate a random search input
            search_input = generate_random_meaningful_lines()

            # Open a new browser tab
            pyautogui.hotkey("ctrl", "t")

            # Pause for a short delay
            time.sleep(sleep_time / 4)

            # Type the generated search input with a random typing interval
            pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))

            # Press the 'Enter' key to initiate the search
            pyautogui.press("enter")
            pyautogui.sleep(sleep_time / 2)
            # Detect if the search results have loaded by looking for specific images
            check_search = Bunch_img_det("E:\\Det_img\\TXT Files\\PC_search.txt",
                                         code_string="pass", kt=0)

            # Continue checking for search results until they are detected
            wwt = 0
            while check_search is None:
                wwt += 1
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
            if Server == 1:
                time.sleep(sleep_time*2)
            if Server == 0:
                time.sleep(3*sleep_time)

            # Close the current browser tab
            pyautogui.hotkey("ctrl", "w")

            # Wait for a brief moment
            if Server == 1:
                time.sleep(sleep_time)
            if Server == 0:
                time.sleep(2*sleep_time)

        def Points_Breakdown_Info(account_number):
            pyautogui.sleep(sleep_time)
            set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later2.png",
                        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                        code_string="pass", img_name="Set Later Button")
            open_pointsbreakdown(account_number)
            pbt = check_pointsbreakdown_tab(account_number)
            if pbt is not None:
                print(Fore.RED + Style.BRIGHT + "Account Suspended!!!!!!!!!" + Style.RESET_ALL)
                add_screenshot_to_pdf(completed_account_pdf)
                time.sleep(1)
                return
            print("Analysing Points Breakdown...")
            # Define file paths for point images
            pc_path_list = ["E:\\Det_img\\PC_points.png", "E:\\Det_img\\PC_points1.png", "E:\\Det_img\\PC_points2.png",
                            "E:\\Det_img\\PC_points3.png", "E:\\Det_img\\PC_points4.png"]
            android_path_list = ["E:\\Det_img\\Android_points.png", "E:\\Det_img\\Android_points1.png",
                                 "E:\\Det_img\\Android_points3.png"]

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
                    wait_path = 1
                    while pc_points_path is None:
                        if wait_path >= 11:
                            print(
                                "\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                            return
                        if wait_path % 6 == 0:
                            etab = det_etab()
                            while etab is None:
                                time.sleep(sleep_time)
                                etab = det_etab()
                            if etab is not None:
                                pyautogui.sleep(sleep_time / 2)
                                open_pointsbreakdown(account_number)
                                pbt = check_pointsbreakdown_tab(account_number)
                                if pbt is not None:
                                    print(Fore.RED + Style.BRIGHT + "Account Suspended!!!!!!!!!" + Style.RESET_ALL)
                                    return
                                time.sleep(sleep_time / 2)
                        pyautogui.sleep(sleep_time / 2)
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
                            if wait_path > 10:
                                print(
                                    "\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                                return
                            if wait_path % 5 == 0:
                                etab = det_etab()
                                while etab is None:
                                    time.sleep(sleep_time)
                                    etab = det_etab()
                                if etab is not None:
                                    pyautogui.sleep(sleep_time / 2)
                                    open_pointsbreakdown(account_number)
                                    pbt = check_pointsbreakdown_tab(account_number)
                                    if pbt is not None:
                                        print(Fore.RED + Style.BRIGHT + "Account Suspended!!!!!!!!!" + Style.RESET_ALL)
                                        return
                                    time.sleep(sleep_time / 2)
                            pyautogui.sleep(sleep_time / 2)
                            and_points_path = find_first_present_image(android_path_list)
                            if and_points_path is not None:
                                break
                            wait_path += 1
                    return and_points_path

                pyautogui.sleep(sleep_time / 2)

                def read():
                    global prev_pc_remain, prev_and_remain, and_rep, pc_rep, Completed
                    pc_points_path = pc_points_first_img()

                    # Pause briefly
                    pyautogui.sleep(sleep_time / 2)
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
                        enhancer = ImageEnhance.Contrast(screenshot)
                        screenshot = enhancer.enhance(2.0)

                        # Perform OCR
                        extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
                        print(extracted_text)

                        # Print the extracted text
                        text = extracted_text
                        print("PC points details: - ")
                        print("Text: - ", text)
                        lst = text.split("/")
                        print(lst)
                        try:
                            if Server == 0:
                                pc_points_left += 150 - int(lst[0])
                            elif Server == 1:
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
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                                            col = Cooldown_acc
                                            for account in Cooldown_acc:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
                                                        return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                elif Server == 0:
                                    if pc_points_left == 150:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                            # Read again
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
                                enhancer = ImageEnhance.Contrast(screenshot)
                                screenshot = enhancer.enhance(2.0)

                                # Perform OCR
                                extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
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
                                    print(
                                        Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                                    failed_pc += 1
                                    if failed_pc >= 3:
                                        failed_pc = 1
                                        break
                                if pc_points_left == 0:
                                    break
                        if failed_pc == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(
                                Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
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
                            time.sleep(sleep_time / 2)
                            add_screenshot_to_pdf(pdf_file_path)
                            add_account_page_to_pdf(completed_account_pdf, account_number)
                            add_screenshot_to_pdf(completed_account_pdf)
                            Completed = 1
                            time.sleep(sleep_time)
                        if android_points_left > 0:
                            print("Opening Android Visuals...")
                            pyautogui.sleep(sleep_time / 3)
                            Open_android_visuals(account_number, sleep_time=sleep_time)
                            pyautogui.sleep(sleep_time / 2)
                            open_pointsbreakdown(account_number)
                            pbt = check_pointsbreakdown_tab(account_number)
                            if pbt is not None:
                                print(Fore.RED + Style.BRIGHT + "Account Suspended!!!!!!!!!" + Style.RESET_ALL)
                                return
                            time.sleep(sleep_time / 2)
                        while android_points_left > 0:
                            if prev_and_remain == android_points_left:
                                and_rep += 1
                                if and_rep >= 2:
                                    time_value = time.time()
                                    cool_account = [account_number, time_value]
                                    pyautogui.hotkey("ctrl", "w")
                                    col = Cooldown_acc
                                    for account in col:
                                        if account[0] == account_number:
                                            if account[1] == None:
                                                Cooldown_acc.remove(account)
                                            elif account[1] != None:
                                                return
                                    Cooldown_acc.append(cool_account)
                                    print(
                                        Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                    print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                    return
                            elif prev_and_remain != android_points_left:
                                and_rep = 0
                            prev_and_remain = android_points_left
                            pyautogui.hotkey('ctrl', 'shift', 'tab')
                            time.sleep(sleep_time / 2)
                            search_in_android(account_number, sleep_time)
                            time.sleep(sleep_time / 2)
                            pyautogui.hotkey('ctrl', 'tab')
                            time.sleep(sleep_time / 2)
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
                                enhancer = ImageEnhance.Contrast(screenshot)
                                screenshot = enhancer.enhance(2.0)

                                # Perform OCR
                                extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
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
                                    time.sleep(sleep_time / 2)
                                    add_screenshot_to_pdf(pdf_file_path)
                                    add_account_page_to_pdf(completed_account_pdf, account_number)
                                    add_screenshot_to_pdf(completed_account_pdf)
                                    Completed = 1
                                    time.sleep(sleep_time)
                                    break

                        if failed_and == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(
                                Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)
                    return "Done"

                read()

            elif account_number in First_level_accounts:
                pyautogui.sleep(sleep_time / 2)

                def read():
                    global prev_pc_remain, prev_and_remain, and_rep, pc_rep, Completed
                    pc_points_path = pc_points_first_img()

                    # Pause briefly
                    pyautogui.sleep(sleep_time / 2)
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
                            if Server == 0:
                                pc_points_left += 50 - int(lst[0])
                            elif Server == 1:
                                pc_points_left += 30 - int(lst[0])

                        except:
                            print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                            pc_points_left = 0
                            failed_pc = 1
                        if pc_points_left == 0:
                            time.sleep(sleep_time / 2)
                            add_screenshot_to_pdf(pdf_file_path)
                            add_account_page_to_pdf(completed_account_pdf, account_number)
                            add_screenshot_to_pdf(completed_account_pdf)
                            Completed = 1
                            time.sleep(sleep_time / 2)
                        while pc_points_left > 0:
                            if prev_pc_remain == pc_points_left:
                                pc_rep += 1
                                if Server == 1:
                                    if pc_points_left == 30:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                                            col = Cooldown_acc
                                            for account in Cooldown_acc:
                                                if account[0] == Cooldown_acc:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
                                                        return
                                            Cooldown_acc.append(cool_account)
                                            print(
                                                Fore.LIGHTYELLOW_EX + Style.NORMAL + f"{cool_account} added to Cooldwon accounts list!" + Style.RESET_ALL)
                                            print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
                                            return
                                elif Server == 0:
                                    if pc_points_left == 50:
                                        if pc_rep >= 4:
                                            time_value = time.time()
                                            cool_account = [account_number, time_value]
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                                            col = Cooldown_acc
                                            for account in col:
                                                if account[0] == account_number:
                                                    if account[1] == None:
                                                        Cooldown_acc.remove(account)
                                                    elif account[1] != None:
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
                            # Read again
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
                                enhancer = ImageEnhance.Contrast(screenshot)
                                screenshot = enhancer.enhance(2.0)

                                # Perform OCR
                                extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
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
                                        pc_points_left = 50 - int(lst[0])
                                    elif Server == 1:
                                        pc_points_left = 30 - int(lst[0])
                                except:
                                    print(
                                        Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                                    failed_pc += 1
                                    if failed_pc >= 3:
                                        failed_pc = 1
                                        break
                                if pc_points_left == 0:
                                    time.sleep(sleep_time / 2)
                                    add_screenshot_to_pdf(pdf_file_path)
                                    add_account_page_to_pdf(completed_account_pdf, account_number)
                                    add_screenshot_to_pdf(completed_account_pdf)
                                    Completed = 1
                                    time.sleep(sleep_time / 2)
                                    break
                        if failed_pc == 1:
                            add_account_page_to_pdf(pdf_file_path, account_number, rep=2)
                            add_screenshot_to_pdf(pdf_file_path)
                            print(
                                Fore.RED + Style.BRIGHT + f"Error while reading points information in Account Number {account_number}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)

                read()

            pyautogui.hotkey('ctrl', 'w')
            return

        def open_rewards_tab(account_number):
            # Close the current tab in the web browser
            pyautogui.hotkey("ctrl", "t")

            # Pause brieflymsedge.exe --profile-directory="Profile 8"

            time.sleep(sleep_time/2)

            # Navigate to the Bing Rewards page
            capslock_state = win32api.GetKeyState(0x14) & 1
            if capslock_state:
                # Press the Caps Lock key to toggle it off
                pyautogui.press('capslock')
            pyautogui.write("https://rewards.bing.com/  ")

            # Pause briefly
            time.sleep(sleep_time / 5)

            # Press Enter to visit the URL
            pyautogui.press("enter")

            # Pause for a specified duration
            if Server == 0:
                time.sleep(2*sleep_time)
            time.sleep(sleep_time * 3)

            # Check if the rewards tab is open
            rewards_tab_open_check = check_rewards_tab(account_number)

            # Initialize a variable to track waiting time
            wait_time = 0

            # Wait until the rewards tab is detected or a timeout occurs
            while rewards_tab_open_check is None:
                time.sleep(1)
                wait_time += 1
                rewards_tab_open_check = check_rewards_tab(account_number)

                # If rewards tab is not found and a timeout occurs, perform additional checks
                if rewards_tab_open_check is None and wait_time % 8 == 0:
                    # Check if other tabs (e.g., Edge browser) are open
                    check_edge_tab = det_etab()

                    # If other tabs are detected, open the rewards tab again
                    if check_edge_tab is not None:
                        pyautogui.hotkey("ctrl", "t")
                        time.sleep(0.5)
                        capslock_state = win32api.GetKeyState(0x14) & 1
                        if capslock_state:
                            # Press the Caps Lock key to toggle it off
                            pyautogui.press('capslock')
                        pyautogui.write("https://rewards.bing.com")
                        time.sleep(0.5)
                        pyautogui.press("enter")
                        time.sleep(sleep_time * 3)
                        rewards_tab_open_check = check_rewards_tab(account_number)

        def open_pointsbreakdown(account_number):
            check_edge = det_etab()
            # If Edge is not open, keep waiting until it is detected
            waits = 0
            while check_edge is None:
                waits += 1
                pyautogui.sleep(sleep_time)
                check_edge = det_etab()
                if waits % 5 == 0:
                    print(
                        Fore.RED + Style.BRIGHT + f"Please open profile of account numbe: {account_number}" + Style.RESET_ALL)
            pyautogui.hotkey("ctrl", "t")
            pyautogui.sleep(sleep_time / 4)
            capslock_state = win32api.GetKeyState(0x14) & 1
            if capslock_state:
                # Press the Caps Lock key to toggle it off
                pyautogui.press('capslock')
            pyautogui.write("https://rewards.bing.com/pointsbreakdown ")
            pyautogui.sleep(sleep_time / 4)
            pyautogui.press("enter")
            pyautogui.sleep(sleep_time * 3)

        def end(account_number, rep=1):
            # Pause briefly
            profile(account_number, Cooldown_acc=Cooldown_acc, sleep_time=sleep_time)
            time.sleep(sleep_time / 2)

            # Add account page in pdf
            add_account_page_to_pdf(pdf_file_path, account_number, rep=rep)

            # Detailed Points Breakdown Information
            if not slp:
                Points_Breakdown_Info(account_number)
            pyautogui.sleep(sleep_time / 4)

            def extra_points():
                open_rewards_tab(account_number)
                check_rewards_tab(account_number)

                # Scroll down to check for extra points
                if Server == 0:
                    for i in range(8):
                        pyautogui.scroll(-250)
                for i in range(10):
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
                            pyautogui.sleep(3*sleep_time)
                        pyautogui.hotkey('ctrl', 'w')
                        if Server == 0:
                            time.sleep(2)
                        time.sleep(1)
                        if clk_plus >= 10:
                            add_screenshot_to_pdf(pdf_file_path)
                            break
                        points_detection = Bunch_img_det("E:\\Det_img\\TXT Files\\Plus_sign.txt",
                                                         code_string="print('No points available!')",
                                                         img_name="Plus Sign")

                # Scroll up to Hi image
                pyautogui.scroll(7000)
                pyautogui.sleep(0.5)
                pyautogui.click(197, 420)

            global Completed
            if slp or Completed == 1:
                extra_points()
                try:
                    pyautogui.sleep(slp)
                    check_rewards_tab(account_number)
                except:
                    pass
                time.sleep(1)
                check_rewards_tab(account_number, force=1)
                with open(r"E:\Det_img\TXT Files\Total-points.txt", 'r') as file:
                    # Read all lines from the file, strip any leading or trailing whitespace characters,
                    # and format each line as a raw string literal
                    lines = [rf'{line.strip()}' for line in file.readlines()]
                total_points = read_below(path_list=lines, sleep_time=sleep_time, text_type="Total Points")

                def convert_to_numeric(string_with_comma_and_newline):
                    # Remove comma and newline characters from the input string
                    cleaned_string = string_with_comma_and_newline.replace(',', '').replace('\n', '')
                    # Return the cleaned string
                    return cleaned_string

                Account_dictionary[account_number] = int(convert_to_numeric(total_points))
                print(Fore.BLUE + Style.BRIGHT + str(Account_dictionary) + Style.RESET_ALL)

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
                add_account_page_to_pdf(completed_account_pdf, account_number=None, strng=strng,
                                        hed=f"Time Taken for Account Number: {account_number}")
            Completed = 0

            # Close the new tab in the web browser
            if ask_for_tab_closing == 0:
                Close_new_tab()

        def Close_all_edge_tabs(cnd=1):
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
            if cnd==1:
                close_edge_tabs()
            elif cnd == 2:
                end_edge_processes()
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

        def play_music(play=None):
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
            if play:
                play_mp3(mp3_file)

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
        for i in provided_list_of_accounts:
            Cooldown_acc.append([i, None])
        if Ask_Shut_Down != 9:
            if error_hand <= 1:
                a = input("Want to continue?")
            if ask_routine == 1:
                Routine_run()

        # Create a new list of customised account numbers
        list_of_customised_account_numbers = []

        # Validate the provided account numbers and add them to the list
        for i in provided_list_of_accounts:
            integer_of_provided_account = int(i)
            list_of_customised_account_numbers.append(integer_of_provided_account)

        def format_time(seconds):
            seconds = float("{:.2f}".format(seconds))
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60

            if hours > 0 or minutes > 0:
                return f"time remaining {int(hours)} hours {int(minutes)} minutes {int(remaining_seconds)} seconds"
            else:
                return f"time remaining {int(remaining_seconds)} seconds"

        rep = 1
        global ask_for_tab_closing
        Quit = 0

        def timer(seconds, Quit):
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
                current_time = datetime.datetime.now().time()
                if datetime.time(0, 0) <= current_time <= datetime.time(0, 2):
                    Quit += 1
                    break
                time.sleep(1)

            print("\nTimer finished!")

        while Cooldown_acc and Quit==0:
            first_cooldwon_acc = Cooldown_acc[0]
            print(Fore.MAGENTA + Style.BRIGHT + f"First Cool Down Account : {first_cooldwon_acc}" + Style.RESET_ALL)
            first_cooldwon_time = first_cooldwon_acc[1]
            #Pausing if cool downtime is not completed
            if first_cooldwon_time:
                print(Fore.CYAN + Style.BRIGHT + f"Time passed : {time.time() - first_cooldwon_time}")
                if time.time() - first_cooldwon_time <= cooldown_time:
                    seconds_remaining = cooldown_time - (time.time() - first_cooldwon_time)
                    timer(seconds_remaining, Quit)
            if Quit == 1:
                break

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
                current_time = datetime.datetime.now().time()
                if datetime.time(0, 0) <= current_time <= datetime.time(0, 2):
                    Quit = 1
                    break
                end(i, rep=rep)
                if ask_for_tab_closing == 1:
                    pyautogui.hotkey("alt", "f4")
                elif ask_for_tab_closing == 0:
                    pyautogui.hotkey("ctrl", "d")
            rep = 2

        # Tab Closing
        if ask_for_tab_closing == 1:
            pyautogui.sleep(sleep_time)
            Close_all_edge_tabs()
        play_music()

    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error on line:", exc_tb.tb_lineno)
        sstt = str(e) + "\n" + "Error on line:" + str(exc_tb.tb_lineno)
        add_account_page_to_pdf(pdf_file_path, rep=0, account_number=None, strng=sstt)
        traceback.print_exc()
        if 0 < error_hand:
            global loop
            my_program()
            error_hand += 1
            loop += 1


# global Ask_Shut_Down, Server, cooldown_time, error_hand, sleep_time, ask_for_tab_closing, want_to_run_for_accounts
my_program()
print(Fore.BLUE + Style.BRIGHT + str(Account_dictionary) + Style.RESET_ALL)
details = ""
for key,value in Account_dictionary.items():
    details = details + f"Account number({key}): - {value} points\n"
add_account_page_to_pdf(completed_account_pdf, rep=0, account_number=None, strng=str(details),
                                        hed=f"Summary of Total Points")
print("\n\n")

# Run time report
end_time = time.time()
runtime = end_time - start_time
runtime = float("{:.2f}".format(runtime))
print("Runtime:- ", runtime, "seconds")
strng1 = "\n" + str(runtime) + " seconds"
minutes = float("{:.2f}".format(runtime / 60))
print("Runtime:- ", minutes, "minutes")
strng2 = "\n" + str(minutes) + " minutes"
hours = float("{:.2f}".format(minutes / 60))
print("Runtime:- ", hours, "hours")
strng3 = "\n" + str(hours) + " hours"
strng = strng1 + strng2 + strng3
add_account_page_to_pdf(pdf_file_path, account_number=None, strng=strng)
if Ask_Shut_Down==1:
    shutdown_computer()
a = input("")