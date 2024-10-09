from nltk.sentiment import SentimentIntensityAnalyzer
# Texto de ejemplo
texto = "La minería de texto nos permite procesar textos."
# Crear un objeto SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# Obtener el análisis de sentimientos
sentimiento = analyzer.polarity_scores(texto)
# Imprimir el resultado
print(f"Texto: {texto}")
print(f"Análisis de Sentimientos: {sentimiento}")
# Clasificar la polaridad del sentimiento
if sentimiento['compound'] >= 0.05:
    print("El texto es positivo.")
elif sentimiento['compound'] <= -0.05:
    print("El texto es negativo.")
else:
    print("El texto es neutral.")