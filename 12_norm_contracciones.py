contracciones = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he's": "he is",
    "I'll": "I will",
    "I'm": "I am",
    "isn't": "is not",
    "it's": "it is",
    "let's": "let us",
    "mustn't": "must not",
    "shan't": "shall not",
    "she's": "she is",
    "shouldn't": "should not",
    "that's": "that is",
    "there's": "there is",
    "they're": "they are",
    "wasn't": "was not",
    "we're": "we are",
    "weren't": "were not",
    "what's": "what is",
    "won't": "will not",
    "wouldn't": "would not",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have"
}

def expandir_contracciones(texto, contracciones):
    palabras = texto.split()
    palabras_expandidas = [contracciones.get(palabra, palabra) for palabra in palabras]
    texto_expandido = ' '.join(palabras_expandidas)
    return texto_expandido

# Ejemplo de uso
texto_original = "I can't believe he hasn't seen it."
texto_expandido = expandir_contracciones(texto_original, contracciones)

print("Texto Original:", texto_original)
print("Texto Expandido:", texto_expandido)
