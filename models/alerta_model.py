from models.conexion import obtener_conexion

def obtener_alertas_activas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT id, titulo, descripcion, nivel_riesgo, fecha_publicacion, estado
        FROM alertas
        WHERE estado = 'activa'
        ORDER BY fecha_publicacion DESC
    """
    cursor.execute(sql)
    alertas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return alertas