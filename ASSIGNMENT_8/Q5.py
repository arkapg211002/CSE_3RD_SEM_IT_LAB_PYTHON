'''
Write a Python program to take a file name and a string pattern from the user. Now print the number of occurrence of the pattern string found in the file.
'''
def count_pattern(file_name, pattern):
    with open(file_name) as file:
        return file.read().count(pattern)
print(count_pattern(input('Enter filename: '), input('Enter pattern to search: ')))