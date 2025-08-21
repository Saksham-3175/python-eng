from PyPDF2 import PdfWriter
merger = PdfWriter()

try:
    pdfs = ["ml.pdf", "pml.pdf"]
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("merged_pdf.pdf")
    merger.close()

except Exception as e:
    print(f"{e}")