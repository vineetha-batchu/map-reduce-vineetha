#Vineetha Batchu
#Practice Mapper

f = open("purchases.txt","r")  # open file, read-only
mp = open("mapout.txt", "w") # open file, write
for line in f:  
    rowList = line.strip().split("    ") 
    print (rowList )
    print (len(rowList ))
    if len(rowList) == 6:
        date, time, location, dept, amount, payType = rowList  #assign names
        print ("{0}\t{1}".format(location, amount))
        mp.write("{0}\t{1}\n".format(location, amount))
f.close()
mp.close()