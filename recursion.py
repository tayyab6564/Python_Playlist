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
"""
num = int(input("Enter number to print factorial: "))
def factorial(n):
   if(n == 1 or n == 0):
      return 1
   else:
      return n * factorial(n - 1)
   
print(factorial(num))   """

#sum of n natural numbers
"""
num = int(input("Ending of natural numbers to add: "))
def add(n):
    if(n == 0):
     return 0
    return n + add(n-1)    
print(add(num))    
"""
#print all elements in a list hint:pass list and index as parameters
list = [1,"banana",2.0,"apple"]
def printlist(lis , idx=0):
   if(idx == len(list)):
      return 
   print(lis[idx])
   printlist(lis , idx+1)
printlist(list)