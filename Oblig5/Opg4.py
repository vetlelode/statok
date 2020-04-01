import numpy as np
import scipy.stats as stats
import math

katter = np.genfromtxt("katter_vekt.csv", delimiter=',')
alfa = float(input("Signifikansnivå:\n"))
my_0 = float(input("μ:\n"))
X = np.average(katter[:, 1])
S = np.std(katter[:, 1])
n = math.sqrt(len(katter[:, 1]))
print("X: {}\nS: {}\nn: {}".format(X, S, n))

t = ((X-my_0)/(S/n))
tav = -stats.t.ppf(alfa, len(katter[:, 1]))

# Hypoteser:
#H0: μ <= μ0
#H1: μ > μ0
# Sjekk om H0 Skal forkastes:
if(t >= tav):
    print("{} > {}, H0 kan forkastes".format(t, tav))
else:
    print("H1 kan forkastes")

_, pval = stats.ttest_1samp(katter[:, 1], 2.75)
print("P-verdien er: {}".format(pval))
x = 1
while(t >= -stats.t.ppf(x, len(katter[:, 1]))):
    x -= 0.0001

print("Verdien {} er signifikansverdien som gjør at vi kan forkaste H0".format(x))

my_0 = 0
while(t > -stats.t.ppf(0.05, len(katter[:, 1]))):
    my_0 += 0.001
    t = ((X-my_0)/(S/n))
print("Verdien μ0 = {} er grensa mellom å forkaste H0 eller H1".format(my_0))
