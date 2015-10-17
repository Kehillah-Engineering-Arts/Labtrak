from . import controllers
from flask import render_template, redirect, url_for
from flask import request
from flask import flash
from flask import Blueprint

import markdown2
import os

tools_bp = Blueprint('tools', __name__, template_folder='templates')


@tools_bp.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        tools = controllers.get_tools()
        return render_template('tools.html', tools=tools)


@tools_bp.route('/pages', methods=['GET'])
@tools_bp.route('/pages/<tool>', methods=['GET'])
def pages(tool=None):
    if request.method == 'GET':
        if not tool:
            return redirect(url_for('tools.index'))
        else:
            try:
                path = os.path.join(os.getcwd(), 'labtrak', 'content', 'tools', tool+'.md')
                with open(path) as f:
                    text = f.read()
                    content=markdown2.markdown(text)
                    #slice from the second character forward, of the first line
                    title = text.split('/n').pop(0)[2:].strip()
                    return render_template('pages/tool.html', title=title, content=content)
            except FileNotFoundError:
                flash('%s not found' % tool)
                return redirect(url_for('tools.index'))
