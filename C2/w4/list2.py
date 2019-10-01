fname = input("Enter file name: ")

fh = open(fname)
word  = list()
count = 0
for line in fh:
    line.rstrip()
    if line =='':continue
    if not line.startswith("From:"): continue

    word = line.split()
    count = count + 1
    print(word[1])



print('There were',count,'lines in the file with From as the first word')

