M = []
M1 = []
#print("input number of strings")
#l = int(input())
#print("input number of columns")
#am = int(input())
#print("input all numbers")
#for i in range(l):
#    M.append([])
#    for k in range(am):
#        M[i].append(int(input()))

#создаем массив, из которого осуществляется выборка
M = [[1, 2, 3, 4, 5, 6, 7, 8],       
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40]]
n = 2
for b in range(0, len(M), n):
    M1.append([])
    for i in range(0, len(M[b]), n):
        M1[int(b/2)].append(int(M[b][i])) #записываем нужные данные в М1

for b in range(len(M1)):
    for i in range(len(M1[b])):
        print(M1[b][i])
