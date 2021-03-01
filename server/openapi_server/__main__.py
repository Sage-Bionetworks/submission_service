#!/usr/bin/env python3

import connexion
import flask
from mongoengine import connect

from openapi_server import encoder
from openapi_server.config import Config

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Submission API'},
            pythonic_params=True)

connect(
    db=Config().db_database,
    username=Config().db_username,
    password=Config().db_password,
    host=Config().db_host
)

app.add_url_rule('/', 'root', lambda: flask.redirect('/api/v1/ui'))
app.add_url_rule('/ui', 'ui', lambda: flask.redirect('/api/v1/ui'))


def main():
    app.run(port=Config().server_port, debug=False)


if __name__ == '__main__':
    main()
