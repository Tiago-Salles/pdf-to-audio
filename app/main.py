import pyttsx3
import PyPDF2

book = open("Einstein_Relativity.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

for voice in speaker.getProperty("voices"):
    if(voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
        speaker.setProperty("voice", voice.id)
speaker.setProperty("rate", 150)

for page in range(6, pages):
    _page = pdfReader.getPage(page)
    pageContent = _page.extractText()
    speaker.say(pageContent)

speaker.runAndWait()
