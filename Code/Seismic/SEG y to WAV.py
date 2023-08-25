from obspy import read

st = read("/Users/danielskomorowski/Dropbox/Python/OpenDetectDataSet/filt_mig.sgy", format="SEGY")
#print(st)

len(st) #get no of traces
traceno = len(st)
print("Number of traces: ", traceno)

tr=st[0] #get trace length
len(tr) #length of traces
tracelen = len(tr)
print ("Trace length: ", tracelen)

a=[] # trace list container

for trF in range(10, traceno, 12): # first channel = 10, then steps of 12
	#print (trF)
	tr1 = st[trF]
	a.append(tr1.data[0:tracelen-1])
else:
	print("Done list")

#convert list to an array

import numpy as np

#npa = np.asarray(a, dtype=np.float32) - original encoding not readable in wave module
npa = np.asarray(a, dtype=np.int16)




# convert array to a single line for mono output
b = npa.ravel()

print(b)

from scipy.io.wavfile import write

#write("Seismic_to_WAV.wav",15902,b) #sample rate, used 44000 and a[0] and compared to length of trace in SeisSee, in my case and arrived at 15902.... was lazy.
write("Seismic_to_WAV3.wav",44100,b) #adjusted frequency 
print("File written.")