s=open("signal.csv")
c=open("coordinates.csv")

signal=s.readlines()
coordinates=c.readlines()
s.close()
c.close()

datas = {}
datac = {}

for s in signal:
	parts = s.strip().split(" ")
	if not len(parts) == 2:
		continue;
	datas[float(parts[0])] = float(parts[1])

for c in coordinates:
	parts = c.strip().split(" ")
	if not len(parts) == 4:
		continue;
	datac[float(parts[0])] = [float(parts[1]), float(parts[2]), float(parts[3])]


result = []

timestamps = list(datac.keys())
timestamps.sort()
timestamps2 = list(datas.keys())
timestamps2.sort()
import re
import utm

for t2 in timestamps2:
	found = False
	end = -1
	oldt = -1
	for t in timestamps:
		if t2 > t:
			end = t2
			oldt = t
		if t2 < t and end != -1:
			break

	if end == -1:
		continue
	
	#print(end, datas[t2], datac[oldt][0], datac[oldt][1],  datac[oldt][2])
	deg = float(re.match("^([41]{2})[0-9\.]+", str(datac[oldt][0])).group(1))
	min = float(re.match("^[41]{2}([0-9\.]+).*", str(datac[oldt][0])).group(1))/60.0
	lat = deg + min
	deg = float(re.match("^([069]{2})[0-9\.]+", str(datac[oldt][1])).group(1))
	min = float(re.match("^[069]{2}([0-9\.]+).*", str(datac[oldt][1])).group(1))/60.0
	lng = deg + min

	u = utm.from_latlon(lat, lng)
	print(end, datas[t2], u[0], u[1],  datac[oldt][2], lat, lng)

