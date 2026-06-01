#       Buillt-in functions
#       =========================
str1 = " my name is Tayyab umar"
print(str1.capitalize())  #print the string with first character in uppercase and rest in lowercase
print(len(str1))  #print the size of the string
print(str1.upper())  #print the string in uppercase
print(str1.lower())  #print the string in lowercase
print(str1.title())  #print the string with first character of each word in uppercase and rest in lowercase
print(str1.count("a"))  #print the number of times "a" is present in the string
print(str1.find("y"))  #print the index of first occurrence of "y"
print(str1.rfind("y"))  #print the index of last occurrence of "y"
print(str1.index("y"))  #print the index of first occurrence of "y"
print(str1.rindex("y"))  #print the index of last occurrence of "y"
print(str1.replace("Tayyab", "Ali"))  #replace "Tayyab" with "Ali" in the string
print(str1.split())  #split the string into a list of words
print(str1.split(" "))  #split the string into a list of words using " " as the delimiter
print(str1.strip())  #remove the leading and trailing whitespace from the string
print(str1.lstrip())  #remove the leading whitespace from the string
print(str1.rstrip())  #remove the trailing whitespace from the string
print(str1.startswith("my"))  #check if the string starts with "my"
print(str1.endswith("umar"))  #check if the string ends with "umar" 
print(str1.isalpha())  #check if the string contains only alphabetic characters
print(str1.isdigit())  #check if the string contains only digits
print(str1.isalnum())  #check if the string contains only alphanumeric characters
print(str1.isspace())  #check if the string contains only whitespace characters
print(str1.islower())  #check if the string is in lowercase
print(str1.isupper())  #check if the string is in uppercase
print(str1.isprintable())  #check if the string contains only printable characters
print(str1.isidentifier())  #check if the string is a valid identifier
print(str1.isnumeric())  #check if the string contains only numeric characters
print(str1.isdecimal())  #check if the string contains only decimal characters
print(str1.isascii())  #check if the string contains only ASCII characters  
print(str1.encode())  #encode the string into bytes
print(str1.center(50))  #center the string in a field of width 50
print(str1.ljust(50))  #left justify the string in a field of width
print(str1.rjust(50))  #right justify the string in a field of width 50
print(str1.zfill(50))  #pad the string with zeros on the left to make it of width 50
print(str1.expandtabs())  #replace tabs with spaces in the string
print(str1.partition("Tayyab"))  #split the string into a tuple of three    parts using "Tayyab" as the separator
print(str1.rpartition("Tayyab"))  #split the string into a tuple of three parts using "Tayyab" as the separator starting from the right
print(str1.splitlines())  #split the string into a list of lines  
print(str1.swapcase())  #swap the case of each character in the string
print(str1.title())  #convert the first character of each word to uppercase and the rest to lowercase
print(str1.upper().count("A"))  #print the number of times "A" is present in the string after converting it to uppercase
print(str1.lower().count("a"))  #print the number of times "a" is present in the string after converting it to lowercase    
print(str1.strip().split())  #remove the leading and trailing whitespace from the string and split it into a list of words  
 