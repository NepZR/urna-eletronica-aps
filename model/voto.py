from datetime import datetime

from model.eleitor import Eleitor
from model.partido import Partido
from model.candidato import Candidato

from typing import Union, Optional


class Voto:
    def __init__(self, voto_type: Union[Candidato, Partido, None], eleitor: Eleitor) -> None:
        self.alvo_voto = voto_type
        self.eleitor = eleitor

    def get_num_titulo_eleitor(self) -> str:
        return self.eleitor.num_titulo

    def get_tipo_voto(self) -> str:
        if self.alvo_voto is None:
            return "branco_nulo_invalido"
        if type(self.alvo_voto) is Candidato:
            return "candidato"
        if type(self.alvo_voto) is Partido:
            return "partido"

    def get_num_votado(self) -> Optional[str]:
        if self.alvo_voto is None:
            return None

        if type(self.alvo_voto) is Candidato:
            return self.alvo_voto.get_num_candidato()
        if type(self.alvo_voto) is Partido:
            return self.alvo_voto.get_num_partido()

    @staticmethod
    def get_datetime_voto() -> datetime:
        return datetime.now()
