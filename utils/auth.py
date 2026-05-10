from flask import session, redirect, url_for, flash


def login_usuario(usuario):
    session['usuario_id'] = usuario['id']
    session['usuario_nombre'] = usuario['nombre']
    session['usuario_rol'] = usuario['rol']
    session['rol'] = usuario['rol']


def logout_usuario():
    session.clear()


def usuario_logueado():
    return 'usuario_id' in session


def es_admin():
    return session.get('usuario_rol') == 'admin'


def redirigir_si_no_logueado():
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión primero')
        return redirect(url_for('auth.login'))
    return None


def redirigir_si_no_admin():
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión primero')
        return redirect(url_for('auth.login'))

    if session.get('usuario_rol') != 'admin':
        flash('No tienes permisos para acceder a esta sección')
        return redirect(url_for('dashboard.dashboard'))

    return None