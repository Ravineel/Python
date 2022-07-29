#%%
#Edge
edges = [(0,1),(0,4),(1,2),(2,0),(3,4),(3,6),\
  (4,0),(4,3),(4,7),(5,3),(5,7),(6,5),(7,4),(7,8),(8,5),(8,9),(9,8)]
#%%
#Adjacency Matrix
import numpy as np
Amat = np.zeros(shape=(10,10))

for i,j in edges:
  Amat[i,j]=1
print(Amat)
#%%
#Neighbours of v
def neighbours(A,i):
  nbrs =[]
  (rows,cols)=A.shape
  for j in range(cols):
    if A[i,j]==1:
      nbrs.append(j)
  return nbrs

#%%
#Adajency List
Alist ={}
for i in range(10):
  Alist[i]=[]

for i,j in edges:
  Alist[i].append(j)

for i in Alist.keys():
  print(i,"-->",Alist[i])
# %%
#neighnours
def neighbours_list(A,i):
  print(i,"-->",A[i])
# %%
