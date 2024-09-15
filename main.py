import deepl
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

import protocol_reader as pr

text_test = pr.extract_text_from_pdf()

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


def create_refined_pdf(file_path, text): #todo: make the table of contents nicer
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

    # Start processing the content
    lines = text.split('\n')

    # Assume the first line is the title
    story.append(Paragraph("Minutes of the Student Council Meeting on 16.05.2024", title_style))
    story.append(Spacer(1, 12))

    for line in lines:
        line = line.strip()

        if line.startswith("TOP"):  # Topical Headings
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
create_refined_pdf('translated_protocol_test.pdf', result)

