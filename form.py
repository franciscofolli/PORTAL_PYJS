from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField

class Comentario(Form):
    nome = StringField("Escreva seu nome:")
    email = EmailField("Escreva seu E-mail:")
    idade = IntegerField("Qual sua idade?")
    comentario = TextField("Comentário")