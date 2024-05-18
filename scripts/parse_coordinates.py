fd = open("../data/coordinates.txt")
lines = fd.readlines()

for l in lines:
	timestamp = l.strip().split(" ")[0]
	lat = l.strip().split(" ")[1].split(",")[2]
	lng = l.strip().split(" ")[1].split(",")[4]
	alt = l.strip().split(" ")[1].split(",")[9]
	print(timestamp, lat, lng, alt)	
