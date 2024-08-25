# a = input("Enter a list of numbers separated by comma(,): -")
# lst = a.split(",")
# lsts = sorted(lst)
# print("Max: -", lsts[len(lst)-1])
# print("Min: -", lsts[0])
import pyautogui

# lst = list(input("Enter a list:- "))
# for i in range(0,len(lst)-1,2):
#     lst[i], lst[i+1] = lst[i+1], lst[i]
# print(lst)

# numbers = list(input("Enter a list:- "))
# element_to_search = int(input("Enter the element to search: "))
#
# if element_to_search in numbers:
#     print(f"{element_to_search} found in the list.")
# else:
#     print(f"{element_to_search} not found in the list.")

# numbers = list(input("Enter a list:- "))
# half_length = len(numbers) // 2
#
# numbers[:half_length], numbers[half_length:] = numbers[half_length:], numbers[:half_length]
#
# print("List after exchanging first and second half elements:", numbers)

# n = int(input("Enter the number of countries: "))
# countries_dict = {}
#
# for i in range(n):
#     country = input("Enter country name: ")
#     capital = input("Enter capital: ")
#     currency = input("Enter currency: ")
#     countries_dict[country] = {'Capital': capital, 'Currency': currency}
#
# # Display in tabular form
# print("\nCountry\t\tCapital\t\tCurrency")
# for country, info in countries_dict.items():
#     print(f"{country}\t\t{info['Capital']}\t\t{info['Currency']}")


# input_string = input("Enter a string: ")
# uppercase_count = 0
# lowercase_count = 0
#
# for char in input_string:
#     if char.isupper():
#         uppercase_count += 1
#     elif char.islower():
#         lowercase_count += 1
#
# counts_dict = {'Uppercase': uppercase_count, 'Lowercase': lowercase_count}
#
# print("Counts Dictionary:", counts_dict)

# input_string = input("Enter a string: ")
# frequency_dict = {}
#
# for i in input_string:
#     if i in frequency_dict:
#         frequency_dict[i] += 1
#     else:
#         frequency_dict[i] = 1
#
# print("Frequency Dictionary:", frequency_dict)

# x = float(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))
# sum_series = 1
# for i in range(1, n+1):
#     term = (-1)**(i-1) * (x**i)
#     sum_series += term
#     print(f"Term {i}: {term}")
#
# print(f"Sum of series: {sum_series}")


# for i in range(5,18):
#     print(f"Email:- DarkInterstellar{i}@gmail.com")
#     print(f"Password:- rewards@DI0{i}\n")

from Det_img import det_img
from txt_testing import Bunch_img_det
import random, time
from colorama import Fore, Style
# from Need_of_Speed import Manage_account
sleep_time =1
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
def Manage_account(work):
    input_dict = All_accounts
    if work == "IS":  # Input Taking String
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

    elif work == "RS":  # Registered account string
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

    elif work == "RA":  # Registered Accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) and key.isdigit() else key
                output_list.append(num)
            else:
                output_list.append(f'Invalid input: {key}')
        return output_list

    elif work == "SLA":  # Second level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, int):
                output_list.append(key)
        return output_list

    elif work == "FLA":  # First level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, str):
                output_list.append(int(key))
        return output_list

    elif work == "ANIP":  # Accounts name image path
        return list(input_dict.values())

def maximize_win():
    pyautogui.sleep(1)
    pyautogui.hotkey("win", "up")

