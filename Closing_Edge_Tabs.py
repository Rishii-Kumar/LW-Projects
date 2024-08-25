import pygetwindow as gw
import win32gui, win32con, pyautogui
import time
num = 1
def Close_tabs():
    def close_edge_tabs():
        global num
        # Get all window titles
        window_titles = gw.getAllTitles()

        # Iterate through window titles and close Microsoft Edge tabs
        for title in window_titles:
            if "Edge" in title:

                # Find the window handle (hwnd) associated with the Edge tab
                hwnd = win32gui.FindWindow(None, title)

                # If a window handle is found
                if hwnd:
                    # Restore the window if minimized and bring it to the foreground
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.SetForegroundWindow(hwnd)  # Activate the window
                    time.sleep(0.5)

                    # Simulate pressing Ctrl+W to close the current tab
                    pyautogui.hotkey('ctrl', 'w')
                    print(f"Closed tab number: {num}")
                    num += 1
                    time.sleep(0.5)  # Wait for a moment to ensure the tab is closed

        # After closing Edge tabs, check for any remaining Edge tabs and close them recursively
        window_titles = gw.getAllTitles()
        print(window_titles)
        for title in window_titles:
            if "Edge" in title:
                close_edge_tabs()
        return window_titles
    close_edge_tabs()