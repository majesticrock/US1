import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, u, q):
    return u*np.e**(-q*x)


werte = csv_read("csv/impuls-echo.csv")
xdata = np.zeros(4)
ydata = np.zeros(4)

badXData = np.zeros(3)
badYData = np.zeros(3)


for i in range(0,7):
    if(i < 5):
        if(i == 3):
            badXData[i-1] = werte[i+1][0]
            badYData[i-1] = float(werte[i+1][1]) - float(werte[i+1][3])
        else:
            if(i < 3):
                xdata[i] = werte[i+1][0]
                ydata[i] = float(werte[i+1][1]) - float(werte[i+1][3])
            else:
                xdata[i-1] = werte[i+1][0]
                ydata[i-1] = float(werte[i+1][1]) - float(werte[i+1][3])
    else:
        badXData[i-5] = werte[i+1][0]
        badYData[i-5] = float(werte[i+1][1]) - float(werte[i+1][3])


x_line = np.linspace(3.11, 13)
plt.plot(xdata, ydata, "r.", label="Messwerte")
plt.plot(badXData, badYData, "rx", label="Nicht betrachtete Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(np.diag(pcov)))

#$u = (-0,62 \pm 0,02)$ V
#$q = (-2,8 \pm 0,6) \cdot 10^{-4} \frac{1}{\symup{cm}} = (-2,8 \pm 0,6) \cdot 10^{-2} \frac{1}{\symup{m}}$

plt.xlabel(r"Distanz $d$ / cm")
plt.ylabel(r"Amplitudendifferenz $\Delta U$ / V")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_daempfung.pdf")