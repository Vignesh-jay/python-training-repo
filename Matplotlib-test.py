import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as stl

# printing version

print("\n",matplotlib.__version__,"\n")
#---------------------------------------------------------------------------------

# using ggplot style

stl.use('ggplot')

# simple Plot view

plt.plot([16,12,11,10,12,8,4,17,9,11,15,14,13])
plt.ylabel('Random numbers')
plt.show()
#---------------------------------------------------------------------------------

# with grids and special effects

plt.plot([7,5,8,11,13,9,11],[5,7,9,12,15,16,17],color='g',linewidth=5.0)
plt.title('user defined color and width of line')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.grid(True)
plt.text(5, 12, 'colored line')
plt.show()
#---------------------------------------------------------------------------------

# draw dot and lines on same chart with axes limit

plt.plot([6,9,7,11,13],[8,11,13,12,15],'ro',[6,9,7,11,13],[8,11,13,12,15],'m')
#first set of data plots dots and the second plots lines 
# ro Mentions red colored dots an m mentions meganda colored lines
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('dot and line togather')
plt.axis([5,15,5,17])
plt.show()
#---------------------------------------------------------------------------------

# Multi lines with multi colors and shapes

a=list(range(1,11))
b=list(range(5,55,5))
c=list(range(10,110,10))
d=list(range(20,210,20))
print("first list : ",a)
print("Second list : ",b)
print("Third List : ",c)
print("Fourth List : ",d)
#chart with different colors
plt.plot(a,a,'g^',a,b,'bs',a,c,'r--',a,d,'mo')
#limits
plt.xlim(0,11)
plt.ylim(0,220)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('Multi lines with multi colors and shapes')
plt.grid(True,color='k')
plt.show()
#---------------------------------------------------------------------------------

# simple pie chart

list1=[10,30,40,30,60,70,80,100,70,40]
plt.pie(list1,labels=list1)
plt.show()
#------------------------------------------------------------------------------------------------

# simple Violin Plot

plt.violinplot([10,11,12,18,23,27,29,30,26,28,24,23,14,12,16,12,12,27,27])
plt.show()
#------------------------------------------------------------------------------------------------

#simple Scatter plot

ecom=['myntra','snapdeal','alibaba','amazon','flipkart']
q1_profit=[35,45,100,70,40]
q2_profit=[38,40,105,65,45]
q3_profit=[30,42,120,72,50]
q4_profit=[25,34,115,60,48]

plt.scatter(ecom, q1_profit,color='green')
plt.scatter(ecom, q2_profit,color='blue')
plt.scatter(ecom, q3_profit,color='pink')
plt.scatter(ecom, q4_profit,color='red')

# Same plot in dotted line chart
plt.plot(ecom,q1_profit,'g--',ecom,q2_profit,'b--',ecom,q3_profit,'r--',ecom,q4_profit,'m--')

plt.xlabel('Organisation Name')
plt.ylabel('Profit')
plt.title('Scatter plot')
plt.show()
#-------------------------------------------------------------------------------------------------------

# histogram

list1 = list(range(1,10,2))
list2= [12,15,17,19,15]
plt.hist2d(list1, list2)
plt.show()
#------------------------------------------------------------------------------------------------------

#Multiple bar charts on one image

ecom=['myntra','snapdeal','alibaba','amazon','flipkart']
q1_profit=[35,45,100,70,40]
q2_profit=[38,40,105,65,45]
q3_profit=[30,42,120,72,50]
q4_profit=[25,34,115,60,48]

#creating different bar charts on one image using subplot()
plt.figure(1,figsize=(10,10))

plt.subplot(221)
plt.bar(ecom, q1_profit)
plt.title('Quarter1 Profit')

plt.subplot(222)
plt.bar(ecom, q2_profit)
plt.title('Quarter1 Profit')

plt.subplot(223)
plt.bar(ecom, q3_profit)
plt.title('Quarter1 Profit')

plt.subplot(224)
plt.bar(ecom, q4_profit)
plt.title('Quarter1 Profit')
plt.suptitle('Profit on Quarter basis')

plt.show()
#-------------------------------------------------------------------------------------

# Stacked bar chart

