from operations import Calculator
from utils import clear_screen

def main():
    calculator = Calculator()

    while True:
        clear_screen()
        calculator.print_menu()
        operation = calculator.get_operation_choice()
        operation_symbol = operation

        print(f"\n>>> {calculator.operations[operation_symbol]} escolhida.\n")

        v1 = calculator.get_value("Qual o primeiro valor? ")
        v2 = calculator.get_value("Qual o segundo valor? ")

        result = calculator.perform_operation(operation_symbol, v1, v2)

        if result is not None:
            print(f"\n{v1} {operation_symbol} {v2} = {result}\n")
        print("===========")
        print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
        
        if calculator.get_value("") == 1:
            break

if __name__ == "__main__":
    main()
