import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def available_operations():
    text = "Available Operators: "
    for key in operations:
        text += key + " "
    print(text)

def get_input(is_symbol=False):
    if is_symbol:
        while True:
            sym = input("> ")
            if sym in operations:
                return sym
            else:
                print(f"{sym} is not a valid option.")
                available_operations()
                print("Please select one in the list.")
    while True:
        num_string = input("> ")
        if num_string == "":
            print("Enter a value.")
        elif is_float(num_string):
            return float(num_string)
        else:
            print("Enter a number.")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

new_calculation = True
result = 0

while True:
    # only executed at the first run
    if new_calculation:
        print(art.logo)
        print("What's the first number?")
        num1 = get_input()
    else:
        num1 = result
        
    available_operations()

    print("Pick an operation from the above list:")
    symbol = get_input(is_symbol=True)

    print("Enter the next number: ")
    while True:
        num2 = get_input()
        if symbol == "/" and num2 == 0:
            print("Divide by zero is infinty. Please input a non-zero number.")
        else:
            break

    result = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {result}")

    print(f"Type \"y\" to continue calculating with {result}, or type \"n\" to start a new calculation. "
          f"Anything else will exit the program.")
    choice = input("> ")
    if choice == "y":
        new_calculation = False
    elif choice == "n":
        new_calculation = True
    else:
        break

print("Goodbye.")
