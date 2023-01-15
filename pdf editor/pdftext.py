from PyPDF2 import PdfReader

reader = PdfReader("dict.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[37]
text = page.extract_text()

file1=open("pw.txt","w")
file1.write(text)