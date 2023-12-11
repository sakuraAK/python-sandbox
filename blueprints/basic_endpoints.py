from flask import Blueprint, request, jsonify
from mocks import DB_FILE_PATH
from assignment_2 import SqlLiteDbWrapper


blueprint = Blueprint('api', __name__, url_prefix='/basic_api')


@blueprint.route('/users/<id>')
def get_user_by_id(id):
    with SqlLiteDbWrapper(DB_FILE_PATH) as db:
        return db.get_user(id)

@blueprint.route('/users', methods=['GET', 'POST'])
def users():
    with SqlLiteDbWrapper(DB_FILE_PATH) as db:
        if request.method == 'POST':
            data = request.get_json()
            name = data.get("name")
            db.add_user(name)
            return f"user {name} added"
        else:
            get_filter = request.args.get("filter")
            print(f'filter: {get_filter}')
            result = db.get_users(get_filter)
            return result


@blueprint.route('/tweets', methods=['GET', 'POST'])
def tweets():
    """
    To implement
    :return:
    """
    pass


@blueprint.route('/hello_world')
def hello_world():
    message = 'Hello World'
    return message


