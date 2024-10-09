from sklearn.feature_extraction.text import TfidfVectorizer
# Corpus de documentos de ejemplo
documentos = [
    "Este es un ejemplo de documento.",
    "Otro documento de ejemplo.",
    "Un tercer documento para ilustrar el cálculo de TF-IDF."
]
# Crear un objeto TfidfVectorizer
vectorizer = TfidfVectorizer()
# Ajustar y transformar los documentos
tfidf_matrix = vectorizer.fit_transform(documentos)
# Obtener el vocabulario (palabras) ordenado alfabéticamente
vocabulario = vectorizer.get_feature_names_out()
# Crear una matriz densa para visualizar mejor los resultados
tfidf_matrix_dense = tfidf_matrix.todense()
# Crear un diccionario que asocie cada palabra con su valor TF-IDF en cada documento
resultados = {}
for i, documento in enumerate(documentos):
    resultados[documento] = {vocabulario[j]: tfidf_matrix_dense[i, j] for j in range(len(vocabulario))}
# Imprimir los resultados
for documento, palabras_tfidf in resultados.items():
    print(f"\nDocumento: {documento}")
    for palabra, tfidf in palabras_tfidf.items():
        print(f"{palabra}: {tfidf:.4f}")
