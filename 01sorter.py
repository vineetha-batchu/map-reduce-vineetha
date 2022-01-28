mapread = open("mapout.txt","r")  # open file, read-only
mapsave = open("mapsorterout.txt", "w") # open file, write
lines = mapread.readlines()
lines.sort()

for line in lines:
 mapsave.write(line)

mapread.close()
mapsave.close()
