sorterread = open("mapsorterout.txt","r")
reducew = open("reducerout.txt", "w")

thisKey = ""
thisValue = 0.0

for line in sorterread:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      reducew.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
reducew.write(thisKey + '\t' + str(thisValue)+'\n')

sorterread.close()
reducew.close()