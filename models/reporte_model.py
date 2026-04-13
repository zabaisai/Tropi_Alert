from models.conexion import obtener_conexion

def crear_reporte(ubicacion, tipo_foco, descripcion, fecha_reporte, nivel_riesgo, usuario_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO reportes_focos
        (ubicacion, tipo_foco, descripcion, fecha_reporte, nivel_riesgo, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (ubicacion, tipo_foco, descripcion, fecha_reporte, nivel_riesgo, usuario_id)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def obtener_reportes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT rf.id, rf.ubicacion, rf.tipo_foco, rf.descripcion,
               rf.fecha_reporte, rf.nivel_riesgo, u.nombre AS usuario_nombre
        FROM reportes_focos rf
        LEFT JOIN usuarios u ON rf.usuario_id = u.id
        ORDER BY rf.fecha_reporte DESC, rf.id DESC
    """
    cursor.execute(sql)
    reportes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return reportes