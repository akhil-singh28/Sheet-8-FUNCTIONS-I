A=input()
def sum_array(A):
    sum=0
    for i in A:
        sum=sum+int(i)
    return sum
Sum=sum_array(A.split())
print(Sum)