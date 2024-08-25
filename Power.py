import os

#Shut Down
def shutdown_computer():
    try:
        # Close all running tasks (forcefully terminate processes)
        os.system("taskkill /f /im explorer.exe")  # Terminate File Explorer
        os.system("taskkill /f /im chrome.exe")  # Terminate Google Chrome (example, add more as needed)

        # Shutdown the computer
        os.system(
            "shutdown /s /f /t 1")  # /s option indicates shutdown, /f forces running applications to close, /t 1 sets a delay of 1 second
        print("Closing all tasks and shutting down the computer...")
    except Exception as e:
        print(f"Error: {e}")