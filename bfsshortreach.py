# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   
        
    def bfs(self, root, n):
        s = root
        visited = [False]*(n)
        queue = []
        distance = [0]*n
        queue.append(s)
        visited[s-1] = True
        distance[s-1] = 0 
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i-1] == False:
                    queue.append(i)
                    distance[i-1] = distance[s-1] + 6
                    #print(i,distance)
                    visited[i-1] = True
        #print (self.graph[16])
        #print(len(distance))
        #print(distance)
        final_output = ""
        for i in range(n):
            if i != root-1:
                if distance[i] != 0:
                    final_output += str(distance[i]) + " "
                else:
                    final_output += "-1 "
        print(final_output.strip())
                    
test = int(input())
for t in range(test):
    g = Graph()
    n,m = input().split()
    n,m = int(n), int(m)
    for el in range(m):
        u,v = input().split()
        u,v = int(u), int(v)
        g.addEdge(u,v)
    s = int(input())
    g.bfs(s,n)
