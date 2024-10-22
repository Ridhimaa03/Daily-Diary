# def append_different_elements(list1, list2, indices):
#     for index in indices:
#         if index < len(list1):
#             list2.append(list1[index])
#         else:
#             print(f"Index {index} is out of range for list1")

# # Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30]
# indices = [0, 2, 4]

# append_different_elements(list1, list2, indices)

# print("Updated list2:", list2)

# #sum of all the items in list use sum function
# l=[1,2,3]
# a=sum(l)
# print(a)

# #Multiply of all the items in list use sum function
# l2=[2,2,3]
# result=1
# for i in l2:
#     result*=i
# print(result)

# #Largst number
# print("Largest number: ",max(l2))

# #Smallest number
# print("Smallest number: ",min(l2))

# #check if list is empty or not
# if (len(l2)==0):
#     print("List is empty")
# else:
#     print("list isn't empty")

# #To remove duplicates from list
# #This is the fastest and smallest method to achieve a particular task. It first removes the duplicates and returns a dictionary which has to be converted to list. 
# l3=["Hi","Hello","Hi"]
# a=[*set(l3)]
# # l4=list(a)
# # print(l4)
# print(a)

# #method two 
# result=[]
# for x in l3:
#     if x is not l3:
#         result.append(x)
# print(result)

# #remove from a particular index
# l=[1,2,3]
# a=l[0]
# l.remove(a)
# print(l)

# # copy list
# b=l
# print(b)


# #if any one element is present return true
# def have_common_element(list1, list2):
#     # Use any() with a list comprehension to check for common elements
#     if any(element in list2 for element in list1):
#         return True

# # Example usage:
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# result = have_common_element(list1, list2)
# print(result)  # Output: True

# #reverse a list
# lis = [1,3,4]
# lis.insert(1,2)
# print(lis)
# lis.reverse()
# print(lis)

# #shuffling list
# import random
# a=[1,2,3,4,5]
# random.shuffle(a)
# print(a)

# #converting character into string
# char= ['a','b','c']
# a= ''.join(char)
# print(a)

# #To find index of item
# my_list = [10, 20, 30, 40, 50]
# item=40
# index= my_list.index(item)
# print(index)


#sort list
a=[7,4,6,3,10,1]
a.sort()
print(a)
b=["Ridhimaa","Jaya"]
b.sort()
print(b)