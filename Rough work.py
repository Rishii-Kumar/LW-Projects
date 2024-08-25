import pyautogui
# pyautogui.sleep(4)
# # print(pyautogui.position())
# for i in range(2):
#     pyautogui.scroll(-1000)
# Point(x=55, y=805)
# Point(x=78, y=817)
# Point(x=1747, y=1049)
# all = {}




# import psutil
#
# def terminate_edge_processes():
#     try:
#         for process in psutil.process_iter(['pid', 'name']):
#             if 'msedge.exe' in process.info['name'].lower():
#                 print(f"Terminating Edge process with PID {process.info['pid']}")
#                 psutil.Process(process.info['pid']).terminate()
#
#         print("All Edge processes terminated.")
#     except Exception as e:
#         terminate_edge_processes()
#
# if __name__ == "__main__":
#     terminate_edge_processes()

# import time
# least = time.time()
# time.sleep(1)
# cooldown_time = 15
#
# def format_time(seconds):
#     seconds = float("{:.2f}".format(seconds))
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     remaining_seconds = seconds % 60
#
#     if hours > 0 or minutes > 0:
#         return f"time remaining {int(hours)} hours {int(minutes)} minutes {int(remaining_seconds)} seconds"
#     else:
#         return f"time remaining {int(remaining_seconds)} seconds"
# while time.time() - least <= cooldown_time:
#     print(format_time(cooldown_time - (time.time() - least)))
#     time.sleep(2)



# Constants
"""
profile_time = 5  # seconds
sleep_time = 1
end_time_average = 70  # seconds
additional_wait_time = sleep_time  # seconds
tab_closing_time = 5  # seconds (assuming "win+d" is used)
cooldown_time_between_rounds = sleep_time  # seconds

# Total time for one round
total_time_one_round = profile_time + end_time_average + additional_wait_time + tab_closing_time

# Total time for one round with cooldown
total_time_one_round_with_cooldown = total_time_one_round + cooldown_time_between_rounds

# Total time for one iteration without cooldown
total_time_one_iteration_without_cooldown = 20 * total_time_one_round

# Total time for one iteration with cooldown
total_time_one_iteration_with_cooldown = 20 * total_time_one_round_with_cooldown

print(f"Total time for one iteration without cooldown: {total_time_one_iteration_without_cooldown:.2f} seconds")
print(f"Total time for one iteration with cooldown: {total_time_one_iteration_with_cooldown:.2f} seconds")
"""
"""
# Constants
profile_time = 5  # seconds
end_time_first_7_rounds = 60  # seconds
end_time_8th_round = 85  # seconds
end_time_remaining_rounds = 90  # seconds
additional_wait_time = 0  # seconds
tab_closing_time = 5  # seconds (assuming "win+d" is used)

# Total time for one round
total_time_first_7_rounds = profile_time + end_time_first_7_rounds + additional_wait_time + tab_closing_time
total_time_8th_round = profile_time + end_time_8th_round + additional_wait_time + tab_closing_time
total_time_remaining_rounds = profile_time + end_time_remaining_rounds + additional_wait_time + tab_closing_time

# Total time for cooldown between rounds
cooldown_time = 900  # seconds

# Total time for one round with cooldown
total_time_first_7_rounds_with_cooldown = total_time_first_7_rounds + cooldown_time
total_time_8th_round_with_cooldown = total_time_8th_round + cooldown_time
total_time_remaining_rounds_with_cooldown = total_time_remaining_rounds + cooldown_time

# Total time for one full iteration (20 accounts) without cooldown
total_time_one_iteration_without_cooldown = (
    13 * total_time_first_7_rounds +
    total_time_8th_round +
    6 * total_time_remaining_rounds +
    19 * additional_wait_time
)

# Total time for one full iteration (20 accounts) with cooldown
total_time_one_iteration_with_cooldown = (
    13 * total_time_first_7_rounds_with_cooldown +
    total_time_8th_round_with_cooldown +
    6 * total_time_remaining_rounds_with_cooldown +
    19 * cooldown_time
)

print(f"Total time for one iteration without cooldown: {total_time_one_iteration_without_cooldown / 60:.2f} minutes")
print(f"Total time for one iteration with cooldown: {total_time_one_iteration_with_cooldown / 60:.2f} minutes")
"""


