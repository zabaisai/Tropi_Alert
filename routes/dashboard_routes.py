from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.reporte_model import crear_reporte, obtener_reportes, eliminar_reporte_por_id
from models.usuario_model import obtener_profesionales_salud, eliminar_personal_salud_por_usuario_id, obtener_estudiantes
from utils.auth import redirigir_si_no_logueado
from utils.validators import validar_campos_vacios, validar_texto_minimo
from werkzeug.utils import secure_filename
import os


dashboard_bp = Blueprint('dashboard', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        if session.get('rol') != 'salud':
            flash('Solo el personal de salud puede registrar reportes de focos.')
            return redirect(url_for('dashboard.reporte'))

        ubicacion = request.form['ubicacion']
        tipo_foco = request.form['tipo_foco']
        descripcion = request.form['descripcion']
        fecha_reporte = request.form['fecha_reporte']
        nivel_riesgo = request.form['nivel_riesgo']
        usuario_id = session['usuario_id']

        foto = request.files.get('foto_reporte')
        ruta_foto_bd = None

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

        if foto and foto.filename != '':
            if not allowed_file(foto.filename):
                flash('Formato de imagen no permitido. Usa PNG, JPG, JPEG o WEBP')
                return redirect(url_for('dashboard.reporte'))

            nombre_archivo = secure_filename(foto.filename)
            nombre_archivo = f"reporte_{usuario_id}_{nombre_archivo}"

            carpeta_destino = os.path.join('static', 'uploads', 'reportes')
            os.makedirs(carpeta_destino, exist_ok=True)

            ruta_foto = os.path.join(carpeta_destino, nombre_archivo)
            foto.save(ruta_foto)

            ruta_foto_bd = f"uploads/reportes/{nombre_archivo}"

        crear_reporte(
            ubicacion,
            tipo_foco,
            descripcion,
            fecha_reporte,
            nivel_riesgo,
            usuario_id,
            ruta_foto_bd
        )

        flash('Reporte registrado correctamente')
        return redirect(url_for('dashboard.reporte'))

    lista_reportes = obtener_reportes()
    lista_profesionales = obtener_profesionales_salud()
    lista_estudiantes = obtener_estudiantes()

    return render_template(
        'dashboard/reporte.html',
        reportes=lista_reportes,
        profesionales=lista_profesionales,
        estudiantes=lista_estudiantes
    )


@dashboard_bp.route('/eliminar-reporte/<int:reporte_id>', methods=['POST'])
def eliminar_reporte(reporte_id):
    control = redirigir_si_no_logueado()
    if control:
        return control

    if session.get('rol') != 'gerente':
        flash('No tienes permisos para eliminar reportes')
        return redirect(url_for('dashboard.reporte'))

    eliminar_reporte_por_id(reporte_id)

    flash('Reporte eliminado correctamente')
    return redirect(url_for('dashboard.reporte'))


@dashboard_bp.route('/eliminar-personal-salud/<int:usuario_id>', methods=['POST'])
def eliminar_personal_salud(usuario_id):
    control = redirigir_si_no_logueado()
    if control:
        return control

    if session.get('rol') != 'gerente':
        flash('No tienes permisos para eliminar personal de salud')
        return redirect(url_for('dashboard.reporte'))

    eliminar_personal_salud_por_usuario_id(usuario_id)

    flash('Personal de salud eliminado correctamente')
    return redirect(url_for('dashboard.reporte'))