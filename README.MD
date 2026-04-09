# Sistema de Gestión de Inventario

## Descripción del Proyecto
Este sistema es una aplicación de consola desarrollada en Python para la gestión eficiente de inventarios de una tienda. Permite realizar el ciclo completo de gestión de datos (registro, consulta, edición y eliminación) de productos, garantizando que la información se mantenga guardada incluso después de cerrar el programa mediante el uso de archivos JSON.

El proyecto fue desarrollado para la asignatura **Lenguaje de Programación III** (6to Semestre - Ingeniería de Sistemas).

## Integrantes del Equipo
***Integrante 1:** [Tu Nombre Completo]
***Integrante 2:** [Nombre de Compañero]
***Integrante 3:** [Nombre de Compañero]

## Requisitos del Sistema
***Lenguaje:** Python.
***Persistencia:** Archivos JSON.
***Dependencias:** Ninguna (solo bibliotecas estándar de Python).

## Estructura del Proyecto
El sistema sigue un diseño modular para garantizar orden y facilidad de mantenimiento:

* `main.py`: Punto de entrada que inicia la aplicación.
* `data/`: Carpeta que contiene el archivo `datos.json` para la persistencia.
* `modules/`: Contiene la lógica del sistema:
    * `menu.py`: Manejo del menú principal y navegación.
    * `validaciones.py`: Funciones para asegurar que los datos ingresados sean correctos.
    * `operaciones.py`: Lógica para registrar, buscar, editar y eliminar productos.
    * `reportes.py`: Generación de resúmenes de bajo stock.
* `utils/`: Carpeta para herramientas de apoyo.
    * `archivos.py`: Funciones específicas para lectura y escritura de archivos.

## Instrucciones de Ejecución
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el comando:
   ```bash
   python main.py
