def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Cannot divide by 0"
num1=float(input())
num2=float(input())
print("Choose operation: +,-,*,/")
operation = input("----------Enter Operations---------- ")
if operation == '+':
    print("\nResult:", add(num1, num2))
elif operation == '-':
    print("\nResult:", subtract(num1, num2))
elif operation == '*':
    print("\nResult:", multiply(num1, num2))
elif operation == '/':
    print("\nResult:", divide(num1, num2))
else:
    print("Invalid")
