import pyautogui
import time
from colorama import Fore, Style

def Routine_run():
    # Function to validate user input for hour (12-hour format)
    def get_hour():
        while True:
            try:
                hour = int(input("Enter hour in which program should start (1-12): "))
                if 1 <= hour <= 12:
                    return hour
                else:
                    print \
                        (Fore.RED + Style.BRIGHT + "Invalid input! Please enter a valid hour between 1 and 12." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a valid hour." + Style.RESET_ALL)

    # Function to validate user input for minutes
    def get_minutes():
        while True:
            try:
                minutes = int(input("Enter minutes at which program should start (0-59): "))
                if 0 <= minutes <= 59:
                    return minutes
                else:
                    print \
                        (Fore.RED + Style.BRIGHT + "Invalid input! Please enter valid minutes between 0 and 59." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter valid minutes." + Style.RESET_ALL)

    # Function to get AM/PM input
    def get_am_pm():
        while True:
            am_pm = input("Enter AM/PM: ").strip().upper()
            if am_pm in ["AM", "PM"]:
                return am_pm
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter either AM or PM." + Style.RESET_ALL)

    # Main function
    def format_time(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60

        if hours > 0:
            if minutes > 0:
                return f"time remaining {hours} hours {minutes} minutes {remaining_seconds} seconds"
            else:
                return f"time remaining {hours} hours {remaining_seconds} seconds"
        elif minutes > 0:
            return f"time remaining {minutes} minutes {remaining_seconds} seconds"
        else:
            return f"time remaining {remaining_seconds} seconds"

    def main():
        hour = get_hour()
        minutes = get_minutes()
        am_pm = get_am_pm()

        # Get current time
        current_time = time.localtime()

        # Calculate specified start time
        specified_start_time = time.strptime(
            f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday} {hour}:{minutes} {am_pm}",
            "%Y-%m-%d %I:%M %p")

        # Calculate current time in 24-hour format for comparison
        current_hour_24h = current_time.tm_hour

        # Calculate specified start time in 24-hour format for comparison
        specified_hour_24h = specified_start_time.tm_hour
        if am_pm == "PM" and specified_hour_24h != 12:  # Adjust for PM
            specified_hour_24h += 12

        # Calculate time difference in seconds
        time_diff_seconds = time.mktime(specified_start_time) - time.mktime(current_time)

        # If specified time is earlier than current time, schedule for the next day
        if specified_hour_24h < current_hour_24h or (
                specified_hour_24h == current_hour_24h and minutes <= current_time.tm_min):
            time_diff_seconds += 24 * 60 * 60  # Add 24 hours in seconds

        # Print current time
        print \
            (Fore.YELLOW + Style.BRIGHT + "Current Time: {:02}:{:02}".format(current_time.tm_hour, current_time.tm_min))

        # Print time after which the program will start
        print(Fore.MAGENTA + Style.BRIGHT + "Program will start at: {:02}:{:02} {}".format(hour, minutes, am_pm) + Style.RESET_ALL)

        # Calculate and print remaining time in hours, minutes, and seconds
        remaining_hours, remainder = divmod(time_diff_seconds, 3600)
        remaining_minutes, remaining_seconds = divmod(remainder, 60)

        if remaining_hours > 0:
            print(Fore.GREEN + Style.BRIGHT + "Time remaining: {} hours".format(remaining_hours) + Style.RESET_ALL)
        if remaining_minutes > 0:
            print(Fore.GREEN + Style.BRIGHT + "Time remaining: {} minutes".format(remaining_minutes) + Style.RESET_ALL)
        if remaining_seconds > 0:
            print(Fore.GREEN + Style.BRIGHT + "Time remaining: {} seconds".format(remaining_seconds) + Style.RESET_ALL)

        # Wait until the specified time is reached
        if time_diff_seconds > 0:
            print(Fore.CYAN + Style.BRIGHT + "Waiting for the specified time..." + Style.RESET_ALL)
            scree_time = 0
            prev_time = time_diff_seconds + 1
            while time_diff_seconds > 0 and time_diff_seconds < prev_time:
                scree_time += 2
                time.sleep(2)
                # Get current time
                current_time = time.localtime()

                # Calculate specified start time
                specified_start_time = time.strptime(
                    f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday} {hour}:{minutes} {am_pm}",
                    "%Y-%m-%d %I:%M %p")

                # Calculate current time in 24-hour format for comparison
                current_hour_24h = current_time.tm_hour

                # Calculate specified start time in 24-hour format for comparison
                specified_hour_24h = specified_start_time.tm_hour
                if am_pm == "PM" and specified_hour_24h != 12:  # Adjust for PM
                    specified_hour_24h += 12

                # Calculate time difference in seconds
                prev_time = time_diff_seconds
                time_diff_seconds = time.mktime(specified_start_time) - time.mktime(current_time)

                # If specified time is earlier than current time, schedule for the next day
                if specified_hour_24h < current_hour_24h or (
                        specified_hour_24h == current_hour_24h and minutes <= current_time.tm_min):
                    time_diff_seconds += 24 * 60 * 60  # Add 24 hours in seconds

                statement = format_time(time_diff_seconds)
                print(Fore.YELLOW + Style.BRIGHT + statement + Style.RESET_ALL)
                if scree_time %90 == 0:
                    pyautogui.moveRel(1, 0)
                    pyautogui.sleep(0.5)
                    pyautogui.press("ctrl")
                    pyautogui.sleep(0.5)
                    pyautogui.press("alt")
                    pyautogui.sleep(0.5)
                    pyautogui.press("space")

            print(Fore.BLUE + Style.BRIGHT + "Program started!" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a future time." + Style.RESET_ALL)

    # Run the program
    main()
