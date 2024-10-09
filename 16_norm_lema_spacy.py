import spacy

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Definir la palabra
palabra = "lematizado"

# Lematización
palabra_lematizada = nlp(palabra)[0].lemma_

# Resultado
print("Palabra original:", palabra)
print("Palabra después de lematización:", palabra_lematizada)

