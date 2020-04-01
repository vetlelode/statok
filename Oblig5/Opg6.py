import numpy as np
import scipy.stats as stats

katter = np.genfromtxt("katter_vekt.csv", delimiter=",")
r, p = stats.pearsonr(katter[:, 1], katter[:, 2])
print(r)
