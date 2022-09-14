'''
Write a Python program to count the number of lines in a text file. 
'''
def count_lines(file_name):
    with open(file_name) as file:
        return len(file.readlines())
print(count_lines('test.txt'))
