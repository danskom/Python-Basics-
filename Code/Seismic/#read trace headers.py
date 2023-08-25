import segyio
import numpy as np
with segyio.open('/Users/danielskomorowski/Dropbox/Python/Code/CoursePrep/Seismic/SEG_ML_facies_comp/TrainingData_Image.segy') as f:
    for trace in f.trace:
        filtered = trace[np.where(trace < 1e-2)]




