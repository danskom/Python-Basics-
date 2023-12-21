#This code opens the volumes given by SEG, it shows a visualisaton by slicing the data, it then saves sub volume of the
#the data from which the facies are going to be extracted. 


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Paths to the saved sub-volume files
seismic_subvol_file = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/seismic_sub_volume.npy'
label_subvol_file = '/Users/danielskomorowski/Dropbox/Seismic Volumes/SEG_ML_facies_comp/label_sub_volume.npy'

# Load the sub-volumes
seismic_sub_volume = np.load(seismic_subvol_file)
label_sub_volume = np.load(label_subvol_file)

# Define facies colors and descriptions
facies_colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']
facies_descriptions = ['Basement/Other', 'Slope Mudstone A', 'Mass Transport Deposit', 
                       'Slope Mudstone B', 'Slope Valley', 'Submarine Canyon System']
cmap_facies = mcolors.ListedColormap(facies_colors)

# Choose an inline to visualize
inline_index = 0  # Adjust as needed

# Rotate the seismic and label data for the chosen inline
seismic_rotated = np.rot90(seismic_sub_volume[inline_index, :, :], 3)
label_rotated = np.rot90(label_sub_volume[inline_index, :, :], 3)

# Create a figure for visualization
plt.figure(figsize=(12, 6))

# Visualize the seismic data
plt.subplot(1, 2, 1)
im_seismic = plt.imshow(seismic_rotated, cmap='gray', aspect='auto')
plt.title(f'Seismic Data - Inline {inline_index + 98}')  # Adjust inline number based on actual range
plt.colorbar(im_seismic, orientation='vertical', pad=0.02)

# Visualize the label data
plt.subplot(1, 2, 2)
im_label = plt.imshow(label_rotated, cmap=cmap_facies, aspect='auto')
plt.title(f'Label Data - Inline {inline_index + 98}')  # Adjust inline number based on actual range

# Add a discrete color bar for the facies
cbar = plt.colorbar(im_label, orientation='vertical', pad=0.02, ticks=range(1, 7))
cbar.set_ticklabels(facies_descriptions)
cbar.set_label('Facies')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Assuming seismic_sub_volume and label_sub_volume are already loaded
# Assuming facies_colors are already defined

# Define the colormap for facies
cmap_facies = mcolors.ListedColormap(facies_colors)

# Choose an inline to visualize
inline_index = 0  # Adjust as needed

# Rotate the seismic and label data for the chosen inline
seismic_rotated = np.rot90(seismic_sub_volume[inline_index, :, :], k=3)
label_rotated = np.rot90(label_sub_volume[inline_index, :, :], k=3)

# Create a figure for visualization
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size as needed

# Visualize the seismic data
im_seismic = ax.imshow(seismic_rotated, cmap='gray', aspect='auto')
ax.set_title(f'Seismic Data - Inline {inline_index + 98}')

# Overlay facies labels with transparency
im_facies = ax.imshow(label_rotated, cmap=cmap_facies, alpha=0.5, aspect='auto')

# Create an axis divider for colorbars
divider = make_axes_locatable(ax)

# Place amplitude colorbar on the left of the plot with increased padding
cax_seismic = divider.append_axes("left", size="5%", pad=1.2)  # Increased pad for amplitude colorbar
cbar_seismic = plt.colorbar(im_seismic, cax=cax_seismic, orientation='vertical')
cbar_seismic.set_label('Amplitude')

# Place facies colorbar on the right of the plot with increased padding
cax_facies = divider.append_axes("right", size="5%", pad=0.3)  # Increased pad for facies colorbar
cbar_facies = plt.colorbar(im_facies, cax=cax_facies, orientation='vertical', ticks=range(1, 7))
cbar_facies.ax.set_yticklabels(['Basement/Other', 'Slope Mudstone A', 'Mass Trans Dep', 
                                'Slope Mudstone B', 'Slope Valley', 'Subm Canyon Sys'])
cbar_facies.set_label('Facies')

# Adjust the main plot to make space for color bars
plt.subplots_adjust(left=0.15, right=0.85)

plt.show()





