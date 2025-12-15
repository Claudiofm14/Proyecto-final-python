import os 
from utils.helpers import imprimir_Error, imprimir_Titulo, imprimir_Exito, limpiar_Pantalla, validar_Input_str, validar_Input_int, validar_Input_float
from utils import db_manager
from config import BD_NAME, TABLE_NAME

import sys

os.system('cls' if os.name == 'nt' else 'clear')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def mostrar_tabla(productos: list) -> None:
    """Muestra una lista de productos en formato de tabla."""
    if not productos:
        imprimir_Error("No hay productos para mostrar.")
        return

    encabezados = ["ID", "Nombre", "Descripción", "Cantidad", "Precio", "Categoría"]
    print(f"{' | '.join(encabezados)}")
    print("-" * 70)
    for producto in productos:
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
    
def menu_registrar():
    imprimir_Titulo("Registrar Nuevo Producto")
    nombre = validar_Input_str("Ingrese el nombre del producto")
    descripcion = validar_Input_str("Ingrese la descripción del producto")
    cantidad = validar_Input_int("Ingrese la cantidad del producto")
    precio = validar_Input_float("Ingrese el precio del producto")
    categoria = validar_Input_str("Ingrese la categoría del producto")
    if db_manager.registrar_producto(nombre, descripcion, cantidad, precio, categoria):
        imprimir_Exito("Producto registrado exitosamente.")
    else:
        imprimir_Error("Error al registrar el producto.")

def menu_ver_productos():
    imprimir_Titulo("Lista de Productos")
    productos = db_manager.obtener_productos()
    mostrar_tabla(productos)

def menu_actualizar_producto():
    imprimir_Titulo("Actualizar Producto")
    producto_id = validar_Input_int("Ingrese el ID del producto a actualizar")
    producto = db_manager.buscar_producto_por_id(producto_id)
    if not producto:
        imprimir_Error("Producto no encontrado.")
        return
    print (f"Actualizando producto: {producto[1]}")
    print("Deje el campo vacío para mantener el valor actual.")
    nombre = input(f"Nombre [{producto[1]}]: ").strip() or producto[1]
    descripcion = input(f"Descripción [{producto[2]}]: ").strip() or producto[2]
    cantidad_input = input(f"Cantidad [{producto[3]}]: ").strip()
    cantidad = int(cantidad_input) if cantidad_input else producto[3]
    precio_input = input(f"Precio [{producto[4]}]: ").strip()
    precio = float(precio_input) if precio_input else producto[4]
    categoria = input(f"Categoría [{producto[5]}]: ").strip() or producto[5]
    if db_manager.actualizar_producto(producto_id, nombre, descripcion, cantidad, precio, categoria):
        imprimir_Exito("Producto actualizado exitosamente.")
    else:
        imprimir_Error("Error al actualizar el producto.")

def menu_eliminar_producto():
    imprimir_Titulo("Eliminar Producto")
    producto_id = validar_Input_int("Ingrese el ID del producto a eliminar")
    producto = db_manager.buscar_producto_por_id(producto_id)
    if not producto:
        imprimir_Error("Producto no encontrado.")
        return
    confirmacion = input(f"¿Está seguro de que desea eliminar el producto '{producto[1]}'? (s/n): ").strip().lower()
    if confirmacion == 's':
        if db_manager.eliminar_producto(producto_id):
            imprimir_Exito("Producto eliminado exitosamente.")
        else:
            imprimir_Error("Error al eliminar el producto.")
    else:
        imprimir_Exito("Operación cancelada.")

def menu_buscar_producto():
    imprimir_Titulo("Buscar Producto")
    texto = validar_Input_str("Ingrese el texto para buscar en nombre o categoría")
    productos = db_manager.buscar_producto_por_texto(texto)
    mostrar_tabla(productos)

def menu_reporte_inventario():
    imprimir_Titulo("Reporte de Inventario")
    productos = db_manager.obtener_productos()
    total_valor = sum(producto[3] * producto[4] for producto in productos)
    print(f"Total de productos en inventario: {len(productos)}")
    print(f"Valor total del inventario: ${total_valor:.2f}")

def main():
    db_manager.inicializar_base_datos()
    while True:
        limpiar_Pantalla()
        imprimir_Titulo("Sistema de Gestión de Inventario")
        print("1. Registrar Nuevo Producto")
        print("2. Ver Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Reporte de Inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == '1':
            menu_registrar()
        elif opcion == '2':
            menu_ver_productos()
        elif opcion == '3':
            menu_actualizar_producto()
        elif opcion == '4':
            menu_eliminar_producto()
        elif opcion == '5':
            menu_buscar_producto()
        elif opcion == '6':
            menu_reporte_inventario()
        elif opcion == '7':
            imprimir_Exito("Saliendo del sistema. ¡Hasta luego!")
            sys.exit()
        else:
            imprimir_Error("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
