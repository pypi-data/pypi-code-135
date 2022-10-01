import librosa
import numpy as np
import random

def _gen_colored_noise (spectral_shape, samples_to_generate):
    # https://www.kaggle.com/holzner/generating-different-colors-of-noise
    def normalize(samples):
        std = samples.std()
        if std > 0:
            return samples / std
        else:
            return samples

    flat_spectrum = np.random.normal(size = samples_to_generate // 2 + 1) + \
            1j * np.random.normal(size = samples_to_generate // 2 + 1)
    return normalize(np.fft.irfft (flat_spectrum * spectral_shape).real)

COLORS = [
    'white',   # flat spectrum
    'pink',    # -3dB (factor 0.5)  per octave / -10 dB (factor 0.1) per decade
    'blue',    # +3dB (factor 2)    per octave / +10 dB (factor 10) per decade
    'brown',   # -6dB (factor 0.25) per octave / -20 dB (factor 0.01) per decade
    'violet'
]
NOISE_CACHE = {}
def _gen_noise (color, samples_to_generate):
    if color == 'white':
        return np.random.normal(size = samples_to_generate)
    spectrum_len = samples_to_generate // 2 + 1
    if color == 'pink':
        return _gen_colored_noise(1. / (np.sqrt(np.arange(spectrum_len) + 1.)), samples_to_generate)
    elif color == 'blue':
        return _gen_colored_noise(np.sqrt(np.arange(spectrum_len)), samples_to_generate)
    elif color == 'brown' or color == 'red':
        return _gen_colored_noise(1. / (np.arange(spectrum_len) + 1), samples_to_generate)
    elif color == 'violet' or color == 'purple':
        return _gen_colored_noise(np.arange(spectrum_len), samples_to_generate)

for color in COLORS:
    NOISE_CACHE [color] = _gen_noise (color, 16000 * 180)

def gen_noise (color, samples_to_generate):
    global NOISE_CACHE

    assert samples_to_generate % 2 == 0
    if samples_to_generate == len (NOISE_CACHE [color]):
        return NOISE_CACHE [color]
    if samples_to_generate <= len (NOISE_CACHE [color]):
        start = random.randrange (0, len (NOISE_CACHE [color]) - samples_to_generate)
        return NOISE_CACHE [color][start:start + samples_to_generate]
    return  _gen_noise (color, samples_to_generate)

def add_noise (y, sr, min_gain = 0.01, max_gain = 0.12):
    if y.shape [0] % 2 == 1:
        y = y [:-1] # make even

    noise = gen_noise (random.choice (COLORS), y.shape [0]) / random.randrange (10, 50)
    if random.randrange (3) == 0:
        noise += gen_noise (random.choice (COLORS), y.shape [0]) / random.randrange (10, 50)
        noise /= 2

    gain = np.random.uniform (min_gain, max_gain)
    return y + ((gain * noise).astype ("float32"))

def speed (y, sr, max_rate = 0.1, min_rate = 0.02):
    rate = 1.0
    if random.randrange (2):
        rate += max (min_rate, random.random () / (max_rate * 100))
    else:
        rate -= max (min_rate, random.random () / (max_rate * 100))
    return librosa.effects.time_stretch (y, rate)

def pitch_shift (y, sr, max_step = 0.5):
    return librosa.effects.pitch_shift (y, sr, random.random () * max_step * random.choice ([1, -1]), bins_per_octave = 12)

def random_laps (y, sr):
    if librosa.get_duration(y, sr = sr) > 1.6:
       time_lap = random.random () / 3
       removable = int (sr * time_lap)
       y = y [removable:len (y) - removable]
       y = np.roll (y, random.randrange (len (y)))
    return y
