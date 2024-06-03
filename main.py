import deepl
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import protocol_reader as pr

text_test = pr.extract_text_from_pdf()

DEEPL_AUTH_KEY = "a6da2cc8-76a5-40e4-8a2c-fe08b7aa288c:fx"
translator = deepl.Translator(DEEPL_AUTH_KEY)

def split_text_by_signal_word(text, signal_word="TOP"):
    chunks = re.split(f'(?=^{signal_word})', text, flags=re.MULTILINE)
    return chunks

def translate_chunk(text):
    result = translator.translate_text(text, target_lang="EN-US")
    return result.text

def reassemble_text(chunks):
    protocol_translated = ''.join(chunks)
    return protocol_translated

def write_document(file_path, text):
    # Create a canvas object
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Define a basic style for the text
    c.setFont("Helvetica", 12)

    # Split the text into lines
    lines = text.split('\n')

    # Set initial position
    x = 40
    y = height - 40

    # Add each line to the PDF
    for line in lines:
        if y < 40:  # Check if the y position is too low
            c.showPage()  # Create a new page
            c.setFont("Helvetica", 12)  # Reset font
            y = height - 40

        c.drawString(x, y, line)
        y -= 15

    c.save()


def main_function(protocol_german):
    chunks_german = split_text_by_signal_word(protocol_german, "TOP")
    chunks_translated = []
    for i in range(len(chunks_german)):
        chunk_translated = translate_chunk(chunks_german[i])
        print(chunk_translated)
        chunks_translated.append(chunk_translated)
    print(chunks_translated)
    protocol_translated = reassemble_text(chunks_translated)
    return protocol_translated

result = main_function(text_test)
print(result)
write_document('protocol_test.pdf', result)