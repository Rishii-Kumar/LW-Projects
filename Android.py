from Closing_Edge_Tabs import Close_tabs
from Det_img import det_img, Bunch_img_det
from Profile import profile
import pyautogui, time
from Random_Meaningful_Lines import generate_random_meaningful_lines
import random
from Bunch_Search import det_searched, det_etab, find_searchbar

def find_dimensions():
    dimensions = Bunch_img_det("E:\\Det_img\\TXT Files\\Dimensions.txt",
                               code_string="print('Finding Dimension button')", img_name="Dimension Button")
    return dimensions
def Open_android_visuals(account_number, sleep_time=1):
    Close_tabs()
    pyautogui.hotkey("win", "d")
    profile(account_number)
    # Display a message indicating the start of the process
    print("Opening Android Visuals...")

    # Open a new tab in the web browser
    pyautogui.hotkey("ctrl", "t")  # New tab

    # Pause briefly
    time.sleep(sleep_time / 2)
    set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img(
        "E:\\Det_img\\Set_later2.png",
        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                                                                    code_string="pass",
                                                                    img_name="Set Later Button")

    # Open the browser's element inspector (F12)
    pyautogui.press("f12")  # Inspect element

    # Pause to allow the element inspector to load
    time.sleep(sleep_time / 2)

    # Find the dimensions of the web page
    dimensions = find_dimensions()

    # If dimensions are not found, keep trying until they are or until a timeout occurs
    while dimensions is None:
        time.sleep(1)
        dimensions = find_dimensions()
        # If dimensions are still not found, check if the Edge browser is open
        if dimensions is None:
            check_edge = det_etab()
            if check_edge is not None:
                remember_my_decision = Bunch_img_det("E:\\Det_img\\TXT Files\\Rem_Decision.txt",
                                                     code_string="pass", img_name="Remember my decision")
                if remember_my_decision is not None:
                    remember_decision_tick = Bunch_img_det("E:\\Det_img\\TXT Files\\Remember_tick.txt",
                                                 code_string="print('Remember Decision Tick NOT FOUND!')", kt=0,
                                                 img_name="Remember my decision tick")
                    while remember_decision_tick is None:
                        remember_decision_tick = Bunch_img_det("E:\\Det_img\\TXT Files\\Remember_tick.txt",
                                                     code_string="print('Remember Decision Tick NOT FOUND!')", kt=0,
                                                     img_name="Remember my decision tick")
                    Open_Developer_Tools = Bunch_img_det("E:\\Det_img\\TXT Files\\Open_DevTools.txt",
                                                  code_string="print('Open DevTools Button NOT FOUND!')",
                                                  img_name="Open DevTools")
                    while Open_Developer_Tools is None:
                        Open_Developer_Tools = Bunch_img_det("E:\\Det_img\\TXT Files\\Open_DevTools.txt",
                                                      code_string="print('Open DevTools Button NOT FOUND!')",
                                                      img_name="Open DevTools")
                    Android_view = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_view.txt",
                                                 code_string="print('Android View Button NOT FOUND!')",
                                                 img_name="Android View Button")
                    while Android_view is None:
                        Android_view = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_view.txt",
                                                     code_string="print('Android View Button NOT FOUND!')",
                                                     img_name="Android View Button")
                #Now again check for dimensions
                dimensions = find_dimensions()
            elif check_edge is None:
                profile(account_number, sleep_time=sleep_time)
                Open_android_visuals(account_number, sleep_time=sleep_time)
                return
        else:
            break




    # Pause briefly
    pyautogui.sleep(sleep_time / 2)

    # Detect the presence of an image (Samsung Galaxy S20 in this case)
    Bunch_img_det("E:\\Det_img\\TXT Files\\Samsung S20.txt",
                  code_string="print('Image: Samsung Galaxy S20 (Not Found)')",
                  img_name="Samsung Galaxy S20")

    # Reload the web page
    # Not_now = det_img("E:\\Det_img\\Not_now.png", code_string="print('Not Now button not popped!')", img_name="Not Now Button")
    # if Not_now != None:
    #     print("Pop up closed!")
    pyautogui.hotkey("ctrl", "r")  # Reload

