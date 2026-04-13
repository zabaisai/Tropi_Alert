from models.conexion import obtener_conexion

def obtener_noticias():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT id, titulo, contenido, fecha_publicacion, autor
        FROM noticias
        ORDER BY fecha_publicacion DESC, id DESC
    """
    cursor.execute(sql)
    noticias = cursor.fetchall()

    cursor.close()
    conexion.close()

    return noticias