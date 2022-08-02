# Write a python program to check the string is anagram or not.
a=input("Enter string: ")
b=input("Enter string: ")
l=[]
l=list(a)
m=[]
m=list(b)
l.sort()
m.sort()
f=1
for i in range(len(l)):
    if l[i]!=m[i]:
       print("NOT ANAGRAM")
       f=0
       break
if f==1:
    print("ANAGRAM")
       
