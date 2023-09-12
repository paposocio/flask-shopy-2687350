from flask import render_template
from . import clientes
import app
from .forms import RegistrarClienteForm

#rutas del modulo "clientes"
@clientes.route("/listar")
def listar():
   
    # listar los productos utilizando
    # modelos
    productos = app.models.Cliente.query.all()
    return render_template("index.html" , 
                           clientes = clientes)

@clientes.route("/nuevo" ,
                  methods= ["GET" , "POST"])
def nuevo():
     #definir el formulario
    form = RegistrarClienteForm()
    #definir el objeto cliente vacio
    p= app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
       
        return "cliente registrado"

    return render_template("new.html" , 
                           form = form) 


