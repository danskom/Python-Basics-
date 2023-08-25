#new environment test

from segysak.segy import segy_loader

print("segysak is successfully imported!")

import pathlib
import platform
from IPython.display import display
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

segy_file = pathlib.Path("/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy")
print("SEG-Y exists:", segy_file.exists())

from segysak.segy import segy_header_scan, segy_header_scrape, get_segy_texthead

print(get_segy_texthead(segy_file))

import segyio

# Open the SEGY file
file_path = "/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy"
with segyio.open(file_path, "r") as segyfile:
    # Print Trace Header keys to see what's available
    print(segyio.TraceField)

    # Read specific trace headers, e.g., Trace UTM X
    #trace_headers = [segyfile.header[trace][segyio.TraceField] for trace in range(segyfile.tracecount)]

    # Print the trace headers
    #print(trace_headers)

with segyio.open(file_path, "r") as segyfile:
    for trace_index in range(len(segyfile.trace)):
        inline = segyfile.header[trace_index][segyio.TraceField.INLINE_3D]
        crossline = segyfile.header[trace_index][segyio.TraceField.CROSSLINE_3D]
        print(f"Trace {trace_index}: Inline {inline}, Crossline {crossline}")

with segyio.open(file_path, "r") as segyfile:
    first_trace = segyfile.trace[0]
    print("First trace as an array:")
    print(first_trace)

with segyio.open(file_path, "r") as segyfile:
    last_trace = segyfile.trace[461379]
    print("Last trace as an array:")
    print(last_trace)

""""

import matplotlib.pyplot as plt
import segyio

file_path = "/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy"

with segyio.open(file_path, "r") as segyfile:
    first_trace = segyfile.trace[0]

plt.plot(first_trace)
plt.title('First Trace')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.show()

"""