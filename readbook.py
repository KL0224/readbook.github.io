import pyttsx3
import PyPDF2

book = open("s.pdf","rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[0].id)
for num in range(2, pages):
    page = pdfReader.pages[8]
    text = page.extract_text()
    bot.say(text)
    bot.runAndWait()

