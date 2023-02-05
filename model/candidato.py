from typing import Tuple


class Candidato:
    def __init__(self, cpf_candidato: str, num_candidato: str, cargo_concorrido: str) -> None:
        self.cpf = cpf_candidato
        self.num_candidatura = num_candidato
        self.cargo_candidatado = cargo_concorrido

    def get_partido(self) -> int:
        num_partido = self.num_candidatura[:2]
        return int(num_partido)

    def get_num_candidato(self) -> str:
        return self.num_candidatura

    def get_cargo_concorrido(self) -> str:
        return self.cargo_candidatado

    def get_cpf_candidato(self) -> str:
        return self.cpf
