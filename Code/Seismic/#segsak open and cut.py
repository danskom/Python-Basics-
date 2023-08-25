#segsak open and cut


from segysak.segy import segy_loader

print("segysak is successfully imported!")




from segysak.segy import segy_loader

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
print(segyio.__version__)

scan = segy_header_scan(segy_file, max_traces_scan=2000)
scan
