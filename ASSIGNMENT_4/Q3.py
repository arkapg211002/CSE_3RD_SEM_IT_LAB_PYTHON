#Write a Python program to count Even and Odd numbers in a List.
l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print("The list is: ",l)
count=0
for i in l:
    if i%2==0:
        count+=1
print("The number of even numbers in the list is: ",count)
print("The number of odd numbers in the list is: ",n-count)