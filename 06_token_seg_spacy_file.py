import spacy
def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y dividirlo en frases.
    """
    nlp = spacy.load('en_core_web_sm')

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        # Tokenización de palabras y frases
        doc = nlp(texto)
        # Resultado
        tokens_palabras = [token.text for token in doc]
        frases = [sent.text for sent in doc.sents]
    return frases

# Nombre del archivo de texto
nombre_archivo = 'articulo.txt'

# Leer el archivo y dividirlo en frases
frases_del_archivo = leer_archivo(nombre_archivo)

# Imprimir el resultado con manejo de errores
for frase in frases_del_archivo:
    try:
        print(frase)
    except:
        print(frase.encode('utf-8', 'replace').decode('utf-8'))
