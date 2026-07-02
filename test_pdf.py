from app.utils.pdf_reader import PDFReader

text = PDFReader.extract_text("uploads/330c1dca-683f-4a8d-985e-c69188bfb39f.pdf")

print(text)