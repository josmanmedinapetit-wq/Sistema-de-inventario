from modules.operaciones import registrar_producto, listar_productos, buscar_producto, editar_producto, eliminar_producto 
from modules.reportes import bajo_stock, exportar_reporte_json

def mostrar_menu():
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Registrar Producto")
        print("2. Listar Productos")
        print("3. Buscar Producto")
        print("4. Editar Producto")
        print("5. Eliminar Producto")
        print("6. Reporte Bajo Stock")
        print("7. Exportar Reporte Bajo Stock (JSON)")
        print("8. Salir")
        
        opc = input("Seleccione una opción: ")
        if opc == "1": registrar_producto()
        elif opc == "2": listar_productos()
        elif opc == "3": buscar_producto()
        elif opc == "4": editar_producto()
        elif opc == "5": eliminar_producto()
        elif opc == "6": bajo_stock()
        elif opc == "7": exportar_reporte_json()
        elif opc == "8": break
        else: print("Opción inválida.")