import numpy as np
import scipy.stats as stats

A = np.array([48, 33, 37, 13, 37, 23, 31, 37, 22, 11])
B = np.array([33, 36, 35, 55, 48, 39, 38, 36, 32])
C = np.array([53, 47, 51, 66, 35, 40, 48, 44, 56, 40, 45])
D = np.array([45, 22, 20, 41, 22, 19, 34, 23, 20, 26, 29])

dfn = 3
dfd = len(A) + len(B) + len(C) + len(D) - dfn
print(dfd)

f, p = stats.f_oneway(A, B, C, D)
print("testobservatoren F:{} er større en kvantilen:{}\nDerfor kan hypotesen H0 forkastes".format(
    f, stats.f.ppf(1-0.05, dfd, dfn)))
