import chromadb
import pandas as pd
from local_setting import archivo_destino


class ChromaMoviesDB:
    def __init__(self):
        client = chromadb.PersistentClient(path="database")
        self.collection = client.get_or_create_collection(name="movies-overviews")
        if self.collection.count() == 0:
            self.load_csv()

    def load_csv(self):
        df_origen = pd.read_csv(archivo_destino)
        for index, row in df_origen.iterrows():
            self.collection.add(
                documents=[row['Overview'].replace('"', '')],
                metadatas=[{"year": row['Released_Year'], "name": row['Series_Title']}],
                ids=[index.__str__()]
            )

    def query(self, text, n_result):
        return self.collection.query(query_texts=[text], n_results=n_result)

    def elements(self):
        return self.collection.count()
