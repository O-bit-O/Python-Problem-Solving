def Multiply_matrix(A,B):
    n = int(len(A))
    C = [ [ 0 for i in range(n) ] for j in range(n) ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] +  A[i][k] * B[k][j]
    return C

A = []
B = []

with open('LAb1input4.txt', 'r') as f:
    A = [[int(num.split('\n')[0]) for num in line.split(" ")] for line in f]
with open('LAb1input4.txt', 'r') as f:
    B = [[int(num.split('\n')[0]) for num in line.split(" ")] for line in f]

out = open('output4.txt', 'w')
p = Multiply_matrix(A,B)

for i in range(len(p)):
    for j in range(len(p)):
        out.write(str(p[i][j])+" ")
    out.write(str('\n'))


