import contractions

def expandir_contracciones(texto):
    texto_expandido = contractions.fix(texto)
    return texto_expandido

# Ejemplo de uso
texto_original = "I can't believe he hasn't."
texto_expandido = expandir_contracciones(texto_original)

print("Texto Original:", texto_original)
print("Texto Expandido:", texto_expandido)