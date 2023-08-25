import segyio
import numpy as np

filename = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy'
new_filename = '/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/new_volume.segy'

iline_range = range(10, 31)
xline_range = range(10, 31)

with segyio.open(filename, 'r') as src:
    iline_indices = [i for i, iline in enumerate(src.ilines) if iline in iline_range]
    xline_indices = [i for i, xline in enumerate(src.xlines) if xline in xline_range]
    ilines = [src.ilines[i] for i in iline_indices]
    xlines = [src.xlines[i] for i in xline_indices]

    class Spec:
        def __init__(self, iline, xline, sorting, format, samples, tracecount):
            self.iline = iline
            self.xline = xline
            self.sorting = sorting
            self.format = format
            self.samples = samples
            self.tracecount = tracecount

    spec = Spec(
        iline=len(iline_range),
        xline=len(xline_range),
        sorting=segyio.TraceSortingFormat.INLINE_SORTING,
        format=5,
        samples=src.samples,
        tracecount=len(iline_indices) * len(xline_indices)
    )

    print("Specification created:", spec)

    with segyio.create(new_filename, spec) as dest:
        for iline in ilines:
            for xline in xlines:
                src_trace_index = iline_indices[iline - 10] * len(src.xlines) + xline_indices[xline - 10]
                dest_trace_index = (iline - 10) * len(xlines) + (xline - 10)
                dest.trace[dest_trace_index] = src.trace[src_trace_index]

print("New SEGY file created:", new_filename)
