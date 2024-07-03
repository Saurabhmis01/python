
# # ==================fix object=========================

# my_list = [2,4,6,8,2,4,6,9,3]
# my_tuple = (10,20,30,"abc123",70,80)
# my_set = {2,3,4,5,"abc@1234"}
# my_dict = {"Name : Saurabh Mishra","Qualification : Bsc (cs)"}

# x= frozenset(my_list)
# y= frozenset(my_tuple)
# z= frozenset(my_set)
# p= frozenset(my_dict)


# print(my_list)
# print(my_tuple)
# print(my_set)
# print(my_dict)

# ===================import sys=================


# import sys
# my_list = [10,20,30,40,50]
# my_tuple = (10,20,30,40,50)
# my_set = {10,20,30,40,50}

# lsix= sys.getsizeof("my_list")
# tsix= sys.getsizeof("my_tuple")
# ssix= sys.getsizeof("my_set")

# print(lsix)
# print(tsix)
# print(ssix)


import keyword
list = keyword.kwlist
print(len(list))