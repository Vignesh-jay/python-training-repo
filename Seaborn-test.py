import seaborn as sbn
import matplotlib.pyplot as plt
import numpy as np


titanic=sbn.load_dataset('titanic')

print(titanic.shape)
print(titanic.keys())
print(titanic.describe())
#---------------------------------------------------------------------------------------------------------------------

# Box plot

sbn.boxplot(x=titanic['class'],y=titanic['fare'],data=titanic).set_title('Box Plot')
plt.show()
#--------------------------------------------------------------------------------------------------------------------

# violin Plot

sbn.violinplot(x="class",y="age",hue="sex",data=titanic).set_title("Violin Plot")
plt.show()
#--------------------------------------------------------------------------------------------------------------------

# point plot

sbn.pointplot(y=titanic['age'],x=titanic['class'],data=titanic).set_title('Point plot')
plt.show()
#-------------------------------------------------------------------------------------------------------------------

# Line plot

sbn.lineplot(y=titanic['fare'],x=titanic['embarked'],data=titanic).set_title('Line plot')
plt.show()
#--------------------------------------------------------------------------------------------------------------------

# count plot

sbn.countplot(y=titanic['alive'],data=titanic).set_title('count plot')
plt.show()
#--------------------------------------------------------------------------------------------------------------------

# Bar plot

sbn.barplot(y=titanic['fare'],x=titanic['embarked'],data=titanic).set_title('Bar plot')
plt.show()
#---------------------------------------------------------------------------------------------------------------------

# factor plot

# default kind
sbn.factorplot(x="sex",y="age",hue="alive",data=titanic)

# Box plot kind
sbn.factorplot(x="sex",y="age",hue="alive",kind="box",data=titanic)

# Bar kind
sbn.factorplot(x="sex",y="age",hue="alive",kind="bar",data=titanic)

# violin Kind
sbn.factorplot(x="sex",y="age",hue="alive",kind="violin",data=titanic)

plt.show()
#---------------------------------------------------------------------------------------------------------------------

# Facet Grid

sbn.FacetGrid(titanic,col="class")

grid1=sbn.FacetGrid(titanic,col="class")
grid1.map(plt.hist,"age")

grid2=sbn.FacetGrid(titanic,col="class",hue="alive")
grid2.map(plt.hist,"age")

grid1=sbn.FacetGrid(titanic,col="class",hue="sex")
grid1.map(plt.scatter,"age","fare")

plt.show()
#----------------------------------------------------------------------------------------------------


# continuous Variable

iris=sbn.load_dataset('iris')

# Scatter Plot

sbn.scatterplot(y="sepal_length",x="petal_length",data=iris).set_title('scatter plot')
plt.show()
#-----------------------------------------------------------------------------------------------------

# regression plot

sbn.regplot(y="petal_width",x="petal_length",data=iris)
sbn.lmplot(y="sepal_width",x="petal_width",data=iris)
sbn.lmplot(y="sepal_width",x="petal_width",data=iris,order=2)
plt.show()
#-------------------------------------------------------------------------------------------------------

# heat map

sbn.heatmap(iris[['petal_length','petal_width']]).set_title('heat map')
plt.show()

sbn.heatmap(iris[['petal_length','petal_width']],cmap="RdYlGn").set_title('heat map')
plt.show()
#-------------------------------------------------------------------------------------------------------

# Univariate Distribution plot

plt.figure(figsize=(10,10))

plt.subplot(311)
sbn.distplot(iris[['petal_length']]).set_title('Distribution plot')

plt.subplot(312)
sbn.distplot(iris[['petal_length']],kde=False).set_title('Distribution plot for kde=False')

plt.subplot(313)
sbn.distplot(iris[['petal_length']],hist=False).set_title('Distribution plot for hist=False')

plt.show()
#----------------------------------------------------------------------------------------------------------

# joint plot 

sbn.jointplot(y="petal_length",x="sepal_length",data=iris)

# regression plot

sbn.jointplot(y="petal_length",x="sepal_length",kind="reg",data=iris)

plt.show()
#-----------------------------------------------------------------------------------------------------------

# joint Hexbin Plot

sbn.jointplot(y="petal_length",x="sepal_length",kind="hex",data=iris)
plt.show()
#-----------------------------------------------------------------------------------------------------------

# joint kernal density Plot

sbn.jointplot(y="petal_length",x="sepal_length",kind="kde",data=iris)
plt.show()
#-----------------------------------------------------------------------------------------------------------

# Pair Plot

sbn.pairplot(iris,vars=['sepal_length','sepal_width','petal_length'],kind='reg')

sbn.pairplot(iris,vars=['sepal_length','sepal_width','petal_length'], hue='species', diag_kind="hist", palette="colorblind")

sbn.pairplot(iris, kind='reg')

sbn.pairplot(iris,hue='species', kind='scatter', diag_kind="kde", palette="deep")

plt.show()
#-------------------------------------------------------------------------------------------------------------

# Pair Grid

grid1=sbn.PairGrid(iris)
grid1.map(plt.scatter)

grid2=sbn.PairGrid(iris)
grid2.map_upper(plt.scatter)
grid2.map_lower(sbn.kdeplot)
grid2.map_diag(plt.hist)

plt.show()
#-------------------------------------------------------------------------------------------------------------

#Color setting using set_palette

def mychart(num=1):
    value=np.linspace(0,10,100)
    for i in range(1,10):
        plt.plot(value,np.sin(value+i*.8)*(10-i)*num)
sbn.set_style("white")

plt.figure(1, figsize=(20,8))

sbn.set_palette("Reds")
plt.subplot(121)
mychart()

sbn.set_palette("BrBG",10)
plt.subplot(122)
mychart()

plt.show()
#----------------------------------------------------------------------------------------------------------
