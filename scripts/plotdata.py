import matplotlib.pyplot as plt

lat = 41 + 07.6900 / 60
lng = 69 + 39.9587 / 60
alt = 794.4
import utm

u = utm.from_latlon(lat, lng)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


fd = open("dataset.csv")

lines = fd.readlines()

X = []
Y = []
Z = []
C = []

max_distance = 0
import math
from math import cos, sin, pi
a = 45*pi/180
for l in lines:
	parts = l.strip().split()
	dist = math.sqrt((float(parts[2]) - u[0])**2 + (float(parts[3]) - u[1])**2 + (float(parts[4]) - alt)**2)
	x = float(parts[2])
	y = float(parts[3]) * cos(a) + float(parts[4]) * sin(a)
	z = float(parts[3]) * (-sin(a)) + float(parts[4]) * cos(a)
	x = float(parts[2])
	y = float(parts[3])
	z = float(parts[4])
	X.append(x)
	Y.append(y)
	Z.append(z)
	C.append(float(parts[1]))
	if dist > max_distance:
		max_distance = dist

print("Maximum distance: " + str(max_distance))
ax.scatter(X, Y, Z, c=C)
plt.show()
