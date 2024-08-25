from Det_img import Bunch_img_det, det_img
from colorama import Fore, Style
from Managing_accounts import Manage_account
import pyautogui, time

def profile(given_account_number=1, Cooldown_acc=None, sleep_time=1):
    print(Fore.BLUE + Style.BRIGHT + f"Accont Number {given_account_number}" + Style.RESET_ALL)
    # List of registered account numbers
    registered_accounts = Manage_account("RA")

    # Check if the given account number is valid
    while given_account_number not in registered_accounts:
        print("Invalid input!")
        given_account_number = int(input("Enter Number: - "))

    # Check if the account number is not 1
    print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + str(time.time()) + Style.RESET_ALL)
    pyautogui.hotkey("win", "r")
    pyautogui.sleep(sleep_time)
    if given_account_number != 1:
        pyautogui.write(f'msedge.exe --profile-directory="Profile {str(int(given_account_number) - 1)}"')
    elif given_account_number == 1:
        pyautogui.write(f'msedge.exe --profile-directory="Default"')
    pyautogui.sleep(sleep_time / 2)
    pyautogui.press("enter")
    pyautogui.sleep(sleep_time)
    pyautogui.hotkey("win", "up")
    # Detect the profile icon image
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt", kt=0,
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    timewait = 0
    # Continue searching for the profile icon until it's found
    if prof is None:
        while prof is None:
            prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt", kt=0,
                                 code_string="pass", img_name="Profile Icon")
            timewait += 1
            if timewait % 2 == 0:
                profile(given_account_number)
                return
    print('Profile Found!')
    set_later = det_img("E:\\Det_img\\Set_later1.png",
        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later2.png",
        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
        code_string="pass", img_name="Set Later Button")