
# to find factorial of a number using recursion.
def factorial (n):
      if n== 0 or n==1:
           return 1
      else:
           return n* factorial (n-1)
                
#main
n =10
fact= factorial(n)
print ( "The Factorial is",fact )
