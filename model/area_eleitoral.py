from typing import Union


class ZonaEleitoral:
    def __init__(self, num_zona: Union[str, int]) -> None:
        self.num_zona = num_zona


class SecaoEleitoral:
    def __init__(self, num_secao: Union[str, int]) -> None:
        self.num_secao = num_secao


class AreaEleitoral:
    def __init__(self, num_zona: Union[str, int], num_secao: Union[str, int]) -> None:
        self.zona_eleitoral = ZonaEleitoral(num_zona=num_zona)
        self.secao_eleitoral = SecaoEleitoral(num_secao=num_secao)

    def get_secao_eleitoral(self) -> Union[int, str]:
        return self.secao_eleitoral.num_secao

    def get_zona_eleitoral(self) -> Union[int, str]:
        return self.zona_eleitoral.num_zona
