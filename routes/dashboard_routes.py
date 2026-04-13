from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.reporte_model import crear_reporte, obtener_reportes
from utils.auth import redirigir_si_no_logueado
from utils.validators import validar_campos_vacios, validar_texto_minimo

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
def dashboard():
    control = redirigir_si_no_logueado()
    if control:
        return control

    return render_template('dashboard/dashboard.html')


@dashboard_bp.route('/reporte', methods=['GET', 'POST'])
def reporte():
    control = redirigir_si_no_logueado()
    if control:
        return control

    if request.method == 'POST':
        ubicacion = request.form['ubicacion']
        tipo_foco = request.form['tipo_foco']
        descripcion = request.form['descripcion']
        fecha_reporte = request.form['fecha_reporte']
        nivel_riesgo = request.form['nivel_riesgo']
        usuario_id = session['usuario_id']

        if not validar_campos_vacios({
            'ubicacion': ubicacion,
            'tipo_foco': tipo_foco,
            'descripcion': descripcion,
            'fecha_reporte': fecha_reporte,
            'nivel_riesgo': nivel_riesgo
        }):
            flash('Todos los campos del reporte son obligatorios')
            return redirect(url_for('dashboard.reporte'))

        if not validar_texto_minimo(ubicacion, 5):
            flash('La ubicación debe ser más específica')
            return redirect(url_for('dashboard.reporte'))

        if not validar_texto_minimo(descripcion, 15):
            flash('La descripción debe tener al menos 15 caracteres')
            return redirect(url_for('dashboard.reporte'))

        crear_reporte(
            ubicacion,
            tipo_foco,
            descripcion,
            fecha_reporte,
            nivel_riesgo,
            usuario_id
        )

        flash('Reporte registrado correctamente')
        return redirect(url_for('dashboard.reporte'))

    lista_reportes = obtener_reportes()
    return render_template('dashboard/reporte.html', reportes=lista_reportes)