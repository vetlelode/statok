import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

katter = np.genfromtxt("katter_vekt.csv", delimiter=',', skip_header=1)


# Dette er bare en instilling som gir litt "finere" grafer
plt.style.use('bmh')
fig, ax1 = plt.subplots()
ax1.set(title="Opg 1", ylabel="Hjertets vekt i gram",
        xlabel="Kattens vekt i kg")
# Plot ut for deloppgave A
ax1.scatter(katter[:, 2], katter[:, 3], label="Spredningsplottet")
# Beregn regresjonslinjen
b_hat, a_hat, r_value, p_value, std_err = stats.linregress(
    katter[:, 2], katter[:, 3])
# Print ut verdiene som er relevante for OPG1 b
print("Y = {} + {}x\nStandardfeil: {}".format(a_hat, b_hat, std_err))
# Plott ut regresjonslinjen over det orginale scatterplottet som en "Bonus"
ax1.plot(katter[:, 2], a_hat + b_hat *
         katter[:, 2], 'r', label='Regresjonslinjen')

# plt.show()
# Deloppgave D
n = len(katter[:, 2])
x_hat = np.average(katter[:, 2])
x = float(input("Skriv in kattens vekt:\n"))
y_hat = a_hat + b_hat*x
t_alfa = stats.t.ppf(0.975, n-2)
S = math.sqrt(2.423)
# Jeg slet mye med å finne standardfeilen her,
# men fant den til slutt (tror jeg) via å kjøre denne dataen gjennom modfisert kode fra Opg2
# og hentet ut verdien res.mse_total
conf_int = t_alfa * S * \
    math.sqrt((1/n)+((x-x_hat)/(S/std_err))**2)
print("Konfidensintevallet for {} er: {} +/- {}".format(x, y_hat, round(conf_int, 1)))
# Deloppgave E
pred_int = t_alfa * S * \
    math.sqrt(1+(1/n)+((x-x_hat)/(S/std_err))**2)
print("Prediksjonsintervallet for {} er: {} +/- {}".format(x, y_hat, round(pred_int, 1)))
