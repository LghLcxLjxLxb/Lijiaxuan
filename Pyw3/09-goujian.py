# 对于数组A【0-n-1】，构建一个数组B，其中B【i】=A[0]*A[1]*...A[i-1]*A[i+1]*A[n-1]
n = int(input('请输入数组规模：'))
A = [0]*n
B = [1]*n
A = [int(x) for x in input('输入一串数字：').split()]
print(A)
for i in range(n):
    for j in A[0:i]:
        B[i] *= j
    for j in A[i+1:n]:
        B[i] *= j
print(B)
