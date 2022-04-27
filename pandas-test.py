import pandas as pd

#Series
#creating list of prices
rate=[10,20,30,40]
#creating a series
productseries=pd.Series(rate,index=['pen','marker','book','mouse'])
#display series
print(productseries,'\n')

#Dataframe
productdf=pd.DataFrame([[10,20,30,40],[15,25,35,45]], columns=['pen','marker','book','mouse'])
#display dataframe
print(productdf,'\n')
#dimensions
print(productdf.shape,'\n')
#size
print(productdf.size,'\n')
#keys - name of columns
print(productdf.keys(),'\n')

#new dataframe
productdf2=pd.DataFrame([[100,200,300,400],[150,250,350,450]], columns=['pen','marker','book','mouse'])
print(productdf2,'\n')

#adding dataframes
productdf3=productdf.append(productdf2)
print(productdf3,'\n')

#adding new column
productdf3["mobile"]=[50,55,500,550]
productdf3["laptop"]=[60,65,600,650]
print(productdf3,'\n')
#dimensions
print(productdf3.shape,'\n')
#size
print(productdf3.size,'\n')
#keys - name of columns
print(productdf3.keys(),'\n')

#Deleting rows and columns
#deleting columns
productdf4=productdf3.drop(columns=["pen","book"])
print(productdf4,"\n")
#deleting rows
productdf4=productdf3.drop(index=[0])
print(productdf4,"\n")

#Importing excel file
mypd=pd.read_excel("excel.xlsx")
print(mypd,"\n")
print(mypd.shape,"\n")

#functions
print(mypd.info(),"\n")
print(mypd.describe(),"\n")
print(mypd.describe,"\n")
print(mypd.head(3),"\n")
print(mypd.tail(3),"\n")
print(mypd['Book'].values,"\n")
print(mypd['Book'].value_counts(),"\n")

#dataframe to list

mylist=mypd['Book'].tolist()
print(mylist,"\n")

#sorting
print(mypd.sort_values(by='Book',ascending=True),"\n")

#data extraction

newds=mypd[mypd['Material']<20]
print(newds,"\n")
print(mypd,"\n")
 
#iloc and loc
print(mypd.iloc[2,1],"\n") #3rd row 2nd column
print(mypd.loc[1]) #only 2nd row
print(mypd.loc[[1],['Notes']],"\n") #only 2nd row and Notes column
print(mypd.loc[:,['Notes']],"\n") #only Notes column

liver=pd.read_csv("ILPD.csv")
print(liver,"\n")
print(liver.shape,"\n")

print(liver.loc[liver['Gender'].str.startswith("Fe")&(liver['ALB']>=5)],"\n") #select rows for gender starts with 'fe', ALB >= 5
print(liver.loc[liver['ALB'].isin([4.4,4.2,4.3]) & (liver['Age']>=60)],"\n") #select rows with ALB=Specified values and age >= 60

print(liver['Gender'].value_counts(),"\n")
print(liver['Gender'].groupby(liver['Gender']).count(),"\n")
print(liver['DB'].groupby([liver['LiverPatient']]).min(),"\n")
print(liver['DB'].groupby([liver['LiverPatient']]).max(),"\n")

print(liver['DB'].groupby([liver['LiverPatient']]).count(),"\n")

print(mypd.shape,"\n")
print(mypd.isnull().sum(),"\n")

mypd2=mypd.copy()
mypd2.dropna(inplace=True)
print(mypd2,"\n")
mypd3=mypd.copy()
mypd3.fillna(0,inplace=True)
print(mypd3,"\n")
