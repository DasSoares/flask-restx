from flask import Flask

from .extensions import api, db
from .resources import *
from .routers.teste import nst

import secrets

def create_app():
    
    app = Flask(__name__)
    # gerar uma chave secreta - secrets.token_hex(20)
    app.config['SECRET_KEY'] = 'cd0be4ba3ea0d157f3aa6ee9a7c5aab066cfb40f'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)
    api.add_namespace(nsc)
    api.add_namespace(nss)
    api.add_namespace(nst)

    return app