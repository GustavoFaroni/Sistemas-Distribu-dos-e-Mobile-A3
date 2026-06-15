from flask import Blueprint, request, jsonify
from models import db, Veiculo

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/veiculos', methods=['POST'])
def criar_veiculo():
    dados = request.get_json()
    
    campos_obrigatorios = ('marca', 'modelo', 'ano', 'placa', 'cor')
    if not all(k in dados for k in campos_obrigatorios):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    
    if Veiculo.query.filter_by(placa=dados['placa']).first():
        return jsonify({'error': 'Veículo com esta placa já existe'}), 400

    novo_veiculo = Veiculo(
        marca=dados['marca'],
        modelo=dados['modelo'],
        ano=dados['ano'],
        placa=dados['placa'],
        cor=dados['cor']
    )
    
    try:
        db.session.add(novo_veiculo)
        db.session.commit()
        return jsonify(novo_veiculo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/veiculos', methods=['GET'])
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return jsonify([v.to_dict() for v in veiculos]), 200

@api_blueprint.route('/veiculos/<int:id>', methods=['GET'])
def buscar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    return jsonify(veiculo.to_dict()), 200

@api_blueprint.route('/veiculos/<int:id>', methods=['PUT'])
def atualizar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    dados = request.get_json()

    veiculo.marca = dados.get('marca', veiculo.marca)
    veiculo.modelo = dados.get('modelo', veiculo.modelo)
    veiculo.ano = dados.get('ano', veiculo.ano)
    veiculo.placa = dados.get('placa', veiculo.placa)
    veiculo.cor = dados.get('cor', veiculo.cor)

    try:
        db.session.commit()
        return jsonify(veiculo.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/veiculos/<int:id>', methods=['DELETE'])
def remover_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    try:
        db.session.delete(veiculo)
        db.session.commit()
        return jsonify({'message': 'Veículo removido com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
