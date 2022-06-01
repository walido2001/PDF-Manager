from PyPDF2 import PdfMerger

def merge(FilePathList):
    merger = PdfMerger()

    for pdf in FilePathList:
        print(pdf)
        merger.append(pdf)
    merger.write("MergedFiles.pdf")
    merger.close()