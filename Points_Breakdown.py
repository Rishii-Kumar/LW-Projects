import pyautogui
from Det_img import det_img
from colorama import Fore,Style
from frequent_detections import check_rewards_tab
import time


def check_points_breakdown():
    points_breakdown = det_img("E:\\Det_img\\points_breakdown.png",
                               code_string='print("Points breakdown button not found!")',
                               img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown0.png",
                                                                       code_string='print("Points breakdown button not found!")',
                                                                       img_name="Points breakdown") or det_img(
        "E:\\Det_img\\points_breakdown1.png", code_string='print("Points breakdown button not found!")',
        img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown2.png",
                                                code_string='print("Points breakdown button not found!")',
                                                img_name="Points breakdown") or det_img(
        "E:\\Det_img\\points_breakdown3.png", code_string='print("Points breakdown button not found!")',
        img_name="Points breakdown") or det_img("E:\\Det_img\\points_breakdown4.png",
                                                code_string='print("Points breakdown button not found!")',
                                                img_name="Points breakdown")
    return points_breakdown

def points_check():
    print("Finding Points Breakdown button...")
    pyautogui.moveTo(x=77, y=371)
    points_breakdown = check_points_breakdown()
    while points_breakdown is None:
        pyautogui.sleep(0.75)
        points_breakdown = check_points_breakdown()
    pyautogui.moveTo(x=77, y=371)

