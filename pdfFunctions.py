from PyPDF2 import PdfMerger

def merge(FilePathList):
    merger = PdfMerger()

    for pdf in FilePathList:
        print(pdf)
        merger.append(pdf)
    merger.write("MergedFiles.pdf")
    merger.close()

input = ['C:/Users/walid/Desktop/Repos/PDF-Manager/Testing/Sample 1.pdf', 'C:/Users/walid/Desktop/Repos/PDF-Manager/Testing/Sample 2.pdf']
merge(input)