import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

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


class Desenvolvedores(Resource):

    def get(self, id):
        try:
            resultado = desenvolvedores[id]
        except IndexError:
            resultado = {'status': 'erro', 'mensagem': 'Desenvolvedor de ID {} nao existe!'.format(id)}
        except Exception:
            resultado = {'status': 'erro', 'mensagem': 'Erro desconhecido!'}
        return resultado

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return desenvolvedores[id]

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'Registro inserido'}


api.add_resource(Desenvolvedores, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == "__main__":
    app.run()
