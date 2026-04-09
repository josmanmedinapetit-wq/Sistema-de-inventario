from utils.archivos import cargar_datos, guardar_datos
from modules.validaciones import validar_entero, validar_texto

def registrar_producto():
    datos = cargar_datos()
    id_prod = validar_entero("ID del producto: ")
    nombre = validar_texto("Nombre: ")
    categoria = validar_texto("Categoría: ")
    cantidad = validar_entero("Cantidad: ")
    
    nuevo = {"id": id_prod, "nombre": nombre, "categoria": categoria, "cantidad": cantidad}
    datos.append(nuevo)
    guardar_datos(datos)
    print("Producto registrado con éxito.")

def listar_productos():
    datos = cargar_datos()
    if not datos:
        print("No hay productos registrados.")
        return
    for p in datos:
        print(f"ID: {p['id']} | {p['nombre']} | Cat: {p['categoria']} | Stock: {p['cantidad']}")

def buscar_producto():
    datos = cargar_datos()
    busqueda = validar_texto("Nombre del producto a buscar: ").lower()
    encontrados = [p for p in datos if busqueda in p['nombre'].lower()]
    for p in encontrados:
        print(p)

def editar_producto():
    datos = cargar_datos()
    id_edit = validar_entero("ID del producto a editar: ")
    for p in datos:
        if p['id'] == id_edit:
            p['nombre'] = validar_texto(f"Nuevo nombre ({p['nombre']}): ")
            p['cantidad'] = validar_entero(f"Nueva cantidad ({p['cantidad']}): ")
            guardar_datos(datos)
            print("Editado correctamente.")
            return
    print("No se encontró el ID.")

def eliminar_producto():
    datos = cargar_datos()
    id_del = validar_entero("ID del producto a eliminar: ")
    nuevos_datos = [p for p in datos if p['id'] != id_del]
    if len(datos) == len(nuevos_datos):
        print("ID no encontrado.")
    else:
        guardar_datos(nuevos_datos)
        print("Producto eliminado.")