#This file opens the both the SEGY test data and label volume and loads a slice to visualise it  

import segyio


seismic_file_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/TrainingData_Image.segy'
label_file_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/TrainingData_Labels.segy'


with segyio.open(seismic_file_path, "r") as seismic_file:
    seismic_data = segyio.tools.cube(seismic_file)
    print("Seismic data loaded. Shape:", seismic_data.shape)


with segyio.open(label_file_path, "r") as label_file:
    label_data = segyio.tools.cube(label_file)
    print("Label data loaded. Shape:", label_data.shape)


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


facies_descriptions_colors = {
    1: ("Basement/Other", 'red'),
    2: ("Slope Mudstone A", 'blue'),
    3: ("Mass Transport Deposit", 'green'),
    4: ("Slope Mudstone B", 'cyan'),
    5: ("Slope Valley", 'magenta'),
    6: ("Submarine Canyon System", 'yellow')
}

cmap = mcolors.ListedColormap([color for _, color in facies_descriptions_colors.values()])


slice_index = 100  

plt.figure(figsize=(18, 6))
plt.subplot(1, 2, 1)
plt.imshow(np.rot90(seismic_data[slice_index,:,:], 3), cmap='gray')
plt.title(f'Seismic Data - Inline {slice_index}')
plt.colorbar(label='Amplitude')
plt.xlabel('Crosslines')
plt.ylabel('Depth/Time')


ax = plt.subplot(1, 2, 2)
cax = ax.imshow(np.rot90(label_data[slice_index,:,:], 3), cmap=cmap)
plt.title(f'Label Data - Inline {slice_index}')
plt.xlabel('Crosslines')
plt.ylabel('Depth/Time')


cbar = plt.colorbar(cax, ax=ax, orientation='vertical', ticks=range(1, 7))
cbar.set_ticklabels([desc for desc, _ in facies_descriptions_colors.values()])
cbar.set_label('Facies')

plt.show()

import segyio
import numpy as np


seismic_file_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/TrainingData_Image.segy'
label_file_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/TrainingData_Labels.segy'


seismic_subvol_save_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/seismic_sub_volume.npy'
label_subvol_save_path = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/label_sub_volume.npy'


inline_range = (98, 102)  
crossline_range = (300, 400)


with segyio.open(seismic_file_path, 'r') as seismic_file:
    seismic_data = segyio.tools.cube(seismic_file)
    seismic_sub_volume = seismic_data[inline_range[0]:inline_range[1], crossline_range[0]:crossline_range[1], :]


np.save(seismic_subvol_save_path, seismic_sub_volume)
print(f"Seismic sub-volume saved to {seismic_subvol_save_path}")


with segyio.open(label_file_path, 'r') as label_file:
    label_data = segyio.tools.cube(label_file)
    label_sub_volume = label_data[inline_range[0]:inline_range[1], crossline_range[0]:crossline_range[1], :]


np.save(label_subvol_save_path, label_sub_volume)
print(f"Label sub-volume saved to {label_subvol_save_path}")




