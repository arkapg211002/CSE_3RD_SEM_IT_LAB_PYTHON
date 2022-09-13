#Write a Python function to find the Max of three numbers.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
def max_of_three( x, y, z ):
    if x > y:
        return x
    elif y > z:
        return y
    else:
        return z
print(max_of_three(a,b,c))