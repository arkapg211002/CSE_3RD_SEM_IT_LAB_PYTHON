'''
Write a Python program, where N number of integer arguments are passed to a function make_sum()
which will print the sum of all the passed integers.
'''
def make_sum(*args):
    print(sum(args))
make_sum(*list(map(int,input("Enter the numbers:").split())))