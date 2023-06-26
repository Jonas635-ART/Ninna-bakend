from config import validador
from marshmallow import fields

class PageRequestDTO(validador.Schema):
    page = fields.Integer(required=False, load_default=1)
    perPage = fields.Integer(required=False, load_default=10)














































