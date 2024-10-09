from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
palabra = "replacements"
# Lematización
palabra_lemma = lemmatizer.lemmatize(palabra)
# Resultado
print("Palabra original:", palabra)
print("Palabra después de lematización:", palabra_lemma)
