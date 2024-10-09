import spacy
nlp = spacy.load("es_core_news_sm")
texto = "La eliminación de stop words es un paso importante en minería de texto."
# Tokenización y eliminación de stop words
doc = nlp(texto)
tokens_sin_stopwords = [token.text for token in doc if not token.is_stop]
# Resultado
print("Tokens sin stop words:", tokens_sin_stopwords)
