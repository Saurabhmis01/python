n=int(input("Enter Your Age:"))
if n<18:
    print("Counter no.1")
elif n<=25:
    print("Counter no.2")
elif n<=35:
    print("Counter no.3")
elif n<=50:
    print("Counter no.4")
elif n<=65:
    print("Counter no.5")
else:
    print("Thanks For Visit")



# =================even======================
x=range(-2,-11,-2)
print(x)
print(list(x))
print(tuple(x))
print(set(x))

# ====================odd========================
x=range(-1,-10,-2)
print(x)
print(list(x))
print(tuple(x))
print(set(x))

# ===============even number square================
my_list=[]
for i in range(2,11,2):
    x=i**2
    my_list.append(x)
print(my_list)

# =====================Total Char==============
my_str=input("Enter Your Name:")
Total_char=0
for i in my_str:
    Total_char=Total_char+1
print(Total_char)

# =================while=========================
n=int(input("enter no.:"))
i=1
while i<=n:
    print(n,end='*')
    n=n-1