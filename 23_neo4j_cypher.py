from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self._uri = uri
        self._user = user
        self._password = pwd
        self._driver = None

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
        
    def query(self, query, parameters=None, db=None):
        assert self._driver is not None, "La conexión no está establecida."
        session = self._driver.session(database=db) if db is not None else self._driver.session()
        result = list(session.run(query, parameters))
        session.close()
        return result

def preprocess_text(text):
    # Aquí puedes implementar tu propio preprocesamiento (normalización, tokenización, etc.).
    # Por ejemplo, puedes utilizar nltk o spacy para el preprocesamiento del texto.
    tokens = text.split()  # Tokenización simple, adaptar según tus necesidades.
    return tokens

def create_graph_from_text(tx, tokens):
    for i in range(len(tokens) - 1):
        word1 = tokens[i]
        word2 = tokens[i + 1]

        # Crear nodos y relaciones
        query = (
            f"MERGE (w1:Word {{value: '{word1}'}})"
            f"MERGE (w2:Word {{value: '{word2}'}})"
            "MERGE (w1)-[r:CONNECTED]->(w2)"
            "   ON CREATE SET r.weight = 1"
            "   ON MATCH SET r.weight = r.weight + 1"
        )
        tx.run(query)

def main():
    # Configuración de la conexión a Neo4j
    neo4j_uri = "bolt://localhost:7687"  # Reemplaza con la URI de tu servidor Neo4j
    neo4j_user = "user"
    neo4j_password = "password"

    # Texto de ejemplo
    texto = "Este es un ejemplo de texto. El texto puede contener múltiples palabras."

    # Preprocesamiento del texto
    tokens = preprocess_text(texto)

    # Conexión a Neo4j
    neo4j_conn = Neo4jConnection(neo4j_uri, neo4j_user, neo4j_password)
    neo4j_conn.connect()

    # Ejecutar la transacción de carga de datos
    with neo4j_conn._driver.session() as session:
        session.write_transaction(create_graph_from_text, tokens)

    # Cerrar la conexión
    neo4j_conn.close()

if __name__ == "__main__":
    main()
