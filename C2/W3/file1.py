
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('wrong file name')

for line in fh:
    print(line.rstrip().upper())