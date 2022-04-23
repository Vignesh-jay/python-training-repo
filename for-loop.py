#Tables

num = int(input("Enter a number for table : "))
for k in range(1,11,):
    print(num,"x",k,"=",num*k)
print("----------------------------------------------")

# Sum of Series

sum=0
num = int(input("Enter last number of sreies : "))
for k in range(1,num+1):
    sum=sum+k
print("the total is :",sum)
print("----------------------------------------------")

# Fibannoci Series

num = int(input("numberof fibonacci series to print: "))
a=0
b=1
print(a)
print(b)
for k in range(3,num+1):
    c=a+b
    a=b
    b=c
    print(c)
print("-----------------------------------------------")

#number of stars

num = int(input("number of lines to print: "))
for k in range(1,num+1):
    for j in range(1,k+1):
        print("*", end=" ")
    print("\n")
print("-----------------------------------------------")