#Write a Python program to add a prefix text to all of the lines in a string.
s=input("Enter the string: ")
l=[]
l=s.split(".")
ps=input("Enter the prefix string: ")
for i in range(len(l)-1):
    print(ps+l[i],end=".")
else:
    print(l[len(l)-1])

    

