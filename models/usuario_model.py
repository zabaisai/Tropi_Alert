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

    usuario_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return usuario_id


def crear_personal_salud(usuario_id, foto, area):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO personal_salud (usuario_id, foto, area)
        VALUES (%s, %s, %s)
    """

    valores = (usuario_id, foto, area)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def buscar_usuario_por_correo(correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM usuarios
        WHERE correo = %s
    """

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
        SELECT 
            id, 
            nombre, 
            correo, 
            rol, 
            fecha_registro
        FROM usuarios
        ORDER BY id DESC
    """

    cursor.execute(sql)
    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return usuarios


def obtener_profesionales_salud():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT 
            u.id,
            u.nombre,
            u.correo,
            u.fecha_registro,
            ps.area,
            ps.foto
        FROM usuarios u
        INNER JOIN personal_salud ps ON u.id = ps.usuario_id
        WHERE u.rol = 'salud'
        ORDER BY u.id DESC
    """

    cursor.execute(sql)
    profesionales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return profesionales


def obtener_estudiantes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT 
            id,
            nombre,
            correo,
            fecha_registro
        FROM usuarios
        WHERE rol = 'estudiante'
        ORDER BY id DESC
    """

    cursor.execute(sql)
    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return estudiantes


def eliminar_personal_salud_por_usuario_id(usuario_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql_reportes = """
        DELETE FROM reportes_focos 
        WHERE usuario_id = %s
    """
    cursor.execute(sql_reportes, (usuario_id,))

    sql_personal = """
        DELETE FROM personal_salud 
        WHERE usuario_id = %s
    """
    cursor.execute(sql_personal, (usuario_id,))

    sql_usuario = """
        DELETE FROM usuarios 
        WHERE id = %s AND rol = 'salud'
    """
    cursor.execute(sql_usuario, (usuario_id,))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_estudiante_por_id(usuario_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        DELETE FROM usuarios
        WHERE id = %s AND rol = 'estudiante'
    """

    cursor.execute(sql, (usuario_id,))
    conexion.commit()

    cursor.close()
    conexion.close()