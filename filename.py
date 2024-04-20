import os
import sys

def change_file_extension(file_path):
    file_name, _ = os.path.splitext(file_path)
    new_file_path = file_name + ".txt"
    os.rename(file_path, new_file_path)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            change_file_extension(file_path)
            print(f"Changed extension of '{file_path}' to .txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python change_extensions.py <target_folder>")
        sys.exit(1)

    target_folder = sys.argv[1]

    if not os.path.isdir(target_folder):
        print(f"Error: The specified target folder '{target_folder}' does not exist.")
        sys.exit(1)

    print(f"Scanning '{target_folder}' and its subdirectories...")
    process_directory(target_folder)
    print(f"File extensions changed successfully in '{target_folder}'.")