"""
from datetime import datetime, timedelta
import time

def get_remaining_time(start_hour, start_minute, start_am_pm):
    current_time = datetime.now()
    start_time = datetime(current_time.year, current_time.month, current_time.day, start_hour, start_minute)

    if start_am_pm.lower() == 'pm':
        start_time += timedelta(hours=12)

    time_difference = start_time - current_time

    return time_difference

def format_remaining_time(time_difference):
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_time = f"{hours:.1f} hours " if hours > 0 else ""
    formatted_time += f"{minutes:.1f} minutes " if minutes > 0 else ""
    formatted_time += f"{seconds:.1f} seconds"

    return formatted_time

def main():
    start_hour = int(input("Enter hour in which program should start (1-12): "))
    start_minute = int(input("Enter minutes at which program should start (0-59): "))
    start_am_pm = input("Enter AM/PM: ").lower()

    while True:
        remaining_time = get_remaining_time(start_hour, start_minute, start_am_pm)
        formatted_time = format_remaining_time(remaining_time)
        print(f"D - {formatted_time}", end='\r')

        if remaining_time.total_seconds() <= 0:
            print("\nIt's time to start the program!")
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
"""


"""
import pyautogui
import time
from colorama import Fore, Style

# Function to validate user input for hour (12-hour format)
def get_hour():
    while True:
        try:
            hour = int(input("Enter hour in which program should start (1-12): "))
            if 1 <= hour <= 12:
                return hour
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a valid hour between 1 and 12." + Style.RESET_ALL)
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
                print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter valid minutes between 0 and 59." + Style.RESET_ALL)
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

    formatted_time = ""

    if hours > 0:
        formatted_time += f"{hours:.1f} hours "
    if minutes > 0:
        formatted_time += f"{minutes:.1f} minutes "
    formatted_time += f"{remaining_seconds:.1f} seconds"

    return f"D - {formatted_time.strip()}"

def main():
    hour = get_hour()
    minutes = get_minutes()
    am_pm = get_am_pm()

    # Calculate initial time difference
    current_time = time.localtime()
    specified_start_time = time.strptime(
        f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday} {hour}:{minutes} {am_pm}",
        "%Y-%m-%d %I:%M %p")

    specified_hour_24h = specified_start_time.tm_hour
    if am_pm == "PM" and specified_hour_24h != 12:
        specified_hour_24h += 12

    time_diff_seconds = time.mktime(specified_start_time) - time.mktime(current_time)

    if specified_hour_24h < current_time.tm_hour or (
            specified_hour_24h == current_time.tm_hour and minutes <= current_time.tm_min):
        time_diff_seconds += 24 * 60 * 60

    # Print current time
    print(Fore.YELLOW + Style.BRIGHT + "Current Time: {:02}:{:02}".format(current_time.tm_hour, current_time.tm_min))

    # Print time after which the program will start
    print(Fore.MAGENTA + Style.BRIGHT + "Program will start at: {:02}:{:02} {}".format(hour, minutes, am_pm) + Style.RESET_ALL)
    prev_time = time_diff_seconds + 1
    pyautogui.sleep(3)
    while time_diff_seconds > 0 and time_diff_seconds < prev_time:
        statement = format_time(time_diff_seconds)
        print(Fore.YELLOW + Style.BRIGHT + statement + Style.RESET_ALL)
        pyautogui.write(statement)
        pyautogui.press('enter')
        time.sleep(300)

        # Update time difference
        current_time = time.localtime()
        specified_start_time = time.strptime(
            f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday} {hour}:{minutes} {am_pm}",
            "%Y-%m-%d %I:%M %p")

        specified_hour_24h = specified_start_time.tm_hour
        if am_pm == "PM" and specified_hour_24h != 12:
            specified_hour_24h += 12

        time_diff_seconds = time.mktime(specified_start_time) - time.mktime(current_time)

        if specified_hour_24h < current_time.tm_hour or (
                specified_hour_24h == current_time.tm_hour and minutes <= current_time.tm_min):
            time_diff_seconds += 24 * 60 * 60

    print(Fore.BLUE + Style.BRIGHT + "Mission Started!" + Style.RESET_ALL)

# Run the program
main()
"""


for i in range(1, 6):
    for y in range(1, i+1):
        print(y, end=" ")
    print("\n", end="")


alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(1, 6):
    for y in range(1, i+1):
        print(alp[y], end=" ")
    print("\n", end="")



# Taking user input for x and n
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Function to calculate series a
def series_a(x, n):
    sum_a = 0
    for i in range(n+1):
        term = x**i
        sum_a += term
        print(f"Term {i+1}: {term}")
    print(f"Sum of Series a: {sum_a}")

# Function to calculate series b
def series_b(x, n):
    sum_b = 0
    for i in range(n+1):
        term = (-1)**i * (x**i)
        sum_b += term
        print(f"Term {i+1}: {term}")
    print(f"Sum of Series b: {sum_b}")

# Function to calculate series c
def series_c(x, n):
    sum_c = 0
    for i in range(1, n+2):
        term = (x**i)/i
        sum_c += term
        print(f"Term {i}: {int(term)}")
    print(f"Sum of Series c: {sum_c}")

# Calling functions to display each series with their sums
series_a(x, n)
print("\n")
series_b(x, n)
print("\n")
series_c(x, n)



student = {1: ["Vaish", 95]}
