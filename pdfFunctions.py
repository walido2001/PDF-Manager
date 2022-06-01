import PyPDF2 as pyPDF

def merge(FilePathList):
    merger = pyPDF()

    for pdf in FilePathList:
        merger.add(pdf)
    merger.write("MergedFiles.pdf")
    merger.close()
