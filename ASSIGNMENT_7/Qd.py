'''
Write a Python function that prints out the first n rows of Pascal's triangle.

     Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

     Sample Pascal's triangle:
                1
              1   1
            1   2   1
          1   3   3   1
Each number is the two numbers above it added together.
'''
def pascal(n):
    for i in range(n):
        print(" "*(n-i)," ".join(map(str,str(11**i))),"\n")
pascal(int(input("Enter the number of rows:")))

