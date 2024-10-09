import spacy
from nltk.tokenize import sent_tokenize, word_tokenize

def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y dividirlo en frases.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        frases = texto
    return frases

# Nombre del archivo de texto
nombre_archivo = 'articulo_limpio2.txt'
# Leer el archivo y dividirlo en frases
texto = leer_archivo(nombre_archivo)
# Supongamos que 'texto' contiene el documento de interés.
# Cargar el modelo de lenguaje de Spacy para NER (Reconocimiento de Entidades con Nombre)
nlp = spacy.load("en_core_web_sm")
# Aplicar NER al texto
doc = nlp(texto)
# Obtener entidades reconocidas
entidades = [(ent.text, ent.label_) for ent in doc.ents]
# Resultado
print("Entidades Reconocidas:")
print(entidades)
