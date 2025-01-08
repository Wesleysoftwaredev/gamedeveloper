"""dict1 = {"burger" : "beef",
         "turkey" : "chicken",
         "chips"  : "potato",
         "fried rice" : "prawn"}
#acsessing a value
print (dict1["burger"])
print (dict1.keys())
print (dict1.values())
print (dict1.items())

#Deleting a key value
del(dict1["turkey"])
print (dict1)

#change the value of a key
dict1["fried rice"]="meat"
print (dict1)"""

"""#nested dictionary
stud1 = {"Neveah" : {"age" : 13, "marks" : [20,40,60,80,100]}, 
        "Aisha" : {"age" : 14, "marks" : [30,60,90,95,100]}}
print (stud1["Neveah"]["age"])
print (stud1["Neveah"]["marks"][2])
total = 0
for i in (stud1["Neveah"]["marks"]):
    total = total + i
average = total/5
print ("average of neveah is", average)"""


dict2 = {"Spain" : "Barcelona",
        "England" : "London",
        "Morroco" : "Rabat",
        "Argetina" : "Buenous Aires"}
while True:
    print ("What would you like to do\n1. View Dictionary\n2. Add a Country and Capital \n3. Print the Capital of a Country \n4. Delete a Country\n5. Exit")
    cond1 = input("Enter your choice:")
    if cond1=="1":
        print (dict2)
    elif cond1=="2":
        country = input("Enter the name of the country:")
        capital = input("Enter the name of the capital:")
        dict2[country] = capital
    elif cond1=="3":
        namcon = input("Enter the name of the country")
        print (dict2.get(namcon, "Does not exist"))

    elif cond1=="4":
        country = input("Which country do you want to be deleted?")
        if country in dict2.keys():
            del country
        else:
            print ("It does not exist")

        
    elif cond1=="5":
        break