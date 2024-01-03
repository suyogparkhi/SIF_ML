from PyPDF2 import PdfReader

def convert_pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            
            # Remove spaces from each line and concatenate
            text += ''.join(page_line.strip() for page_line in page_text.split('\n'))

    return text

# Example usage
pdf_path = 'Aditya Pande _resume.pdf'
result_text = convert_pdf_to_text(pdf_path)
print(result_text)

