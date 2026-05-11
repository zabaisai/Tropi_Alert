from flask import Blueprint, render_template
from models.usuario_model import obtener_todos_los_usuarios
from models.reporte_model import obtener_reportes
from models.alerta_model import obtener_alertas_activas
from models.noticia_model import obtener_noticias
from models.zona_model import obtener_zonas_riesgo
from utils.auth import redirigir_si_no_admin
from utils.auth import redirigir_si_no_admin

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def panel_admin():
    control = redirigir_si_no_admin()
    if control:
        return control

    usuarios = obtener_todos_los_usuarios()
    reportes = obtener_reportes()
    alertas = obtener_alertas_activas()
    noticias = obtener_noticias()
    zonas = obtener_zonas_riesgo()

    return render_template(
        'admin/admin.html',
        total_usuarios=len(usuarios),
        total_reportes=len(reportes),
        total_alertas=len(alertas),
        total_noticias=len(noticias),
        total_zonas=len(zonas)
    )


@admin_bp.route('/usuarios')
def admin_usuarios():
    control = redirigir_si_no_admin()
    if control:
        return control

    usuarios = obtener_todos_los_usuarios()
    return render_template('admin/usuarios.html', usuarios=usuarios)


@admin_bp.route('/reportes')
def admin_reportes():
    control = redirigir_si_no_admin()
    if control:
        return control

    reportes = obtener_reportes()
    return render_template('admin/reportes.html', reportes=reportes)


@admin_bp.route('/alertas')
def admin_alertas():
    control = redirigir_si_no_admin()
    if control:
        return control

    alertas = obtener_alertas_activas()
    return render_template('admin/gestionar_alertas.html', alertas=alertas)


@admin_bp.route('/noticias')
def admin_noticias():
    control = redirigir_si_no_admin()
    if control:
        return control

    noticias = obtener_noticias()
    return render_template('admin/gestionar_noticias.html', noticias=noticias)


@admin_bp.route('/zonas')
def admin_zonas():
    control = redirigir_si_no_admin()
    if control:
        return control

    zonas = obtener_zonas_riesgo()
    return render_template('admin/gestionar_zonas.html', zonas=zonas)