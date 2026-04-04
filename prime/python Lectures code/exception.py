#try except else finally

try:
    x = int (input("Enter a number: "))
    ans = 10 / x

except ZeroDivisionError: 
    print("Invalid input divide by zero is not allowed")

except ValueError: 
    print("Invalid input only integer is allowed")

else: 
    print(f"ans is {ans}")