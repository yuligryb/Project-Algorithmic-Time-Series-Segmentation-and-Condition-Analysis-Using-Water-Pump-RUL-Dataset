from kadane import kadane_algorithm
from segmentation import segment_signal

arr = [1,-2,3,4,-1,2,-5]

print(kadane_algorithm(arr))

signal = [1,1,1,10,10,10,1,1,1]

segments = []
segment_signal(signal,0,len(signal),2,segments)

print(segments)