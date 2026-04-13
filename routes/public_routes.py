from flask import Blueprint, render_template
from data.enfermedades import enfermedades
from models.alerta_model import obtener_alertas_activas
from models.noticia_model import obtener_noticias
from models.zona_model import obtener_zonas_riesgo

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def inicio():
    return render_template('public/index.html')

@public_bp.route('/enfermedades')
def ver_enfermedades():
    return render_template('public/enfermedades.html', enfermedades=enfermedades)

@public_bp.route('/alertas')
def alertas():
    lista_alertas = obtener_alertas_activas()
    return render_template('public/alertas.html', alertas=lista_alertas)

@public_bp.route('/noticias')
def noticias():
    lista_noticias = obtener_noticias()
    return render_template('public/noticias.html', noticias=lista_noticias)

@public_bp.route('/zonas')
def zonas():
    lista_zonas = obtener_zonas_riesgo()
    return render_template('public/zonas.html', zonas=lista_zonas)