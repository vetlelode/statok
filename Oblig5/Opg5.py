import numpy as np
import scipy.stats as stats

katter = np.genfromtxt("opg5.csv", delimiter=",")
r, p = stats.pearsonr(katter[:, 0], katter[:, 1])
print(r)
