# Dragon-Nest-Patch-Bulk-Downloader
This is a simple Python script designed to download files from a specified base URL in a structured manner. It utilizes progress bars and file size conversion to provide a user-friendly experience.

## Features

- Validates URLs to ensure they are correct and reachable.
- Downloads files with a visually appealing, color-coded progress bar.
- Converts file sizes into a human-readable format (B, KB, MB, GB).
- Supports downloading multiple files by generating URLs based on a user-defined range.

## Requirements

To run this script, you need:

- Python 3.x
- The following Python packages:
  - [requests]()
  - [progressbar2](https://progressbar-2.readthedocs.io/en/latest/)
  - [validators](https://validators.readthedocs.io/en/latest/)

You can install the required packages using pip:

```bash
pip install requests progressbar2 validators
```

## Usage

1. Clone this repository or download the script.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using:
```bash
python main.py
```
4. Follow the prompts:
   - Enter the base URL from which you want to download files.
   - Specify the range of patch numbers to download (e.g., starting from 1 to 10).

**!Note**
- The script will create directories named after each patch number and download the following files into them.

## URL

- SEA: `http://patchsea.dragonnest.com/Game/DragonNest/Patch/`
- SDO: `NA`
- KR: `NA`
- TH: `NA`
- JP: `NA`
