import requests
import sys

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        print("File downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print("Error downloading file:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_script.py <url> <file_path>")
    else:
        url = sys.argv[1]
        file_path = sys.argv[2]
        download_file(url, file_path)