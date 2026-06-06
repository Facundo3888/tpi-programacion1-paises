#Aqui irian las funciones que escriben o leen el csv 
import csv

#Esta funcion lee el csv y lo transforma en una lista para ser operada en ram durante la ejecucion
def cargar_datos_csv(nombre_archivo):
    lista_paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            #iteramos sobre el diccionario que creo dictreader para pasarlo a una version limpia
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)

    #En caso de error indicamos segun sea apropiado
    except FileNotFoundError:
        print(f"advertencia! no se encontro el archivo {nombre_archivo}. Se inicia con lista vacia.")
    except ValueError:
        print("Error: hay datos con formato incorrecto en el CSV (población o superficie no son números).")

    return lista_paises

#Esta funcion transforma la lista actualizada durante la ejecucion en un nuevo archivo csv que sobreescribe al anterior
def guardar_datos_csv(nombre_archivo, lista_paises):
    try:
        #Usamos el modo w para que sobreescriba el archivo viejo con la lista actualizada
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            #Esto escribe los encabezados del nuevo csv
            escritor.writeheader()
            #Esto transforma cada diccionario de la lista en una linea del csv
            escritor.writerows(lista_paises)
            print("Datos guardados correctamente.")

    except Exception as error:
        print(f"Error al guardar el archivo: {error}")
