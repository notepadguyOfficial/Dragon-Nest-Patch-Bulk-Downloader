import requests
import os
import progressbar
import validators
import time

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_url(url):
    """Check if it's a correct and reachable URL."""
    if not validators.url(url):
        return False
        
    return True

def convert_bytes(size):
    """Convert bytes to a human-readable format (B, KB, MB, GB)."""
    if size == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB")
    i = 0
    while size >= 1024 and i < len(size_name) - 1:
        size /= 1024.0
        i += 1
    return f"{size:.1f} {size_name[i]}"

def download_file(url, file_path):
    """Downloads a file from a URL with a color-coded progress bar."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_length = int(response.headers.get('content-length', 0))
        
        with open(file_path, 'wb') as file:
            fixed_width = 50
            bar_width = fixed_width - 20
            
            widgets = [
                f"Downloading {os.path.basename(file_path)} ({convert_bytes(total_length)}) ",
                progressbar.Bar(marker='━', left=GREEN, right=RESET, width=bar_width),
                ' ',
                progressbar.FormatLabel(f'{GREEN}0 B/{convert_bytes(total_length)}{RESET}', width=25),
                ' ', f'{RED}', progressbar.FileTransferSpeed(), f'{RESET}',
                ' ', f'{BLUE}', progressbar.ETA(), f'{RESET}'
            ]
            
            with progressbar.ProgressBar(max_value=total_length, widgets=widgets) as bar:
                current_downloaded = 0
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        current_downloaded += len(chunk)
                        bar.update(current_downloaded)
                        widgets[3] = progressbar.FormatLabel(f'{GREEN}{convert_bytes(current_downloaded)}/{convert_bytes(total_length)}{RESET}', width=25)
                        bar.widgets = widgets
                        bar.update(current_downloaded)

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def main():
    while True:
        url_base = input("Enter base URL: ")
        if not check_url(url_base):
            print("Invalid or unreachable URL. Retrying in 5 seconds...")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        break
            
    start = int(input("Download Patch Starting From: "))
    end = int(input("Up to: "))

    for i in range(start, end + 1):
        padded_index = f"{i:08d}"
        directory = padded_index
        os.makedirs(directory, exist_ok=True)
        
        files = {
            'pak': (f"{url_base}{padded_index}/Patch{padded_index}.pak", f"{directory}/Patch{padded_index}.pak"),
            'md5': (f"{url_base}{padded_index}/Patch{padded_index}.pak.MD5", f"{directory}/Patch{padded_index}.pak.MD5"),
            'txt': (f"{url_base}{padded_index}/Patch{padded_index}.txt", f"{directory}/Patch{padded_index}.txt"),
        }
        for file_type, (url, file_path) in files.items():
            download_file(url, file_path)

if __name__ == '__main__':
    main()
