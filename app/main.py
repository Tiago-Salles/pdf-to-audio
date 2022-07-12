import pyttsx3
import PyPDF2

book = open("Advanced C.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

for voice in speaker.getProperty("voices"):
    if(voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
        speaker.setProperty("voice", voice.id)
speaker.setProperty("rate", 125)
page = pdfReader.getPage(181)
pageContent = page.extractText()
speaker.say(pageContent)
speaker.runAndWait()
