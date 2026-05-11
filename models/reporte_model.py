from models.conexion import obtener_conexion


def crear_reporte(
    ubicacion,
    tipo_foco,
    descripcion,
    fecha_reporte,
    nivel_riesgo,
    usuario_id,
    foto_reporte=None
):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO reportes_focos
        (ubicacion, tipo_foco, descripcion, fecha_reporte, nivel_riesgo, usuario_id, foto_reporte)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        ubicacion,
        tipo_foco,
        descripcion,
        fecha_reporte,
        nivel_riesgo,
        usuario_id,
        foto_reporte
    )

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def obtener_reportes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT 
            rf.id,
            rf.ubicacion,
            rf.tipo_foco,
            rf.descripcion,
            rf.fecha_reporte,
            rf.nivel_riesgo,
            rf.foto_reporte,
            u.nombre AS usuario_nombre,
            u.rol,
            ps.area,
            ps.foto AS foto_personal
        FROM reportes_focos rf
        LEFT JOIN usuarios u ON rf.usuario_id = u.id
        LEFT JOIN personal_salud ps ON u.id = ps.usuario_id
        ORDER BY rf.fecha_reporte DESC, rf.id DESC
    """

    cursor.execute(sql)
    reportes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return reportes


def eliminar_reporte_por_id(reporte_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        DELETE FROM reportes_focos 
        WHERE id = %s
    """

    cursor.execute(sql, (reporte_id,))
    conexion.commit()

    cursor.close()
    conexion.close()