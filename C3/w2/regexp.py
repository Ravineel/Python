import re

hf = open('mbox.txt')
a = hf.read()

y  = re.findall('[0-9]+' ,a)


sum=0

for i in range(len(y)):
    sum = sum + int(y[i]) #totaling the sum

#printing the sum
print(sum)
