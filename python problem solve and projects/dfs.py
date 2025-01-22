def dfs_visit(graph,node):
    visited[int(node)]=1
    p.append(node)
    for i in graph[node]:
        if visited[i]==0:
            dfs_visit(graph,i)


def dfs(graph,end):
    file=open("output_dfs.txt",'w')
    file.write("Places: ")
    for i in range(1,int(end)+1):
        if visited[i]==0:
            dfs_visit(graph,i)
    
    for i in range(0,len(p)):
        if str(p[i])==end:
            file.write(str(p[i])+" ")
            break
        else:
            file.write(str(p[i])+" ")

with open("input1.txt") as data:
    nodes=int(data.readline())
    graph=[[]]
    for edges in data:
        edges=[int(x) for x in edges.split("  ")]
        graph+=[edges[0:]]

visited=[0]*(nodes+1)
p=[]
dfs(graph,'12')



