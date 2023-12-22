#This code opens the volumes given by SEG, it shows a visualisaton by slicing the data, it then saves sub volume of the
#the data from which the facies are going to be extracted. It also overlays the facies label volume on the seismic to show 
#where the boundaries are for each facies. 


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


seismic_subvol_file = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/seismic_sub_volume.npy'
label_subvol_file = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/label_sub_volume.npy'


seismic_sub_volume = np.load(seismic_subvol_file)
label_sub_volume = np.load(label_subvol_file)


facies_colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']
facies_descriptions = ['Basement/Other', 'Slope Mudstone A', 'Mass Transport Deposit', 
                       'Slope Mudstone B', 'Slope Valley', 'Submarine Canyon System']
cmap_facies = mcolors.ListedColormap(facies_colors)


inline_index = 0  


seismic_rotated = np.rot90(seismic_sub_volume[inline_index, :, :], 3)
label_rotated = np.rot90(label_sub_volume[inline_index, :, :], 3)


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
im_seismic = plt.imshow(seismic_rotated, cmap='gray', aspect='auto')
plt.title(f'Seismic Data - Inline {inline_index + 98}') 
plt.colorbar(im_seismic, orientation='vertical', pad=0.02)


plt.subplot(1, 2, 2)
im_label = plt.imshow(label_rotated, cmap=cmap_facies, aspect='auto')
plt.title(f'Label Data - Inline {inline_index + 98}') 


cbar = plt.colorbar(im_label, orientation='vertical', pad=0.02, ticks=range(1, 7))
cbar.set_ticklabels(facies_descriptions)
cbar.set_label('Facies')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable


cmap_facies = mcolors.ListedColormap(facies_colors)


inline_index = 0  


seismic_rotated = np.rot90(seismic_sub_volume[inline_index, :, :], k=3)
label_rotated = np.rot90(label_sub_volume[inline_index, :, :], k=3)


fig, ax = plt.subplots(figsize=(12, 6)) 

im_seismic = ax.imshow(seismic_rotated, cmap='gray', aspect='auto')
ax.set_title(f'Seismic Data - Inline {inline_index + 98}')


im_facies = ax.imshow(label_rotated, cmap=cmap_facies, alpha=0.5, aspect='auto')


divider = make_axes_locatable(ax)


cax_seismic = divider.append_axes("left", size="5%", pad=1.2) 
cbar_seismic = plt.colorbar(im_seismic, cax=cax_seismic, orientation='vertical')
cbar_seismic.set_label('Amplitude')


cax_facies = divider.append_axes("right", size="5%", pad=0.3)  
cbar_facies = plt.colorbar(im_facies, cax=cax_facies, orientation='vertical', ticks=range(1, 7))
cbar_facies.ax.set_yticklabels(['Basement/Other', 'Slope Mudstone A', 'Mass Trans Dep', 
                                'Slope Mudstone B', 'Slope Valley', 'Subm Canyon Sys'])
cbar_facies.set_label('Facies')


plt.subplots_adjust(left=0.15, right=0.85)

plt.show()





