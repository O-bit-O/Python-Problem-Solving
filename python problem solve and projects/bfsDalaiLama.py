def bfs(visited,graph,nodes,end):
    q=[]
    visited[int(nodes)-1]=1
    q.append(nodes)
    counter=0

    while len(q):
        x=q.pop(0)   
      
        if int(x)==int(end):
            break
        for n in graph[int(x)]:
            if visited[int(n)-1]==0:
                visited[int(n)-1]=1
                q.append(n)
                counter+=1
    print(counter)




fdata = open('input4(DalaiLama).txt','r')
fdata = fdata.read().splitlines()
num_of_graphs=int(fdata[0])
data= fdata[1].split(" ")
k=0
for i in range(0,num_of_graphs):
    vertices=int(data[0])
    edges=int(data[1])
    graph=[[]]
    for j in range(2+k,2+k+edges):
        j=fdata[j]
        j=[int(x) for x in j.split(" ")]
        graph+=[j[0:]]
        k+=1
    k+=1
    
    visited=[0]*vertices
    bfs(visited,graph,'1',vertices)
    data=fdata[2+edges].split(" ")
    
        

