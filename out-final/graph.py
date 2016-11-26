import json
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

file_path = '../out-final/inDegreeDist-original-graph.out'
with open(file_path) as data_file:    
    data = json.load(data_file)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)