import segyio
import segysak


print(segyio.__version__)
print(segysak.__version__)

with segyio.open('/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy', "r") as f:
    print(f.ilines)
    print(f.xlines)



file_path = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy'
with segyio.open(file_path, "r") as f:
    inlines = f.attributes(segyio.TraceField.INLINE_3D)[:]
    crosslines = f.attributes(segyio.TraceField.CROSSLINE_3D)[:]

    inline_number = 10 
    crossline_number = 20 
    for i, (iline, xline) in enumerate(zip(inlines, crosslines)):
        if iline == inline_number and xline == crossline_number:
            trace_data = f.trace[i]
            break
    
    print(trace_data) 


import segyio
import sys

file_path = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy'
inline_number = 10 # The inline you want

with segyio.open(file_path, "r") as f:
    inlines = f.attributes(segyio.TraceField.INLINE_3D)[:]

    trace_count = 0
    desired_trace_data = None

    for i, iline in enumerate(inlines):
        if iline == inline_number:
            trace_count += 1
            if trace_count == 200:
                desired_trace_data = f.trace[i]
                break

    if desired_trace_data is None:
        print("Error: 200th trace on the specified inline not found.")
        sys.exit(1)

    print(desired_trace_data) # Print the trace data






""""

inline_indices = segyio.tools.metadata(f).iline
print(inline_indices)
crossline_indices = segyio.tools.metadata(f).xline
print(crossline_indices)

inline_number = 10 
crossline_number = 20 

#trace_data = segyio.tools.gather(f, inline=inline_indices[inline_number], crossline=crossline_indices[crossline_number])
#print(trace_data)

inlines = f.attributes(segyio.TraceField.INLINE_3D)[:]
print(inlines)
crosslines = f.attributes(segyio.TraceField.CROSSLINE_3D)[:]
print(crosslines)

inline_number = 10 # Replace with the inline you want
crossline_number = 20 # Replace with the crossline you want

for i, (iline, xline) in enumerate(zip(inlines, crosslines)):
    if iline == inline_number and xline == crossline_number:
        trace_data = f.trace[i]
        break

"""




