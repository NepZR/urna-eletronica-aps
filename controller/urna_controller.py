from model.eleitor import Eleitor
from model.candidato import Candidato
from model.partido import Partido
from model.voto import Voto


class UrnaController:
    def __init__(self, num_titulo_eleitor: str) -> None:
        self.num_titulo_eleitor: num_titulo_eleitor

    def efetivar_voto(self) -> Voto:
        pass
