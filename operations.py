operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

class Calculator:
    def __init__(self):
        self.operations = operations

    def print_menu(self):
        print("===============================")
        print("          Calculadora"          )
        print("===============================")
        for i, operation in enumerate(self.operations.values()):
            print(f"{i} : {operation}")
        print("")

    def get_operation_choice(self):
        while True:
            try:
                choice = int(input("Escolha a operação que deseja realizar: "))
                if choice in range(len(self.operations)):
                    return list(self.operations.keys())[choice]
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    def get_value(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    def add(self, v1, v2):
        return v1 + v2

    def subtract(self, v1, v2):
        return v1 - v2

    def multiply(self, v1, v2):
        return v1 * v2

    def divide(self, v1, v2):
        try:
            return v1 / v2
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            return None

    def exponentiate(self, v1, v2):
        return v1 ** v2

    def perform_operation(self, operation, v1, v2):
        if operation == "+":
            return self.add(v1, v2)
        elif operation == "-":
            return self.subtract(v1, v2)
        elif operation == "*":
            return self.multiply(v1, v2)
        elif operation == "/":
            return self.divide(v1, v2)
        elif operation == "^":
            return self.exponentiate(v1, v2)
