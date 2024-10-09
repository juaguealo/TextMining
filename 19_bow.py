from sklearn.feature_extraction.text import CountVectorizer
documentos = [
    "La minería de texto es fascinante.",
    "Los modelos de espacio vectorial son poderosos.",
    "La Bolsa de Palabras es una técnica común en minería de texto."
]
# Crear la matriz de BoW
vectorizer = CountVectorizer()
matriz_bow = vectorizer.fit_transform(documentos)
# Obtener las palabras (características) en el vocabulario
vocabulario = vectorizer.get_feature_names_out()
# Resultado
print("Matriz de BoW:")
print(matriz_bow.toarray())
print("Vocabulario:", vocabulario)