def Points_Breakdown_Info(account_number):
    pyautogui.sleep(1)
    points_check()
    pyautogui.sleep(sleep_time)
    print("Analysing Points Breakdown...")
    report = ""
    data = ""
    global final_report
    pyautogui.sleep(1)
    pyautogui.click(x=951, y=384)
    pyautogui.sleep(0.75)

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
    pc_points_path = find_first_present_image(pc_path_list)
    if pc_points_path == None:
        wait_path = 0
        while pc_points_path is None:
            pyautogui.sleep(0.75)
            if wait_path > 5:
                final_report += str \
                    ("\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                return
            if wait_path % 5 == 0:
                etab = det_etab()
                if etab is None:
                    profile(account_number)
                    pyautogui.sleep(0.75)
                    pyautogui.hotkey("ctrl", "t")
                    time.sleep(1 / 4)
                    pyautogui.write("https://rewards.bing.com")
                    time.sleep(1 / 4)
                    pyautogui.press("enter")
                    pyautogui.sleep(0.75)
                    rewards_tab_open_check = check_rewards_tab()
                    while rewards_tab_open_check is None:
                        pyautogui.sleep(0.75)
                        rewards_tab_open_check = check_rewards_tab()
                    print("Finding Points Breakdown button...")
                    pyautogui.moveTo(x=77, y=371)
                    points_breakdown = check_points_breakdown()
                    pyautogui.sleep(1)
                    pyautogui.click(x=951, y=384)
                    if points_breakdown is None:
                        print("Not Found!")
                elif etab is not None:
                    pyautogui.hotkey("ctrl", "t")
                    time.sleep(1 / 4)
                    pyautogui.write("https://rewards.bing.com")
                    time.sleep(1 / 4)
                    pyautogui.press("enter")
                    pyautogui.sleep(0.75)
                    rewards_tab_open_check = check_rewards_tab()
                    while rewards_tab_open_check is None:
                        pyautogui.sleep(0.75)
                        rewards_tab_open_check = check_rewards_tab()
                    print("Finding Points Breakdown button...")
                    pyautogui.moveTo(x=77, y=371)
                    points_breakdown = check_points_breakdown()
                    pyautogui.sleep(1)
                    pyautogui.click(x=951, y=384)
                    if points_breakdown is None:
                        print("Not Found!")
            pc_points_path = find_first_present_image(pc_path_list)
            if pc_points_path is not None:
                break
            wait_path += 1

    if account_number in Second_level_accounts:
        and_points_path = find_first_present_image(android_path_list)
        if and_points_path == None:
            wait_path = 0
            while and_points_path is None:
                pyautogui.sleep(0.75)
                if wait_path > 5:
                    final_report += str \
                        ("\n\n" + Fore.RED + Style.BRIGHT + f"FAILED for Account: - {account_number}" + Style.RESET_ALL + "\n\n")
                    return
                if wait_path % 5 == 0:
                    etab = det_etab()
                    if etab is None:
                        profile(account_number)
                        pyautogui.sleep(0.75)
                        pyautogui.hotkey("ctrl", "t")
                        time.sleep(1 / 4)
                        pyautogui.write("https://rewards.bing.com")
                        time.sleep(1 / 4)
                        pyautogui.press("enter")
                        pyautogui.sleep(0.75)
                        rewards_tab_open_check = check_rewards_tab()
                        while rewards_tab_open_check is None:
                            pyautogui.sleep(0.75)
                            rewards_tab_open_check = check_rewards_tab()
                        print("Finding Points Breakdown button...")
                        pyautogui.moveTo(x=77, y=371)
                        points_breakdown = check_points_breakdown()
                        pyautogui.sleep(1)
                        pyautogui.click(x=951, y=384)
                        if points_breakdown is None:
                            print("Not Found!")
                    elif etab is not None:
                        pyautogui.hotkey("ctrl", "t")
                        time.sleep(1 / 4)
                        pyautogui.write("https://rewards.bing.com")
                        time.sleep(1 / 4)
                        pyautogui.press("enter")
                        pyautogui.sleep(0.75)
                        rewards_tab_open_check = check_rewards_tab()
                        while rewards_tab_open_check is None:
                            pyautogui.sleep(0.75)
                            rewards_tab_open_check = check_rewards_tab()
                        print("Finding Points Breakdown button...")
                        pyautogui.moveTo(x=77, y=371)
                        points_breakdown = check_points_breakdown()
                        pyautogui.sleep(1)
                        pyautogui.click(x=951, y=384)
                        if points_breakdown is None:
                            print("Not Found!")
                and_points_path = find_first_present_image(android_path_list)
                if and_points_path is not None:
                    break
                wait_path += 1

        pyautogui.sleep(0.5)
        def read():
            # Pause briefly
            pyautogui.sleep(1)

            pc_points_left, android_points_left, pc_search_freq_left, android_search_freq_left = 0, 0, 0, 0

            # Check if the image is present on the screen
            print(pc_points_path)
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
                pyautogui.sleep(2)
                if Ask_report_file == 1:
                    global pdf_file_path
                    add_screenshot_to_pdf(pdf_file_path)
                # Print the extracted text
                text = extracted_text
                print("PC points details: - ")
                print("Text: - ", text)
                lst = text.split("/")
                print(lst)
                try:
                    pc_points_left += 150 - int(lst[0])
                except:
                    print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                    pc_points_left = 0
                    failed_pc = 1
                if pc_points_left > 0:
                    pc_search_freq_left += pc_points_left // 5
                    print(Fore.YELLOW + Style.BRIGHT + f"{pc_points_left} points are left for PC!" + Style.RESET_ALL)
                    if want_complete_points == 1:
                        pyautogui.sleep(0.5)
                        for i in range(pc_search_freq_left):
                            pc_search()
                        infor = read()
                        return infor
                if failed_pc == 1:
                    pc_points_left = None
                    pc_search_freq_left = None
            else:
                print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)

            # Check if the image is present on the screen
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

                # Print the extracted text
                text = extracted_text
                print("Android pints details: - ")
                print(text)
                lst = text.split("/")
                print(lst)
                try:
                    android_points_left += 100 - int(lst[0])
                except:
                    print(Fore.RED + Style.BRIGHT + "Failed to read android points details!" + Style.RESET_ALL)
                    android_points_left = 0
                    failed_and = 1
                if android_points_left > 0:
                    android_search_freq_left += android_points_left // 5
                    print \
                        (Fore.YELLOW + Style.BRIGHT + f"{android_points_left} points are left for PC!" + Style.RESET_ALL)
                    Close_tabs()
                    pyautogui.hotkey("win", "d")
                    pyautogui.sleep(2)
                    profile(account_number)
                    pyautogui.sleep(1)
                    open_rewards_tab()
                    check_points_breakdown()
                    if want_complete_points == 1:
                        print("Opening Android Visuals...")
                        pyautogui.sleep(0.75)
                        Open_android_visuals()
                        pyautogui.sleep(0.5)
                        for i in range(android_search_freq_left):
                            search_in_android()
                        pyautogui.hotkey("ctrl", "w")
                        infor = read()
                        return infor
                if failed_and == 1:
                    android_points_left = None
                    android_search_freq_left = None
            else:
                print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)

            final_data = str(f"\nReport of Account Number {account_number}: - " +
                             f"\nPC points left: - {pc_points_left}" +
                             f"\nPC Search Frequency needed: - {pc_search_freq_left}" +
                             f"\nAndroid points left: - {android_points_left}" +
                             f"\nAndroid Search Frequency needed: - {android_search_freq_left}")
            return "\n\n" + final_data + "\n\n"

        data += read()

    elif account_number in First_level_accounts:
        pyautogui.sleep(0.75)
        def read():
            # Pause briefly
            pyautogui.sleep(1)

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
                pyautogui.sleep(2)
                if Ask_report_file == 1:
                    global pdf_file_path
                    add_screenshot_to_pdf(pdf_file_path)
                # Print the extracted text
                text = extracted_text
                print("PC points details: - ")
                print("Text: - ", text)
                lst = text.split("/")
                print(lst)
                try:
                    pc_points_left += 50 - int(lst[0])
                except:
                    print(Fore.RED + Style.BRIGHT + "Failed to read pc points details!" + Style.RESET_ALL)
                    pc_points_left = 0
                    failed_pc = 1
                if pc_points_left > 0:
                    pc_search_freq_left += pc_points_left // 5
                    print(Fore.YELLOW + Style.BRIGHT + f"{pc_points_left} points are left for PC!" + Style.RESET_ALL)
                    if want_complete_points == 1:
                        pyautogui.sleep(0.5)
                        for i in range(pc_search_freq_left):
                            pc_search()
                        infor = read()
                        return infor
                if failed_pc == 1:
                    pc_points_left = None
                    pc_search_freq_left = None
            else:
                print(Fore.RED + Style.BRIGHT + "Image For PC Points Not Found!" + Style.RESET_ALL)
            final_data = str(f"\nReport of Account Number {account_number}: - " +
                             f"\nPC points left: - {pc_points_left}" +
                             f"\nPC Search Frequency needed: - {pc_search_freq_left}")
            return "\n\n" + final_data + "\n\n"

        data += read()

    report += data
    return report