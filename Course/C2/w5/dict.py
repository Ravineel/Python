name = input("Enter file:")

handle = open(name)
counts = dict()
for line in handle:
    if line == '' :continue
    if not line.startswith('From:'):
    	continue
    	
    words = line.split()
    word = words[1]
    counts[word]=counts.get(word,0)+1

bigcount = 0
bigword = 0 

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word 
        
print(bigword,bigcount)
    
    