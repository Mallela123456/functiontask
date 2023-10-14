#1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
#def upper_lower(s):
 #   upper_s = 0
  #  lower_s = 0
   # for i in s:
    #    if i.islower():
     #       lower_s = lower_s + 1 
      #  elif i.isupper():
       #     upper_s = upper_s + 1
    #print("No. of Upper case characters :", upper_s)  
    #print("No. of Lower case Characters upper_s :",lower_s)
#t = input("enter the case: ")
#upper_lower(t)


#2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.

#def new_list(name):
 #   order_1 = []
  #  for i in name:
   #     if i not in order_1:
    #        order_1.append(i)
    #return order_1
#print(new_list([1,2,3,3,3,3,4,5]))


#3.Write a Python function to check whether a string is a pangram or not.
#def pangram_1(string_1):
 #   alpahbat = "abcdefghijklmnopqrstuvwxyz"
  #  for char in alpahbat:
   #     if char not in string_1.lower():
    #       return False
    #return True 
#string_1 = input("Enter string: ")
#if(pangram_1(string_1) == True):
 #   print("yes")
#else:
 #   print("No")
 
 #4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10.
 
#def squre_1():
#    list_1 = []
 #   for i in range(1, 11):
  #      list_1.append(i ** 2)
   # print(list_1)
#squre_1()


#5.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20 

#def function_1(sum):
 #   total = 0 
  #  for i in sum:
   #     total = total + i 
    #return total 
#print(function_1([8,2,3,0,7]))

#6.write a function to find sum of given values, pass values has variable number of arguments to function.


def sum_numbers(number):
    total = 0 
    for num in number:
        total = total + num 
    return total 
print(sum_numbers([1,2,3,4,5,6]))

    