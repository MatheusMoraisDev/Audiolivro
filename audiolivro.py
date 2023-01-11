import PyPDF2
import pyttsx3

#Abre o ebook .pdf
path = open('Alice no País das Maravilhas.pdf','rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init(driverName='sapi5')
speak.setProperty('rate', 200)

#Percorre as páginas do ebook, extrai o texto e faz a leitura
for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()

sn = input("Você deseja exportar esse áudiolivro para mp3?('s' ou 'n'): ")
if sn == 's':
    speak.
