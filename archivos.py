import json
import os

# Ruta por defecto
RUTA_BASE = "data/"
NOMBRE_ARCHIVO = "datos.json"
RUTA = os.path.join(RUTA_BASE, NOMBRE_ARCHIVO)

def cargar_datos(nombre_archivo=RUTA):
    """Carga datos desde un archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(nombre_archivo):
        return []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return []

def guardar_datos(datos, nombre_archivo=RUTA):
    """Guarda datos en un archivo JSON, creando la carpeta si no existe."""
    try:
        # Asegurar que el directorio existe
        directorio = os.path.dirname(nombre_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar datos: {e}")