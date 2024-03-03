name = input("Enter your name: ")
print("Select the arithamatic symbol:")
print("1.addition(+)")
print("2.subtraction(-)")
print("3.modular(%)")
print("4.multiplication(*)")
arithamatic_symbol = input("Enter the option number for the missing value: ")
if arithamatic_symbol == "+":
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number: "))
    answer = Num1 + Num2
    print(f"{name} your sum is {answer}")
elif arithamatic_symbol == "-":
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number:"))
    answer = Num1 - Num2
    print(f"{name} your difference is {answer}")

elif arithamatic_symbol == "%":
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number: "))
    answer = Num1 % Num2
    print(f"{name} your modular is {answer}")


elif arithamatic_symbol == "*":
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number: "))
    answer = Num1 * Num2
    print(f"{name} your product is {answer}")

else:
    print("Invalid option selected for the missing value.")