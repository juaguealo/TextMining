from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Supongamos que 'documentos' contiene textos y 'etiquetas' contiene las categorías asociadas.
# Vamos a simular algunos datos de ejemplo.

documentos = [
    "Este es un documento de la categoría A.",
    "Otro documento de la categoría B.",
    "Un tercer documento de la categoría A."
]

etiquetas = ["A", "B", "A"]

# Paso 3: Preprocesamiento de Texto y Paso 4: Representación Vectorial (TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documentos)

# Paso 5: División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, etiquetas, test_size=0.2, random_state=42)

# Paso 6: Entrenamiento del Modelo
modelo_nb = MultinomialNB()
modelo_nb.fit(X_train, y_train)

# Paso 7: Evaluación del Modelo (Opcional)
predicciones = modelo_nb.predict(X_test)

# Resultados
print("Predicciones de Categorías:")
print(predicciones)

# Medidas de rendimiento
print("\nMedidas de rendimiento:")
print(classification_report(y_test, predicciones))

# Exactitud
accuracy = accuracy_score(y_test, predicciones)
print(f"\nExactitud del Modelo: {accuracy}")
