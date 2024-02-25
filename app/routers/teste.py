from flask_restx import Resource, Namespace

nst = Namespace('/teste')


@nst.route('/')
class Teste(Resource):
    def index():
        return { 'Teste': 'sucess' }
