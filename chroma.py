import chromadb
import pandas as pd
from chromadb import Settings

from local_setting import archivo_destino

chroma_client = chromadb.Client(Settings(persist_directory="/database"))
collection = chroma_client.create_collection(name="movies-overviews")

df_origen = pd.read_csv(archivo_destino)


for index, row in df_origen.iterrows():
    collection.add(
        documents=[row['Overview'].replace('"','')],
        metadatas=[{"year": row['Released_Year'], "name":row['Series_Title']}],
        ids=[index.__str__()]
    )

result = collection.query(
    query_texts=["anillo"],
    n_results=2
)

print(result)