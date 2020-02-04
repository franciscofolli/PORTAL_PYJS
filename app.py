from flask import Flask, render_template #Importa funções flask e renderização de templates html
from flask import request #importa funções de parâmetros para request
import form
import json
import requests
import post_account
import base64

# notações de variáveis
#f --> função
#c --> caracter/string
#ft --> float
#a --> array
#l --> boolean

app = Flask(__name__) #Instância para que o Flask funcione / Objeto
#caso criar uma pasta especifica para templates, adicionar virgula e a função 
#template_folder = "nome da pasta"
#ex: app = Flask(__name__, template_folder = 'pãotemplates')



#Pagina inicial
@app.route('/', methods = ['GET', 'POST']) # Define Rotas para serem executadas / Embrulho --> descorador --> Wrap
# e logo a seguir as requisições permitidas em determinada rota 
def index():#Chamada de função que ira ser executada ao utilizar a Rota
    return render_template('index.html')


@app.route('/cursos', methods = ['GET', 'POST'])
def curs():
    return render_template('cursos.html')

#page detalhes dos cursos/faculdade
@app.route('/detalhes', methods = ['GET', 'POST'])
def detalhes():
    return render_template('detalhes.html')

#page disciplinas
@app.route('/disciplinas', methods = ['GET', 'POST'])
def disciplinas():
    return render_template('disciplinas.html')
#page noticias
@app.route('/noticias', methods = ['GET', 'POST'])
def noticias():
    return render_template('noticias.html')

@app.route('/testeparam', methods = ['GET', 'POST']) #parametros simples com ? separando da rota
def param():
    nome = request.args.get('param1', 'não há valor neste parâmetro')
    email = request.args.get('param2', 'não há valor neste parâmetro')
    return f"o Parâmetro é {nome} e {email} "

#@app.route('/param/') #rota alternativa caso não seja informado valor
#@app.route('/param/<nome>/') #informar rota e o parâmetro junto separando por slash e sempre colocando mais uma na frente
#@app.route('/param/<nome>/<sobrenome>/') #adicionar mais parâmetros com mais rotas, assim acrescentando também o parâmetro
@app.route('/param2', methods = ['GET', 'POST'])#para validar um tipo de valor, como inteiro, coloque o tipo seguido por :
def param2(t=''):
    title = 'Curso Flask'
    comentario = form.Comentario(request.form)
    cUser = comentario.user.data
    cPass = comentario.password.data
    if cUser != "" and cPass != "":
        json = {"user":"{0}".format(cUser),
                "password":"{0}".format(cPass)

        }
        api_token =  base64.b64encode('fabio.desk:abc123'.encode("utf-8"))
        api_token = str(api_token)
        api_token = api_token.replace(api_token[:api_token.index('b')+1],"") 
        api_token = api_token.replace('b','')
        api_token = api_token.replace("'","")
        print("Basic {0}".format(api_token))
        api_url = 'http://192.168.15.251:8866/rest/appticketdfs/v1/'
        headers = { "Content-Type": "application/json",
                    "Authorization": "Basic {0}".format(api_token),
                    "XToken": "1234567890",
        			#"User-Agent": "PostmanRuntime/7.22.0",
        			"Accept": "*/*",
        			"Cache-Control": "no-cache",
        			#"Postman-Token": "a04e0af8-26ba-43d5-a6ea-b566498fed19",
        			#"Host": "192.168.15.251:8866",
        			#"Accept-Encoding": "gzip, deflate, br",
        			#"Content-Length": "80",
        			#"Connection": "keep-alive"
        			#"Origin":"http://192.168.15.251/rest"
        			}

        print(post_account.POST_userLogin(api_url,headers,json))
        print(json)
    return render_template('python_tags.html', form=comentario, title = title, json = json)
    # render_template('python_tags.html', nome=nome, sobrenome=sobrenome, idade=idade, lista=litswx, form=comentario)


app.run() # Executa o servidor por padrão na porta 5000

#app.run(debug = false | true, port = <informa porta personalizada>)



#Funções do Flask

#return render_template('python_tags.html', nome=nome, sobrenome=sobrenome, idade=idade)
#quando colocas-se variaveis nessa função é possivel chamar as variaveis no html utilizando {{ <nome da variavel> }}
#que devera ser definida na chamada da função, conforme abaixo.
#return render_template('nomedo.html', variavelparahtml=varpython, variavelparahtml=varpython, variavelparahtml=varpython)

#Request para criação de parâmetros.

#request.args.get('<nome da variavel>','<valor padrão caso não seja recebido valor na variável>')

#quando representado na url ficará por: /rota?<nome do parâmetro>='valor passado'

#ex: http://localhost:5000/testeparam?param1=Zeca%20Homem

#acrescentando chamadas de funções é possivel RETORNAR a quantidade de parâmetros maior, veja:

# @app.route('/testeparam')
# def param():
#     parametro = request.args.get('param1', 'não há valor neste parâmetro')
#     parametro2 = request.args.get('param2', 'não há valor neste parâmetro')
#     return f"o Parâmetro é {parametro} e {parametro2} "