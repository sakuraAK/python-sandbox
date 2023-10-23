from flask import Flask, request
import json

app = Flask(__name__)
import model.bank_management as bm

@app.route('/')
def index():
    return 'Index Page'

@app.route('/bank_api/hello_world')
def hello_world():
    return 'Hello, World!'

@app.route('/bank_api/clients', methods=['GET', 'POST'])
def clients():
    service = bm.Bank("", "", "")
    if request.method == 'GET':
        service.add_client('John Doe', 1234)
        service.add_client('John Doe 1', 12345)
        service.add_client('John Doe 2', 12346)
        clients = service.get_all_clients()
        return [x.__dict__ for x in clients]
    if request.method == 'POST':
        data = dict(request.json)
        # print(request.json)
        # client = bm.Client(data['name'], data['pin'])
        return { "client_number" : service.add_client(data['name'], data['pin']).client_number }

