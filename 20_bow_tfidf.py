from sklearn.feature_extraction.text import TfidfVectorizer
documentos = [
    "Este es un ejemplo de documento.",
    "Otro documento de ejemplo.",
    "Un tercer documento para ilustrar el cálculo de TF-IDF."
]
# Crear la matriz TF-IDF
vectorizer_tfidf = TfidfVectorizer()
matriz_tfidf = vectorizer_tfidf.fit_transform(documentos)
# Obtener las palabras (características) en el vocabulario
vocabulario_tfidf = vectorizer_tfidf.get_feature_names_out()
# Resultado
print("Matriz TF-IDF:")
print(matriz_tfidf.toarray())
print("Vocabulario TF-IDF:", vocabulario_tfidf)