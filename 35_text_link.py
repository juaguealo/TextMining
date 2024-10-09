from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

# Función para procesar y tokenizar el texto
def procesar_texto(texto):
    # Tokenización
    tokens = word_tokenize(texto.lower())
    # Eliminar stopwords y realizar stemming
    stop_words = set(stopwords.words('english'))
    tokens = [PorterStemmer().stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

# Cargar el conjunto de datos de noticias
url = "texto_sumarizacion.txt"
df = pd.read_csv(url)

# Imprimir los nombres de las columnas
print("Nombres de las columnas:")
print(df.columns)

# Verificar si 'reasoning' está presente en las columnas
if ' reasoning' not in df.columns:
    print("La columna ' reasoning' no está presente en el conjunto de datos.")
    # Puedes ajustar el nombre de la columna según sea necesario.

# Aplicar la función a los documentos si 'reasoning' está presente
if ' reasoning' in df.columns:
    df['tokens'] = df[' reasoning'].apply(procesar_texto)
    # Convertir tokens a texto para CountVectorizer
    df['texto_procesado'] = df['tokens'].apply(' '.join)
    # Construir matriz de co-ocurrencia
    vectorizer = CountVectorizer()
    matriz_coocurrencia = vectorizer.fit_transform(df['texto_procesado'])
    # Crear un DataFrame para visualizar la matriz
    df_coocurrencia = pd.DataFrame(matriz_coocurrencia.toarray(), columns=vectorizer.get_feature_names_out())
    print(df_coocurrencia.head())

    # Construir grafo a partir de la matriz de co-ocurrencia
    grafo_semantico = nx.from_numpy_array(matriz_coocurrencia.T * matriz_coocurrencia)

    # Calcular medidas de centralidad
    centralidad = nx.degree_centrality(grafo_semantico)
    betweenness = nx.betweenness_centrality(grafo_semantico)

    # Asignar medidas de centralidad a nodos
    nx.set_node_attributes(grafo_semantico, centralidad, 'degree_centrality')
    nx.set_node_attributes(grafo_semantico, betweenness, 'betweenness')

    # Visualizar la red semántica
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(grafo_semantico)

    # Obtener la centralidad de grado
    centralidad = nx.degree_centrality(grafo_semantico)

    # Crear un objeto mappable con scatter
    scatter = nx.draw_networkx_nodes(
        grafo_semantico,
        pos,
        node_color=list(centralidad.values()),
        cmap='viridis',
        node_size=[v * 3000 for v in centralidad.values()]
    )

    # Añadir barra de colores
    plt.colorbar(scatter, label='Centralidad de Grado')

    # Dibujar las aristas
    nx.draw_networkx_edges(grafo_semantico, pos, edge_color='gray')

    plt.title('Red Semántica de Términos Clave')
    plt.show()

