from controller.db_controller import DBController
from model.eleitor import Eleitor
from controller.voto_controller import VotoController


class UrnaEletronicaCLIController:
    def __init__(self) -> None:
        self.db_controller = DBController()
        self.voto_controller = VotoController()
        self.login_active = False

    def is_fiscal_valid(self, fiscal_id: str) -> bool:
        fiscal_exists = self.db_controller.db.exists(index="aps_urna_fiscal", id=fiscal_id)

        return fiscal_exists

    def get_eleitor_object(self, num_titulo: str) -> Eleitor:
        eleitor = Eleitor(num_titulo)
        if self.voto_controller.check_if_already_voted(eleitor_data=eleitor):
            raise PermissionError(
                f"O Eleitor com Título No. {num_titulo} votou anteriormente. Não poderá votar novamente."
            )

        return eleitor
