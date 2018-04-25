from flask import render_template
from app import appvar
from .forms import SearchForm
    
@appvar.route('/')
@appvar.route('/index')
def index():
    return render_template('index.html', title='Home')
