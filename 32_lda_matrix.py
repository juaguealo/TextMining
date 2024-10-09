from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y devolver su contenido.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    return texto

# Nombre del archivo de texto
nombre_archivo = 'articulo_limpio2.txt'
# Leer el contenido del archivo
texto = leer_archivo(nombre_archivo)

# Vectorización de documentos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([texto])  # Aquí estamos tratando el texto como un solo documento

# Modelo LDA
modelo_lda = LatentDirichletAllocation(n_components=5, random_state=42)
temas_lda = modelo_lda.fit_transform(X)

# Resultado
print("Distribución de Tópicos para el Documento:")
print(temas_lda)
