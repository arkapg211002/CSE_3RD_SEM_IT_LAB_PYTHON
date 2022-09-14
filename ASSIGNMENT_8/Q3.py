'''
Write a Python program to write a list to a file.
'''
def write_list_to_file(file_name, list):
    with open(file_name, 'w') as file:
        for i in list:
            file.write(i + ' ')
write_list_to_file('test1.txt', list(map(str, input('Enter list: ').split())))
