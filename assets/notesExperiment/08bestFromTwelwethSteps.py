import numpy as np
from scipy.io import wavfile
import scipy as sc


import numpy as np


def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

def get_fuller_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    # wave = np.clip(wave*10, -1, 1)    # makes it more square
    # wave = np.cumsum(np.clip(wave*10, -1, 1))   # makes it triangular
    
    # this adds multiples of the base freq
    # and so tries to mimic the timbre of instruments.
    # Theoretically it can mimic any instrument.
    c = 8
    wave = wave + amplitude*np.sin(c*np.pi*frequency*t)
    c = 4
    wave = wave + amplitude*np.sin(c*np.pi*frequency*t) 
    return wave


# C2 has around these hertz
baseFreq = 65
theOkayOnes = [12, 14, 15, 16, 18, 20, 21, 22]
baseTones = [  baseFreq*(1 + (i / 12))    for i in theOkayOnes]

# Prvih 12 naredis
# Naslednja oktava bo morala vsak ton imeti 2x toliksen, kot je bil v prejsnji iteraciji.
# Preprosto zato, da je to potem sploh isti ton.

for i in range(5):
    for j in range(len(baseTones)):
        final_sine = get_fuller_wave(baseTones[j]*(2**(i+1)), 1)
        name = str(len(baseTones)*i+j + 1) + ".wav"
        wavfile.write(name, rate=44100, data=final_sine.astype(np.int16))



