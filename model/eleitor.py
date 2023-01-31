from typing import Union


class Eleitor:
    def __init__(self, num_titulo: Union[int, str]) -> None:
        self.num_titulo = num_titulo

    def votar(self) -> bool:
        pass
