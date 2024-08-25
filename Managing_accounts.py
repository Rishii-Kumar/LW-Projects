def file_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            formatted_content = '{' + file_content.strip() + '}'
            result_dict = eval(formatted_content)
            return result_dict
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


# Replace 'your_file.txt' with the path to your file containing the dictionary
file_path = "E:\\Det_img\\TXT Files\\Accounts.txt"
All_accounts = file_to_dict(file_path)

# Accounts Management
def Manage_account(work):
    input_dict = All_accounts
    if work == "IS":  # Input Taking String
        output_strings = []
        for key, value in input_dict.items():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) else key
                val = value.split("\\")[2]
                val = val.split(".")[0]
                if num < 10:
                    output_strings.append(f'\n{num} - {val}')
                else:
                    char = chr(ord('A') + num - 10)
                    output_strings.append(f'\n{char.upper()}/{char.lower()} - {val}')
            else:
                output_strings.append(f'Invalid input: {key}')
        return ''.join(output_strings)

    elif work == "RS":  # Registered account string
        output_strings = []
        for key in input_dict.keys():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) and key.isdigit() else key
                if num < 10:
                    output_strings.append(f'{num}')
                else:
                    char = chr(ord('A') + num - 10)
                    output_strings.append(f'{char.upper()}{char.lower()}')
            else:
                output_strings.append(f'Invalid input: {key}')
        return ''.join(output_strings) + "#@*"

    elif work == "RA":  # Registered Accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, (int, str)):
                num = int(key) if isinstance(key, str) and key.isdigit() else key
                output_list.append(num)
            else:
                output_list.append(f'Invalid input: {key}')
        return output_list

    elif work == "SLA":  # Second level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, int):
                output_list.append(key)
        return output_list

    elif work == "FLA":  # First level accounts
        output_list = []
        for key in input_dict.keys():
            if isinstance(key, str):
                output_list.append(int(key))
        return output_list

    elif work == "ANIP":  # Accounts name image path
        return list(input_dict.values())