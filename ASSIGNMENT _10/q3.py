'''
 In Python, write an interactive calculator. Take input as command line arguments, which is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Check whether the input arguments are valid before computing the result:

If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.

Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError

If the second input is not '+' or '-', again raise a FormulaError

If the input is valid, perform the calculation and print the result, else  print appropriate error messages and quit.
'''
f=list(map(str,input("Enter the formula: ").split()))
print(f)
if len(f)!=3:
   print("Wrong Input")
   raise ArithmeticError
try:
   f[0]=float(f[0])
   f[2]=float(f[2])
except ValueError:
   print("Wrong input value type")
   raise ArithmeticError
if f[1]!='+' and f[1]!='-':
   print("Wrong operation input")
   raise ArithmeticError
if f[1]=='+':
   print((f[0]+f[2]))
else:
   print((f[0]-f[2]))

