from flask import Blueprint, jsonify, request


API = Blueprint('api', __name__, url_prefix='/api')


@API.route('/genres', methods=['GET'])
def genres():
    return jsonify({'success': False})


@API.route('/actors', methods=['GET'])
def actors():
    return jsonify({'success': True})


@API.route('/directors', methods=['GET'])
def directors():
    return jsonify({'success': 'opah'})
