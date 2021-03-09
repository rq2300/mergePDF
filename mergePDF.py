import os
from fpdf import FPDF
from PyPDF2 import PdfFileReader, PdfFileMerger

directory = "./2020_taxe"

# Convert Cover Page to pdf
cover = FPDF()
cover.add_page()
cover.set_font("Arial", size = 15)

with open(os.path.join(directory,"cover.txt"), "r") as file:
    for x in file:
        cover.cell(200, 10, txt = x, ln=1, align='C')
    cover.output(os.path.join(directory,"01-cover.pdf"))

# Merge all pdfs in directory
output = PdfFileMerger()
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        filePath = os.path.join(directory, filename)
        print(filePath)
        pdfFile = PdfFileReader(filePath)
        output.append(pdfFile)

output_path = os.path.join(directory,"02-merged.pdf")
with open(output_path, "wb") as output_stream:
    output.write(output_stream)