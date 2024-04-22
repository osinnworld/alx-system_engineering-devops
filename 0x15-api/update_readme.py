#!/usr/bin/env python3

import os

def update_readme(directory=".", title="List of Programs"):
    """
    Update the README.md file with a list of files in the specified directory.

    Args:
        directory (str, optional): Directory path to list files from. Defaults to current directory.
        title (str, optional): Title for the list in the README.md file. Defaults to "List of Programs".
    """
    # Delete the contents of README.md file
    with open("README.md", "w") as f:
        pass

    # Add custom title block to README.md
    with open("README.md", "a") as f:
        f.write(f"## {title}\n\n")

    # Append the output of ls -1 to README.md (listing file names with line numbers)
    with open("README.md", "a") as f:
        files = os.listdir(directory)
        for index, filename in enumerate(files, start=1):
            f.write(f"{index}. {filename}\n")

    print("List of programs has been updated in README.md.")

# Call the function with custom directory and title
update_readme(directory=os.getcwd(), title="MY PROGRAMS")

