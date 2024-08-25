import cv2
import pyautogui
import numpy as np

def det_img(file_path, code_string="print('Error')", kt=1, img_name=None, roi=None):
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

        # Define Region of Interest (ROI)
        if roi is not None:
            x, y, w, h = roi
            screenshot = screenshot[y:y + h, x:x + w]

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
            elif kt == 4:
                if img_name != 0:
                    print(f"Image found at location: {max_loc} for image: {img_name}")
                return max_loc
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



def Bunch_img_det(file_path, code_string="print('Error')", kt=1, img_name = None):
    result = None
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                current_result = det_img(str(line.strip()), code_string=code_string, kt=kt, img_name = img_name)
                if current_result is not None:
                    result = current_result
                    break
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return result