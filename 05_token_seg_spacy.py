import spacy
nlp = spacy.load("es_core_news_sm")
texto = "La tokenización es esencial en minería de texto. ¿No lo crees?"
# Tokenización de palabras y frases
doc = nlp(texto)
# Resultado
tokens_palabras = [token.text for token in doc]
tokens_frases = [sent.text for sent in doc.sents]
print("Tokens de palabras:", tokens_palabras)
print("Tokens de frases:", tokens_frases)
