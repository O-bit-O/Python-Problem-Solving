def bfs(visited,graph,nodes,end):
    q=[]
    visited[int(nodes)-1]=1
    q.append(nodes)
    file=open("output_bfs.txt",'w')
    file.write("Places: ")

    while len(q):
        x=q.pop(0)
        file.write(str(x)+" ")
        if int(x)==int(end):
            break
        for n in graph[int(x)]:
            if visited[int(n)-1]==0:
                visited[int(n)-1]=1
                q.append(n)


with open("input1.txt") as data:
    nodes=int(data.readline())
    graph=[[]]
    for edges in data:
        edges=[int(x) for x in edges.split("  ")]
        graph+=[edges[0:]]

visited=[0]*nodes
bfs(visited,graph,'1','12')

