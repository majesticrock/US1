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
    return u - q*x


werte = csv_read("csv/impuls-echo.csv")
xdata = np.zeros(5)
ydata = np.zeros(5)

badXData = np.zeros(2)
badYData = np.zeros(2)

badXData[0] = float(werte[4][0])*2
badYData[0] = np.log(float(werte[4][3]))

badXData[1] = float(werte[6][0])*2
badYData[1] = np.log(float(werte[6][3]))

for i in range(0,3):
    xdata[i] = float(werte[i+1][0])*2
    ydata[i] = np.log(float(werte[i+1][3]))

i=4
xdata[i-1] = float(werte[i+1][0])*2
ydata[i-1] = np.log(float(werte[i+1][3]))
i=6
xdata[i-2] = float(werte[i+1][0])*2
ydata[i-2] = np.log(float(werte[i+1][3]))

x_line = np.linspace(3.11, 18.26)*2
plt.plot(xdata, ydata, "r.", label="Messwerte")
plt.plot(badXData, badYData, "rx", label="Nicht betrachtete Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(np.diag(pcov)))

#$\ln \bigg( \frac{U_0}{1\symup{V}} \bigg) = (0,6 \pm 0,1)$
#
#$\alpha = (0,031 \pm 0,005) \frac{1}{\symup{cm}} = (3,1 \pm 0,5) \frac{1}{\symup{m}}$

plt.xlabel(r"Distanz $d$ / cm")
plt.ylabel(r"$\ln \bigg( \frac{U}{1\symup{V}} \bigg)$")
plt.legend(loc="center left")
plt.tight_layout()
plt.savefig("build/plot_daempfung.pdf")