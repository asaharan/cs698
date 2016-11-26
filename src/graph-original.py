import json
import numpy as np
import pylab as plt
import plotly.plotly as py
py.sign_in('j46799','7EaywDuHnzCVpSsHx7Q9')

file_path = '../out-final/inDegreeDist-original-graph.out'
with open(file_path) as data_file:    
    data = json.load(data_file)

data = data['random edge']
print data
fig = plt.figure()

# x = 200 + 25*plt.randn(1000)
# y = 150 + 25*plt.randn(1000)
x = []
y = []
for i in data:
	x.append(int(i))
	y.append(int(data[i]))
n, bins, patches = plt.hist([y, x])


plot_url = py.plot_mpl(fig, filename='mpl-histogram')