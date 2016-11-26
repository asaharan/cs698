import json

path = "../out-final/hopDist.out"
path_original = "../out-final/hopDist-original-graph.out"
out_path = "../out-final/hopDist.plotData"
fp = open(path, 'r')
fmain = open(path_original, 'r')
count = 0
data = {}
for line in fp.readlines():
	if line != '':
		data[count] = json.loads(line.strip())
		key = data[count].keys()[0]
		data[count] = data[count][key]
		count += 1
for line in fmain.readlines():
	if line != '':
		main = json.loads(line.strip())
		main = main[main.keys()[0]]
fout = open(out_path, 'w')
keys = set()
for key in main.keys():
	keys.add(int(key))
for key in data[0].keys():
	keys.add(int(float(key)))
for key in data[1].keys():
	keys.add(int(float(key)))
for key in data[2].keys():
	keys.add(int(float(key)))
for key in data[3].keys():
	keys.add(int(float(key)))
keys = list(keys)
for key in sorted(keys):
	key = str(key)
	string = str(key) + "\t"
	if key in main.keys():
		string += str(main[key]) + "\t"
	else:
		string += "0\t"
	if key in data[0].keys():
		string += str(data[0][key]) + "\t"
	else:
		string += "0\t"
	if key in data[1].keys():
		string += str(data[1][key]) + "\t"
	else:
		string += "0\t"
	if key in data[2].keys():
		string += str(data[2][key]) + "\t"
	else:
		string += "0\t"
	key = str(key) + ".0"
	if key in data[3].keys():
		string += str(data[3][key]) + "\n"
	else:
		string += "0\n"
	fout.write(string)
