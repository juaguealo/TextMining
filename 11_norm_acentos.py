from unidecode import unidecode
def eliminar_acentos(texto):
    # Utilizar unidecode para eliminar acentos y caracteres especiales
    texto_normalizado = unidecode(texto)
    return texto_normalizado
# Ejemplo de uso
texto_original = "Hoy es un día muy emocionante con café y piñatas."
texto_normalizado = eliminar_acentos(texto_original)
print("Texto Original:", texto_original)
print("Texto Normalizado:", texto_normalizado)