# dependencias del proyecto
from flask import Flask, render_template 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687350'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# crear el objeto sqlalchemy
db = SQLAlchemy(app)
#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

#crear el formulario de registro
#de productos
class RegistroProductosForm(FlaskForm):
    nombre_producto = StringField('Nombre del producto')


##Modelos <<entities>>
class Cliente(db.Model):
    
    __tablename__ = "clientes"
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))

class Producto(db.Model):

    __tablename__ = "productos"
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(64))
    precio = db.Column(db.Numeric(precision = 10 , 
                                  scale = 2) )
    imagen = db.Column(db.String(100),
                        nullable = True)



class Venta(db.Model):

    __tablename__ = "ventas"
    id = db.Column(db.Integer , primary_key=True)
    fecha = db.Column(db.DateTime ,
                       default = datetime.utcnow )
    cliente_id = db.Column(db.Integer, 
                db.ForeignKey('clientes.id'))

class Detalle(db.Model):

    __tablename__ = "detalles"
    id = db.Column(db.Integer , primary_key=True)
    cliente_id = db.Column(db.Integer, 
                db.ForeignKey('ventas.id'))
    producto_id = db.Column(db.Integer, 
                db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)

@app.route('/productos/registrar')
def registrar():
    return render_template('registrar.html')





