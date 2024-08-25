import cv2
import pyautogui
import numpy as np
import pyperclip
import time
from colorama import Fore, Style

def report():
    def det_img(file_path, code_string="print('Error')", kt=1, img_name=None):
        try:
            if img_name is None:
                img_name = file_path
            else:
                img_name = img_name
            # Load the target image
            target_image = cv2.imread(file_path)

            # Get screen dimensions
            screen_width, screen_height = pyautogui.size()

            # Take a screenshot
            screenshot = pyautogui.screenshot()
            screenshot = np.array(screenshot)

            # Convert BGR to RGB
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

            # Match template
            result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Click if match found
            if max_val > 0.8:
                target_width, target_height = target_image.shape[1], target_image.shape[0]
                target_center = (max_loc[0] + target_width // 2, max_loc[1] + target_height // 2)
                if kt == 1:
                    pyautogui.click(target_center)
                    if img_name != 0:
                        print(f"Clicked on the image: {img_name}")
                    else:
                        pass
                elif kt == 2:
                    pyautogui.moveTo(target_center)
                    if img_name != 0:
                        print(f"Moved on the image: {img_name}")
                    else:
                        pass
                else:
                    if img_name != 0:
                        print(f"Image Found, not clicked on it! file: {img_name}")
                    else:
                        pass
                return 1
            else:
                try:
                    exec(code_string)
                except Exception as e:
                    print("Error executing code!")
                return None
        except Exception as e:
            e = str(e)
            if "E:" in e or "Screenshot" in e:
                print(e)
            try:
                exec(code_string)
            except Exception as e:
                print("Error executing given code.")
                return None

    def open_wsp():
        pyautogui.hotkey('win', '6')
        pyautogui.sleep(4)

    pyautogui.sleep(1)
    open_wsp()

    #Check Whatsapp
    time.sleep(1)
    chats = det_img("E:\\Det_img\\Chats.png",
                    code_string="print('Chats not found!')", img_name="Chats") or det_img("E:\\Det_img\\Chatss.png",
                    code_string="print('Chats not found!')", img_name="Chats") or det_img("E:\\Det_img\\Chatsss.png",
                    code_string="print('Chats not found!')", img_name="Chats")
    chat_wait = 0
    while chats is None:
        time.sleep(0.75)
        chat_wait += 1
        if chat_wait > 10:
            open_wsp()
        chats = det_img("E:\\Det_img\\Chats.png",
                code_string="print('Chats not found!')", img_name="Chats") or det_img("E:\\Det_img\\Chatss.png",
                code_string="print('Chats not found!')",img_name="Chats") or det_img("E:\\Det_img\\Chatsss.png",
                code_string="print('Chats not found!')", img_name="Chats")

    #Find my chat
    def find_me():
        Me = det_img("E:\\Det_img\\Me.png",
             code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\Me1.png",
             code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\Me2.png",
             code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\Me3.png",
             code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\Me4.png",
             code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\Me5.png",
             code_string="pass", img_name="Rishi's Chat")
        if Me is None:
            pyautogui.sleep(0.75)
            pyautogui.hotkey("ctrl", "f")
            pyautogui.write("Rishi")
            pyautogui.sleep(1)
            mee = det_img("E:\\Det_img\\R1.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R2.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R3.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R4.png",
                  code_string="pass", img_name="Rishi's Chat")
            if mee is None:
                pyautogui.sleep(0.75)
                cross = det_img("E:\\Det_img\\cross.png",
                        code_string="print('cross not found!')") or det_img("E:\\Det_img\\crosss.png",
                        code_string="print('cross not found!')")
                cr_wait = 0
                while cross is None:
                    cr_wait += 1
                    if cr_wait > 5:
                        find_me()
                        return
                    pyautogui.sleep(0.5)
                    cross = det_img("E:\\Det_img\\cross.png",
                            code_string="print('cross not found!')") or det_img("E:\\Det_img\\crosss.png",
                            code_string="print('cross not found!')")
                pyautogui.sleep(0.5)
                pyautogui.hotkey("ctrl", "f")
                pyautogui.sleep(0.5)
                pyautogui.write("9153413379")
                pyautogui.sleep(0.75)
                my = det_img("E:\\Det_img\\R1.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R2.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R3.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R4.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R5.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R6.png",
                  code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R7.png",
                  code_string="pass", img_name="Rishi's Chat")
                m_wait = 0
                while my is None:
                    m_wait += 1
                    if m_wait > 5:
                        find_me()
                        return
                    pyautogui.sleep(0.5)
                    my = det_img("E:\\Det_img\\R1.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R2.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R3.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R4.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R5.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R6.png",
                         code_string="pass", img_name="Rishi's Chat") or det_img("E:\\Det_img\\R7.png",
                         code_string="pass", img_name="Rishi's Chat")
    find_me()

    #Writing report
    pyautogui.sleep(0.75)
    account_info = str("\n1 - Rishi 1"
                     "\n2 - Rishi 2"
                     "\n3 - Rishi 3"
                     "\n4 - Rishi 4"
                     "\n5 - Rishi 5"
                     "\n6 - Shalini 1"
                     "\n7 - Shalini 2"
                     "\n8 - Shalini 3"
                     "\n9 - Shalini 4"
                     "\n10 - Rishi 7"
                     "\n11 - Shalini 5"
                     "\n12 - Rishi 6"
                     "\n13 - Rishi 8"
                     "\n14 - Shalini 6"
                     "\n15 - Shalini 7"
                     "\n16 - Rishi 9"
                     "\n17 - Shalini 4ed"
                     "\n18 - Shalini 5ed")
    repo = str(account_info + final_report)
    pyperclip.copy(repo)
    pyautogui.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    global Ask_report_file
    if Ask_report_file == 1:
        open_directory_in_explorer()
        pyautogui.sleep(2)
        pyautogui.click(x=1098, y=589)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.sleep(0.75)
        pyautogui.hotkey("ctrl", "c")
        pyautogui.sleep(0.75)
        pyautogui.hotkey("alt", "tab")
        pyautogui.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.sleep(2)
        pyautogui.press("enter")
        pyautogui.sleep(5.5)
        pyautogui.hotkey("alt", "f4")
        pyautogui.sleep(1)
        pyautogui.click(x=1098, y=589)
        pyautogui.sleep(1)
        pyautogui.hotkey("ctrl", "w")
        pyautogui.sleep(2)
        print(Fore.CYAN + Style.BRIGHT + "REPORT SENT TO RISHI" + Style.RESET_ALL)