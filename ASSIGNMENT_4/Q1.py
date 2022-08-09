#Python program to interchange first and last elements in a list.

l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print("The list is: ",l)
l[0],l[-1]=l[-1],l[0]
print("The list after swapping is: ",l)
