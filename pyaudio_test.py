import pyaudio
from math import pi
import numpy as np

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1, )


def make_sinewave(frequency, length, sample_rate=44100):
    length = int(length * sample_rate)
    factor = float(frequency) * (pi * 2) / sample_rate
    waveform = np.sin(np.arange(length) * factor)

    return waveform


while True:
    event = input()
    print(event)
    wave = make_sinewave(ord(event)*2, 0.1)
    stream.write(wave.astype(np.float32).tobytes())
    # stream.stop_stream()
    # stream.close()