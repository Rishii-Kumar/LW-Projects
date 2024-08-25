
def read_last_line(file_path):
    with open(file_path, 'r') as file:
        last_line = None
        for line in file:
            last_line = line.rstrip()
        if last_line:
            return last_line
        else:
            return None