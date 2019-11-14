word = [4,5,6,3,2,1,4,5]
while word:
        for x in range(len(word)-1):
            if word[x+1]<word[x]:
                temp=word[x]
                word[x]=word[x+1]
                word[x+1]=temp
print(word)