fruit1 = input("enter 3 favroit fruit names: ")
fruit2 = input()
fruit3 = input()
list1 = [fruit1 , fruit2 , fruit3]
print(list1)

#check if list is palindrome (elements are same if we read from beginning or from end) or not
list2 = [1,2,3,4,5]
list3 = ["mango", "banana", "grapes", "banana", "mango"]

cp_list2 = list2.copy()
cp_list2.reverse()
if list2 == cp_list2:
    print("list2 is palindrome")
else:   
     print("list2 is not palindrome")
     
cp_list3 = list3.copy()
cp_list3.reverse()
if list3 == cp_list3:
    print("list3 is palindrome")
else:
    print("list3 is not palindrome")