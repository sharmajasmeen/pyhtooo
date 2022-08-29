import pandas as pd
df_faa_datasheet=pd.read_csv('E:\\value added\\Lovepreet.csv')
print(df_faa_datasheet.shape)
# print(df_faa_datasheet.head())
# print(df_faa_datasheet.columns)
# #print(df_final_datasheet)
df_analyze_datasheet=df_faa_datasheet[['Country code', 'Country', 'Continental region',
       'NO. OF Internet Plans', 'Average price of 1GB (USD)']]
print(type(df_analyze_datasheet))
# print(df_analyze_datasheet)

#replace 
# print(df_analyze_datasheet['NO. OF Internet Plans'].fillna(value='No',inplace=True))
# df_final_dataset=df_analyze_datasheet.dropna(subset=['Country code'])
# print(df_final_dataset)
# aircrafttype=df_analyze_datasheet.groupby('Country code')
# print(aircrafttype)
# print(aircrafttype.size())
# print(df_faa_datasheet.describe())

correlations = df_analyze_datasheet.corr(method='pearson')
print(correlations)
# Skew for each attribute
skew = df_analyze_datasheet.skew()
print(skew)

# Univariate Histograms
from matplotlib import pyplot
df_analyze_datasheet.hist()
pyplot.show()

# Univariate Density Plots
from matplotlib import pyplot
df_analyze_datasheet.plot(kind='density', subplots=True, layout=(3,3), sharex=False) 
pyplot.show()

#Box and Whisker Plots
from matplotlib import pyplot
df_analyze_datasheet.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()

# Correlation Matrix Plot
correlations = df_analyze_datasheet.corr()
# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
pyplot.show()

# Scatterplot Matrix
from pandas.plotting import scatter_matrix
scatter_matrix(df_analyze_datasheet)
pyplot.show()