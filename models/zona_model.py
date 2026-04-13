from models.conexion import obtener_conexion

def obtener_zonas_riesgo():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT id, nombre_zona, descripcion, nivel_riesgo, latitud, longitud
        FROM zonas_riesgo
        ORDER BY
            CASE nivel_riesgo
                WHEN 'alto' THEN 1
                WHEN 'medio' THEN 2
                WHEN 'bajo' THEN 3
            END,
            id DESC
    """
    cursor.execute(sql)
    zonas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return zonas