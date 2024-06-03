from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import fitz

def extract_text_from_pdf():
    driver = webdriver.Firefox()
    driver.get('https://fsr.physik.uni-goettingen.de/der-fachschaftsrat/sitzungsprotokolle/')

    html_protocol = driver.find_element(By.LINK_TEXT, '16.05.2024')
    time.sleep(5)
    html_protocol.click()

    # Wait for a while to ensure the PDF is loaded
    time.sleep(5)

    # Get the URL of the opened PDF
    pdf_url = driver.current_url

    # Close the browser
    driver.quit()

    # Download the PDF file
    response = requests.get(pdf_url)
    pdf_path = "Protokoll_20240516.pdf"

    with open(pdf_path, 'wb') as f:
        f.write(response.content)

    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(pdf_path)

    # Extract text from each page and concatenate it
    all_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        all_text += page.get_text()

    # Close the document
    pdf_document.close()

    # Print the content
    return all_text
