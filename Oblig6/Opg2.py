import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from pandas import DataFrame

# Last inn dataen og hopp over kolonnen løpenummer siden denne ikke har noen effekt
data = np.genfromtxt("blodtrykk.csv", delimiter=",",
                     usecols=(1, 2, 3), dtype="i8")

df = DataFrame(data, columns=['Blodtrykk', 'Vekt', 'Alder'])
# Definer X1 og X2
X = df[['Vekt', 'Alder']]
# Definer Y
Y = df['Blodtrykk']
X = sm.add_constant(X)
res = sm.OLS(Y, X).fit()
print(res.summary())
