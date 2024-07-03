

# my_list = [10,20,30,40,'abc123','abc','abc',10]
# my_list[0]="Saurabh"   mutable
# print(my_list)
# print(my_list[0])
# print(my_list[1+1])   indexing
# print(my_list[0:5])   slice
# print(my_list[-0:-3])
# print(my_list)        mutable

my_list4 = ['Saurabh','Mishra','saurabh123',10,20,30,40,50]
my_list4[0] = "Ambuj"
print(my_list4)
print(my_list4[0])
print(my_list4[4+1])
print(my_list4[0:2])



# ==============In build Function===========================

# my_list1 = [10,20,30,40,'abc123','abc','abc',10]
# print(my_list1)
# print(len(my_list1))
# print(max(my_list1))
# print(min(my_list1))
# print(sum(my_list1))



# ===================In build Method=======================


# my_list = [10,20,30,40,'abc123','abc','abc',10]
# my_list.append('50')
# print(my_list)

my_list = ["Saurabh Mishra", "Anurag Tiwari","Gaurav Mishra"]
my_list.append("Vikash mishra")
print(my_list)


my_list0 = [10,20,30,40,50]
my_list9 = [10,20,30,40,50]
my_list0.extend(my_list9)
print(my_list0)



# my_list1 = [10,20,30,40,'abc123','abc','abc',10]
# my_list2 = [10,20,30,'saurabh','mishra']
# my_list3 = ['saurabh123']
# my_list1.extend(my_list2+my_list3)
# print(my_list1)


my_list1 = [10,20,30,40,'abc123','abc','abc',10]
my_list1.pop()
my_list1.remove('abc123')
print(my_list1)

my_list1 = [10,20,30]
my_list1.remove(10)
print(my_list1)

my_list2 = [10,20,30,40,50,60]
my_list2.insert(20,80)
print(my_list2)

my_list3 = [10,20,30,40,50,60]
my_list3.sort(reverse='true')
print(my_list3)



my_list7 = [10,20,30,40,50,[10,20,30,40,50]]
my_list7.append(60)
print(my_list7)

my_list8 = ['saurabh','gaurav',['bhavesh','himanshu']]
my_list8.extend(my_list8)
print(my_list8)


