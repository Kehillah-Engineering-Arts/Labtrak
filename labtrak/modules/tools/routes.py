from . import controllers
from flask import render_template, redirect, url_for
from flask import Blueprint

import os

tools_bp = Blueprint('tools', __name__, template_folder='templates')


@tools_bp.route('/')
def index():
    tools = controllers.get_tools()
    return render_template('tools.html', tools=tools)


@tools_bp.route('/pages')
@tools_bp.route('/pages/<tool>')
def pages(tool=None):
    if not tool:
        return redirect(url_for('tools.index'))
    else:
        try:
            path = os.path.join(os.getcwd(), 'labtrak', 'content', 'tools', tool)
            with open(path) as f:
                return f.read()
        except FileNotFoundError:
            print('%s not found.' % path)
            return redirect(url_for('tools.index'))
