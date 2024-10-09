import networkx as nx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt

def leer_archivo(nombre_archivo):
    """
    Función para leer un archivo de texto y dividirlo en frases.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        frases = sent_tokenize(texto)
    return frases

# Nombre del archivo de texto
nombre_archivo = 'texto_sumarizacion.txt'  # Reemplaza 'tu_archivo.txt' con tu propio archivo
# Leer el archivo y dividirlo en frases
documentos = leer_archivo(nombre_archivo)
# Supongamos que 'documentos' contiene textos.
# Vectorización con TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documentos).toarray()
# Cálculo de similitud de coseno entre oraciones
similitud_cos = np.dot(X, X.T)
# Creación de un grafo ponderado
grafo_dirigido = nx.DiGraph()
grafo_dirigido.add_weighted_edges_from([(i, j, similitud_cos[i, j]) for i in range(similitud_cos.shape[0]) for j in range(similitud_cos.shape[1])])

# Visualización del grafo dirigido, en este caso puede llevar bastante tiempo de proceso
pos = nx.spring_layout(grafo_dirigido)  # Puedes cambiar el algoritmo de disposición según tus preferencias
etiquetas = {i: i for i in range(len(documentos))}
pesos = nx.get_edge_attributes(grafo_dirigido, 'weight')
nx.draw(grafo_dirigido, pos, labels=etiquetas, with_labels=True, font_size=8, node_size=500, node_color='lightblue')
nx.draw_networkx_edge_labels(grafo_dirigido, pos, edge_labels=pesos, font_color='red')
plt.title('Grafo Dirigido Ponderado')
plt.show()
# Fin de visualización


# Aplicación de algoritmo PageRank para obtener la importancia de las oraciones
puntuaciones = nx.pagerank(grafo_dirigido)
# Selección de las oraciones más importantes
oraciones_importantes = sorted(((i, puntuacion) for i, puntuacion in enumerate(puntuaciones)), key=lambda x: x[1], reverse=True)[:5]
oraciones_resumen = [documentos[i] for i, _ in oraciones_importantes]
# Resultado
print("Resumen Extractivo:")
print(oraciones_resumen)