"""Crea una clase Usuario y una clase Cliente que herede de ella y añada un número de cliente."""

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        return f"Usuario: {self.nombre} | Email: {self.email}"


class Cliente(Usuario):
    def __init__(self, nombre, email, numero_cliente):
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Nº Cliente: {self.numero_cliente}"


def main():
    usuario = Usuario("Carlos Gómez", "carlos@example.com")
    print(usuario.mostrar_info())

    cliente = Cliente("Ana Martínez", "ana@example.com", "CLI-0042")
    print(cliente.mostrar_info())


if __name__ == "__main__":
    main()
