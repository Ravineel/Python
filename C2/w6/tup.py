name = input("Enter file:")

handle = open(name)
time = dict()

for line in handle:
    if line ==" ":continue
    if not line.startswith("From"):continue
    words = line.split()
    a = line.find(":")-2
    b = line.find(":")
    word = line[a:b]
    time[word] = time.get(word,0)+1
lst = list()
for k,v in time.items():
    t = (k,v)
    lst.append(t)
lst = sorted(lst)

for k,v in lst:
    print(k,v)