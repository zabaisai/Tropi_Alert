from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario_model import crear_usuario, buscar_usuario_por_correo, verificar_usuario, crear_personal_salud
from utils.auth import login_usuario, logout_usuario
from utils.validators import validar_email, validar_password, validar_texto_minimo, validar_campos_vacios
from werkzeug.utils import secure_filename
import os


auth_bp = Blueprint('auth', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        if not validar_campos_vacios({
            'correo': correo,
            'contrasena': contrasena
        }):
            flash('Todos los campos son obligatorios')
            return redirect(url_for('auth.login'))

        if not validar_email(correo):
            flash('Correo electrónico inválido')
            return redirect(url_for('auth.login'))

        if not validar_password(contrasena):
            flash('La contraseña debe tener al menos 6 caracteres')
            return redirect(url_for('auth.login'))

        usuario = verificar_usuario(correo, contrasena)

        if usuario:
            login_usuario(usuario)
            return redirect(url_for('dashboard.dashboard'))

        flash('Correo o contraseña incorrectos')
        return redirect(url_for('auth.login'))

    return render_template('auth/login.html')


@auth_bp.route('/registro')
def registro():
    return render_template('auth/registro.html')


@auth_bp.route('/guardar-registro', methods=['POST'])
def guardar_registro():
    nombre = request.form['nombre']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    rol = request.form['rol']

    area = request.form.get('area')
    foto = request.files.get('foto')

    if not validar_campos_vacios({
        'nombre': nombre,
        'correo': correo,
        'contrasena': contrasena,
        'rol': rol
    }):
        flash('Todos los campos son obligatorios')
        return redirect(url_for('auth.registro'))

    if rol not in ['estudiante', 'salud', 'gerente']:
        flash('Tipo de usuario inválido')
        return redirect(url_for('auth.registro'))

    if not validar_texto_minimo(nombre, 3):
        flash('El nombre debe tener al menos 3 caracteres')
        return redirect(url_for('auth.registro'))

    if not validar_email(correo):
        flash('Correo electrónico inválido')
        return redirect(url_for('auth.registro'))

    if not validar_password(contrasena):
        flash('La contraseña debe tener al menos 6 caracteres')
        return redirect(url_for('auth.registro'))

    if rol == 'salud':
        if not area or area.strip() == '':
            flash('El área profesional es obligatoria para el personal de salud')
            return redirect(url_for('auth.registro'))

        if not foto or foto.filename == '':
            flash('La foto de perfil es obligatoria para el personal de salud')
            return redirect(url_for('auth.registro'))

        if not allowed_file(foto.filename):
            flash('Formato de imagen no permitido. Usa PNG, JPG, JPEG o WEBP')
            return redirect(url_for('auth.registro'))

    usuario_existente = buscar_usuario_por_correo(correo)

    if usuario_existente:
        flash('El correo ya está registrado')
        return redirect(url_for('auth.registro'))

    usuario_id = crear_usuario(nombre, correo, contrasena, rol)

    if rol == 'salud':
        nombre_archivo = secure_filename(foto.filename)
        nombre_archivo = f"perfil_{usuario_id}_{nombre_archivo}"

        carpeta_destino = os.path.join('static', 'uploads', 'perfiles')
        os.makedirs(carpeta_destino, exist_ok=True)

        ruta_foto = os.path.join(carpeta_destino, nombre_archivo)
        foto.save(ruta_foto)

        ruta_foto_bd = f"uploads/perfiles/{nombre_archivo}"

        crear_personal_salud(usuario_id, ruta_foto_bd, area)

    flash('Usuario registrado correctamente')
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
def logout():
    logout_usuario()
    flash('Sesión cerrada correctamente')
    return redirect(url_for('auth.login'))