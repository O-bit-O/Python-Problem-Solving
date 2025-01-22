import queue
priorityQueue=queue.PriorityQueue

def Dijkstra(Graph, source):
    a=len(Graph)
    if a!=0:
        dist[source]=0
        Q=priorityQueue()
        visited=([False]*(a+1))
        for i in Graph:
            if source is not i:
                dist[i]=float("inf")
                prev[i]=None
            Q.put((dist[i], i))
        while Q.empty() is False:
            u=Q.get()[1]
            if visited[u]:
                continue
            visited[u]=True
            for i in Graph[u]:
                alt=dist[u]+i[1]
                if alt<dist[i[0]]:
                    dist[i[0]]=alt
                    prev[i[0]]=u
                    Q.put((dist[i[0]], i[0]))
    return dist[a]


def Node(edge):
    d=dict()
    for i in edge:
        i=list(map(int, i.split()))
        try:
            d[i[0]].append(i[1], i[2])
        except:
            d[i[0]]=[(i[1], i[2])]
        try:
            d[i[1]].append((i[0], i[2]))
        except:
            d[i[1]]=[(i[0], i[2])]
    return d


fdata=open("input1.txt", "r")
file=fdata.read().split("\n")
output=open("output1.txt", "w")
i=0
j=1

while int(file[0]) > i:
    n=int(file[j].split()[1])
    Graph=Node(file[j+1:j+1+n])
    dist=[0]*(len(Graph)+1)
    prev=[None]*(len(Graph)+1)
    output.write(str(Dijkstra(Graph, 1))+"\n")
    i=i+1
    j=j+1+n