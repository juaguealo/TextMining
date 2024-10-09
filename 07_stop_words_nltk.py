from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
texto = "La eliminación de stop words es un paso importante en minería de texto."
# Tokenización
tokens = word_tokenize(texto)
# Eliminación de stop words
stop_words = set(stopwords.words("spanish"))
tokens_sin_stopwords = [word for word in tokens if word.lower() not in stop_words]
# Resultado
print("Tokens sin stop words:", tokens_sin_stopwords)
