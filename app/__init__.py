from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TRADEBOT',
          version='1.0',
          description='tradebot: version 1.0'
          )

api.add_namespace(user_ns, path='/user')

