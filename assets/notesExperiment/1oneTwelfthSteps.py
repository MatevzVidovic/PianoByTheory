import numpy as np
from scipy.io import wavfile
import scipy as sc


import numpy as np


def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave


# C3 has around these hertz
baseFreq = 130
baseTones = [  (1 + (i / 12)) * 130    for i in range(12)]

# Prvih 12 naredis
# Naslednja oktava bo morala vsak ton imeti 2x toliksen, kot je bil v prejsnji iteraciji.
# Preprosto zato, da je to potem sploh isti ton.

for i in range(3):
    for j in range(12):
        final_sine = get_sine_wave(baseTones[j]*(2**(i+1)), 1)
        name = str(12*i+j + 1) + ".wav"
        wavfile.write(name, rate=44100, data=final_sine.astype(np.int16))



