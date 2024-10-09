from gensim.models import KeyedVectors

# Ruta al archivo GloVe preentrenado (por ejemplo, glove.6B.50d.txt)
glove_file = 'glove/glove.6B/glove.6B.50d.txt'

# Cargar el modelo GloVe directamente
modelo_glove = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True)

# Obtener el vector de una palabra
vector_mineria_glove = modelo_glove['mining']  # Ajusta la palabra según tu necesidad

# Imprimir el vector resultante
print("Vector de 'mining' según GloVe:")
print(vector_mineria_glove)
