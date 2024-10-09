from nltk.tokenize import word_tokenize, sent_tokenize
texto = "La tokenización es esencial en minería de texto. ¿No lo crees?"
# Tokenización de palabras
tokens_palabras = word_tokenize(texto)
# Tokenización de frases
tokens_frases = sent_tokenize(texto)
# Resultado
print("Tokens de palabras:", tokens_palabras)
print("Tokens de frases:", tokens_frases)
