user= "what is the word you want to put"
word=user.split(" ")
blank_list=[]
for x in word:
    blank_list.append(x.capitalize())
print(" ". join(blank_list))

