from flask import Blueprint, request, json
from mocks import DB_FILE_PATH
from assignment_2 import SqlLiteDbWrapper


blueprint = Blueprint('api', __name__, url_prefix='/basic_api')


@blueprint.route('/users/<id>')
def get_user_by_id(id):
    with SqlLiteDbWrapper(DB_FILE_PATH) as db:
        try:
            return json.dumps(db.get_user(id).to_dict()), 200
        except Exception as e:
            print(f"Error occurred in /users/<id>. Error: {e}")
            return "Error occurred", 500

@blueprint.route('/users', methods=['GET', 'POST'])
def users():
    try:
        with SqlLiteDbWrapper(DB_FILE_PATH) as db:
            if request.method == 'POST':
                data = request.get_json()
                name = data.get("name")
                user = db.add_user(name)
                return json.dumps(user.to_dict()), 200
            else:
                get_filter = request.args.get("filter")
                print(f'filter: {get_filter}')
                result = db.get_users(get_filter)
                return [r.to_dict() for r in result], 200
    except Exception as e:
        print(f"Error occurred in /users. Error: {e}")
        return "Error occurred", 500



@blueprint.route('/tweets', methods=['GET', 'POST'])
def tweets():
    """
    To implement
    :return:
    """
    try:
        with SqlLiteDbWrapper(DB_FILE_PATH) as db:
            if request.method == 'POST':
                data = request.get_json()
                message = data.get("message")
                user_id = data.get("userId")
                tweet = db.add_tweet(message, user_id)
                return json.dumps(tweet.to_dict()), 200
            else:
                get_filter = request.args.get("filter")
                result = db.get_tweets(get_filter)
                return [r.to_dict() for r in result], 200
    except Exception as e:
        print(f"Error occurred in /tweets. Error: {e}")
        return "Error occurred", 500


@blueprint.route('/followers/<followee_id>/<follower_id>', methods=['POST', 'DELETE'])
def follow_unfollow_user(followee_id, follower_id):
    pass

@blueprint.route('/likes/<tweet_id>/<user_id>', methods=['POST', 'DELETE'])
def add_remove_like(tweet_id, user_id):
    pass

@blueprint.route('/feeds/<user_id>')
def get_feed(user_id):
    pass

@blueprint.route('/hello_world')
def hello_world():
    message = 'Hello World'
    return message


