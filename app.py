

from flask import Flask, render_template, request
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtener la imagen del formulario
    imagen = request.files['imagen']
    imagen.save('imagen.png')

    # Extraer texto de la imagen
    texto = pytesseract.image_to_string(Image.open('imagen.png'))

    # Dividir el texto en líneas y asignar a los campos de entrada
    lineas = texto.split('\n')
    campo1 = lineas[0]
    campo2 = lineas[1]
    campo3 = lineas[2]

    return render_template('index.html', campo1=campo1, campo2=campo2, campo3=campo3)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request
# from pdf2image import convert_from_path
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     # Obtener el archivo PDF del formulario
#     archivo_pdf = request.files['archivo_pdf']
    
#     # Convertir el PDF a una lista de imágenes
#     imagenes = convert_from_path(archivo_pdf)
    
#     # Inicializar variable para almacenar el texto extraído
#     texto = ""

#     # Extraer texto de cada imagen
#     for img in imagenes:
#         # Convertir la imagen a texto utilizando pytesseract
#         texto += pytesseract.image_to_string(img)
    
#     # Dividir el texto en líneas y asignar a los campos de entrada
#     lineas = texto.split('\n')
#     campo1 = lineas[0]
#     campo2 = lineas[1]
#     campo3 = lineas[2]

#     return render_template('index.html', campo1=campo1, campo2=campo2, campo3=campo3)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request
# from PyPDF2 import PdfReader

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     # Obtener el archivo PDF del formulario
#     archivo_pdf = request.files['archivo_pdf']
    
#     # Crear un objeto PdfReader para leer el PDF
#     pdf_reader = PdfReader(archivo_pdf)
    
#     # Extraer texto de todas las páginas del PDF
#     texto = ""
#     for page_num in range(len(pdf_reader.pages)):
#         texto += pdf_reader.pages[page_num].extract_text()
    
#     # Dividir el texto en líneas y asignar a los campos de entrada
#     lineas = texto.split('\n')
#     campo1 = lineas[0]
#     # campo2 = lineas[1]
#     # campo3 = lineas[2]

#     return render_template('index.html', campo1=campo1, campo2=campo2, campo3=campo3)

# if __name__ == '__main__':
#     app.run(debug=True)
