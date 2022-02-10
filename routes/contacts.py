from flask import Blueprint

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return "Hello world"


@contacts.route("/new")
def addcontact():
    return "salvando contacto"
