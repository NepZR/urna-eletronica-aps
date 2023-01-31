from model.eleitor import Eleitor
from model.partido import Partido
from model.candidato import Candidato

from typing import Union


class Voto:
    def __init__(self, voto_type: Union[Candidato, Partido], eleitor: Eleitor) -> None:
        self.alvo_voto = voto_type
        self.eleitor = eleitor
