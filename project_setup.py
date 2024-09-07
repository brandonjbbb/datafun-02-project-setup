import os
import time
from pathlib import Path


# Function to create folders based on a list of folder names
def create_folders_from_list(
    folder_names, base_path=".", lowercase=False, underscores=False
):
    """
    Creates folders based on a list of names.

    Parameters:
    - folder_names (list): List of folder names to create.
    - base_path (str): The base directory where folders will be created.
    - lowercase (bool): Convert folder names to lowercase if True.
    - underscores (bool): Replace spaces with underscores if True.
    """
    for name in folder_names:
        folder_name = name.lower() if lowercase else name
        folder_name = folder_name.replace(" ", "_") if underscores else folder_name
        folder_path = Path(base_path) / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")


# Function to create folders based on a specified range of numbers
def create_folders_for_range(start, end, base_path=".", prefix="folder_"):
    """
    Creates folders for a specified range of numbers.

    Parameters:
    - start (int): Starting number.
    - end (int): Ending number (inclusive).
    - base_path (str): The base directory where folders will be created.
    - prefix (str): Prefix for folder names.
    """
    for i in range(start, end + 1):
        folder_path = Path(base_path) / f"{prefix}{i}"
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")


# Main function to demonstrate the folder creation
def main():
    # Example 1: Creating folders from a list
    folder_list = ["Data_2020", "Data_2021", "Data_2022", "Data_2023"]
    create_folders_from_list(folder_list, lowercase=True, underscores=True)

    # Example 2: Creating folders for a range
    create_folders_for_range(1, 5)

    # Add more functionality as needed based on project requirements


if __name__ == "__main__":
    main()
