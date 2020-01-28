import json

from flask import Flask, jsonify, request

app = Flask(__name__)

app.config.from_object('config')

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Pedro',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Victor',
        'habilidades': ['PHP', 'Laravel']
    }
]


@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    resultado = ''
    if request.method == 'GET':
        try:
            resultado = jsonify(desenvolvedores[id])
        except IndexError:
            resultado = jsonify({'status': 'erro', 'mensagem': 'Desenvolvedor de ID {} nao existe!'.format(id)})
        except Exception:
            resultado = jsonify({'status': 'erro', 'mensagem': 'Erro desconhecido!'})

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        resultado = desenvolvedores[id]
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        resultado = jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})
    return resultado


@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    resultado = ''
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        resultado = jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        resultado = jsonify(desenvolvedores)
    return resultado




if __name__ == '__main__':
    app.run()
