from utils.archivos import cargar_datos, guardar_datos

def bajo_stock():
    datos = cargar_datos()
    print("--- Productos con bajo stock (menos de 5) ---")
    encontrados = [p for p in datos if p['cantidad'] < 5]
    if not encontrados:
        print("No hay productos con bajo stock.")
        return encontrados
    
    for p in encontrados:
        print(f"{p['nombre']}: {p['cantidad']} unidades")
    return encontrados

def exportar_reporte_json():
    productos = bajo_stock()
    if productos:
        nombre_reporte = "data/reporte_bajo_stock.json"
        guardar_datos(productos, nombre_reporte)
        print(f"Reporte exportado a {nombre_reporte}")