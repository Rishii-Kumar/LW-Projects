import time

import pyautogui

# from Det_img import det_img
import pyautogui
import cv2
import numpy as np
import time

def det_img(image_path, roi, code_string="print('Error')", img_name=None, kt=1):
    try:
        # Load the image to be detected
        template = cv2.imread(image_path)

        # Get the dimensions of the template image
        template_height, template_width, _ = template.shape

        # Take a screenshot of the specified region of interest (roi)
        screenshot = pyautogui.screenshot(region=roi)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # Perform template matching
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Get the coordinates of the matched region
        top_left = max_loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

        # Calculate the center of the matched region
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2

        # Click on the center of the matched region
        if kt==1:
            pyautogui.click(x=roi[0] + center_x, y=roi[1] + center_y)
        if img_name:
            print(f"Clicked on image: {img_name}")
    except Exception as e:
        e = str(e)
        if "E:" in e or "Screenshot" in e:
            print(e)
        try:
            exec(code_string)
        except Exception as e:
            print("Error executing given code.")
            return None
time.sleep(4)
roi_coo=(78, 817, 1747, 1049)
def starting_quiz():
    quiz_strt_bttn = det_img("C:\\Users\\Rishi\\Pictures\\Screenshots\\Screenshot 2024-01-12 170934.png",
                             code_string="pass", img_name="quiz button", roi=roi_coo) or det_img("C:\\Users\\Rishi\\Pictures\\Screenshots\\Screenshot 2024-01-12 170911.png",
                             code_string="pass", img_name="quiz button", roi=roi_coo)
    while quiz_strt_bttn is None:
        time.sleep(0.5)
        quiz_strt_bttn = det_img("C:\\Users\\Rishi\\Pictures\\Screenshots\\Screenshot 2024-01-12 170934.png",
                                 code_string="pass", img_name="quiz button", roi=roi_coo) or det_img(
            "C:\\Users\\Rishi\\Pictures\\Screenshots\\Screenshot 2024-01-12 170911.png",
            code_string="pass", img_name="quiz button", roi=roi_coo)
    time.sleep(4)
    def det_opt_box():
        option_box = det_img("E:\\test_fol\\opt1.png", code_string="pass", img_name="quiz button1", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt2.png", code_string="pass", img_name="quiz button2", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt3.png", code_string="pass", img_name="quiz button3", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt4.png", code_string="pass", img_name="quiz button4", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt5.png", code_string="pass", img_name="quiz button5", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt6.png", code_string="pass", img_name="quiz button6", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt7.png", code_string="pass", img_name="quiz button7", roi=roi_coo) or \
             det_img("E:\\test_fol\\opt8.png", code_string="pass", img_name="quiz button8", roi=roi_coo)


        return option_box
    det_opt_box()
    green_tick = det_img("E:\\Det_img\\gt1.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                 det_img("E:\\Det_img\\gt2.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                 det_img("E:\\Det_img\\gt3.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                 det_img("E:\\Det_img\\gt4.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo)
    time.sleep(2)
    while green_tick is None:
        det_opt_box()
        time.sleep(2)
        green_tick = det_img("E:\\Det_img\\gt1.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                     det_img("E:\\Det_img\\gt2.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                     det_img("E:\\Det_img\\gt3.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo) or \
                     det_img("E:\\Det_img\\gt4.png", code_string="pass", kt=0, img_name="green tick", roi=roi_coo)
    print("Quiz Completed")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "w")

starting_quiz()

