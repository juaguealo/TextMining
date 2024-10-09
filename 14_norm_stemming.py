from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("spanish")
palabra = "minería"
# Stemming
palabra_stem = stemmer.stem(palabra)
# Resultado
print("Palabra original:", palabra)
print("Palabra después de stemming:", palabra_stem)