def profile(given_account_number):
    print(Fore.BLUE + Style.BRIGHT + f"Accont Number {given_account_number}" + Style.RESET_ALL)
    # List of registered account numbers
    registered_accounts = Manage_account("RA")

    # Check if the given account number is valid
    while given_account_number not in registered_accounts:
        print("Invalid input!")
        given_account_number = int(input("Enter Number: - "))

    # Check if the account number is not 1
    # print(Fore.CYAN + Style.NORMAL + str(Cooldown_acc) + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + str(time.time()) + Style.RESET_ALL)
    pyautogui.hotkey("win", "r")
    time.sleep(sleep_time)
    if given_account_number != 1:
        pyautogui.write(f'msedge.exe --profile-directory="Profile {str(int(given_account_number) - 1)}"')
    elif given_account_number == 1:
        pyautogui.write(f'msedge.exe --profile-directory="Default"')
    time.sleep(sleep_time / 2)
    pyautogui.press("enter")
    maximize_win()
    # Detect the profile icon image
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt", kt=0,
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    timewait = 0
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt", kt=0,
                             code_string="pass", img_name="Profile Icon")
        timewait += 1
        if timewait % 5 == 0:
            profile(given_account_number)
            # Maximize the window to ensure visibility
            maximize_win()
            return
    set_later = det_img("E:\\Det_img\\Set_later1.png",
                        code_string="pass", img_name="Set Later Button") or det_img(
        "E:\\Det_img\\Set_later2.png",
        code_string="pass", img_name="Set Later Button") or det_img("E:\\Det_img\\Set_later3.png",
                                                                    code_string="pass",
                                                                    img_name="Set Later Button")

import inflect

def number_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num)

