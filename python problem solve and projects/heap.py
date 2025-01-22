import heapq
heap=heapq

def Network(Graph, source):
    a=len(Graph)
    dist[source]=0
    maxQ=list()
    visited=([False]*(a+1))
    prev[source]=0
    for v in Graph:
        if v!=source:
            dist[v]=float("-inf")
            prev[v]=None
        heap.heappush(maxQ, (dist[v], v))
        heap._heapify_max(maxQ)

    while len(maxQ)!=0:
        extract_max, u=heap._heappop_max(maxQ)
        if visited[u]:
            continue
        visited[u]=True
        for v in Graph[u]:
            if extract_max!=0:
                alt=min(extract_max, v[1])
            else:
                alt=v[1]
            if alt>dist[v[0]]:
                dist[v[0]]=alt
                prev[v[0]]=u
                heap.heappush(maxQ, (dist[v[0]], v[0]))
                heap._heapify_max(maxQ)
    return dist[1::1]

def Node(edge):
    d=dict()
    for i in edge:
        i = list(map(int, i.split()))
        try:
            d[i[0]].append((i[1], i[2]))
        except:
            d[i[0]]=[(i[1], i[2])]
        try:
            d[i[1]]
        except:
            d[i[1]]=list()
    return d

fdata=open("input5.txt", "r")
file=fdata.read().split("\n")
output=open("output5.txt", "w")
i = 0
j = 1


while int(file[0])>i:
    n=int(file[j].split()[1])
    if n==0:
        Graph={int(file[j].split()[0]):list()}
    else:
        Graph=Node(file[j+1:j+1+n])
    dist=[float("-inf")]*(len(Graph)+1)
    prev=[None]*(len(Graph)+1)
    for i in Network(Graph, int(file[j+1+n])):
        if i==float("-inf"):
            i=- 1
        output.write(str(i) + " ")
    output.write("\n")
    i=i+1
    j=j+2+n
