import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data = np.array([[100, 200, 300, 400, 500], [240, 480, 670, 820, 1040]])
print(data[0, :], data[1, :])
b_hat, a_hat, r_value, p_value, std_err = stats.linregress(
    data[0, :], data[1, :])
print("Y = {} + {}n\nStandardfeil: {}".format(a_hat, b_hat, std_err))

T = b_hat-b0/std_err
