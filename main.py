import argparse
import deepl
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

import protocol_reader as pr

with open('deepl_api_key.txt', 'r') as file:
    DEEPL_AUTH_KEY = file.read().strip()

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

def format_agenda(text):
    # Regular expression to match and fix agenda numbering issues
    text = re.sub(r'(\d)\s+\.\s+', r'\1. ', text)  # Fix spaces between numbers and topics
    return text

def create_refined_pdf(file_path, text, date):
    # Create a document
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    story = []

    # Define styles for different parts of the document
    styles = getSampleStyleSheet()

    # Custom styles to match the original document
    title_style = ParagraphStyle(name='Title', fontSize=14, spaceAfter=12, alignment=TA_CENTER,
                                 fontName="Helvetica-Bold")
    heading_style = ParagraphStyle(name='Heading1', fontSize=12, spaceAfter=8, fontName="Helvetica-Bold")
    subheading_style = ParagraphStyle(name='Heading2', fontSize=11, spaceAfter=8, fontName="Helvetica-Bold")
    body_style = ParagraphStyle(name='BodyText', fontSize=10, spaceAfter=6, fontName="Helvetica", leading=12)
    list_item_style = ParagraphStyle(name='ListItem', fontSize=10, leftIndent=18, spaceAfter=6)

    # Format the agenda section specifically
    text = format_agenda(text)

    # Split text into lines
    lines = text.split('\n')

    # Add title
    story.insert(0, Paragraph(f"Minutes of the Student Council Meeting on {date}", title_style))
    story.insert(1, Spacer(1, 12))

    # Main content processing (after TOC/Agenda)
    for line in lines:
        line = line.strip()

        # Check for specific sections "Legend", "Agenda", "Present"
        if line.lower() in ["legend", "agenda", "present"]:
            story.append(Paragraph(line, heading_style))
            story.append(Spacer(1, 6))

        elif line.startswith("TOP"):  # Topical Headings
            story.append(Paragraph(line, heading_style))
            story.append(Spacer(1, 6))

        elif re.match(r'\d+\.', line):  # Sub-topics (like 1., 2.)
            story.append(Paragraph(line, subheading_style))
            story.append(Spacer(1, 6))

        elif re.match(r'[a-z]\)', line):  # List items (like a), b), etc.)
            story.append(Paragraph(line, list_item_style))

        elif line:  # Normal body text
            story.append(Paragraph(line, body_style))

    # Adding a page break at the end
    story.append(PageBreak())

    # Building the PDF
    doc.build(story)

def main(date, save_path= None):
    protocol_german = pr.extract_text_from_pdf(date)
    chunks_german = split_text_by_signal_word(protocol_german, "TOP")
    chunks_translated = []
    print("Translating protocol")
    for i in range(len(chunks_german)):
        chunk_translated = translate_chunk(chunks_german[i])
        chunks_translated.append(chunk_translated)
    protocol_translated = reassemble_text(chunks_translated)
    print("Creating PDF")
    if save_path is None:
        path_saving = f"protocols/translated_protocol_test_{date.replace('.', '')}.pdf"
    else:
        path_saving = save_path + f"translated_protocol_test_{date.replace('.', '')}.pdf"
    create_refined_pdf(path_saving, protocol_translated, date)
    print(f"Saved translated protocol at {path_saving}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a date.")
    parser.add_argument('date', type=str, help="The date in 'DD.MM.YYYY' format.") # For testing use '16.05.2024'
    parser.add_argument('save_path', nargs='?', type=str, help="The path the translated document should be saved to.", default=None)
    args = parser.parse_args()
    main(args.date, args.save_path)