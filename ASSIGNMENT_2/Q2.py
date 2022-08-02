#Write a program to print a table of a number accepted from the user.
a=int(input("Enter the number: "))
b=int(input("Enter the limit: "))
for i in range(1,b+1):
   print(a," * ",i," = ",(a*i))
