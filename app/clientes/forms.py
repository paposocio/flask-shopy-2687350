from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , PasswordField , EmailField
from wtforms.validators  import InputRequired

class RegistrarClienteForm(FlaskForm):
    nombreUser = StringField ("nombre de usuario:" , validators = [InputRequired(message="nombre de usuario requerido")] )
    clave = PasswordField ("clave:" , validators = [InputRequired(message="contraseña requerida")] )
    correo = EmailField ("correo:" , validators = [InputRequired(message="correo requerido")] )
    submit = SubmitField("Guardar")
