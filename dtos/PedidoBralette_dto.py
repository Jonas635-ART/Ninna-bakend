from models import validador
from models.Pedido_Bralette import PedidoBralette


class PedidoBraletteRequestDTO(validador.SQLAlchemyAutoSchema):

    class Meta:
        model = PedidoBralette
        include_fk = True


































