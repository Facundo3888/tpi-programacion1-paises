import os

def cargar_datos_csv(nombre_archivo):
    
    lista_paises = []
    
    #si el archivo no existe, lo inicializamos con el dataset base de la consigna
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            #formato de la consigna (pais,continente,poblacion,pbi)
            archivo.write("Argentina,America,45376763,490000\n")
            archivo.write("Japon,Asia,125800000,4940000\n")
            archivo.write("Brasil,America,213993437,1610000\n")
            archivo.write("Alemania,Europa,83149300,4220000\n")
            
    #lectura del archivo
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, 1):
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
        for p in lista_paises:
            linea = f"{p['pais']},{p['continente']},{p['poblacion']},{p['pbi']}\n"
            archivo.write(linea)


#agregar nuevos paises
def agregar_pais(lista_paises):
    print("--- Registrar nuevo pais ---")
    
    #validamos el nombre sin campos vacios y sacando espacios extras
    while True:
        pais = input("Ingrese el nombre del pais: ").strip()
        if not pais:
            print("Error! El nombre del país no puede estar vacio.")
            continue
        
        #validacion de duplicados e indiferencia de mayusculas o minusculas
        duplicado = False
        for p in lista_paises:
            if p["pais"].lower() == pais.lower():
                duplicado = True
                break
        if duplicado:
            print(f"Error! El pais '{pais}' ya se encuentra registrado.")
            continue
        break

    #validamos el continente. no puede estar vacio
    while True:
        continente = input(f"Ingrese el continente de '{pais}': ").strip()
        if not continente:
            print("Error! El continente no puede estar vacio.")
            continue
        break

    #validacion numerica de poblacion (solo numeros enteros positivos mayores a cero)
    while True:
        try:
            poblacion = int(input(f"Ingrese la poblacion de '{pais}': "))
            if poblacion < 0:
                print("Error! La poblacion no puede ser un valor negativo.")
                continue
            break
        except ValueError:
            print("Error! Debe ingresar un numero entero valido para la poblacion.")

    #validacion numerica de PBI (solo numeros enteros positivos mayores a cero)
    while True:
        try:
            pbi = int(input(f"Ingrese el PBI de '{pais}': "))
            if pbi < 0:
                print("Error! El PBI no puede ser un valor negativo.")
                continue
            break
        except ValueError:
            print("Error! Debe ingresar un numero entero valido para el PBI.")

    nuevo_pais = {
        "pais": pais,
        "continente": continente,
        "poblacion": poblacion,
        "pbi": pbi
    }
    lista_paises.append(nuevo_pais)
    print(f"\nExito! '{pais}' fue agregado con exito!\n")


#modificar datos de un pais
def actualizar_pais(lista_paises):
    print("--- Modificar datos de un pais ---")
    if not lista_paises:
        print("Error! No hay datos cargados en el sistema.\n")
        return

    busqueda = input("Ingrese el nombre del país a modificar: ").strip().lower() #indiferencia mayusculas o minusculas 
    encontrado = False
    
    for p in lista_paises:
        if p["pais"].lower() == busqueda:
            encontrado = True
            print(f"\nPais: {p['pais']} | Continente: {p['continente']}")
            print(f"-- Datos actuales -- Poblacion: {p['poblacion']} hab. | PBI: {p['pbi']} millones de USD")
            
            #validamos el nuevo valor de poblacion
            while True:
                try:
                    nueva_pob = int(input("Ingrese el nuevo valor de poblacion: "))
                    if nueva_pob < 0:
                        print("Error! La población no puede ser negativa.")
                        continue
                    p["poblacion"] = nueva_pob
                    break
                except ValueError:
                    print("Error! Ingrese un numero entero valido.")

            #validamos el nuevo valor de PBI
            while True:
                try:
                    nuevo_pbi = int(input("Ingrese el nuevo valor de PBI: "))
                    if nuevo_pbi < 0:
                        print("Error! El PBI no puede ser negativo.")
                        continue
                    p["pbi"] = nuevo_pbi
                    break
                except ValueError:
                    print("Error! Ingrese un numero entero valido.")
                    
            print(f"\nExito! Los datos de '{p['pais']}' fueron actualizados!\n")
            break

    if not encontrado:
        print(f"Error! El pais '{busqueda}' no se encuentra en el registro.\n")


#buscar pais por nombre
def buscar_pais_nombre(lista_paises):
    print("--- Buscar pais por nombre (Exacto o Parcial) ---")
    if not lista_paises:
        print("Error! No hay datos cargados en el sistema.\n")
        return

    busqueda = input("Ingrese el nombre del pais a buscar: ").strip().lower()
    coincidencias = []
    
    for p in lista_paises:
        if busqueda in p["pais"].lower():
            coincidencias.append(p)
            
    if not coincidencias:
        print(f"No se encontraron resultados para la busqueda: '{busqueda}'.\n")
    else:
        print(f"\nSe encontraron {len(coincidencias)} coincidencias:")
        imprimir_tabla_paises(coincidencias)


