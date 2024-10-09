from textblob import TextBlob
# Texto de ejemplo
texto = "La minería de texto nos permite procesar textos."
# Crear un objeto TextBlob
blob = TextBlob(texto)
# Realizar el análisis de sentimientos
sentimiento = blob.sentiment
# Imprimir el resultado
print(f"Texto: {texto}")
print(f"Análisis de Sentimientos: Polaridad = {sentimiento.polarity}, Subjetividad = {sentimiento.subjectivity}")
# Clasificar la polaridad del sentimiento
if sentimiento.polarity > 0:
    print("El texto es positivo.")
elif sentimiento.polarity < 0:
    print("El texto es negativo.")
else:
    print("El texto es neutral.")