from fuzzywuzzy import fuzz
def corregir_errores_tipograficos(palabra_incorrecta, opciones_correctas, umbral_similitud=80):
    # Calcular similitud difusa con todas las opciones
    similitudes = [(opcion, fuzz.ratio(palabra_incorrecta, opcion)) for opcion in opciones_correctas]
    # Seleccionar la opción con la mayor similitud si supera el umbral
    mejor_opcion = max(similitudes, key=lambda x: x[1]) if max(similitudes, key=lambda x: x[1])[1] > umbral_similitud else None
    return mejor_opcion[0] if mejor_opcion else palabra_incorrecta
# Ejemplo de uso
palabra_incorrecta = "orror"
opciones_correctas = ["error", "errante", "terreno", "horror", "terror", "oración"]
palabra_corregida = corregir_errores_tipograficos(palabra_incorrecta, opciones_correctas)
print("Palabra corregida:", palabra_corregida)
