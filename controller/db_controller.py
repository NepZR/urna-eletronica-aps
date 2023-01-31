from typing import Tuple

from opensearchpy import OpenSearch


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
        self.index = "aps_urna_eletronica"

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
