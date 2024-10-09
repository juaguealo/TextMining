from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import sent_tokenize

# Función para leer un archivo de texto y dividirlo en frases
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        frases = sent_tokenize(texto)
    return frases

# Nombre del archivo de texto
nombre_archivo = 'articulo_limpio2.txt'
# Leer el archivo y dividirlo en frases
documentos = leer_archivo(nombre_archivo)

# Vectorización de documentos con TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documentos)

# Modelo LDA
modelo_lda = LatentDirichletAllocation(n_components=5, random_state=42)
temas_lda = modelo_lda.fit_transform(X)

# Obtener las palabras clave más representativas para cada tópico
palabras_clave_tópicos = []
num_palabras_clave = 10

# Resultado
print("Distribución de Tópicos para el Documento:")
print(temas_lda)

for tópico, distribución in enumerate(modelo_lda.components_):
    palabras_clave = [vectorizer.get_feature_names_out()[i] for i in distribución.argsort()[:-num_palabras_clave - 1:-1]]
    palabras_clave_tópicos.append((tópico, palabras_clave))

# Imprimir las palabras clave para cada tópico
for tópico, palabras_clave in palabras_clave_tópicos:
    print(f"Tópico {tópico + 1}: {', '.join(palabras_clave)}")
