import os
from pdf2docx import Converter

input_folder = 'Input'
output_folder = 'Output'
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
for pdf_file in pdf_files:
	print(f"Converting: {pdf_file}") # Debug print
	pdf_path = os.path.join(input_folder, pdf_file)
	docx_name = os.path.splitext(pdf_file)[0] + '.docx'
	docx_path = os.path.join(output_folder, docx_name)
	if not os.path.exists(docx_path):
		cv = Converter(pdf_path)
		cv.convert(docx_path)
		cv.close()
		print(f"Converted: {pdf_file} -> {docx_name}")
	else:
		print(f"Already exists: {docx_name}")
print("All available PDFs converted!")