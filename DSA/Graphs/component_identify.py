#%%
#Edge and Adacency List for undirected graph

edges = [(0,1),(0,4),(4,8),(4,9),\
  (2,3),(2,6),(3,7),(2,7),(6,7),(7,10),(7,11),(6,10)]

Alist ={}
for i in range(12):
  Alist[i]=[]

for i,j in edges:
  Alist[i].append(j)
  Alist[j].append(i)



#%%
#Queue
class Queue:
  def __init__(self):
    self.queue = []
  
  def addq(self,v):
    self.queue.append(v)
  
  def isempty(self):
    return self.queue == []
  
  def delq(self):
    v=None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
      return v
    else:
      return v

  def __str__(self):
    return str(self.queue)
    

#%%
#BFS

def BFSList(A,v):
  visited ={}
  for i  in A.keys():
    visited[i]=False
  
  q=Queue()
  visited[v]=True
  q.addq(v)

  while not q.isempty():
    j = q.delq()
    for k in A[j]:
      if not visited[k]:
        visited[k]=True
        q.addq(k)

  return visited


#%%
#Connected Components
def Components(A):
  component={}
  for i in A.keys():
    component[i]=-1
  
  (compid,seen)=(0,0)

  while seen <= max(A.keys()):
    startv = min([i for i in A.keys() if component[i]==-1])
    visited = BFSList(A,startv)
    for i in visited.keys():
      seen=seen+1
      component[i]=compid
    compid=compid+1
  return component

#%%
#Eg
Components(Alist)

# %%
