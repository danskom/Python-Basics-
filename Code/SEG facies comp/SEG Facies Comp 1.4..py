#This series of code pieces does simple statistical analyses of each facies - the code does one analysis at a time 

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis



#Max amplitude


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski//Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]

import numpy as np
import matplotlib.pyplot as plt


facies_volumes = [np.load(path) for path in facies_paths]


max_amplitudes = [np.nanmax(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, max_amplitudes, color='skyblue')
plt.xlabel('Facies')
plt.ylabel('Maximum Amplitude')
plt.title('Maximum Amplitude per Facies Volume')
plt.show()


#Mean amplitude


import numpy as np
import matplotlib.pyplot as plt


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


mean_amplitudes = [np.nanmean(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, mean_amplitudes, color='green')
plt.xlabel('Facies')
plt.ylabel('Mean Amplitude')
plt.title('Mean Amplitude per Facies Volume')
plt.show()


#Standard Deviations

import numpy as np
import matplotlib.pyplot as plt



facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


std_dev_amplitudes = [np.nanstd(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, std_dev_amplitudes, color='red')
plt.xlabel('Facies')
plt.ylabel('Standard Deviation of Amplitudes')
plt.title('Standard Deviation of Amplitudes per Facies Volume')
plt.show()


#Variance


import numpy as np
import matplotlib.pyplot as plt


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


variance_amplitudes = [np.nanvar(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, variance_amplitudes, color='purple')
plt.xlabel('Facies')
plt.ylabel('Variance of Amplitudes')
plt.title('Variance of Amplitudes per Facies Volume')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Paths for the 6 facies volumes
facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]

# Load facies volumes from .npy files
facies_volumes = [np.load(path) for path in facies_paths]

# Calculate the median amplitude for each facies volume
median_amplitudes = [np.nanmedian(volume) for volume in facies_volumes]

# Facies labels for plotting
facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']

# Creating the plot
plt.figure(figsize=(10, 6))
plt.bar(facies_labels, median_amplitudes, color='orange')
plt.xlabel('Facies')
plt.ylabel('Median Amplitude')
plt.title('Median Amplitude per Facies Volume')
plt.show()



#Median Amplitude


import numpy as np
import matplotlib.pyplot as plt

facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


median_amplitudes = [np.nanmedian(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, median_amplitudes, color='orange')
plt.xlabel('Facies')
plt.ylabel('Median Amplitude')
plt.title('Median Amplitude per Facies Volume')
plt.show()


#Amplitude Range 

import numpy as np
import matplotlib.pyplot as plt


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


amplitude_ranges = [np.nanmax(volume) - np.nanmin(volume) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(10, 6))
plt.bar(facies_labels, amplitude_ranges, color='pink')
plt.xlabel('Facies')
plt.ylabel('Amplitude Range (Max-Min)')
plt.title('Amplitude Range per Facies Volume')
plt.show()


#Skew and Kurtosis

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


skewnesses = [skew(volume[~np.isnan(volume)]) for volume in facies_volumes]
kurtoses = [kurtosis(volume[~np.isnan(volume)]) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.bar(facies_labels, skewnesses, color='brown')
plt.xlabel('Facies')
plt.ylabel('Skewness')
plt.title('Skewness of Amplitude Distribution')


plt.subplot(1, 2, 2)
plt.bar(facies_labels, kurtoses, color='gray')
plt.xlabel('Facies')
plt.ylabel('Kurtosis')
plt.title('Kurtosis of Amplitude Distribution')

plt.tight_layout()
plt.show()


#Percentiles


import numpy as np
import matplotlib.pyplot as plt


facies_paths = [
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_1_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_2_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_3_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_4_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_5_sub_volume.npy',
    '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/Facies_Volumes_6_sub_volume.npy'
]


facies_volumes = [np.load(path) for path in facies_paths]


percentiles_25th = [np.nanpercentile(volume, 25) for volume in facies_volumes]

percentiles_75th = [np.nanpercentile(volume, 75) for volume in facies_volumes]


facies_labels = ['Facies 1', 'Facies 2', 'Facies 3', 'Facies 4', 'Facies 5', 'Facies 6']


plt.figure(figsize=(12, 6))


plt.bar(np.array(range(len(facies_labels))) - 0.2, percentiles_25th, width=0.2, color='yellow', label='25th Percentile')

plt.bar(np.array(range(len(facies_labels))) + 0.2, percentiles_75th, width=0.2, color='blue', label='75th Percentile')

plt.xlabel('Facies')
plt.ylabel('Amplitude')
plt.title('Quantile Analysis per Facies Volume')
plt.xticks(range(len(facies_labels)), facies_labels)
plt.legend()

plt.show()
