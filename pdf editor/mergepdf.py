from PyPDF2 import PdfWriter
merger = PdfWriter()
fr=open("finfo.txt",'r')
alst=fr.read().split("\n")
print(alst)
for pdf in alst:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
print("<Done>")
merger.close()