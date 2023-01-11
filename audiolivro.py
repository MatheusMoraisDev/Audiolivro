import PyPDF2
import pyttsx3
pdf = 'Alice no País das Maravilhas.pdf'
#Abre o ebook .pdf
path = open(pdf,'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init(driverName='sapi5')
speak.setProperty('rate', 200)

#Percorre as páginas do ebook, extrai o texto e faz a leitura

text = ''

for pages in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[pages].extract_text()
    print(f'página {pages} executada')
print("Execução completa Aguarde o download do arquivo.")
speak.save_to_file(text, "audio.mp3")
speak.runAndWait()


