import PyPDF2

def getPdfFile(fileName):
    pdfFile = PyPDF2.PdfFileReader(open(fileName, "rb"))
    docInfo = pdfFile.getDocumentInfo()
    for info in docInfo:
        print(info + " : " + docInfo[info])

getPdfFile("resources/lorem.pdf")