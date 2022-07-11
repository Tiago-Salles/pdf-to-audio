import pyttsx3
import PyPDF2

book = open("Advanced C.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
page = pdfReader.getPage(181)
pageContent = page.extractText()
speaker.say(pageContent)
speaker.runAndWait()
