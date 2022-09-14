'''
Write a Python program to copy the contents of a file to another file .
'''
def copy_file(file_name, file_name1):
    with open(file_name) as file, open(file_name1, 'w') as file1:
        file1.write(file.read())
copy_file('test.txt', 'test2.txt')
