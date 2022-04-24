
#simple function
def prin():
    print("\nhello world \n")
    print("good day\n")

prin()

#Calling funtion with returns

def fun():
    a=int(input("Enter a Value : "))
    b=int(input("enter b Value : "))
    c=a*b
    return c

print("the a * b value is ",fun(),"\n")

#nesting of funtions

def greet():
    print("Hello !\n")
def welcome():
    greet()
    print("Welcome...!\n")
greet()
welcome()

#Recursive funtions - factorial computing

def fact(num):
    if num==0:
        return 1
    else:
        ans=num*fact(num-1)
        return ans
value=int(input("input the number : "))
print("\nthe factorial of ",value," is : ",fact(value),"\n")

#Scope of variables - Global

total=1000

def offer():
    global dis
    dis=300
def amount():
    print(total-dis)

offer()
amount()
