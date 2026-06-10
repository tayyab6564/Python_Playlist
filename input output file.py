# 1.r  -->  read       
# 2.a  -->  append(add at last)    
# 3.w  -->  write(overwrite and delete previous data)
# 4.r+ -->  read+write(while writing it starts overwriting from front of file and start reading from next place from currently written text )
# 5.w+ --> write+read(file will open and all data will be erased)
# 6.a+ --> append plus(data do not truncate, can read data and can write at end)
# 7. with syntex (it automatically close file do not need manually to close a file)
# 8. import os  os.remove --> delete file
# 9. replace(to be replaced , which will be replaced)
#10. find a world in file
#11. find line of first occurance of a number
#12. count even numbers in a file


#            1.read data from file
"""
f = open("file.txt","r")#use file name if file is in same folder
#f = open("D:\Tayyab\io file.txt","r") #use file location when file is in another folder
data = f.read()
print("data in file is: \n \t",data)
"""

#read only some piece of initial data  :first eight characters
"""
f = open("file.txt","r")
data = f.read(8)
print("\nfirst eight characters: \n \t",data)

#print one line
#f = open("file.txt","r")
data = f.readline()
print("\nfirst line is: \n \t",data)
f.close()
"""

#                2.write into file 
"""
f = open("file.txt","w")
f.write("todary i am learning python. \nTomorrow i will learn javascript.")
f.close()
"""

#              3.append data(add dta at the last of a file)
"""
f = open("file.txt","a")
f.write("\nThis data is appended and is added to last of the file")
f.close()
"""

#                   4. read + write
"""
f = open("file.txt","r+")
f.write("start")
data1 = f.read()
print(data1)
f.close()
"""

#                   5. write + read
"""
f = open("file.txt","w+")
data = f.read()
print("\ndata in file is: \n",data)
f.write("Python is easy")
f.close()
f = open("file.txt","r")
data = f.read()
print("data in file is: \n",data)
f.close()
"""

#               6. append plus
"""
f = open("file.txt","a+")
data = f.read() #pointer is at end so no data will print
print("data in file is: \n",data)
f.write(" writing at end")
f.close()
"""

#            7. with syntax
"""
with open("file.txt","a+") as f:  # "as" mean aliance
 f.write("\nThis is next line")

with open("file.txt","r+") as f:  # "as" mean aliance
 data = f.read()
print("data in file is: \n",data)
"""

#             8. delete a file
"""
import os 
os.remove("File.txt")
"""

#             9. replace(new , old)
"""
with open("file.txt","r+") as f: 
 data = f.read()
 data1 = data.replace("ali" , "umar")

with open("file.txt","r+") as f: 
 f.write(data1)
print("data in file is: \n",data1)
"""

#            10. find a world in file
"""
def find_word():
 with open("file.txt","r") as f: 
  word = input("Enter world to find from file: ")
  data = f.read()
  if(data.find(word) != -1):
   print("present")
  else:
   print("Not found")
find_word()
"""

#            11. find line of first occurance of a number
"""
def find_word():
 with open("file.txt","r") as f: 
   word = input("Enter world to find from file: ")
   line = 1
   while True:
    data = f.readline()
    if(word in data):
     print(line)
     return
    line+=1
    if(data == ""):
     print("not found")
     return

find_word()
"""

#              12. count even numbers in a file
def count_num():
 with open("file.txt","w") as f: 
  f.write("1,2,3,4,5,6,7,8,9")

 with open("file.txt","r") as f: 
   count = 0
   data =  f.read()
   data1 = data.split(",") #<--split data using 'num1','num2',....
   for val in data1:
    if(int(val) % 2 == 0): #use typecasting to convert to integers
     count += 1
   print("Total even numbers are: ",count)

count_num()

