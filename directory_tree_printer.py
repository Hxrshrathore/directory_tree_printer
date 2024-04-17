import os

def print_tree(directory, prefix='', file=None):
    """
    Recursively prints the directory structure as a stylized tree.
    """
    files = []
    directories = []
    # Separate files and directories
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            directories.append(item)
        else:
            files.append(item)

    entries = directories + files
    pointers = ['├── '] * (len(entries) - 1) + ['└── ']

    for pointer, name in zip(pointers, entries):
        path = os.path.join(directory, name)
        if file:
            file.write(f"{prefix}{pointer}{name}\n")
        else:
            print(f"{prefix}{pointer}{name}")
        if os.path.isdir(path):  # If directory, recurse
            extension = '│   ' if pointer == '├── ' else '    '
            print_tree(path, prefix=prefix+extension, file=file)

if __name__ == "__main__":
    root_directory = 'Flask'
    output_path = 'output.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"{root_directory}/\n")
        print_tree(root_directory, file=f)
