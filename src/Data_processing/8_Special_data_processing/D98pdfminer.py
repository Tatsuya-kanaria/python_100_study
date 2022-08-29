# %%
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams


pdf_data = open('./data/サンプル_PDF.pdf', 'rb')
txt_file = './data/サンプル_PDF.txt'
out_data = open(txt_file, mode='w')

rscmgr = PDFResourceManager()
laprms = LAParams()
device = TextConverter(rscmgr, out_data, laparams=laprms)
itprtr = PDFPageInterpreter(rscmgr, device)

for page in PDFPage.get_pages(pdf_data):
    itprtr.process_page(page)

out_data.close()
device.close()
pdf_data.close()

# with 自動で閉じてくれる
with open('./data/サンプル_PDF.txt', mode='r') as f:
    content = f.read()
print(content)

# %%
