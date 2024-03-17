import fitz
import argparse
import pathlib

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def main():
    parser = argparse.ArgumentParser(description='Convert PDF to Text')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file')
    args = parser.parse_args()

    pdf_file = args.pdf_file
    if not pdf_file.lower().endswith('.pdf'):
        raise ValueError("The file must be a PDF")

    txt_file = pathlib.Path(pdf_file).with_suffix('.txt')
    text = pdf_to_text(pdf_file)
    save_text_to_file(text, txt_file)

if __name__ == "__main__":
    main()
