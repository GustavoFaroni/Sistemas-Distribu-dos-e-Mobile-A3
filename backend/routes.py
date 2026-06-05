from flask import Blueprint, request, jsonify
from models import db, Veiculo

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/veiculos', methods=['POST'])
def create_veiculo():
    data = request.get_json()
    
    if not all(k in data for k in ('marca', 'modelo', 'ano', 'placa', 'cor')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if placa already exists
    if Veiculo.query.filter_by(placa=data['placa']).first():
        return jsonify({'error': 'Veículo com esta placa já existe'}), 400

    new_veiculo = Veiculo(
        marca=data['marca'],
        modelo=data['modelo'],
        ano=data['ano'],
        placa=data['placa'],
        cor=data['cor']
    )
    
    try:
        db.session.add(new_veiculo)
        db.session.commit()
        return jsonify(new_veiculo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/veiculos', methods=['GET'])
def get_veiculos():
    veiculos = Veiculo.query.all()
    return jsonify([v.to_dict() for v in veiculos]), 200

@api_blueprint.route('/veiculos/<int:id>', methods=['GET'])
def get_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    return jsonify(veiculo.to_dict()), 200

@api_blueprint.route('/veiculos/<int:id>', methods=['PUT'])
def update_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    data = request.get_json()

    veiculo.marca = data.get('marca', veiculo.marca)
    veiculo.modelo = data.get('modelo', veiculo.modelo)
    veiculo.ano = data.get('ano', veiculo.ano)
    veiculo.placa = data.get('placa', veiculo.placa)
    veiculo.cor = data.get('cor', veiculo.cor)

    try:
        db.session.commit()
        return jsonify(veiculo.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/veiculos/<int:id>', methods=['DELETE'])
def delete_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    try:
        db.session.delete(veiculo)
        db.session.commit()
        return jsonify({'message': 'Veículo removido com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
