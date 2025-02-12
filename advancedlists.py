"""AT1 = ["Cobra Kai", "Stranger Things", 1]
print(AT1[1])=
for i in AT1:
    print(i)"""
    
#creating a 2d list

"""MAT1 = [[1,2,3,11],[4,5,6,12],[7,8,9,13]]
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
    print()"""

#markssegragation

L1 = []
L2 = []
L3 = []
for i in range(20):
    mark2 = int(input("Please enter your test mark:"))
    if mark2<=30:
        L1.append(mark2)
    elif mark2>30 and mark2<=69:
        L2.append(mark2)
    elif mark2>=70:
        L3.append(mark2)
Matrix = [L1,L2,L3]
print(Matrix)