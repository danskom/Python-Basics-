import numpy as np
from scipy.io.wavfile import write

# Sampling rate (samples per second)
sampling_rate = 44100

# Frequency of the sine wave in Hertz
frequency = 440

# Duration of the sine wave in seconds
duration = 5

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), False)

# Generate the sine wave
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Save the sine wave as a 16-bit PCM WAV file
write('sine_wave.wav', sampling_rate, (sine_wave * 32767).astype(np.int16))

import sounddevice as sd
import scipy.io.wavfile as wav

# Read the WAV file
rate, data = wav.read('sine_wave.wav')

# Play the WAV file
sd.play(data, rate)
sd.wait()
