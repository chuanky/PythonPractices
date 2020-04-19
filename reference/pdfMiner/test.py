from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from pdf_settings import Settings

m_settings = Settings()
file_path = 'reference/webCrawler/downloads/公告.pdf'
output_string = StringIO()
output_dir = m_settings.txt_file_dir
file_name = '公告.txt'

with open(file_path, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

with open(output_dir + file_name, 'w') as out_file:
    out_file.write(output_string.getvalue())


