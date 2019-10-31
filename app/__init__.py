from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    
    # Creating app configs
    app.config.from_object(config_options[config_name])
    
    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint - main and auth  
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app

