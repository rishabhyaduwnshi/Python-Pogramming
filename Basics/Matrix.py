#matrix - list of list

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,8,7],[6,5,4],[3,2,1]]

result = []

for i in range(len(matrix1)):
    dummy_list = []
    for j in range(len(matrix1[i])):
        dummy_list.append(matrix1[i][j] + matrix2[i][j])
    result.append(dummy_list)
    
print(result)
