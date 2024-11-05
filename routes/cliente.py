from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
  """ listar os clientes """
  return render_template('lista_clientes.html', clientes = CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
  """ inserir os dados do cliente """

  data = request.json

  novo_usuario = {
    "id": len(CLIENTES) + 1,
    "nome": data['nome'],
    "email": data['email']
  }

  CLIENTES.append(novo_usuario)

  return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
  """ fomulario para cadastrar um cliente """
  return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
  """mostra os dados do cliente"""

  cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
  return render_template('detalhe_cliente.html', cliente = cliente)


@cliente_route.route('/<int:cliente_id>/edit>')
def form_edit_cliente(cliente_id):
  """edita os dados do cliente"""

  cliente = None
  for c in CLIENTES:
    if c['id'] == cliente_id:
      cliente = c

  return render_template('form_cliente.html', cliente = cliente)


@cliente_route.route('/<int:cliente_id>/update>', methods=['PUT'])
def atualizar_cliente(cliente_id):
  """atualiza os dados do cliente"""
  data = request.json
  cliente_editado = None

  for c in CLIENTES:
    if c['id'] == cliente_id:
      c['nome'] = data['nome']
      c['email'] = data['email']

      cliente_editado = c

  return render_template('item_cliente.html', cliente = cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete>', methods=['DELETE'])
def deletar_cliente(cliente_id):
  """deleta o registro do cliente"""
  global CLIENTES
  CLIENTES = [ c for c in CLIENTES if c["id"] != cliente_id ]

  return {'deleted': 'ok'}

