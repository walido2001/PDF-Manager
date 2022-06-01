from posixpath import expanduser
from PyPDF2 import PdfMerger
import shutil
import os
import platform

def merge(FilePathList, outputLocation):
    merger = PdfMerger()

    for pdf in FilePathList:
        # print(pdf)
        merger.append(pdf)
    merger.write("MergedFiles.pdf")

    platformUsed = platform.system()

    if outputLocation is not None:
        outputLocation += "\MergedFiles.pdf"
        shutil.move("MergedFiles.pdf", outputLocation)
    else:
        if platformUsed == "Windows":
            DesktopPath = os.environ['USERPROFILE'] + "\Desktop"
        # or Mac
        else:
            DesktopPath = os.expanduser("~/Desktop")

        shutil.move("MergedFiles.pdf", DesktopPath)
    merger.close()
    
# # C:/Users/walid/Documents
# input = ['C:/Users/walid/Desktop/Repos/PDF-Manager/Testing/Sample 1.pdf', 'C:/Users/walid/Desktop/Repos/PDF-Manager/Testing/Sample 2.pdf']
# location = 'C:/Users/walid/Documents'

# merge(input, location)