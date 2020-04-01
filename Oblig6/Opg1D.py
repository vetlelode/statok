import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import statsmodels.api as sm
from pandas import DataFrame

# Last inn dataen og hopp over kolonnen løpenummer siden denne ikke har noen effekt
data = np.genfromtxt("katter_vekt.csv", delimiter=",",
                     usecols=(2, 3), skip_header=1)

df = DataFrame(data, columns=['Vekt', 'Hjertevekt'])
# Definer X1 og X2
X = df['Vekt']
# Definer Y
Y = df['Hjertevekt']
X = sm.add_constant(X)
res = sm.OLS(Y, X).fit()
print(float(res.mse_resid))
