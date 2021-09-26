from PyPDF2 import PdfFileReader

pdffileobject = open("book.pdf", "rb")
reader = PdfFileReader(pdffileobject)

bookmarks = reader.getOutlines()

bookarr = []
for b in bookmarks:
    bookarr.append(reader.getDestinationPageNumber(b) + 1)

#print(reader.outlines["/Title"],reader.outlines["/Page"])

titlearr = []
for i in reader.outlines :
    titlearr.append(i["/Title"])

txtfile = open("book.txt","w")

for i in range(len(titlearr)):
    txtfile.write("+"+'"' +str(titlearr[i]) + '"' + "|" + str(bookarr[i])+"\n")

txtfile.close()