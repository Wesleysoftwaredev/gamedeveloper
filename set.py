s1 = {1,2,4,6,1,3}

print(type(s1))
s1.add(10)
s1.remove(1)
print(s1)

#set operations

a1 = {1,2,3,4,5}
b1 = {4,5,6,7,8}

#union

print(a1.union(b1))

#intersection

print(a1.intersection(b1))

#difference

print(a1.difference(b1))

#symmetric difference

print(a1.symmetric_difference(b1))