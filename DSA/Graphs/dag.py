#%%
#edges
edges = [(0,1),(0,4),(1,2),(2,0),(3,4),(3,6),\
  (4,0),(4,3),(4,7),(5,3),(5,7),(6,5),(7,4),(7,8),(8,5),(8,9),(9,8)]
#%%
#Adjacency Matrix
#undirected
import numpy as np
Amat = np.zeros(shape=(10,10))
for i,j in edges:
  Amat[i,j]=1
  Amat[j,i]=1

#Adjacency List
AList = {}

for i in range(10):
  AList[i] = []

for i,j in edges:
  AList[i].append(j)
  AList[j].append(i)