plt.figure(1,figsize=(15,10))
count=['a','b','c','d','e']
pop_1930=[10,20,24,30,20]
pop_1940=[12,27,30,42,26]
pop_1950=[15,35,34,50,33]
pop_1960=[27,43,43,57,38]
pop_1970=[35,45,46,62,40]
pop_1980=[38,49,55,65,45]
pop_1990=[48,54,65,75,58]
pop_2000=[48,54,65,75,58]
pop_2010=[53,58,70,77,63]

plt.bar(count, pop_1930,color='green')
plt.bar(count, pop_1940,color='red',bottom=pop_1930)
plt.bar(count, pop_1950,color='yellow',bottom=pop_1940)
plt.bar(count, pop_1960,color='blue',bottom=pop_1950)
plt.bar(count, pop_1970,color='brown',bottom=pop_1960)
plt.bar(count, pop_1980,color='orange',bottom=pop_1970)
plt.bar(count, pop_1990,color='purple',bottom=pop_1980)
plt.bar(count, pop_2000,color='pink',bottom=pop_1990)
plt.bar(count, pop_2010,color='magenta',bottom=pop_2000)

plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Stacked bar chart')
plt.show()
#-----------------------------------------------------------------------------------

# Area plot

msale = [1,2,3,4,5,6,7,8,9,10,11,12]
Electronics = [8,11,9,8,10,9,10,11,12,9,10,11]
Clothing = [8,7,8,6,8,7,5,8,5,7,8,6]
Food = [5,6,2,4,6,5,2,4,2,3,4,5]
Books = [3,4,5,3,3,6,6,2,6,5,3,4]

plt.plot([],[],color='pink',label='Books', linewidth=5)
plt.plot([],[],color='blue',label='Food', linewidth=5)
plt.plot([],[],color='red',label='Clothing', linewidth=5)
plt.plot([],[],color='cyan',label='Electronics', linewidth=5)

plt.stackplot(msale,Books,Food,Clothing,Electronics,colors=['pink','blue','red','cyan'])
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Area chart for sales of different catagories')
plt.legend()
plt.show()
#--------------------------------------------------------------------------------------

# quiver plot 

a=[10,20,30,40,50,60,70]
b=[60,40,80,100,120,140,150]
plt.figure(1,figsize=(15,15))

plt.subplot(3,2,1)
plt.quiver(a,b,color='r')

plt.subplot(3,2,2)
plt.quiver(b,a,color='b')

plt.subplot(3,2,3)
x=8
y=6
m,n=np.mgrid[0:x,0:y]
plt.quiver(m,n)

plt.subplot(3,2,4)
plt.quiver(n,m)

plt.subplot(3,2,5)
x=20
y=15
m,n=np.mgrid[10:x,10:y]
plt.quiver(m,n)

plt.subplot(3,2,4)
plt.quiver(n,m)
plt.suptitle('Quiver plots')

plt.show()
#----------------------------------------------------------------------------------

val1=np.linspace(-9, 9,600)
val2=np.linspace(-5, 5,500)

a,b=np.meshgrid(val1,val2)
plt.figure(1,figsize=(10,5))
plt.subplot(131)
plt.imshow(a+b)
plt.subplot(132)
plt.imshow(a-b)
plt.subplot(133)
plt.imshow(a*b)
plt.show()
#------------------------------------------------------------------------------------

val1=np.linspace(-9, 9,600)
val2=np.linspace(-5, 5,500)

a,b=np.meshgrid(val1,val2)
plt.figure(1,figsize=(15,10))

plt.subplot(2,4,1)
plt.contour(a,b,a+b,alpha=.75,cmap='jet')

plt.subplot(2,4,2)
plt.contourf(a,b,a+b,alpha=.75,cmap='jet')

plt.subplot(2,4,3)
plt.contour(a,b,a*b,alpha=.75,cmap='jet')

plt.subplot(2,4,4)
plt.contourf(a,b,a*b,alpha=.75,cmap='jet')

plt.subplot(2,4,5)
plt.contour(a,b,a-b,alpha=.75,cmap='jet')

plt.subplot(2,4,6)
plt.contourf(a,b,a-b,alpha=.75,cmap='jet')

plt.subplot(2,4,7)
plt.contour(a,b,b-a,alpha=.75,cmap='jet')

plt.subplot(2,4,8)
plt.contourf(a,b,b-a,alpha=.75,cmap='jet')

plt.suptitle('Contour Plot')
plt.show()
#-----------------------------------------------------------------------------------------------------
