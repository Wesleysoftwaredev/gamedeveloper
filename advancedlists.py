"""AT1 = ["Cobra Kai", "Stranger Things", 1]
print(AT1[1])=
for i in AT1:
    print(i)"""
    
#creating a 2d list

MAT1 = [[1,2,3,11],[4,5,6,12],[7,8,9,13]]
#number of rows
print(len(MAT1))
#number of collums
print(len(MAT1[0]))
#acsessing internal values
print(MAT1[0][3])
print(MAT1[0][0])
print(MAT1[1][0])

for i in MAT1[0]:
    print(i)

for i in range(len(MAT1)):
    for j in range(len(MAT1[0])):
        print(MAT1[i][j],end=" ")
    print()