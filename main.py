from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route
# INICIALIZACAO
app = Flask(__name__)


app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix = '/clientes')
# EXECUCAO
app.run(debug = True)

