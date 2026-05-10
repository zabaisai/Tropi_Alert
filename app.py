from flask import Flask
from config import Config
from routes.public_routes import public_bp
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.admin_routes import admin_bp
from utils.helpers import color_riesgo, resumen_texto


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(public_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(admin_bp)

app.jinja_env.globals.update(color_riesgo=color_riesgo)
app.jinja_env.globals.update(resumen_texto=resumen_texto)

if __name__ == '__main__':
    app.run(debug=True)