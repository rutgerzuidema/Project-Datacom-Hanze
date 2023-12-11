import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib as mpl
import matplotlib.pyplot as plt

"General properties"
N = 600
F = 800     #[Hz]
T = 1.0 / F #[s]
t = np.linspace(0.0, N * T, N, endpoint = False)

"Input signal definition"
y = np.sin(50.0 * 2.0 * np.pi * t) + 0.5 * np.sin(80.0 * 2.0 * np.pi * t)

"FFT"
tf = fftfreq(N, T)[:N // 2]
yf = fft(y)

"Visualization"
plt.plot(tf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.show()