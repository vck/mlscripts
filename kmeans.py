import math as m
import pandas as pd


df = pd.read_excel("../Data/Data Hasil Panen Normalisasii.xlsx", skiprows=9)

columns = ["PROUCTION", "POKOK PANEN"]

x = df[columns[0]].values


def distance(a, y):
	error = a-y
	dist = m.sqrt((error)**2)
	return dist 

#x = [0.11446523, 0.23005144, 0.21551243, 0.33112576, 0.18344812]

k = 3
init_center = x[:3]
tidak_sama = True 
max_iter = 1
counter = 0

while tidak_sama:
	center_candidate = []

	for x_ in x:
		dist_data = {}
		for center in init_center:
			dist = distance(x_, center)
			dist_data[dist] = (x_, center)

		center_candidate.append(dist_data)
	
	nc = []
	# 1/ N * sum(X1+X2+X3+...+XN)
	dmaxes = []
	for i in center_candidate:
		min_ = min(i.keys())
		nc.append(i[min_])


	hadeeh = {}
	hadeeeeh = {}

	for hani_jelek in nc:
    	# bikin key dulu sama list kosong bosqu hadeeeh
		hadeeh[hani_jelek[1]] =[]
	
	for hani_jelek in nc:
		for key in hadeeh:
			if hani_jelek[1] == key:
				hadeeh[key].append(hani_jelek[0])

	new_center = []

	for k in hadeeh.keys():
		N = len(hadeeh[k])
		c_new = 1/N * sum(hadeeh[k])
		new_center.append(c_new)

	if init_center == new_center:
		print("center found!")
		print(new_center)
		print(init_center)
		tidak_sama = False
	counter=counter+1
	init_center = new_center
	print("[{}] center belum sama, keep digging!".format(counter))









