# Python File Management System

A simple command-line-based File Management System built using Python. This project allows users to perform basic file operations such as creating, reading, updating, renaming, and deleting files using Python's built-in file handling capabilities.

## Overview

The project demonstrates how Python can interact with the local file system through file handling and the `pathlib` module. It provides a menu-driven interface where users can select an operation and perform it on a specified file.

## Features

- **Create File:** Create a new file and write initial content into it.
- **Read File:** Read and display the contents of an existing file.
- **Rename File:** Change the name of an existing file.
- **Append Content:** Add new information to an existing file without removing its previous content.
- **Overwrite File:** Replace the existing content of a file with new information.
- **Delete File:** Permanently delete an existing file.
- **Exception Handling:** Handle errors during file operations using `try-except` blocks.
- **File Existence Validation:** Check whether a file exists before performing operations.

## Technologies Used

- Python 3
- pathlib
- os
- File Handling
- Exception Handling
- Match-Case Statement

## Project Structure

```text
File-Management/
│
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Abhishek-maurya9/File-Management
   ```

2. Navigate to the project directory:

   ```bash
   cd File-Management
   ```

3. Run the Python application:

   ```bash
   python main.py
   ```

## Available Operations

When the program starts, users are presented with the following menu:

| Option | Operation |
|--------|-----------|
| 1 | Create a new file |
| 2 | Read an existing file |
| 3 | Update an existing file |
| 4 | Delete an existing file |

The update operation provides three additional choices:

- Rename an existing file.
- Append content to a file.
- Overwrite existing file content.

## Python Concepts Practiced

This project helped me practice and understand:

- Functions and modular programming.
- File handling (`open`, `read`, `write`).
- File modes (`r`, `w`, `a`).
- `pathlib.Path` for file system operations.
- Conditional statements and match-case.
- Exception handling using `try-except`.
- Working with file paths and checking file existence.

## Learning Outcome

Through this project, I gained practical experience working with Python file handling, managing local files, implementing CRUD-like operations, and handling runtime exceptions.

## Future Improvements

- Add a loop-based menu to perform multiple operations without restarting the application.
- Add support for creating directories.
- Implement file search functionality.
- Add file extension validation.
- Improve input validation and error handling.
- Introduce logging to track file operations.

---