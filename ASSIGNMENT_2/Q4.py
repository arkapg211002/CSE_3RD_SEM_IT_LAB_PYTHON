#Write a program to print all prime numbers that fall between two numbers including both (accept two numbers from the user)
a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
def prime(n):
    if n==1:
       return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
           return 0
    return 1
print("The prime numbers from ",a," to ",b," are ")
for i in range(a,b+1):
    if prime(i)==1:
       print(i)
   
