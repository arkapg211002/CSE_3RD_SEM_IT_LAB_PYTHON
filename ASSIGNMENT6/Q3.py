'''
Write a program to create two Dictionaries. Take a key from the 1st dictionary and find it in the 2nd dictionary. Display the corresponding value if found otherwise print appropriate message.

Also merge the two dictionaries and display the output.
'''
d1={}
d2={}
n=int(input("Enter the number of elements in the dictionary: "))
for i in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d1[key]=value
print("The dictionary is: ",d1)
n=int(input("Enter the number of elements in the dictionary: "))
for i in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d2[key]=value
print("The dictionary is: ",d2)
for key in d1:
    if key in d2:
        print("The value of ",key," is: ",d2[key])
    else:
        print("The key ",key," is not found in the dictionary")
d3={}
for key in d1:
    d3[key]=d1[key]
for key in d2:
    d3[key]=d2[key]
print("The merged dictionary is: ",d3)
