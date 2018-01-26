import sys

#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:

    def mindist(self, dist, visited):
        # This function takes the list of distance and
        # check all the vertices and find the min distance edge
        # and returns the index of the element with smallest edge
        mdist = sys.maxint
        mindex = -1
        for v in range(len(dist)):
            if ( (dist[v] <= mdist) and (visited[v] == False) ):
                mdist = dist[v]
                mindex = v
        return mindex


    def Dijkstra_alg(self, n, e, mat, s):
         #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return a two dimensional array as output (Please see testcase file)

         # Initialize a adjacency graph with n x n elements
         graph = [[0 for x in range(n)] for x in range(n)]
         visited = [False]*n
         usp = [1]*n
         cost_usp = [[0 for x in range(2)] for y in range(n)]
         src = 0
         src = s

         # Assign the edge (u,v) weight to the
         # corresponding G(u,v) position in the graph
         # Since this is an undirected graph G(u,v) = G(v,u)
         m = 0
         p = 0
         for i in range(e):
             m = mat[i][0]
             p = mat[i][1]
             graph[m-1][p-1] = mat[i][2]
             graph[p-1][m-1] = mat[i][2]
         #print(graph)

         # List to save the shortest path distance from source to a vertex
         dist = [sys.maxint] * n
         dist[src-1] = 0

         # RUnning for (n-1) vertices
         for x in range(n-1):
             print "x=",x
             # pop the vertex with the smallest weight edge
             u = self.mindist(dist, visited)
             print "Returned index, u =", u
             visited[u] = True

             # Test for all vertex in graph
             # That are not yet visisted by the Algorithm
             # And whose shortest path distance is more than the new path dist
             for v in range(n):
                 if (graph[u][v] != 0 and visited[v] == False and
                     (dist[v] > dist[u] + graph[u][v])):
                     print "Update the distance for v:", v
                     dist[v] = dist[u] + graph[u][v]
                     usp[v] = usp[u]
                 elif (graph[u][v] != 0 and visited[v] == False and
                     (dist[v] == dist[u] + graph[u][v])):
                     usp[v] = 0
         #print dist
         #print usp
         # Format the output array from the two lists returned by the functions
         for i in range(n):
             cost_usp[i][0] = dist[i]
             cost_usp[i][1] = usp[i]
         print cost_usp
         return cost_usp
