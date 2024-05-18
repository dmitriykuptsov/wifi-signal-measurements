import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

s=open("signal.csv")
c=open("coordinates.csv")

signal=s.readlines()
coordinates=c.readlines()
s.close()
c.close()

datas = {}
datac = {}

import re
import utm

X = []
Y = []
Z = []
C = []

for s in signal:
	parts = s.strip().split(" ")
	if not len(parts) == 2:
		continue;
	datas[float(parts[0])] = float(parts[1])

for c in coordinates:
	parts = c.strip().split(" ")
	if not len(parts) == 4:
		continue;

	deg = float(re.match("^(41)[0-9\.]+", parts[1]).group(1))
	min = float(re.match("^41([0-9\.]+).*", parts[1]).group(1))/60.0
	lat = deg + min
	deg = float(re.match("^(069)[0-9\.]+", parts[2]).group(1))
	min = float(re.match("^069([0-9\.]+).*", parts[2]).group(1))/60.0
	lng = deg + min

	u = utm.from_latlon(lat, lng)
	print(parts[0], u[0], u[1],  parts[3], lat, lng)

	#X.append(float(u[0]))
	#Y.append(float(u[1]))
	X.append(lat)
	Y.append(lng)
	Z.append(float(parts[3]))

ax.scatter(X, Y, Z)
plt.show()

