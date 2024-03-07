from typing import List
import queue
class Solution:
    
    def __init__(self):
        self.visited = None

    def build_graph(self,n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])      
        return g
    
    def bfs(self,g : List[List[int]], starting_node: int) -> int:
        q = queue.Queue()
        q.put(starting_node)
        self.visited[starting_node] = True
        while not q.empty():
            node = q.get()
            nbrs = g[node]
            for nbr in nbrs:
                if self.visited[nbr] == False:
                    self.visited[nbr] = True
                    q.put(nbr)


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = [False] * n
        g = self.build_graph(n,edges)
        count = 0
        for i in range(n):
            if (self.visited[i] == False):
                count +=1
                self.bfs(g,i)
        return count
    

my_instance = Solution()
n = 5
edges = [[0,1],[1,2],[3,4]]
c = my_instance.countComponents(5,edges)
print (c)
