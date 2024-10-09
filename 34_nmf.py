import os
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

# Función para leer un archivo de texto y dividirlo en frases
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        frases = sent_tokenize(texto)
    return frases

# Carpeta que contiene los archivos de texto
carpeta_archivos = 'articulos_limpios'  # Reemplaza con la ruta correcta

# Lista para almacenar los documentos de todos los archivos
documentos_totales = []

# Iterar sobre los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta_archivos):
    if nombre_archivo.endswith(".txt"):
        ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)
        documentos_archivo = leer_archivo(ruta_archivo)
        documentos_totales.extend(documentos_archivo)

# Vectorización de documentos con TF-IDF
vectorizer_tfidf = TfidfVectorizer()
X_tfidf = vectorizer_tfidf.fit_transform(documentos_totales)

# Modelo NMF
modelo_nmf = NMF(n_components=5, init='random', random_state=42)
temas_nmf = modelo_nmf.fit_transform(X_tfidf)

# Resultado
print("Distribución de Tópicos para Documentos (NMF):")
print(temas_nmf)

# Palabras más representativas para cada tópico
palabras_clave = vectorizer_tfidf.get_feature_names_out()

# Imprimir tópicos y palabras clave
for i, t in enumerate(temas_nmf):
    print(f"Tópico {i + 1}:")
    indices_palabras_clave = t.argsort()[:-6:-1]
    palabras_clave_t = [palabras_clave[idx] for idx in indices_palabras_clave]
    print(", ".join(palabras_clave_t))
    print()
    