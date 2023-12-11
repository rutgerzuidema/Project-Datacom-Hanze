import numpy as np
from scipy import signal
import matplotlib as mpl
import matplotlib.pyplot as plt

"Input signal properties"
f_max = 20000   #[Hz]
f_s = 2 * f_max #[Hz]
Ts = 1 / f_s    #[s]
t = np.linspace(0, 1, 1000, False)  # 1 second

"Filter properties"
order = 5
f_low = 20      #[Hz]
f_high = 200    #[Hz]

"Test signal"
freq1 = np.sin(2*np.pi*5*t)
freq2 = np.sin(2*np.pi*20*t)
freq3 = np.sin(2*np.pi*80*t)
freq4 = np.sin(2*np.pi*320*t)
sig = freq1 + freq2 + freq3 + freq4

"Import audio signal"


"Filter"
sos = signal.butter(order, Wn=[f_low, f_high], btype='bandpass', analog=False, output='sos', fs=f_s)
output = signal.sosfilt(sos, sig)

"Visualization"
fig, ax = plt.subplots()
ax.plot(sig)
ax.plot(output)
ax.legend(['Input', 'Output'])
plt.show()