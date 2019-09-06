from matplotlib import pyplot as plt
import numpy as np
import csv
import statistics

RESOLUTION = 2 ** 14
BITS_PER_COUNT = 2 # For converting 16-bit MA702 data to 14-bit
# BITS_PER_COUNT = 0
DETREND = True

FILENAME = 'ma702_data.csv'
# FILENAME = 'as5048a_data.csv'

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data_counts = [int(float(x[0][:4])) // (2 ** BITS_PER_COUNT) for x in list(csv_reader) if len(x)]

sd_counts = statistics.stdev(data_counts)
mean_counts = statistics.mean(data_counts)

data_counts = list(filter(lambda x: mean_counts - 3 * sd_counts < x < mean_counts + 3 * sd_counts, data_counts))
data_degrees = [x * 360.0/RESOLUTION for x in data_counts]

print('Standard deviation:', statistics.stdev(data_degrees))
print('Variance:', statistics.variance(data_degrees))

from scipy import signal
freqs, spectrogram = signal.periodogram(data_degrees, fs=8000)
spectrogram = [x ** 0.5 for x in spectrogram]

plt.subplot(1, 3, 1)
plt.plot(freqs, spectrogram)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10, 10 ** 3 * 4)
plt.ylim(10 ** -4, 10 ** -1.5)
plt.ylabel('noise density (deg / Hz ^ 1/2)')
plt.xlabel('frequency (Hz)')

plt.subplot(1, 3, 2)
plt.hist(data_counts, bins=max(data_counts) - min(data_counts))

plt.subplot(1, 3, 3)

a = np.array(data_counts) - mean_counts if DETREND else 0
A = np.fft.fft(a)
S = np.conj(A)*A/a.size
corr = np.fft.ifft(S)

plt.plot(corr)
plt.xlim(0, 100)

plt.show()
