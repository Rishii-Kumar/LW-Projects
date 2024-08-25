"""
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.txt' with the path to your text file
"""
from Det_img import det_img

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