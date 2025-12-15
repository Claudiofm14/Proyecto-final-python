import sqlite3
from utils.helpers import imprimir_Error
from config import BD_NAME, TABLE_NAME

def obtener_conexion()-> sqlite3.Connection:
    """Establece y devuelve una conexión a la base de datos SQLite."""
    return sqlite3.connect(BD_NAME)

def inicializar_base_datos()-> None:
    """Crea la tabla de productos si no existe."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                )
            ''')
            conexion.commit()
    except sqlite3.Error as e:
        imprimir_Error(f"Error al inicializar la base de datos: {e}")
        
def registrar_producto(nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str)-> None:
    """Registra un nuevo producto en la base de datos."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (nombre, descripcion, cantidad, precio, categoria)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, cantidad, precio, categoria))
            conexion.commit()
            return True
    except sqlite3.Error as e:
        imprimir_Error(f"Error al registrar el producto: {e}")
        return False

def obtener_productos()-> list:
    """Obtiene todos los productos de la base de datos."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'SELECT * FROM {TABLE_NAME}')
            productos = cursor.fetchall()
            return productos
    except sqlite3.Error as e:
        imprimir_Error(f"Error al obtener los productos: {e}")
        return []

def buscar_producto_por_id(producto_id: int)-> tuple:
    """Busca un producto por su ID."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = ?', (producto_id,))
            producto = cursor.fetchone()
            return producto
    except sqlite3.Error as e:
        imprimir_Error(f"Error al buscar el producto: {e}")
        return None

def buscar_producto_por_texto(texto: str)-> list:
    """Busca productos que coincidan con el texto en nombre o descripción."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'''
                SELECT * FROM {TABLE_NAME}
                WHERE nombre LIKE ? OR categoria LIKE ?
            ''', (f'%{texto}%', f'%{texto}%'))
            productos = cursor.fetchall()
            return productos
    except sqlite3.Error as e:
        imprimir_Error(f"Error al buscar productos: {e}")
        return []

def actualizar_producto(producto_id: int, nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str)-> None:
    """Actualiza los detalles de un producto existente."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'''
                UPDATE {TABLE_NAME}
                SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                WHERE id = ?
            ''', (nombre, descripcion, cantidad, precio, categoria, producto_id))
            if cursor.rowcount == 0:
                conexion.commit()
                return True
    except sqlite3.Error as e:
        imprimir_Error(f"Error al actualizar el producto: {e}")
        return False

def eliminar_producto(producto_id: int)-> None:
    """Elimina un producto de la base de datos."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = ?', (producto_id,))
            conexion.commit()
    except sqlite3.Error as e:
        imprimir_Error(f"Error al eliminar el producto: {e}")

def reportar_bajo_stock(umbral: int)-> list:
    """Genera un reporte de productos con stock por debajo del umbral especificado."""
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE cantidad < ?', (umbral,))
            productos = cursor.fetchall()
            return productos
    except sqlite3.Error as e:
        imprimir_Error(f"Error al generar el reporte de bajo stock: {e}")
        return []



