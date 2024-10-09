from summarizer import Summarizer

def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y devolver el contenido.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

# Nombre del archivo de texto
nombre_archivo = 'texto_sumarizacion.txt'
# Leer el archivo
contenido_articulo = leer_archivo(nombre_archivo)

# Inicialización del modelo BERT para sumarización abstractiva
modelo_bert = Summarizer()

# Generación del resumen abstractivo
resumen_abstractivo = modelo_bert(contenido_articulo)

# Resultado
print("Resumen Abstractivo:")
print(resumen_abstractivo)
