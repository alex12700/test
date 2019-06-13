def Deikstra(N, S, matrix, end):
    valid = [True]*N        
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight[end]

f = list(map(int, input().split()))


matrix = []
for _ in range(f[0]):
    temp = (list(map(int, input().split())))
    for i in range(len(temp)):
        temp2 = temp[i]
        if (temp2 < 0): 
            temp[i] = 10000000
    matrix.append(temp)


print(matrix)

print(Deikstra(f[0], f[2] - 1,matrix))