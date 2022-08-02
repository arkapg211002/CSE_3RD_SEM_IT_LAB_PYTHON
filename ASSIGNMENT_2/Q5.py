# Write a program that keeps on accepting numbers from the user until the user enters Zero. Display the sum and average of all the numbers.
s=0
c=0
a=1
while a==1:
      n=int(input("Enter the number: "))
      s=s+n
      c=c+1
      a=int(input(" Enter 1 to continue , 0 to end: "))
print("The sum is ",s)
print("The average is ",s/c)
      
