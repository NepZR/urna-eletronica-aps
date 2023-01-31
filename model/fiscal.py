from typing import Union

from model.area_eleitoral import AreaEleitoral


class Fiscal:
    def __init__(self, cod_id: Union[str, int], zona_eleitoral: AreaEleitoral) -> None:
        self.cod_id = cod_id
        self.zona_eleitoral = zona_eleitoral
