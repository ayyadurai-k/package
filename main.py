from arithmetic_package.addition import add
from arithmetic_package.subtraction import subtract
from arithmetic_package.multiplication import multiply
from arithmetic_package.division import divide

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))

print("Addition : ",add(n1,n2))
print("Subtraction : ",subtract(n1,n2))
print("Multiplication : ",multiply(n1,n2))
print("Division : ",divide(n1,n2))
