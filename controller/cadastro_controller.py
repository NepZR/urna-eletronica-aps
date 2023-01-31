import random
from typing import Union


from model.candidato import Candidato
from model.partido import Partido

from controller.db_controller import DBController


class Executivo:
    def __init__(self) -> None:
        pass


class Legislativo:
    def __init__(self, cargo: str) -> None:
        self.cargo_name = cargo

    def get_param_cargo(self) -> int:
        if self.cargo_name in ["depest", "depfed"]:
            return 3
        elif self.cargo_name in ["pres", "gov"]:
            return 0


class CadastroController:
    def __init__(self) -> None:
        self.db = DBController()

    @staticmethod
    def _gen_sufixo_candidato(num_partido: str, tipo_cargo: Union[Executivo, Legislativo]) -> str:
        random.seed(a=num_partido)
        generated_suffix = ""
        for _ in range(tipo_cargo.get_param_cargo()):
            generated_suffix += random.randint(a=0, b=9)

    def cadastrar_candidato(self, cpf_candidato: str, partido_associado: Partido) -> Candidato:
        num_partido = partido_associado.get_num_partido()
        sufixo_candidato = self._gen_sufixo_candidato(num_partido)

        candidato = Candidato(cpf_candidato=cpf_candidato)
