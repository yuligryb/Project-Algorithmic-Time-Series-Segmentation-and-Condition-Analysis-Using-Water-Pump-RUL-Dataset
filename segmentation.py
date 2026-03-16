import numpy as np

def segment_signal(signal,start,end,threshold,segments):
    part = signal[start:end]
    variance = np.var(part)

    if variance > threshold and (end-start) > 20:
        mid = (start+end)//2
        segment_signal(signal,start,mid,threshold,segments)
        segment_signal(signal,mid,end,threshold,segments)

    else:
        segments.append((start,end))