from flask import Blueprint

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')


@blueprint.route('/hello_world')
def hello_world():
    message = 'Hello World'
    return message

@blueprint.route('/echo?name')
def echo(name):
    message = f'Hello {name}'
    return message