import scipy
print('scipy: {}'.format(scipy.__version__)) 
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__)) 
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))


import pandas as pd
from pandas import read_csv
import numpy as np
data=pd.read_csv(r"")
print(data)

# View first 20 rows 
peek = data.head(20)
print(peek)


#Dimensions of your data
shape = data.shape
print(shape)
 
#Data type for each attribute
types=data.dtypes
print(types)

# Descriptive statististical summary
from pandas import set_option
set_option('display.width', 110)
description = data.describe()
print(description)


# Pairwise Pearson correlations
from pandas import set_option
set_option('display.width', 100)
#set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)


# Skew for each attribute
skew = data.skew()
print(skew)

# Univariate Histograms
from matplotlib import pyplot
data.hist()
pyplot.show()

# Univariate Density Plots
from matplotlib import pyplot
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False) 
pyplot.show()

 #Box and Whisker Plots
from matplotlib import pyplot
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()

# Correlation Matrix Plot
correlations = data.corr()
# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
pyplot.show()

# Scatterplot Matrix
from pandas.plotting import scatter_matrix
scatter_matrix(data)
pyplot.show()