#filtrar países por criterios (Continente, Población, PBI)
def filtrar_paises(lista_paises):
    print("--- Filtrar paises por criterios ---")
    if not lista_paises:
        print("Error! No hay datos cargados en el sistema.\n")
        return

    print("1) Filtrar por continente")
    print("2) Filtrar por rango de poblacion")
    print("3) Filtrar por rango de PBI")
    subopcion = input("Seleccione la opcion a filtrar (1-3): ").strip()
    
    filtrados = []
    
    if subopcion == "1":
        continente_buscado = input("Ingrese el continente por el cual filtrar: ").strip().lower()
        for p in lista_paises:
            if p["continente"].lower() == continente_buscado:
                filtrados.append(p)
        criterio_desc = f"Continente: '{continente_buscado.capitalize()}'"
        
    elif subopcion == "2":
        try:
            min_pob = int(input("Ingrese la población minima: "))
            max_pob = int(input("Ingrese la población maxima: "))
            if min_pob < 0 or max_pob < min_pob:
                print("Error! Rangos de población no validos.")
                return
            for p in lista_paises:
                if min_pob <= p["poblacion"] <= max_pob:
                    filtrados.append(p)
            criterio_desc = f"Rango de poblacion [{min_pob} - {max_pob}]"
        except ValueError:
            print("Error! Ingrese valores numericos validos.")
            return
            
    elif subopcion == "3":
        try:
            min_pbi = int(input("Ingrese el PBI minimo: "))
            max_pbi = int(input("Ingrese el PBI maximo: "))
            if min_pbi < 0 or max_pbi < min_pbi:
                print("Error! Rangos de PBI no validos.")
                return
            for p in lista_paises:
                if min_pbi <= p["pbi"] <= max_pbi:
                    filtrados.append(p)
            criterio_desc = f"Rango de PBI [{min_pbi} - {max_pbi} millones USD]"
        except ValueError:
            print("Error! Ingrese valores numericos validos.")
            return
    else:
        print("Opcion de filtrado no valida.\n")
        return

    if not filtrados:
        print(f"No se encontraron paises que cumplan con el criterio: {criterio_desc}.\n")
    else:
        print(f"\nMostrando resultados para: {criterio_desc}")
        imprimir_tabla_paises(filtrados)


#ordenar paises
def ordenar_paises(lista_paises):
    print("--- Ordenar paises ---")
    if not lista_paises:
        print("Error! No hay datos cargados en el sistema.\n")
        return

    print("Criterio de ordenamiento:")
    print("1) Ordenar por nombre")
    print("2) Ordenar por poblacion")
    print("3) Ordenar por PBI")
    crit = input("Seleccione una opcion (1-3): ").strip()
    
    if crit not in ["1", "2", "3"]:
        print("Criterio invalido.\n")
        return
        
    print("\nDireccion de ordenamiento:")
    print("A) Ascendente")
    print("B) Descendente")
    direccion = input("Seleccione una direccion (A/B): ").strip().upper()
    
    if direccion not in ["A", "B"]:
        print("Dirección invalida.\n")
        return

    clave = "pais" if crit == "1" else "poblacion" if crit == "2" else "pbi"
    n = len(lista_paises)
    lista_ordenada = list(lista_paises)

    #ordenamiento por burbuja
    for i in range(n):
        for j in range(0, n - i - 1):
            debe_intercambiar = False
            
            valor_actual = lista_ordenada[j][clave]
            valor_siguiente = lista_ordenada[j + 1][clave]
            
            if clave == "pais":
                valor_actual = valor_actual.lower()
                valor_siguiente = valor_siguiente.lower()
                
            if direccion == "A":
                if valor_actual > valor_siguiente:
                    debe_intercambiar = True
            else:
                if valor_actual < valor_siguiente:
                    debe_intercambiar = True
                    
            if debe_intercambiar:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    sentido = "Ascendente" if direccion == "A" else "Descendente"
    print(f"\nExito! Lista ordenada por {clave.capitalize()} ({sentido}):")
    imprimir_tabla_paises(lista_ordenada)


#reporte de estadisticas completo
def mostrar_estadisticas(lista_paises):
    print("--- Reporte estadistico general ---")
    if not lista_paises:
        print("Error! No hay datos cargados en el sistema.\n")
        return

    total_pob = 0
    total_pbi = 0
    max_pob_pais = lista_paises[0]
    min_pob_pais = lista_paises[0]
    conteo_continentes = {}

    for p in lista_paises:
        total_pob += p["poblacion"]
        total_pbi += p["pbi"]
        
        if p["poblacion"] > max_pob_pais["poblacion"]:
            max_pob_pais = p
            
        if p["poblacion"] < min_pob_pais["poblacion"]:
            min_pob_pais = p
            
        cont_limpio = p["continente"].capitalize()
        conteo_continentes[cont_limpio] = conteo_continentes.get(cont_limpio, 0) + 1

    promedio_pob = total_pob / len(lista_paises)
    promedio_pbi = total_pbi / len(lista_paises)

    print(f"-> Promedio de poblacion: {promedio_pob:.2f} habitantes")
    print(f"-> Promedio de PBI: {promedio_pbi:.2f} millones de USD")
    print(f"-> Pais con mayor poblacion: {max_pob_pais['pais']} ({max_pob_pais['poblacion']} hab.)")
    print(f"-> Pais con menor poblacion: {min_pob_pais['pais']} ({min_pob_pais['poblacion']} hab.)")
    print("\nCantidad de paises por continente:")
    for cont, cantidad in conteo_continentes.items():
        print(f"   - {cont}: {cantidad} país(es)")
    print()


def imprimir_tabla_paises(lista):
    print(f"{'País':<18} | {'Continente':<15} | {'Poblacion':<15} | {'PBI (Millones USD)':<15}")
    print("-" * 70)
    for p in lista:
        print(f"{p['pais']:<18} | {p['continente']:<15} | {p['poblacion']:<15} | {p['pbi']:<15}")
    print("-" * 70 + "\n")
