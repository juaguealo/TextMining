import spacy
# Cargar el modelo lingüístico para español (o el idioma que necesites)
nlp = spacy.load("es_core_news_sm")  # Cambia 'es' por el código de idioma correspondiente
def tokenizar_con_spacy(texto):
    # Procesar el texto con Spacy
    doc = nlp(texto)
    # Obtener las palabras tokenizadas
    palabras_tokenizadas = [token.text for token in doc]
    return palabras_tokenizadas
# Ejemplo de uso
texto_ejemplo = "La minería de texto es una disciplina fascinante."
palabras_tokenizadas = tokenizar_con_spacy(texto_ejemplo)
# Imprimir el resultado
print(palabras_tokenizadas)
