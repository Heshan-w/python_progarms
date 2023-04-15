def add(num1, num2):
    return (num1 + num2)


def sub(num1, num2):
    return (num1 - num2)


def mul(num1, num2):
    return round((num1 * num2), 5)


def div(num1, num2):
    return round((num1 / num2), 5)


while True:
    operator = input(
    "select mathematical operator\n"
    "(1) addition\n"
    "(2) subtraction\n"
    "(3) multiplication\n"
    "(4) division\n"
    "enter operator number : "
    )

    num1 = float(input("first number : "))
    num2 = float(input("second number : "))

    if operator == "1":
        print(add(num1, num2))
    elif operator == "2":
        print(sub(num1, num2))
    elif operator == "3":
        print(mul(num1, num2))
    elif operator == "4":
        print(div(num1, num2))
    else:
        print("invalid operator")
    end = input("do you want to quit? (y/n) : ")
    if end.lower() == "y":
        quit()
