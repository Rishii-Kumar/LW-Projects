import os

def rename_png_files(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"The provided path '{folder_path}' is not a valid directory.")
        return

    # Get a list of all files in the directory
    files = os.listdir(folder_path)

    # Filter out only PNG files
    png_files = [file for file in files if file.lower().endswith(".png")]

    if not png_files:
        print(f"No PNG files found in the directory '{folder_path}'.")
        return

    # Rename PNG files
    for index, old_name in enumerate(png_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"QS{index}{extension}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

# Take user input for the folder path
folder_path = "E:\\test_fol"

# Call the function to rename PNG files in the provided folder
rename_png_files(folder_path)
