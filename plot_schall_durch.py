import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b


werte = csv_read("csv/durchschall.csv")
xdata = np.zeros(5)
ydata = np.zeros(5)


for i in range(0,5):
    xdata[i] = werte[i+1][1]
    ydata[i] = werte[i+1][0]


x_line = np.linspace(12.6, 45.4)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(np.diag(pcov)))

#$c_\text{Schall} = (0,271 \pm 0,003) \frac{\symup{cm}}{\symup{µs}} = (2,71 \ pm 0,03) \cdot 10^{3} \frac{\symup{m}}{\symup{s}}$
#$y_0 = (-0,21 \pm 0,08)$ cm

plt.xlabel(r"Zeit $\Delta t$ / µs")
plt.ylabel(r"Distanz $d$ / cm")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_schall_durch.pdf")