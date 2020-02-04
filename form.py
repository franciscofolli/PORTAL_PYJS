from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField

class Comentario(Form):
    user = EmailField("Escreva seu E-mail:")
    password = StringField("Escreva sua senha:")
    #idade = IntegerField("Qual sua idade?")
    #comentario = TextField("Comentário")