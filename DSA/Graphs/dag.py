#%%
#Edges, Adjacency Matrix, Adjacency List
import numpy as np

edges = [(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(3,5),(3,7),(3,7),(5,6),(6,7)]

Amat = np.zeros(shape=(8,8))

for i,j in edges:
  Amat[i,j]=1

Alist = {}

for i in range(8):
  Alist[i]=[]

for i,j in edges:
  Alist[i].append(j)

#%%
#Topological Sort Adjacency Matrix
def Toposort(A):
  (rows,cols)= A.shape
  indegree ={}
  toposortlist = []
  for c in range(cols):
    indegree[c]=0
    for r in range(rows):
      if A[r,c]==1:
        indegree[c]+=1
  
  for i in range(rows):
    j  =min([k for k in range(cols) if indegree[k]==0])
    toposortlist.append(j)
    indegree[j]=indegree[j]-1
    for k in range(cols):
      if A[j,k]==1:
        indegree[k]-=1
  return toposortlist

#%%
#Eg Mat
Toposort(Amat)
#%%
#Class Queue
class Queue:
  def __init__(self):
    self.queue = []
  
  def isempty(self):
    return self.queue == []
  
  def addq(self,v):
    self.queue.append(v)
    return
  
  def delq(self):
    v= None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
      
    return v

  def __str__(self):
    return str(self.queue)

#%%
#Topological Sort Adjacency List
def TopologicalSort(A):
  indegree,toposortlist = {},[]
  for u in A.keys():
    indegree[u]=0
  
  for u in A.keys():
    for v in A[u]:
      indegree[v]+=1

  zerodegreeq = Queue()
  for u in A.keys():
    if indegree[u]==0:
      zerodegreeq.addq(u)

  while not zerodegreeq.isempty():
    j = zerodegreeq.delq()
    toposortlist.append(j)
    indegree[j]-=1
    for k in A[j]:
      indegree[k]-=1
      if indegree[k]==0:
        zerodegreeq.addq(k)

  return toposortlist  
# %%
#Eg list
TopologicalSort(Alist)

# %%
#Longest Path in DAG 

def longestpath(A):
  (indegree,lpath)=({},{})
  for u in A.keys():
    indegree[u],lpath[u]=0,0
  
  for u in A.keys():
    for v in A[u]:
      indegree[v]+=1
  
  zerodegreeq = Queue()
  for u in A.keys(): 
    if indegree[u]==0:
      zerodegreeq.addq(u)
  
  while not zerodegreeq.isempty():
    j = zerodegreeq.delq()
    indegree[j]-=1
    for k in A[j]:
      indegree[k]-=1
      lpath[k] = max(lpath[k],lpath[j]+1)  
      if indegree[k]==0:
        zerodegreeq.addq(k)
  
  return lpath

#%%
longestpath(Alist)    
# %%
