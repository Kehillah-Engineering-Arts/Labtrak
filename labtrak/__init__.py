from flask import Flask
from datetime import date
from . import config

app = Flask(__name__)

app.config.from_object('labtrak.config.Develop')

# Flask blueprints
from labtrak.modules import home, tools
app.register_blueprint(home.home_bp)
app.register_blueprint(tools.tools_bp, url_prefix='/tools')

# Template Globals
app.jinja_env.globals['year'] = date.today().year
