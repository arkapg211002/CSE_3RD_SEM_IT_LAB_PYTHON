'''
Write a Python program to read first n lines of a file
'''
def read_first_n_lines(file_name, n):
    with open(file_name) as file:
        for i in range(n):
            print(file.readline(), end='')
read_first_n_lines('test.txt', int(input('Enter number of lines to read: ')))
