from flask import Flask
from flask_login import LoginManager
from views.landing_views import landing_bp
from views.auth_views import auth_bp  # если есть auth модуль

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # Инициализация расширений
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    # Регистрация blueprint'ов
    app.register_blueprint(landing_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')  # если есть
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)