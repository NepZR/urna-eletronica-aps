from controller.db_controller import DBController
from model.eleitor import Eleitor


class VotoController:
    def __init__(self) -> None:
        self.db_controller = DBController()

    def check_if_already_voted(self, eleitor_data: Eleitor) -> bool:
        status_eleitor = self.db_controller.retrieve_status_eleitor(num_titulo=eleitor_data.num_titulo)
        return status_eleitor
