import os

from controller.cli_controller import UrnaEletronicaCLIController


class UrnaEletronicaCLI(UrnaEletronicaCLIController):
    def __init__(self) -> None:
        super().__init__()
        self.columns = 59

    def _print_sys_header(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * self.columns)
        print("------------------- URNA ELETRÔNICA APS -------------------")
        print()
        print("-" * self.columns)
        print()

    def _print_sys_footer(self) -> None:
        print()
        print("-" * self.columns)

    def print_login_screen(self) -> None:
        id_fiscal = input("> Sr(a). Fiscal, digite o seu Cod. ID: ")
        retry = False
        while not self.is_fiscal_valid(fiscal_id=id_fiscal):
            retry = True
            if retry:
                print(f"- O ID {id_fiscal} não existe como um Fiscal registrado na base. Impossível proceder.")

            print()
            id_fiscal = input("> Sr(a). Fiscal, digite o seu Cod. ID: ")

    def print_main_fiscal(self) -> None:
        self._print_sys_header()

        print("> 1 - Modo de Votação")
        print("> 2 - Modo Administrativo")

        self._print_sys_footer()

    def print_menu_admin(self) -> None:
        self._print_sys_header()

        print("> 1 - Cadastro de candidatos")
        print("> 2 - Gerar boletim de urna")
        print("> 3 - Apurar votação")

        self._print_sys_footer()

    def print_menu_votacao(self) -> None:
        self._print_sys_header()

        num_titulo = input("> Sr(a). Fiscal, digite o número do título de eleitor: ")
        eleitor = self.get_eleitor_object(num_titulo)
        os.system("cls" if os.name == "nt" else "clear")

        print("-" * self.columns)
        print("> Para votar branco, digite * e confirme.")
        print("> Para votar nulo, digite # e confirme.")
        print("-" * self.columns)

        print("> Digite o número do DEPUTADO ESTADUAL: ")
        # dep_fed = self.get_candidado_object()

        print("> Digite o número do DEPUTADO FEDERAL: ")
        # dep_fed = self.get_candidado_object()

        print("> Digite o número do SENADOR: ")
        # dep_fed = self.get_candidado_object()

        print("> Digite o número do GOVERNADOR: ")
        # dep_fed = self.get_candidado_object()

        print("> Digite o número do PRESIDENTE: ")
        # dep_fed = self.get_candidado_object()

    def command_handler(self) -> None:
        option = input("> Digite a opção desejada: ")
        if not option.isnumeric():
            raise ValueError("Essa opção não existe no sistema.")

        if option == "1":
            self.print_menu_votacao()
        elif option == "2":
            self.print_main_fiscal()

        self.command_handler()
