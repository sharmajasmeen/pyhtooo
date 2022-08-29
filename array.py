# import numpy
# a=numpy.array([23.2,231])
# print(a)
# import math
# from numpy import pi
# print(math.sin(pi))

# #shape manipulation-examples
# import numpy as np
# new_cyclist_trails=np.array([[23,23,34,34,45,23],[34,34,24,34,4,5]])
# print(new_cyclist_trails.ravel()) #Flattens the dataset
# print(new_cyclist_trails.reshape(3,4)) #Changes or reshapes the dataset to 3 rows ,4 columns
# print(new_cyclist_trails.resize(2,6)) #resize again to 2 rows and 6 columns
# n=np.hsplit(new_cyclist_trails,3) #split the array into 3
# print(n)
# n1=np.array([23,23,34,23,12])
# n2=np.array([23,23,34,23,12])
# h=np.hstack((n1,n2)) #stacks the array together
# print(h)

#pandas

import numpy as np
import pandas as pd
first_series=pd.Series(list('abcdef')) #here list is passed as an argument.
print(first_series) 
# we have not created index
#  for data but data alignment is done automatically.
#index is automatically assigned  for each data element is passed in the list.
#This is key feature when it comes to data wrangling
#it also shows the data types of the elemenets.

#This example shows you how to ................create a series from ndarray:................
np_countary=np.array(['luxembourg','norway','japan','switaerland','united states','qatar','iceland','sweden','singapore','denmark'])
s_country=pd.Series(np_countary)
print(s_country)

#................create series from dict................
dict_country_gdp=pd.Series([123,432,2334,122222223,123,234,23,4,123,23],index=['luxembourg','norway','japan','switaerland','united states','qatar','iceland','sweden','singapore','denmark'])
print(dict_country_gdp)     #countries have been passed as an index and gdp as the actual data value\

#................create series from scalar................
#print series with scalar input
scalar_series=pd.Series(3.,index=['a','b','c','d','e'])
print(scalar_series)

#................ACCESSING ELEMENTS IN SERIES................

#Data can be accessed through different function like loc,iloc by passing data elements position or index range

#access elements in the series
print(dict_country_gdp[0])

#access first 5 countries from series
print(dict_country_gdp[0:5])

#Look up a country by name or index
print(dict_country_gdp.loc['norway'])

#Look up by position 
print(dict_country_gdp.iloc[1])

#................vectorized operations in series................
#vectorized operations are performed by the data element's position.

first_vector_series=pd.Series([1,22,3,2],index=['a','b','c','d'])


second_vector_series=pd.Series([1,22,3,2],index=['a','b','e','d'])
print(first_vector_series+second_vector_series)

second_vector_series=pd.Series([1,22,3,2],index=['a','c','b','d'])
print(first_vector_series+second_vector_series)

#...........././////////Data Frame.......................
#Data frame is a two dimensional labeled data structure with columns of potetially different data types.

#.................. Create dataframe from lists........

import pandas  as pd
#create data frame from dict of equal length lists

#last five olympics data:place,year and number of countries participated
olympic_data_list={'hostcity':['london','beijing','athens','sydney','atlanta'],
                    'year':[2012,2008,2004,2000,1996],
                    'No.of participating countries':[203,204,201,200,197]}
df_olympic_data=pd.DataFrame(olympic_data_list)
print(df_olympic_data)

#Create dataframe from dict

#This example shows how to create a dataframe from a series of dicts:

#create  dataframe from dicts of dicts

olympic_data_dict={'london':{2015:205},'beijing':{2008:202}}
df_olympic_data_dict=pd.DataFrame(olympic_data_dict)
print(df_olympic_data_dict)