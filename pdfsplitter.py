from PyPDF2 import PdfFileReader, PdfFileWriter

#TODO Put the input pdf fileName below
inputPdfFileName = "Name of input PDF File"
inputPdfFile = open(inputPdfFileName, "rb")

inputPdfReader = PdfFileReader(inputPdfFile)
output = PdfFileWriter()

if inputPdfReader.isEncrypted:
    print("File is encrypted and cannot be split")
    exit()
    
#TODO First Number of Range is startPageNumber
#TODO Second Number of Range is endPageNumber
for i in range(1, 2):
    output.addPage(inputPdfReader.getPage(i))

#TODO Put the output pdf fileName below
splitFile = open ("Name of output PDF File", "wb")

print("File split successfully")
output.write(splitFile)
splitFile.close()
inputPdfFile.close()