import random
from typing import Union


from model.candidato import Candidato
from model.partido import Partido

from controller.db_controller import DBController


class CargoPolitico:
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
    def _gen_num_candidato(num_partido: str, tipo_cargo: CargoPolitico) -> str:
        random.seed(a=num_partido)
        generated_suffix = ""
        for _ in range(tipo_cargo.get_param_cargo()):
            generated_suffix += random.randint(a=0, b=9)

        num_candidato = num_partido + generated_suffix
        return num_candidato

    def cadastrar_candidato(self, cpf_candidato: str, partido_associado: Partido, cargo_concorrido: str) -> None:
        num_partido = partido_associado.get_num_partido()
        num_candidato = self._gen_num_candidato(num_partido, tipo_cargo=CargoPolitico(cargo=cargo_concorrido))

        candidato = Candidato(
            cpf_candidato=cpf_candidato,
            num_candidato=num_candidato,
            cargo_concorrido=cargo_concorrido
        )

        DBController().save_candidato(candidato_data=candidato)
