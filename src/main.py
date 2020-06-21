import time
import math
import random

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addlist(self, l1={}):
        self.graph = l1


    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, sr):

        dist = [float("Inf")] * self.V
        dist[sr] = 0

        for _ in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w


        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print("Graph contains negative weight cycle")
                        return


        self.printArr(dist)

storeVal=[]
newVal=[]
tot=0

src=int(input("\nEnter the source vertex"))

nV=int(input('\nenter the no of vertices in the graph'))

g=Graph(nV)

for i in range(0,nV):
    print ('\nour current edge is ', i )
    newVal.append(i)
    conn=int(input('Enter the no of connections from this edge'))
    tot=tot+conn
    k=0
    while(k!=conn):
        lastV=int(input('\nEnter the terminal edge from vertex'))
        newVal.append(lastV)
        wt=int(input('enter the weight of the edge'))
        newVal.append(wt)

        k=k+1

        storeVal.append(newVal)
        newVal = []
        newVal.append(i)
    newVal = []

g.addlist(storeVal)
g.BellmanFord(src)
for i in range (3):
    a = []
    for i in range(10):
        a.append(math.floor(100*random.normalvariate(0,0.1)))
    for i in range (tot):
        storeVal[i][2] = a[i]
    # print("array value:")
    # print(a)
    # print("stored val:")
    # print(storeVal)
    g.addlist(storeVal)
    g.BellmanFord(src)
    time.sleep(3)
