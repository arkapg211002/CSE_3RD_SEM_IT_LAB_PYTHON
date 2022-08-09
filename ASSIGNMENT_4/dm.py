#to count the positive and negative numbers in a list
list=[]
pos=neg=0
n=int(input('Enter the number of items in the list:'))
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
num=[x for x in list if x.isdigit()]
for i in num:
    if int(i)>0:
        pos+=1
    else:
        neg+=1
print('The number of positive numbers in the list is:',pos)
print('The number of negative numbers in the list is:',neg)


