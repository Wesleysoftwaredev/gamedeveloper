t=("tin1",124,'A',9,"C2S", [120,"Semaine",1.2,'A'], 'A')
print(type(t))
l=[120,"Semaine",1.2,'A']


print(t,l)
print(t[4])
print(t[5][1])

#slicing
#slicing relates to acsessing multiple values
print(t[2:5])
print(t[1:])

#count the occurance of a value in a tuple
print(t.count("A"))
print(t.index("C2S"))

#packing and unpacking
address=(1, "Lang", "Sparta", 187341)
dno, stn, ctn, zpc=address
print(ctn)