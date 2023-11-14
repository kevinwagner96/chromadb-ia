from chroma import ChromaMoviesDB
from prettytable import PrettyTable

def print_table(data):
    field_names = ["ID", "Distancia", "Metadatos", "Overview"]
    # Agregar datos a la tabla
    print("Result:")
    for i in range(len(data['ids'][0])):
        id_value = data['ids'][0][i]
        distance_value = data['distances'][0][i]
        year = data['metadatas'][0][i]['year']
        name = data['metadatas'][0][i]['name']
        document_value = data['documents'][0][i]
        print("ID: {} | {} | Year: {} | Distance: {}\n{}".format(id_value,name,year,distance_value,document_value))



def ingresar_texto():
    texto = input("Ingresa el texto: ")
    return texto


def menu():
    db = ChromaMoviesDB()
    while True:
        print("\nMenú:")
        print("1. Busqueda contextual de una pelicula")
        print("2. Cantidad de elementos")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            result = db.query(ingresar_texto(), 2)
            print_table(result)
        elif opcion == '2':
            print(db.elements())
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")


if __name__ == '__main__':
    menu()
