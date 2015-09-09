from flask import Flask
from datetime import date
from . import config

app = Flask(__name__)

app.config.from_object('labtrak.config.Develop')

# blueprints
from labtrak.modules import home
app.register_blueprint(home.home_bp)

# Template Globals
app.jinja_env.globals['year'] = date.today().year
