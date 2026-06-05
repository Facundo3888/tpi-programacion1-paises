#Este es el archivo principal de ejecucion.
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

def main():
        while True:
            match menu():
                case "1":
                    pass

                case "2":
                    pass

                case "3":
                    pass

                case "4":
                    pass

                case "5":
                    pass

                case "6":
                    pass

                case "7":
                    pass
                
                case "8":
                    pass

                case _:
                    print("Error: el dato ingresado no corresponde a ninguna opcion del menu.")

main()