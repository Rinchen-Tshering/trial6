print("Newton's second law")
print("----------------------------------------------------------------------------")

#determine the missing value
print("Select the missing value: ")
print("1. mass(m)")
print("2. acceleration(a)")
print("3. force(F)")
missing_value_choice = input("Enter the option number of the missing value")

#prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("enter acceleration (a): "))
    F = float(input("enter force (F): "))
    m = F / a
    print(f"mass (m) = {m}")

elif missing_value_choice == "2":
    m = float(input("enter mass (m): "))
    F = float(input("enter force(F): "))
    a = F / m
    print(f"acceleration (a) = {a}")

elif missing_value_choice == "3":
    m = float(input("enter mass (m): "))
    a = float(input("enter acceleration (a): "))
    F = m * a
    print(f"force (F) = {F}")

else:
    print("invalid option selected for the missing value.")