# Function calls itself is called recursion
"""
def counting(n):
    if(n == 0):
     return
    counting(n-1)
    print(n)

counting(50)    
    """

#Print factorial using recursion
num = int(input("Enter number to print factorial: "))
def factorial(n):
   if(n == 1 or n == 0):
      return 1
   else:
      return n * factorial(n - 1)
   
print(factorial(num))   