from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact  #Se encagara de que la carpeta models importe contacto para obtener sus funcionalidades
from utils.db import db # Esta linea de codigo se encarga en Importar la base de datos

contacts = Blueprint("contacts", __name__)


@contacts.route('/') #Aqui tenemos nuestra ruta principal
def index(): #Con esto nos permite obtener todos los datos desde la base de datos
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])#Este metodo que se encuentra post ligado a la funcion agregar contacto, se puede decir que se usa este metodo para agregar a un contacto nuevo
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))# Esta linea hara que Nos mandara a la página de inicio.


@contacts.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id) #Con el id se actualizara el contacto en la base de datos

    if request.method == "POST":
        #Con este codigo se obtendra los datos del formulario
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()#Guardar los cambios en la base de datos

        flash('Contact updated successfully!')#Mensaje 

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)#Se encarga de redirigir la pantalla donde estaba la informacion del contacto


@contacts.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id) #Se elimina mediante el id del contacto
    db.session.delete(contact)#SE ENCARGARA DE ELIMINAR CONTACTO
    db.session.commit()#GUARDARA LOS CAMBIOS EN LA BASE DE DATOS

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


@contacts.route("/about")
def about():
    return render_template("about.html")
