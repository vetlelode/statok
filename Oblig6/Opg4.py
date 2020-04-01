import numpy as np
import scipy.stats as stats

data = np.array([[55, 59, 62, 64, 61, 59, 65, 57, 57, 60],
                 [50, 49, 49, 53, 60, 62, 50, 50, 52]])

t, pval = stats.ttest_ind(data[0], data[1], equal_var=False)
print(t, stats.t.ppf(0.95, len(data)-1))
