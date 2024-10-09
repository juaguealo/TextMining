from itertools import combinations
from nltk.tokenize import sent_tokenize, word_tokenize

def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y dividirlo en frases.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        frases = sent_tokenize(texto)
    return frases

# Nombre del archivo de texto
nombre_archivo = 'articulo.txt'

# Leer el archivo y dividirlo en frases
frases_del_archivo = leer_archivo(nombre_archivo)
# Imprimir el resultado con manejo de errores
for frase in frases_del_archivo:
    try:
        print(frase)
    except UnicodeEncodeError:
        print(frase.encode('utf-8', 'replace').decode('utf-8'))