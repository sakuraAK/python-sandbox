from flask import Blueprint, request, jsonify
from mocks import USERS
from e2e_demo import DbWrapper


blueprint = Blueprint('api', __name__, url_prefix='/basic_api')


def get_users():
    return USERS

@blueprint.route('/users/<id>')
def get_user_by_id(id):
    db = DbWrapper()
    return db.get_user(id)

@blueprint.route('/users', methods=['GET', 'POST'])
def users():
    db = DbWrapper()
    if request.method == 'POST':
        data = request.get_json()
        name = data.get("name")
        db.add_user(name)
        return f"user {name} added"
        # email = data.get("email")
        # return f'adding user:{name} - {email}'
    else:
        get_filter = request.args.get("filter")
        print(f'filter: {get_filter}')
        result = db.get_users()
        return result
# @blueprint.route('/echo?name')
# def echo(name):
#     message = f'Hello {name}'
#     return message

@blueprint.route('/hello_world')
def hello_world():
    message = 'Hello World'
    return message


