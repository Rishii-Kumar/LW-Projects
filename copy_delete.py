import os
import shutil
from colorama import Fore, Style


#Copy Files
def copy_files():
    source_directory = r"E:\Report Files"
    destination_directory = r"E:\report store"
    try:
        # List all files in the source directory
        files = os.listdir(source_directory)

        # Copy each file from the source to the destination directory
        for file in files:
            source_file_path = os.path.join(source_directory, file)
            destination_file_path = os.path.join(destination_directory, file)
            shutil.copy2(source_file_path, destination_file_path)  # shutil.copy2 preserves metadata

        print(Fore.YELLOW + Style.BRIGHT+ "Files copied successfully." + Style.RESET_ALL)
    except Exception as e:
        print(f"Error: {e}")

#Deleting Files
def delete_all_files_in_directory():
    try:
        directory_path = r"E:\Report Files"
        # Iterate through all files and subdirectories in the specified directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if the current path points to a file or a directory
            if os.path.isfile(file_path):
                # If it's a file, delete it
                os.remove(file_path)
                print(Fore.RED + Style.BRIGHT + f"Deleted file: {file_path}" + Style.RESET_ALL)
            elif os.path.isdir(file_path):
                # If it's a directory, use shutil.rmtree to delete it recursively
                shutil.rmtree(file_path)
                print(f"Deleted directory and its contents: {file_path}")

        print(Fore.RED + Style.BRIGHT + f"All files and directories in '{directory_path}' have been deleted." + Style.RESET_ALL)
    except Exception as e:
        print(f"Error: {e}")

#Open directory
def open_directory_in_explorer():
    try:
        directory_path = r"E:\Report Files"
        # Open the specified directory in the default file explorer
        os.startfile(directory_path)
        print(f"Opened directory in file explorer: {directory_path}")
    except Exception as e:
        print(f"Error: {e}")


