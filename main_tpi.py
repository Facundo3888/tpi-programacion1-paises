#Este es el archivo principal de ejecucion.
#Aqui se deben importar los otros .py 

from logica_paises import (
    cargar_datos_csv, 
    guardar_datos_csv,
    agregar_pais,
    actualizar_pais,
    buscar_pais_nombre,
    filtrar_paises,
    ordenar_paises,
    mostrar_estadisticas
)

def menu():
    print("╔═════════════════════════════════════════════════╗")
    eleccion_menu = input("""║   SISTEMA DE GESTION DE PAISES (TPI)            ║
╠═════════════════════════════════════════════════╣
║   1) Cargar/Recargar datos desde CSV            ║
║   2) Agregar nuevo pais                         ║
║   3) Modificar datos de un pais                 ║
║   4) Buscar pais por nombre                     ║
║   5) Filtrar paises por criterios               ║
║   6) Ordenar paises (Burbuja)                   ║
║   7) Mostrar reporte estadistico                ║
║   8) Guardar cambios y salir                    ║
╚═════════════════════════════════════════════════╝
¿Que desea hacer?: """)
    return eleccion_menu


def main():
    # Inicializamos la lista en memoria como exige la consigna
    lista_paises = []
    
    while True:
        match menu():
            case "1":
                print("Accediendo al archivo CSV...")
                lista_paises = cargar_datos_csv("paises.csv")
                print(f"Datos cargados. {len(lista_paises)} registros en memoria.\n")

            case "2":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    agregar_pais(lista_paises)

            case "3":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    actualizar_pais(lista_paises)

            case "4":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    buscar_pais_nombre(lista_paises)

            case "5":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    filtrar_paises(lista_paises)

            case "6":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    ordenar_paises(lista_paises)

            case "7":
                if not lista_paises:
                    print("Error! La lista esta vacia. Primero cargue los datos (Opcion 1).\n")
                else:
                    mostrar_estadisticas(lista_paises)
            
            case "8":
                if not lista_paises:
                    print("No hay datos cargados en memoria para guardar. Saliendo...")
                else:
                    print("Guardando cambios en el archivo CSV...")
                    guardar_datos_csv("paises.csv", lista_paises)
                    print("Cambios guardados con exito! Saliendo...")
                break

            case _:
                print("Error! Opcion invalida del menu.\n")

#Llama a la funcion main para ejecutar el programa
if __name__ == "__main__":
    main()
