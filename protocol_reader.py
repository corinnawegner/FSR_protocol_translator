from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import PyPDF2


def extract_text_from_pdf():
    # Set up the Selenium WebDriver (Firefox)
    driver = webdriver.Firefox()
    driver.get('https://fsr.physik.uni-goettingen.de/der-fachschaftsrat/sitzungsprotokolle/')

    # Click the link to download the PDF
    html_protocol = driver.find_element(By.LINK_TEXT, '16.05.2024')
    time.sleep(5)  # Wait for 5 seconds
    html_protocol.click()

    # Wait for the page to load completely
    time.sleep(5)

    # Get the URL of the opened PDF
    pdf_url = driver.current_url

    # Close the browser after retrieving the URL
    driver.quit()

    # Download the PDF from the URL
    response = requests.get(pdf_url)
    pdf_path = "Protokoll_20240516.pdf"

    # Save the downloaded PDF to a file
    with open(pdf_path, 'wb') as f:
        f.write(response.content)

    # Open and read the PDF using PyPDF2
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        all_text = ""

        # Extract text from each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            all_text += page.extract_text()

    # Return the extracted text
    return all_text


# Call the function and print the output
extracted_text = extract_text_from_pdf()
print(extracted_text)
