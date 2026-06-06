#Aqui irian las funciones que escriben o leen el csv 
import csv

#Esta funcion debe ser capaz de leer el csv y guardar su contenido en una lista 
def cargar_datos_csv(nombre_archivo):
    lista_paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            #iteramos sobre el diccionario que creo que dictreader para pasarlo a una version limpia
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