#Write a python program to Reverse a List.
l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print("The list is: ",l)
l.reverse()
print("The list after reversing is: ",l)
