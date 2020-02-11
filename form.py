from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import PasswordField

class Comentario(Form):
    user = EmailField("Escreva seu E-mail:")
    password = PasswordField("Escreva sua senha:")
    #idade = IntegerField("Qual sua idade?")
    #comentario = TextField("Comentário")

class CriarChamado(Form):
    cPriority       = SelectField(u'Prioridade',choices=[('0','Urgente'),('1','Alta'),('2','Média'),('3','Baixa')])
    cIdUser         = StringField("ID de Usuário")
    ctitle          = StringField("Titulo do chamado")
    cidCategory     = SelectField(u'Categoria',choices=[('001','INTERNO'),('002','SISTEMA')])
    cidPlataform    = SelectField(u'Plataforma',choices=[('000001','PROTHEUS')])
    cidSubject      = SelectField(u'Assunto',choices=[('000001','FATURAMENTO')])
    cidProcess      = SelectField(u'Processo',choices=[('000009','Pedido de Venda')])
    cidUsrObs       = StringField("Observador do chamado (não obrigatório)")
    ctag            = StringField("Tag")
    cmsg            = TextAreaField("Descrição do chamado")
    cidEntity       = SelectField(u"Entidade",choices=[('000001','Smith-Nephew')])
    cidGroup        = SelectField(u"Grupo",choices=[('01','São Paulo')])
    cidSubGroup     = SelectField(u"Sub-Grupo",choices=[('002','FATURAMENTO')])

