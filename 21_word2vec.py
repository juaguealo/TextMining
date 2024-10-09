from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
documentos = [
    "Este es un ejemplo de documento.",
    "Otro documento de ejemplo.",
    "Un tercer documento para ilustrar el cálculo de TF-IDF."
]
# Tokenizar documentos
documentos_tokenizados = [word_tokenize(doc) for doc in documentos]
# Entrenar el modelo Word2Vec
modelo_word2vec = Word2Vec(sentences=documentos_tokenizados, vector_size=100, window=5, min_count=1, workers=4)
# Obtener el vector de una palabra
vector_mineria = modelo_word2vec.wv['ejemplo']
# Resultado
print("Vector de 'ilustrar' según Word2Vec:")
print(vector_mineria)
