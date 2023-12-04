import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grid dimensions
nx, ny, nz = 11, 20, 10

# Initialize the voxel array (all True, indicating voxels are present)
voxelarray = np.ones((nx, ny, nz), dtype=bool)

# Initialize the colors array (all voxels initially set to blue)
colors = np.full(voxelarray.shape, 'blue', dtype=object)

# Starting position for the diagonal
start_x, start_z = 5, 9

# Creating the diagonal lines and removing voxels above
for i in range(nz):
    # Check boundaries for x and z
    if start_x + i < nx and start_z - i >= 0:
        colors[start_x + i, :, start_z - i] = 'black'
        voxelarray[start_x + i, :, start_z - i + 1:] = False
    if start_x - i >= 0 and start_z - i >= 0:
        colors[start_x - i, :, start_z - i] = 'black'
        voxelarray[start_x - i, :, start_z - i + 1:] = False

# Plotting the 3D grid with specified voxel colors
ax.voxels(voxelarray, facecolors=colors, edgecolor='gray')

# Define the vertical plane at x=5.5
y, z = np.meshgrid(range(ny), range(nz))
x = np.full(y.shape, 5.5)

# Plot the vertical plane
ax.plot_surface(x, y, z, color='red', alpha=0.5)

# Setting axis labels and adjusting the view angle
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.view_init(elev=20, azim=-45)

plt.show()




















