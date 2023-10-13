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


number = [1,2,3,3,4,5]
list_1 = []
for n in number:
    if n not in list_1:
        list_1.append(n)
print(list_1)




    