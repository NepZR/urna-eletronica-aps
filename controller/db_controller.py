from typing import Tuple, Optional

from loguru import logger
from opensearchpy import OpenSearch
from model.candidato import Candidato
from model.voto import Voto


class DBController:
    def __init__(
            self,
            host: str = "localhost",
            port: int = 9200,
            credentials: Tuple[str] = ("pybrnews", "pybrnews")
    ) -> None:
        self.db = self.set_connection(host=host, port=port, credentials=credentials)
        self.host = host
        self.port = port
        self.index = None

    @staticmethod
    def _get_index(usage_type: str = "candidato") -> str:
        if "candidato" in usage_type:
            return "aps_urna_candidatos"

        if "voto" in usage_type:
            return "aps_urna_votos"

        if "eleitor" in usage_type:
            return "aps_urna_eleitores"

        if "partido" in usage_type:
            return "aps_urna_partidos"

    @staticmethod
    def set_connection(
            host: str = "localhost",
            port: int = 9200,
            credentials: Tuple[str] = ("pybrnews", "pybrnews")
    ) -> OpenSearch:
        """
        Sets the connection host:port parameters for the OpenSearch. By default, uses the standard localhost:9200 for
        local usage.
        Parameters:
             host (str): Hostname or address to connect.
             port (int): Port to be used in the connection.
             credentials (Tuple[str]): Credentials for auth on ElasticSearch backend.
        """
        host_data = [{"host": host, "port": port}]

        database = OpenSearch(
            hosts=host_data, http_compress=True, http_auth=credentials,
            use_ssl=True, verify_certs=False, ssl_assert_hostname=False, ssl_show_warn=False
        )

        return database

    def retrieve_candidato(self, num_candidato: str) -> Optional[Candidato]:
        dados_candidato = self.db.get(index=self.index, id=num_candidato)
        if dados_candidato is None:
            return None

        candidato = Candidato(
            cpf_candidato=dados_candidato["_source"]["cpf"],
            num_candidato=dados_candidato["_source"]["num_candidatura"],
            cargo_concorrido=dados_candidato["_source"]["cargo_concorrido"]
        )

        return candidato

    def save_candidato(self, candidato_data: Candidato) -> None:
        self.index = self._get_index(usage_type="candidato")
        data = {
            "cpf": candidato_data.get_cpf_candidato(),
            "num_candidatura": candidato_data.get_num_candidato(),
            "cargo_concorrido": candidato_data.get_cargo_concorrido()
        }

        inserted_data = self.db.index(index=self.index, body=data, id=candidato_data.get_num_candidato())
        logger.debug(inserted_data)

    def registrar_voto(self, voto_data: Voto) -> None:
        self.index = self._get_index(usage_type="voto")
        data = {
            "num_titulo_eleitor": voto_data.get_num_titulo_eleitor(),
            "tipo_voto": voto_data.get_tipo_voto(),
            "num_votado": voto_data.get_num_votado(),
            "datetime_voto": voto_data.get_datetime_voto(),
        }

        self.db.index(index=self.index, body=data)

    def retrieve_status_eleitor(self, num_titulo: str) -> bool:
        self.index = self._get_index(usage_type="eleitor")
        if self.db.exists(index=self.index, id=num_titulo):
            return True
        else:
            return False
