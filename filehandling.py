"""with open("Story.TxT", "w") as file:
    file.write("Once upon a time, there was a boy called David, he killed Goliath and the might king of the jungle, the lion.")



with open("Story.TxT", "a") as file:
   file.write("Once upon a time, there was a boy called David, he killed Goliath and the might king of the jungle, the lion. Not only this but he was nighted by King Kolaph, now this was the biggest feat David had achieved in his life.")



with open("Story.TxT", "a") as file:
    file.write("Mary, once upon a time, had a little lamb and it got killed by 10 wolves.")


with open("Story.TxT", "r") as file:
  print (file.read())"""


doc = '"C:\\Users\\vivio\\OneDrive\\Documents\\CV VIVIAN (CV).docx"'
with open(doc,"r") as file:
    print (file.read(10))