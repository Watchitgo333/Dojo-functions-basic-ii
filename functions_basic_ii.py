# 1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# def count_down(num = 0):
#     list = []
#     for x in range(num,-1,-1):
#         list.append(x)
#     return list

# count_down()
# new_list = count_down(5)
# print(new_list)
# newer_list = count_down(10)
# print(newer_list)

# 2. Print and Return - 
# Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

# def print_and_return(list2):
#     print(list2[0])
#     return list2[1]

# print_and_return([1,2])
# index1 = print(print_and_return([1,2]))

# 3. First Plus Length - 
# Create a function that accepts a list and returns the sum 
# of the first value in the list plus the list's length.

# def first_plus_length(list3):
#     return list3[0] + len(list3)
# sum = first_plus_length([1,2,3,4,5])
# print(sum)

# 4. Values Greater than Second - 
# Write a function that accepts a list and creates a new list containing 
# only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False.

# def values_greater_than_second(list4):
#     new_list4 = []
#     for x in range(0,len(list4)):
#         if len(list4) >= 2:
#             if list4[x] > list4[1]:
#                 new_list4.append(list4[x])
#         elif len(list4) < 2:
#             return False
#     print(len(new_list4))
#     return new_list4

# greater_list = values_greater_than_second([5,2,3,5,1])
# print(greater_list)

# 5. This Length, That Value - 
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.

# def length_and_value(length,value):
#     list5 = []
#     for x in range(0, length):
#         list5.append(value)
#     return list5
# length_val = length_and_value(4,7)
# print(length_val)