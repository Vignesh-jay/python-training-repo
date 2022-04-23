#Billing

amount=0
choice="y"

while(choice=="y"):
    price=eval(input("enter the price : "))
    qty=eval(input("Enter Quantity : "))
    amount=(price*qty)+amount
    choice=input("wanna continue - y/n : ")
print("Your bill amount is : ",amount)
print("----------------------------------------------")

#nested while

k=1
x=int(input("Enter number of lines : "))
while k<=x:
    j=1
    while j<=k:
        print(j,end=" ")
        j=j+1
    print("\n")
    k=k+1
print("----------------------------------------------")