#Aqui irian las funciones que escriben o leen el csv 
import csv
import os

def cargar_datos_csv(nombre_archivo):
    lista_paises = []
    
    #si el archivo no existe, lo inicializamos con el dataset base de la consigna
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            #formato de la consigna (pais,continente,poblacion,pbi)
            archivo.write("pais,continente,poblacion,pbi\n")
            archivo.write("Argentina,America,45376763,490000\n")
            archivo.write("Japon,Asia,125800000,4940000\n")
            archivo.write("Brasil,America,213993437,1610000\n")
            archivo.write("Alemania,Europa,83149300,4220000\n")
            
    #lectura del archivo
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, 1):
            if numero_linea == 1:  # salta el encabezado
                continue           
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue  #ignoramos las lineas vacias

            datos = linea_limpia.split(",")
            if len(datos) < 4:
                print(f"Error de formato en linea {numero_linea}. Se omitio esta linea.")
                continue
                
            try:
                #limpiamos los datos de entrada
                pais = datos[0].strip()
                continente = datos[1].strip()
                poblacion = int(datos[2].strip())
                pbi = int(datos[3].strip())
                
                if not pais or not continente:
                    raise ValueError("El nombre de país o continente no pueden ser campos vacios.")
                
                pais_dict = {
                    "pais": pais,
                    "continente": continente,
                    "poblacion": poblacion,
                    "pbi": pbi
                }
                lista_paises.append(pais_dict)
            except ValueError as e:
                print(f"Error de conversión en linea {numero_linea}. Se omitio esta linea.")
                
    return lista_paises


def guardar_datos_csv(nombre_archivo, lista_paises):

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("pais,continente,poblacion,pbi\n")
        for p in lista_paises:
            linea = f"{p['pais']},{p['continente']},{p['poblacion']},{p['pbi']}\n"
            archivo.write(linea)

