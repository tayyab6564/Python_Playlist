# Functions are used to enhance re-useability and redundancy of code
"""
def sum(a , b):
    return a + b
addition = sum(4 , 5)
print("Result of sum is : " , addition)

#Function call :

addition = sum(5 , 6)
print("Result of sum is : " , addition)
addition = sum(2 , 1)
print("Result of sum is : " , addition)
addition = sum(598 , 67)
print("Result of sum is : " , addition)
addition = sum(7001 , 2)
print("Result of sum is : " , addition)
"""

#         print hello world
def hello():
  print("Hello world")
hello()  

#         Average of values
"""
def average(a , b , c):
   return (a+b+c)/3
print(average(4 , 6 , 2))
"""

#         print length of 2 lists using function
"""
cities = ["islamabad","karachi","Multan","Faisalabad"]
fruits = ["Mango","Banana","Guava","Graps","Orange","Cherry","Peach"]

def length(list):
   print(len(list))
length(cities)
length(fruits)
"""

# print elements of list in a line using function
cities = ["Mandi-bahauddin","Phalia","Hafizabad","Gujrat"]

def city(i):
  for i in cities:
    print(i,end=" ")
city(cities)    

#print factorial of a number using parameter n
"""
num = int(input("\nEnter a number to print its factorial: "))

def fac(n):
 i = 1
 fact = 1
 while i<n+1:
   fact*=i
   i+=1

 return fact

print(fac(num))
"""

#convert usd to pkr using function
"""
amount = int(input("\nenter ammount in usd: "))
def conversion(n):
   ans = n * 278 
   print(ans," pkr")

conversion(amount)"""

#Even or Odd
num = int(input("\nEnter a number: "))
def number(n):
 if(n % 2 == 0):
  print(n,"is an even number.")
 else:
      print(n,"is an odd number.")

number(num)      