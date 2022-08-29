import pandas as pd
dict1={'Name':['jas','ricky','rishu'],'marks':[89,80,80],'Gender':['female','male','female']}
df1=pd.DataFrame(dict1)
print(df1 )

#if we don't pass any value in head or tail then by default it is 5
print(df1.head(2)) #will print first 2 rows
print(df1.tail(2)) #will print last 2 rows

# find shape of our data set
print(df1.shape)

print("no.of rows",df1.shape[0])
print("no.of columns",df1.shape[0])

#get information about dataset like total no. of rows ,total no. of columns,datatypes of each column and memory requirement
print(df1.info())
print(df1.isnull().sum(axis=1))

#get overall statistics about the dataframe
print(df1.describe())
print(df1.describe(include='all'))

#Find unique value from the gender column
print(df1['Gender'].unique())

#find number of unique values from the gender column
print(df1['Gender'].nunique())

#display count of unique values in gender column
print(df1['Gender'].value_counts())

#find total number of students having marks between 80 to100 (inclusive) using between method
print(df1[df1['marks']>=80])

print(len(df1[(df1['marks']>=85)&(df1['marks']<=90)])) #returns length

print(sum(df1['marks'].between(80,89))) #total no. of students having marks b/w 80 to 89

print(df1['marks'].max())


#Apply method
def marks(x):
    return x/2
print(df1['marks'].apply(marks))

new=df1[df1['half_marks']=(df1['marks'].apply(marks)]
