#Este es el archivo principal de ejecucion.
#Aqui se deben importar los otros .py 
from archivos import cargar_datos_csv

#Funcion de seleccion de menu
def menu():
    print("╔═════════════════════════════════════════════════╗")
    eleccion_menu = input("""║   SISTEMA DE GESTION DE PAISES                  ║
╠═════════════════════════════════════════════════╣
║   1) Cargar/Recargar datos desde CSV            ║
║   2) Agregar nuevo pais                         ║
║   3) Modificar datos de un pais                 ║
║   4) Buscar pais por nombre                     ║
║   5) Filtrar paises por criterios               ║
║   6) Ordenar paises                             ║
║   7) Mostrar reporte estadistico                ║
║   8) Guardar cambios y salir                    ║
╚═════════════════════════════════════════════════╝
¿Que desea hacer?: """)
    return eleccion_menu

#Funcion que llama a las demas para ejecutar el programa
def main():
        while True:
            match menu():
                case "1":
                    print("Accediendo al archivo CSV...")
                    lista_paises = cargar_datos_csv("paises.csv")
                    print("Datos recargados desde el archivo.")


                case "2":
                    #logica_paises.agregar_pais(****)
                    pass

                case "3":
                    #logica_paises.actualizar_pais(****)
                    pass

                case "4":
                    #logica_paises.buscar_pais_nombre(****)
                    pass

                case "5":
                    #logica_paises.filtrar_paises(****)
                    pass

                case "6":
                    #logica_paises.ordenar_paises(****)
                    pass

                case "7":
                    #logica_paises.mostrar_estadisticas(****)
                    pass
                
                case "8":
                    print("Guardando cambios en el archivo CSV...")
                    #archivos.guardar_datos(****)
                    print("¡Gracias por usar el sistema! Saliendo...")
                    break

                case _:
                    print("Error: el dato ingresado no corresponde a ninguna opcion del menu.")