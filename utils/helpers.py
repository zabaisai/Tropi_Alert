def color_riesgo(nivel):
    if nivel == "alto":
        return "danger"
    elif nivel == "medio":
        return "warning"
    elif nivel == "bajo":
        return "success"
    return "secondary"


def resumen_texto(texto, limite=120):
    if texto and len(texto) > limite:
        return texto[:limite] + "..."
    return texto