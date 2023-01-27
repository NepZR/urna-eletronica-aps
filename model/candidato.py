from typing import Tuple


class Candidato:
    def __init__(self, num_candidato: int, cargo_concorrido: str) -> None:
        self.num_candidatura = num_candidato
        self.cargo_candidatado = cargo_concorrido

    def get_partido(self) -> int:
        num_partido = str(self.num_candidatura)[:2]
        return int(num_partido)
