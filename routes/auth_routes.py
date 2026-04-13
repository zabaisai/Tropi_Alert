from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario_model import crear_usuario, buscar_usuario_por_correo, verificar_usuario
from utils.auth import login_usuario, logout_usuario
from utils.validators import validar_email, validar_password, validar_texto_minimo, validar_campos_vacios

auth_bp = Blueprint('auth', __name__)


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

            if usuario['rol'] == 'admin':
                return redirect(url_for('admin.panel_admin'))

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

    if not validar_campos_vacios({
        'nombre': nombre,
        'correo': correo,
        'contrasena': contrasena,
        'rol': rol
    }):
        flash('Todos los campos son obligatorios')
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

    usuario_existente = buscar_usuario_por_correo(correo)

    if usuario_existente:
        flash('El correo ya está registrado')
        return redirect(url_for('auth.registro'))

    crear_usuario(nombre, correo, contrasena, rol)
    flash('Usuario registrado correctamente')
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
def logout():
    logout_usuario()
    flash('Sesión cerrada correctamente')
    return redirect(url_for('auth.login'))