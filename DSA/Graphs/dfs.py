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

#%%
#Neughbours

def neighbours(A,i):
  nbrs =[]
  (rows,cols)=A.shape
  for j in range(cols):
    if A[i,j]==1:
      nbrs.append(j)
  return nbrs

#%%
#Depth First Search

def DFSInit(A):
  rows,cols = A.shape

  for i in range(rows):
    visited[i] = False
    parent[i] = -1
  
  return 

def DFS(A,v):
  visited[v] = True
  
  for k in neighbours(A,v):
    if not visited[k]:
      parent[k] = v
      DFS(A,j)

  return


#%%
#EG
visited,parent ={},{} 
DFSInit(Amat)
DFS(Amat,visited,parent,4)# %%

#%%
#DFS List

def DFSInitList(A):
  for i in A.keys():
    visited[i] = False
    parent[i] = -1
  
  return 

def DFSList(A,v):
  visited[v] = True
  
  for k in A[v]:
    if not visited[k]:
      parent[k] = v
      DFSList(A,k)

  return 

#%%
#eg 
visited,parent ={},{}
DFSInitList(AList)
DFSList(AList,visited,parent,4)
# %%
