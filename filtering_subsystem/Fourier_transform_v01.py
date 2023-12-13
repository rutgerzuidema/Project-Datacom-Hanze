import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"General properties"
N = 600
F = 800     #[Hz]
T = 1.0 / F #[s]
t = np.linspace(0.0, N * T, N, endpoint = False)

"Input signal definition"
y = np.sin(50.0 * 2.0 * np.pi * t) + 0.5 * np.sin(80.0 * 2.0 * np.pi * t)


"Calculate Fourier series to the Nth harmonic"
def fourierSeries(period, N):
    result = []
    T = len(period)
    t = np.arange(T)
    
    for n in range(N+1):
        an = 2 / T * (period * np.cos(2 * np.pi * n * t / T)).sum()
        bn = 2 / T * (period * np.sin(2 * np.pi * n * t / T)).sum()
        result.append((an, bn))
    
    return np.array(result)

"Visualization"
#General
fig, axs = plt.subplots(2)

#Labels
fig.suptitle("Input signal and its component frequencies")
axs[0].set_ylabel('Input signal')
axs[1].set_ylabel('Component frequencies')

#Input signal plot
axs[0].plot(t, y)

#Component frequencies plot
axs[1].plot(fourierSeries(y, N))

plt.show()

#t_period = np.arange()