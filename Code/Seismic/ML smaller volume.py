 
import segyio

filename = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy' 
    
import numpy as np



    
with segyio.open(filename, 'r') as src:
    # Get the inlines and crosslines
    ilines = src.ilines
    xlines = src.xlines

    # Determine the indices of the inlines and crosslines you want to extract
    iline_indices = [i for i, iline in enumerate(ilines) if 10 <= iline <= 31]
    xline_indices = [i for i, xline in enumerate(xlines) if 10 <= xline <= 31]

# Print the indices to make sure they are correct
print("Inline indices:", iline_indices)
print("Crossline indices:", xline_indices)

# Define the inline and crossline ranges
iline_range = range(10, 31)
xline_range = range(10, 31)

# Lists to hold the extracted traces and headers
extracted_traces = []
extracted_headers = []

with segyio.open(filename, 'r') as src:
    for iline_index in iline_indices:
        for xline_index in xline_indices:
            trace_index = iline_index * len(src.xlines) + xline_index
            extracted_traces.append(src.trace[trace_index])
            extracted_headers.append(src.header[trace_index])

# Convert to NumPy arrays
extracted_traces = np.array(extracted_traces)

# Print shapes to confirm the extracted data
print("Extracted traces shape:", extracted_traces.shape)

# Print the type of the first trace in extracted_traces
print(type(extracted_traces[0]))

# Determine the dimensions
num_ilines = len(iline_range)
num_xlines = len(xline_range)
num_samples = len(src.samples)

# Define the new specification
# Define the new specification
spec = {
    'iline': 189,  # Inline byte location (can be different depending on your file)
    'xline': 193,  # Crossline byte location (can be different depending on your file)
    'samples': num_samples,
    'tracecount': num_ilines * num_xlines,
    'sorting': segyio.TraceSortingFormat.INLINE_SORTING,
    'format': 5,  # Format code for IEEE floating point (4 bytes)
}


new_filename = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp'  # Change this to your desired path

# Create the new SEGY file with the defined specification
with segyio.create(new_filename, spec) as dest:
    pass  # We'll fill this in later









   



