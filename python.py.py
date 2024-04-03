#DFS
visited = set()
#set to keep track of visited nodes
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
   
graph={}
nodes = int(input("enter the number nof nodes:"))
for _ in range(nodes):
    node,*neighbours=input("enter node and its neighbour seperated by spaces(eg,ABC)").split()
    graph[node]=neighbours
#Driver code
start_node=input("enter the starting node for DFS traversal:")
goal_node=input("enter the goal node for DFS travesral:")
dfs(visited,graph,start_node)
if goal_node in visited:
    print("Goal found")
else:
    print("Goal not found")
