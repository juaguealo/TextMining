import re
texto = "La normalización de texto, ¿es esencial?"
# Eliminación de caracteres especiales y puntuación
texto_normalizado = re.sub(r"[^a-zA-Z0-9]", " ", texto)
# Resultado
print("Texto normalizado:", texto_normalizado)