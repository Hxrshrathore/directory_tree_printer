# Directory Tree Printer

This Python script generates a stylized tree structure of a directory, which helps in visualizing the arrangement of files and subdirectories. This can be particularly useful for understanding the layout of project directories or for documentation purposes.

## Features

- **Recursive Tree Traversal:** The script traverses all subdirectories and files within the specified root directory recursively.
- **Output Options:** The tree structure can be printed directly to the console or saved to a file.

## Requirements

The script is built using Python's standard library, so no additional installations are required.

## Usage

To use the script, simply specify the root directory and the output file name in the script. Here's how you can run it:

1. Modify the `root_directory` variable in the script to the path of the directory you want to visualize.
2. Optionally, change the `output_path` to specify where the output should be written.
3. Run the script:
   ```bash
   python directory_tree_printer.py
   ```

### Output

The script will generate a visual representation of the directory structure either on the console or in a file, depending on your configuration. The tree structure will look something like this:

```
Flask/
├── app.py
├── templates/
│   ├── index.html
│   └── login.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Contributions

Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This script is distributed under the MIT License. See `LICENSE` for more information.
