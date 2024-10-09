import networkx as nx
from itertools import combinations
from nltk.tokenize import word_tokenize

# Lista de documentos de ejemplo
documentos = ["El análisis de texto es fascinante.", "La minería de datos revela patrones interesantes.", "Los grafos son fundamentales en la representación de relaciones."]

# Tokenización y construcción del grafo semántico
grafo_semantico = nx.Graph()

for documento in documentos:
    tokens = word_tokenize(documento.lower())
    
    # Agregar nodos y aristas al grafo
    for palabra in tokens:
        if not grafo_semantico.has_node(palabra):
            grafo_semantico.add_node(palabra)

    # Conectar todas las palabras que aparecen juntas en el mismo documento
    for par in combinations(tokens, 2):
        if grafo_semantico.has_edge(*par):
            grafo_semantico[par[0]][par[1]]['weight'] += 1
        else:
            grafo_semantico.add_edge(*par, weight=1)

# Visualización del grafo semántico
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(grafo_semantico)
nx.draw(grafo_semantico, pos, with_labels=True, font_size=10, font_color='black', node_color='skyblue', node_size=2000, edge_color='gray', linewidths=0.5)
plt.title('Grafo Semántico')
plt.show()
