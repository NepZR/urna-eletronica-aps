from view.cli_urna import UrnaEletronicaCLI


class UrnaEletronica(UrnaEletronicaCLI):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        self.print_login_screen()
        self.print_main_fiscal()
        self.command_handler()


if __name__ == "__main__":
    app = UrnaEletronica()
    app.run()
