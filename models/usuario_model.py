from models.conexion import obtener_conexion
from werkzeug.security import generate_password_hash, check_password_hash


def crear_usuario(nombre, correo, contrasena, rol):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    contrasena_hash = generate_password_hash(contrasena)

    sql = """
        INSERT INTO usuarios (nombre, correo, contrasena, rol)
        VALUES (%s, %s, %s, %s)
    """
    valores = (nombre, correo, contrasena_hash, rol)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def buscar_usuario_por_correo(correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = "SELECT * FROM usuarios WHERE correo = %s"
    cursor.execute(sql, (correo,))
    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario


def verificar_usuario(correo, contrasena):
    usuario = buscar_usuario_por_correo(correo)

    if usuario and check_password_hash(usuario['contrasena'], contrasena):
        return usuario

    return None


def obtener_todos_los_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT id, nombre, correo, rol, fecha_registro
        FROM usuarios
        ORDER BY id DESC
    """
    cursor.execute(sql)
    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return usuarios