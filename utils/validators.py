import re


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def validar_password(password):
    return len(password) >= 6


def validar_texto_minimo(texto, minimo=3):
    return texto is not None and len(texto.strip()) >= minimo


def validar_campos_vacios(data):
    for campo in data:
        if not str(data[campo]).strip():
            return False
    return True