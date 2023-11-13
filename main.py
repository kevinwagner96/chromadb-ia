# This is a sample Python script.
import chromadb
from chromadb import Settings


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    chroma_client = chromadb.Client(Settings(persist_directory="persistent.db"))
    #client = chromadb.PersistentClient(path="persistent.db")
    cole = chroma_client.list_collections()
    print(client.list_collections())
    collection = client.get_collection(name="movies-overviews")
    result = collection.query(
        query_texts=["anillo"],
        n_results=2
    )
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
