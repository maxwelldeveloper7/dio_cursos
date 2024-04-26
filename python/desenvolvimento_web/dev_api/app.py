""" Implementa uma API REST """
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Maxwell',
        'habilidades':['Python', 'Flask']
    },
    {
        'id':'1',
        'nome':'Chaves',
        'habilidades':['Python', 'Django']
    }
]

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    """Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor """
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        print(response)
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    """ Lista todos os desenvolvedores e permite registrar um novo desenvolvedor """
    if request.method == 'POST':
        dados  = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
