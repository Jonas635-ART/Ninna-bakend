from config import validador
from models.bralettes import Bralette
from marshmallow_sqlalchemy import auto_field, fields
from marshmallow import validate


class BraletteRequestDTO(validador.SQLAlchemyAutoSchema):

    nombre = auto_field(validate=validate.And(validate.Length(min=1), validate.Regexp("[A-Z]|[a-z]+")))
    class Meta:
        model = Bralette


class BraletteResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Bralette

class BraletteResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Bralette

class PedidobraletteResponseDTO(validador.SQLAlchemyAutoSchema):
    bralette = fields.Nested(nested=BraletteResponseDTO, many=True, only=['descripcion',''])
    class Meta:
        model = Bralette







