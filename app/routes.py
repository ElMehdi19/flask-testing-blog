from flask import request
from app import app
from app.decorators import is_json


@app.route('/')
def home():
    return {'message': 'Hello Flask!'}


@app.route('/service', methods=['POST'])
@is_json
def service():
    return {'success': True}
