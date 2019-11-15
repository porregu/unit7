word = ["guillermo", "xander", "kwame", "scout", "allison", "liana", "ariana"]
switched=True
while switched:
    switched=False
    for x in range(len(word)-1):
        if word[x+1]<word[x]:
            switched=True
            temp=word[x]
            word[x]=word[x+1]
            word[x+1]=temp
print(word)