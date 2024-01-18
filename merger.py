# 1. import libraries
import PyPDF2
import sys
import os

# 2. get arguments from command line
arguments = sys.argv
pdf_folder = arguments[1]
name_of_merged_file = arguments[2]

# 3. get folder of pdf files
cwd = os.getcwd()
pdf_directory_str = os.path.join(cwd, pdf_folder)
pdf_directory = os.fsdecode(pdf_directory_str)

# 4. initialize a merger
merger = PyPDF2.PdfFileMerger()

# 5. iterate through the pdfs
for pdf in os.listdir(pdf_directory):
    
    # 6. add pdf to merger
    merger.append(pdf)

# 6. write the new merged pdf file
merger.write(f'{name_of_merged_file}.pdf')