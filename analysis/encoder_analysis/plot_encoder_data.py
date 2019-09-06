from matplotlib import pyplot as plt
import numpy as np
import csv
import statistics

RESOLUTION = 2 ** 14
# RESOLUTION = 2 ** 14

with open('ma702_data.csv') as csv_file:
# with open('as5048a_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # data_counts = [int(float(x[0][:4])) for x in list(csv_reader) if len(x)]
    data_counts = [int(float(x[0][:4]))//4 for x in list(csv_reader) if len(x)]

data_counts = list(filter(lambda x: 3500/4 < x < 4400/4, data_counts))
# data_counts = list(filter(lambda x: 8105 < x < 8120, data_counts))
data = [x * 360.0/RESOLUTION for x in data_counts]

print('Standard deviation:', statistics.stdev(data))
print('Variance:', statistics.variance(data))

from scipy import signal
freqs, spectrogram = signal.periodogram(data, fs=8000)
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
# plt.hist(data_counts, bins=(max(data_counts) - min(data_counts))//4)
plt.hist(data_counts, bins=max(data_counts) - min(data_counts))

plt.subplot(1, 3, 3)

a = np.array(data_counts)
# corr = np.correlate(a,a,mode='full')/a.size
# corr = corr[corr.size//2:]

A = np.fft.fft(a)
S = np.conj(A)*A/a.size
corr = np.fft.ifft(S)

plt.plot(corr)
plt.xlim(0, 100)

plt.show()
