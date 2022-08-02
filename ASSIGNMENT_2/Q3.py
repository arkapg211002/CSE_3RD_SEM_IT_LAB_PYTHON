a=int(input("Enter the number:"))
p=int(1)
b=int(a)
if a==0 or a==1:
  print("The factorial of ",a," is ",1)
while a>0:
   p=p*a
   a=a-1
print("The factorial of ",b," is ",p)
