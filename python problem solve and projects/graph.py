with open("input1.txt") as data:
    nodes=int(data.readline())
    graph=[[]]
    for edges in data:
        edges=[int(x) for x in edges.split("  ")]
        graph+=[edges[0:]]


print(graph)
data.close()