a = 2
def pro_logg(acc):
    global a
    pyautogui.hotkey('ctrl', 't')
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                             code_string="pass", img_name="Profile Icon")
    arr = det_img(r"E:\Fold\Screenshot 2024-02-17 194304.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    while arr is None:
        arr = det_img(r"E:\Fold\Screenshot 2024-02-17 194304.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    na = det_img(r"E:\Fold\Screenshot 2024-02-17 194314.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022034.png")
    while na is None:
        na = det_img(r"E:\Fold\Screenshot 2024-02-17 194314.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022034.png")
    pyautogui.sleep(1/2)
    sign = det_img(r"E:\Fold\Screenshot 2024-02-17 151013.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 023251.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    while sign is None:
        sign = det_img(r"E:\Fold\Screenshot 2024-02-17 151013.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 023251.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    pyautogui.sleep(1)
    sgn = det_img(r"E:\Fold\Screenshot 2024-02-17 194122.png", kt=0)
    while sgn is None:
        sgn = det_img(r"E:\Fold\Screenshot 2024-02-17 194122.png", kt=0)
    pyautogui.write(f"locoid000{a}@gmail.com", interval=random.uniform(0.01, 0.02))
    pyautogui.sleep(1/2)
    pyautogui.press('enter')
    entpass = det_img(r"E:\Fold\Screenshot 2024-02-17 151138.png", kt=0)
    while entpass is None:
        entpass = det_img(r"E:\Fold\Screenshot 2024-02-17 151138.png", kt=0)
    pyautogui.write("adarsh7641", interval=random.uniform(0.01, 0.02))
    pyautogui.sleep(1/2)
    pyautogui.press('enter')
    pyautogui.sleep(4)
    app = det_img(r"E:\Fold\Screenshot 2024-02-17 150745.png")
    while app is None:
        app = det_img(r"E:\Fold\Screenshot 2024-02-17 150745.png")
    pyautogui.sleep(3)
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                             code_string="pass", img_name="Profile Icon")
    pyautogui.sleep(0.7)
    set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022421.png")
    while set is None:
        set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022421.png")
        if set is None:
            prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                                 code_string="pass", img_name="Profile Icon")
    pyautogui.sleep(1)
    ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    while ak is None:
        ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    pyautogui.sleep(0.5)
    ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    while ab is None:
        ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    p = number_to_words(i)
    if a < 10:
        pyautogui.write(f"Locoid 0{a}", interval=random.uniform(0.1, 0.2))
    if a >= 10:
        pyautogui.write(f"Locoid {a}", interval=random.uniform(0.1, 0.2))
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    a += 1
def pro_log(acc):
    global a
    pyautogui.hotkey('ctrl', 't')
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                             code_string="pass", img_name="Profile Icon")
    arr = det_img(r"E:\Fold\Screenshot 2024-02-17 194304.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    while arr is None:
        arr = det_img(r"E:\Fold\Screenshot 2024-02-17 194304.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    na = det_img(r"E:\Fold\Screenshot 2024-02-17 194314.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022034.png")
    while na is None:
        na = det_img(r"E:\Fold\Screenshot 2024-02-17 194314.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022034.png")
    pyautogui.sleep(1/2)
    sign = det_img(r"E:\Fold\Screenshot 2024-02-17 151013.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 023251.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    while sign is None:
        sign = det_img(r"E:\Fold\Screenshot 2024-02-17 151013.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 023251.png") or det_img(
            r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022040.png")
    pyautogui.sleep(1)
    sgn = det_img(r"E:\Fold\Screenshot 2024-02-17 194122.png", kt=0)
    while sgn is None:
        sgn = det_img(r"E:\Fold\Screenshot 2024-02-17 194122.png", kt=0)
    if acc!= 16:
        pyautogui.write(f"DarkInterstellar{acc}@outlook.com", interval=random.uniform(0.01, 0.02))
    if acc== 16:
        pyautogui.write(f"DarkInterstellar0{acc}@outlook.com", interval=random.uniform(0.01, 0.02))
    pyautogui.sleep(1/2)
    pyautogui.press('enter')
    entpass = det_img(r"E:\Fold\Screenshot 2024-02-17 151138.png", kt=0)
    while entpass is None:
        entpass = det_img(r"E:\Fold\Screenshot 2024-02-17 151138.png", kt=0)
    pyautogui.write(f"rewards@DI0{acc}", interval=random.uniform(0.01, 0.02))
    pyautogui.sleep(1/2)
    pyautogui.press('enter')
    pyautogui.sleep(4)
    app = det_img(r"E:\Fold\Screenshot 2024-02-17 150745.png")
    while app is None:
        app = det_img(r"E:\Fold\Screenshot 2024-02-17 150745.png")
    pyautogui.sleep(3)
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                             code_string="pass", img_name="Profile Icon")
    pyautogui.sleep(0.7)
    set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022421.png")
    while set is None:
        set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png") or det_img(r"C:\Users\Rishi\Pictures\Screenshots\Screenshot 2024-02-29 022421.png")
        if set is None:
            prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                                 code_string="pass", img_name="Profile Icon")
    pyautogui.sleep(1)
    ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    while ak is None:
        ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    pyautogui.sleep(0.5)
    ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    while ab is None:
        ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    p = number_to_words(i)
    if acc < 10:
        pyautogui.write(f"Dark 0{acc}", interval=random.uniform(0.1, 0.2))
    if acc >= 10:
        pyautogui.write(f"Dark {acc}", interval=random.uniform(0.1, 0.2))
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    a += 1

def chng(acc):
    prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                         code_string="pass", img_name="Profile Icon")
    print("Finding Profile Icon...")
    # Continue searching for the profile icon until it's found
    while prof is None:
        prof = Bunch_img_det("E:\\Det_img\\TXT Files\\Profile_icon.txt",
                             code_string="pass", img_name="Profile Icon")
    pyautogui.sleep(0.7)
    set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png")
    while set is None:
        set = det_img(r"E:\Fold\Screenshot 2024-02-17 150806.png")
    pyautogui.sleep(1)
    ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    while ak is None:
        ak = det_img(r"E:\Fold\Screenshot 2024-02-17 150825.png")
    pyautogui.sleep(0.5)
    ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    while ab is None:
        ab = det_img(r"E:\Fold\Screenshot 2024-02-17 150835.png")
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(f"Dark 0{acc}", interval=random.uniform(0.1, 0.2))
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('alt', 'f4')

for i in range(22, 23):
    profile(i)
    pyautogui.sleep(2)
    pro_logg(i)
    a+=1
    pyautogui.sleep(1)

