#Write a Python program to find second largest number in a list.
l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print("The list is: ",l)
l.sort()
print("The list after sorting is: ",l)
print("The second largest number in the list is: ",l[-2])
