#disctionary

mydict={'Country':'india','State':'Tamilnadu'}
print(mydict)
print((mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict['Country'])
print(mydict['State'])
print(mydict.__len__())
mydict['District']='PDKT'
print(mydict)
mydict['State']='Karnataka'
print(mydict)
print(mydict.get('State'))
print(len(mydict))
print(sorted(mydict))
new_dict=mydict.copy()
print(new_dict)
print(new_dict.clear())
print('District' in mydict)
print('State' in new_dict)

#cube of a number
fresh_dict=dict()
end=int(input("enter number : "))

for i in range(1,end+1):
    fresh_dict[i]=i*i*i

print(fresh_dict)

#upper & lower case counter

text_dict={'upper':0,'lower':0}
str=input("Enter a String :")

for x in str:
    if x.isupper():
        text_dict['upper']+=1
    elif x.islower():
        text_dict['lower']+=1
    else:
        pass

print("Total upper case letters : ",text_dict['upper'])
print("Total lower case letters : ",text_dict['lower'])

#Alpha & Number counter

test_dict={'Alpha':0,'Number':0}
str=input("Enter a String :")

for x in str:
    if x.isalpha():
        test_dict['Alpha']+=1
    elif x.isdigit():
        test_dict['Number']+=1
    else:
        pass

print("Total letters : ",test_dict['Alpha'])
print("Total Numbers : ",test_dict['Number'])