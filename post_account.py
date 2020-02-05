import requests
import json
import base64

def POST_userLogin (url='',headers='',cChave = ''):
    if url == '':
        print("Não há url")
    if headers == '':
        print("Sem headers")
    if cChave == {}:
        print("Json VAZIO")
    #cChave = cChave.strip(" ")
    #cChave = cChave.strip("\n")
    #print(cChave)
    api_url = "{0}user".format(url)
    Post_request = requests.post(api_url, headers=headers, json=cChave)
    print(Post_request)

    if Post_request.status_code == 200 or Post_request.status_code == 201:
        return json.loads(Post_request.content.decode('utf-8'))
    else:
        return None

def POST_AbrirCham (url='',headers='',cChave = ''):
    if url == '':
        print("Não há url")
    if headers == '':
        print("Sem headers")
    if cChave == {}:
        print("Json VAZIO")
    #cChave = cChave.strip(" ")
    #cChave = cChave.strip("\n")
    #print(cChave)
    api_url = "{0}servicedesk/create/".format(url)
    Post_request = requests.post(api_url, headers=headers, json=cChave)
    print(Post_request)

    if Post_request.status_code == 200 or Post_request.status_code == 201:
        return json.loads(Post_request.content.decode('utf-8'))
    else:
        return None
