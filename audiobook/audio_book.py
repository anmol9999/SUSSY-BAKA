import pyttsx3
import PyPDF2


book = open('pulkit.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractedText()
    speaker.say(text)
    speaker.runAndWait()