# 🦟 Sistema Inteligente de Monitoreo de Enfermedades Tropicales

![Estado](https://img.shields.io/badge/Estado-Funcional-success)
![Backend](https://img.shields.io/badge/Backend-Flask-blue)
![DB](https://img.shields.io/badge/Base%20de%20Datos-MySQL-orange)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-yellow)

---

## 🌎 Descripción

El **Sistema Informativo para la Prevención de Enfermedades Tropicales** es una plataforma web desarrollada en **Flask (Python)** que permite la gestión, monitoreo y consulta de información sanitaria en zonas tropicales.

La aplicación centraliza información clave sobre enfermedades, alertas, zonas de riesgo y reportes ciudadanos, facilitando la toma de decisiones en salud pública.

---

## 🎯 Objetivo

Crear una herramienta digital que permita:

- Consultar enfermedades tropicales
- Visualizar alertas sanitarias
- Identificar zonas de riesgo
- Registrar focos de contagio
- Gestionar información desde un panel administrador

---

## 🧠 Problema que Resuelve

En muchos entornos:

- La información sanitaria está dispersa  
- No hay seguimiento de focos  
- No existe monitoreo centralizado  

👉 Este sistema integra todo en una sola plataforma.

---

## 🚀 Funcionalidades

### 👤 Usuarios
- Registro de usuario
- Inicio de sesión
- Control de sesión

### 🦠 Enfermedades
- Información estructurada:
  - Qué es
  - Síntomas
  - Prevención
  - Tratamiento
  - Signos de alarma

### 🚨 Alertas
- Visualización de alertas activas
- Clasificación por nivel de riesgo:
  - 🔴 Alto
  - 🟡 Medio
  - 🟢 Bajo

### 🗺️ Zonas de riesgo
- Consulta de zonas afectadas
- Clasificación por nivel

### 📋 Reportes
- Registro de focos sanitarios
- Seguimiento de casos

### 🛠️ Panel administrador
- Gestión de usuarios
- Gestión de reportes
- Control de alertas, noticias y zonas

---

## 🧱 Arquitectura del Proyecto

El sistema está organizado de forma modular siguiendo buenas prácticas:
sistema_enfermedades_tropicales/
│
├── models/ # Acceso a base de datos
│ ├── usuario_model.py
│ ├── reporte_model.py
│ └── ...
│
├── routes/ # Controladores (Flask)
│ ├── public_routes.py
│ ├── auth_routes.py
│ ├── dashboard_routes.py
│ └── admin_routes.py
│
├── templates/ # Vistas HTML (Jinja2)
│ ├── public/
│ ├── auth/
│ ├── dashboard/
│ └── admin/
│
├── static/ # Recursos estáticos
│ ├── css/
│ ├── js/
│ └── img/
│
├── utils/ # Lógica reutilizable
│ ├── auth.py # Manejo de sesión
│ ├── validators.py # Validaciones
│ └── helpers.py # Funciones auxiliares
│
├── app.py # Archivo principal
├── config.py # Configuración
└── README.md

---

## 🧠 Arquitectura Interna

El sistema separa responsabilidades en:

- **Routes:** lógica del flujo (Flask)
- **Models:** consultas SQL
- **Utils:**
  - `auth.py` → manejo de sesión
  - `validators.py` → validaciones
  - `helpers.py` → funciones reutilizables
- **Templates:** interfaz visual

---

## 🔐 Autenticación y Seguridad

- Contraseñas encriptadas con `Werkzeug`
- Validaciones de formularios
- Control de sesiones (`session`)
- Protección de rutas privadas
- Control de acceso por roles (`admin / usuario`)

---

## 💬 Sistema de Flash Messages

El sistema utiliza `flash()` de Flask para mostrar mensajes dinámicos:

Ejemplo:

```python
flash("Usuario registrado correctamente")
flash("Correo inválido")
flash("Debes iniciar sesión primero")

EN EL FRONTEND
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for msg in messages %}
      <div class="flash-message">{{ msg }}</div>
    {% endfor %}
  {% endif %}
{% endwith %}
Esto permite:

Mostrar errores
Confirmaciones
Alertas de seguridad
⚙️ Tecnologías Utilizadas
Backend
Python
Flask
MySQL (XAMPP)
Werkzeug
Frontend
HTML5
CSS3
JavaScript
Arquitectura
Jinja2
Blueprints (Flask)
Modularización
🗄️ Base de Datos

Tablas principales:

usuarios
reportes
alertas
noticias
zonas_riesgo