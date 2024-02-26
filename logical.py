print("And operator")
# And operator
# Example 1
x = 5
print(x > 3 and x < 10) # true because both conditions are true

# Example 2
y = 5
print(x > 10 and y % 5 == 0) # False because the second condition is false

print("---------------------------------------------------------")
print("Or operator")
# Or operator
# Example  1
x = 5
print(x < 3 or x > 10) # False because both conditions are false

# Example 2
y = 12
print(y < 10 or y % 2 ==0) # True because the second condition is true

print("-------------------------------------------------------------")
print("Not operator")
# Not operator
# Example 1
x = 5
print(not(x > 3 and x < 10)) # False because the conditions inside the not is true

# Eample 2
y = 12
print(not(y > 10 and y % 5 == 0)) # true because the condition inside the not is false