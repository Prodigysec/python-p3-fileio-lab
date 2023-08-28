def write_file(file_name, file_content):
    fileName = f"{file_name}.txt"
    with open(fileName, 'w') as f:
        f.write(file_content)


def append_file(file_name, append_content):
    fileName = f"{file_name}.txt"
    with open(fileName, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    fileName = f"{file_name}.txt"
    with open(fileName, 'r') as f:
        return f.read()
