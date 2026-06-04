#Este es el archivo principal de ejecucion.


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
    pass


menu()