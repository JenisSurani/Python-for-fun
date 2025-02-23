from pypdf import PdfWriter
import os

# choose your directory make sure all pdf you want to merge is in same directory
directory="Your Path Here"


# don't use \ because it is escape character in python 
# instead of use \ use \\ "or" use /(forwardslash) "or" use raw strings(r"")

# example= "C://Myfile//temp//New folder"
# example= "C:\Myfile\temp\New folder" 
# example= r"C:/Myfile/temp/New folder"


#collecting all the pdfs from directory
pdfInFolder = [pdf for pdf in os.listdir(directory) if pdf.endswith(".pdf")]

# to merge the pdf use PdfWriter class:
#creating an object of PdfWriter class
merger=PdfWriter()

# Append each PDF to the writer
for pdf in pdfInFolder:
    
    # first we need to create the path
    path=os.path.join(directory,pdf)
    
    merger.append(path)
  
# save the merged pdf as name given
savedLocation = os.path.join(directory, "MergedPDF.pdf")  # Save in the same directory

if os.path.exists(savedLocation):
    print("Already done")
else:
    merger.write(savedLocation)
    merger.close() # good practice to close the object to prevent any data loss!

    print(f"{pdfInFolder}   →  \"MergedPdf\"") # your pdf name here
    print(f"Please Check your {directory}")


# Author : Jenis Surani
# Topic  : MergeThePDF
# Date   : 23/02/2025