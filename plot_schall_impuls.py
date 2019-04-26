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


werte = csv_read("csv/impuls-echo.csv")
xdata = np.zeros(5)
ydata = np.zeros(5)

badXData = np.zeros(2)
badYData = np.zeros(2)

for i in range(0,7):
    if(i < 5):
        xdata[i] = float(werte[i+1][5])
        ydata[i] = float(werte[i+1][0])*2
    else:
        badXData[i-5] = float(werte[i+1][5])
        badYData[i-5] = float(werte[i+1][0])*2


x_line = np.linspace(22.7, 88.1)
plt.plot(xdata, ydata, "r.", label="Messwerte")
plt.plot(badXData, badYData, "rx", label="Nicht betrachtete Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(np.diag(pcov)))

#$c_\text{Schall} = (0,271 \pm 0,002) \frac{\symup{cm}}{\symup{µs}} = (2,71 \ pm 0,02) \cdot 10^{3} \frac{\symup{m}}{\symup{s}}$
#$y_0 = (0,1 \pm 0,1)$ cm

plt.xlabel(r"Zeit $\Delta t$ / µs")
plt.ylabel(r"Distanz $d$ / cm")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_schall_impuls.pdf")