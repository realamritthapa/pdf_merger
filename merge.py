import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(directory, output_filename):
    directory = os.path.expanduser(directory)
    pdf_writer = PdfWriter()

    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            pdf_reader = PdfReader(filepath)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print(f'Merged PDF saved as {output_filename}')

merge_pdfs('~/Desktop/pdf_test', 'all_lecture.pdf')

