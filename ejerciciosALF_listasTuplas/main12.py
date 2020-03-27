'''
Created on 26 mar. 2020

@author: Sidney
Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto. 
        1 2 3
A = (   4 5 6 )
      −1 0
B =(   0 1
       1 1 )

'''
A = ((1,2,3),(4,5,6))
B = ((-1,0),(0,1),(1,1))

C = [[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
            
print(C)