import os
import shutil
import zipfile
import tarfile
import gzip
import rarfile

def extract_archive(file_path, extract_path):
    _, ext = os.path.splitext(file_path)
    base_filename = os.path.basename(file_path)
    base_folder = os.path.splitext(base_filename)[0]

    if ext.lower() == '.zip':
        extract_folder = os.path.join(extract_path, base_folder)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
    elif ext.lower() == '.tar':
        extract_folder = os.path.join(extract_path, base_folder)
        with tarfile.open(file_path, 'r') as tar_ref:
            tar_ref.extractall(extract_folder)
    elif ext.lower() == '.gz':
        extract_folder = os.path.join(extract_path, base_folder)
        with gzip.open(file_path, 'rb') as gz_ref:
            with open(os.path.join(extract_folder, os.path.basename(file_path)[:-3]), 'wb') as f_out:
                shutil.copyfileobj(gz_ref, f_out)

    elif ext.lower() == '.rar':
        extract_folder = os.path.join(extract_path, base_folder)
        with rarfile.RarFile(file_path, 'r') as rar_ref:
            rar_ref.extractall(extract_folder)

    # Check if the extracted file is an archive and extract nested archives
    new_file_path = os.path.join(extract_folder, os.path.basename(file_path)[:-4])
    _, new_ext = os.path.splitext(new_file_path)

    if new_ext.lower() in ['.zip', '.tar', '.gz', '.rar']:
        extract_archive(new_file_path, extract_folder)

def scan_and_extract_archives(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file_path)

            if ext.lower() in ['.zip', '.tar', '.gz', '.rar']:
                extract_archive(file_path, root)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    scan_and_extract_archives(current_directory)
    print('Extraction completed.')
