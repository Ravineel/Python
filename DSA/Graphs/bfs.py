#Implemented using Queue
#%%
#Class Queue
def neighbours(A,i):
  nbrs =[]
  (rows,cols)=A.shape
  for j in range(cols):
    if A[i,j]==1:
      nbrs.append(j)
  return nbrs

class Queue:
  def __init__(self):
    self.queue = []
    
  def isEmpty(self):
    return self.queue == []
   
  def addq(self,v):
    self.queue.append(v)

  def delq(self):
    v=None
    if not self.isEmpty():
      v=self.queue[0]
      self.queue=self.queue[1:]
    
    return v 

  def __str__(self):
    return str(self.queue)
    
    
# %%
q = Queue()

for i in range(3):
  q.addq(i)
  print(q)
print(q.isEmpty())


for j in range(3):
  print(q.delq(),q)
print(q.isEmpty())

# %%
#BFS function

def BFS(A,v,l=1):
  if l:
    (rows,cols)= A.shape
  else:
    rows = len(A)
  
  visited={}
  for i in range(rows):
    visited[i]=False
  q = Queue()

  visited[v]=True
  q.addq(v)

  if l:

    while not q.isEmpty():
      j = q.delq()
      print(j)
      for k in neighbours(A,j):
        if not visited[k]:
          visited[k]=True
          q.addq(k)

  else:
    while not q.isEmpty():
      j = q.delq()
      print(j)
      for k in A[j]:
        if not visited[k]:
          visited[k]=True
          q.addq(k)

  return visited
# %%

#Edge
edges = [(0,1),(0,4),(1,2),(2,0),(3,4),(3,6),\
  (4,0),(4,3),(4,7),(5,3),(5,7),(6,5),(7,4),(7,8),(8,5),(8,9),(9,8)]
#%%
#Adjacency Matrix
#eg 
import numpy as np
Amat = np.zeros(shape=(10,10))
for i,j in edges:
  Amat[i,j]=1
v = 7
BFS(Amat,v)

# %%
#Adjacency List
#eg
Alist ={}
for i in range(10):
  Alist[i]=[]

for i,j in edges:
  Alist[i].append(j)
v = 7
BFS(Alist,v,0)
# %%
