from flask import Blueprint
productos = Blueprint('clientes',
                      __name__,
                      url_prefix = '/clientes',
                      template_folder = 'templates')
#vincular el archivo de rutas
from . import routes