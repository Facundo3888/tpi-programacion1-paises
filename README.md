# Sistema de Gestión de Países
**Trabajo Práctico Integrador — Programación 1**
Universidad Tecnológica Nacional (UTN) — Tecnicatura Universitaria en Programación

---

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar información sobre países del mundo. El sistema lee y escribe datos desde un archivo CSV, y ofrece un menú interactivo con funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

---

## Integrantes

| Nombre | Participación |
| Facundo Uriel Rodriguez | Módulo de archivos CSV, menú principal |
| René Alejandro Medina | Lógica de búsqueda, filtros, ordenamiento por burbuja, estadísticas |

---

## Estructura del proyecto

tpi-programacion1-paises/
├── main_tpi.py        ← Archivo principal, menú y flujo del programa
├── archivos.py        ← Lectura y escritura del archivo CSV
├── logica_paises.py   ← Funciones de búsqueda, filtros, orden y estadísticas
├── paises.csv         ← Dataset base con países de ejemplo
└── README.md          ← Este archivo

---

## Requisitos

- Python 3.10 o superior (necesario para el uso de `match/case`)
- No requiere librerías externas

---

## Cómo ejecutar el programa

1. Clonar o descargar el repositorio
2. Abrir una terminal en la carpeta del proyecto
3. Ejecutar el archivo principal:
python main_tpi.py

---

## Menú de opciones

1) Cargar/Recargar datos desde CSV
2) Agregar nuevo pais
3) Modificar datos de un pais
4) Buscar pais por nombre
5) Filtrar paises por criterios
6) Ordenar paises (Burbuja)
7) Mostrar reporte estadistico
8) Guardar cambios y salir

---

## Ejemplos de uso

**Agregar un país:**

Ingrese el nombre del pais: Francia
Ingrese el continente de 'Francia': Europa
Ingrese la poblacion de 'Francia': 67413000
Ingrese el PBI de 'Francia': 2780000

Exito! 'Francia' fue agregado con exito!

**Buscar por nombre (coincidencia parcial):**

Ingrese el nombre del pais a buscar: ar

Se encontraron 1 coincidencias:
País               | Continente      | Poblacion       | PBI (Millones USD)
----------------------------------------------------------------------
Argentina          | America         | 45376763        | 490000
----------------------------------------------------------------------


**Filtrar por continente:**

Seleccione la opcion a filtrar (1-3): 1
Ingrese el continente por el cual filtrar: europa

Mostrando resultados para: Continente: 'Europa'
País               | Continente      | Poblacion       | PBI (Millones USD)
----------------------------------------------------------------------
Alemania           | Europa          | 83149300        | 4220000
----------------------------------------------------------------------


**Reporte estadístico:**

-> Promedio de poblacion: 116829875.00 habitantes
-> Promedio de PBI: 2815000.00 millones de USD
-> Pais con mayor poblacion: Brasil (213993437 hab.)
-> Pais con menor poblacion: Alemania (83149300 hab.)

Cantidad de paises por continente:
   - America: 2 país(es)
   - Asia: 1 país(es)
   - Europa: 1 país(es)

---

## Validaciones implementadas

- No se permiten campos vacíos al agregar un país
- No se permiten países duplicados (indiferente a mayúsculas/minúsculas)
- Población y PBI deben ser números enteros no negativos
- Búsquedas sin resultados muestran mensajes claros
- Rangos de filtrado inválidos son detectados y notificados
- Errores de formato en el CSV son reportados sin detener el programa

---

## Video demostrativo

Link: https://drive.google.com/file/d/1_vJhSA6u2Kh8z35_d_mOtsBdYYucvlwZ/view?usp=sharing

---