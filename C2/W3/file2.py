
fname = input("Enter file name: ")
fh = open(fname)
avg = 0.0
count = 0
for line in fh:
     
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    a = line.find(' ')
    b = line.find('\n',a)
    avg = avg + float(line[a+1:b])
print('Average spam confidence:',avg/count)