# Android Works
def search_in_android(account_number, sleep_time=1):
    # Attempt to find the search bar element
    click_on_search_bar = find_searchbar()

    # Initialize a wait counter
    wait = 0

    # Print a message indicating that the search bar is being searched for
    print("Finding Searchbar...")

    # Continue searching for the search bar until it's found or a timeout occurs
    while click_on_search_bar is None:
        pyautogui.sleep(sleep_time)
        click_on_search_bar = find_searchbar()
        # If the search bar is still not found, check for specific visual cues
        if click_on_search_bar is None:
            print("Checking Visuals...")
            # Check for various visual cues indicating Android visuals are not found
            check_etab = det_etab()
            # If specific visual cues are detected, proceed with further actions
            if check_etab is not None:
                wait = wait + 1
                # Simulate clicking on specific coordinates
                pyautogui.click(x=142, y=722)
                pyautogui.sleep(sleep_time / 2)
                pyautogui.moveTo(x=621, y=814)
                pyautogui.sleep(sleep_time / 2)
                pyautogui.scroll(10000)
                time.sleep(sleep_time)

                # Attempt to find the search bar again
                click_on_search_bar = find_searchbar()

                # If the search bar is found, break out of the loop
                if click_on_search_bar is not None:
                    break

            # If no search bar is found and the wait condition is not met, reset the wait counter
            elif check_etab is None:
                wait = wait - wait
            # If no search bar is found, and we've waited for a certain number of times, proceed with reopening Android visuals
            if wait % 2 == 0:
                print("Reopening Android visuals...")
                time.sleep(sleep_time)
                Open_android_visuals(account_number, sleep_time=sleep_time)
                pyautogui.sleep(sleep_time)
                click_on_search_bar = find_searchbar()

                # If the search bar is found after reopening Android visuals, break out of the loop
        elif click_on_search_bar is not None:
            break

    # Generate a random search input
    search_input = generate_random_meaningful_lines()

    # Simulate typing the search input with random typing intervals
    pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))  # type search

    # Pause briefly
    pyautogui.sleep(sleep_time / 4)

    # Simulate pressing the Enter key to perform the search
    pyautogui.press("enter")  # search
    # Pause for a duration
    time.sleep(sleep_time)

    # Simulate clicking on specific coordinates
    pyautogui.click(x=142, y=722)

    # Check for specific images to verify if the search was successful
    check_searched = det_searched()

    # Continue checking for the presence of specific images until they are detected
    check_freq = 1
    etab_frequency = 0
    while check_searched is None:
        time.sleep(sleep_time)
        check_searched = det_searched()

        # If the specific images are detected, break out of the loop
        if check_searched is not None:
            break

        # If the specific images are not detected, check for visual cues again
        elif check_searched is None:
            print(f"Checking Android Searched for Account Number: {account_number}")
            check_freq += 1

            # Check for specific visual cues indicating Android visuals are not found
            check_etab = det_etab()

            # If specific visual cues are detected, proceed with further actions
            if check_etab is not None:
                etab_frequency += 1
                click_on_search_bar = find_searchbar()
                # If the search bar is found after checking visual cues, proceed with typing the search input and performing the search
                if click_on_search_bar is not None:
                    pyautogui.write(search_input, interval=random.uniform(0.001, 0.002))  # type search
                    pyautogui.sleep(0.25)
                    pyautogui.press("enter")  # search
                    time.sleep(sleep_time)
                    check_searched = det_searched()
                    # If the search is successful, break out of the loop
                    if check_searched is not None:
                        break
                elif etab_frequency % 3 == 0:
                    search_in_android(account_number)
                    return
            elif check_etab is None:
                etab_frequency = etab_frequency - etab_frequency
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
