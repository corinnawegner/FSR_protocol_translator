---

# Protocol Translator and Formatter

## Overview

This repository contains a Python script for automating the process of downloading, translating, and formatting meeting protocols from a specified website. The tool is designed to handle protocols in German, translate them into English, and generate a refined PDF document with structured formatting.

## Features

- **PDF Downloading:** Uses Selenium to automatically download PDF files from a specified website.
- **Text Extraction:** Extracts text from downloaded PDF files using PyPDF2.
- **Text Translation:** Translates German text to English using the DeepL API.
- **PDF Formatting:** Creates a well-formatted PDF document with custom styling using ReportLab.

## Prerequisites

- Python 3.x
- Selenium
- PyPDF2
- DeepL API key
- ReportLab
- Firefox WebDriver (or other compatible WebDriver for Selenium)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/corinnawegner/FSR_protocol_translator.git
   cd FSR_protocol_translator
   ```

2. **Install required Python packages:**

   ```bash
   pip install selenium pypdf2 deepl reportlab
   ```

3. **Download the Firefox WebDriver:**

   - Follow the instructions [here](https://github.com/mozilla/geckodriver/releases) to download and install the WebDriver.

4. **Get your DeepL API key:**

   - Sign up for a DeepL account and obtain your API key from [DeepL](https://www.deepl.com/pro#developer).

5. **Save your DeepL API key:**

   - Create a file named `deepl_api_key.txt` in the root directory of the repository and paste your API key into this file.

## Usage

To process a protocol, run the following command with the desired date in the format `DD.MM.YYYY`:

```bash
python script.py 16.05.2024
```

Replace `16.05.2024` with the date of the protocol you want to process.

## Script Details

1. **`script.py`**
   - Main script to handle text extraction, translation, and PDF generation.
   - Uses `argparse` for command-line arguments.

2. **`protocol_reader.py`**
   - Contains functions to interact with the website, download the PDF, and extract text using PyPDF2.

## Configuration

- **DeepL API Key:** Ensure `deepl_api_key.txt` contains your valid API key.
- **PDF Storage Path:** Adjust the `protocols` directory path in the script as needed to match your environment.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

---

