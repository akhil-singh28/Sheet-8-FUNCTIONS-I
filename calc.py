a=int(input())
b=int(input())
def calc(a,b):
    sum=a+b
    subtract=a-b
    prod=a*b
    div=a/b
    return sum,subtract,prod,div
Sum,Subtract,Prod,Div=calc(a,b)
print("Sum is:",Sum)    
print("Subtraction is:",Subtract)
print("Product is:",Prod)
print("Division is:",Div)
