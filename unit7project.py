one= "abcdefghijklmnpqrstuvwxyz"
user_shift= int(input("how many times you wanna shift the alphabet "))
second=one[0:user_shift]
rest=one[user_shift:]
second_alphabet=rest+second
user_word=input("which word you wanna put?")
word_no_space=[]
for x in user_word:
    user_code=one.index(x)
    user_word_code=second_alphabet[user_code]
    word_no_space.append(user_word_code)
print("this is your code shhhh","".join(word_no_space))
uncode_word=[]
for x in word_no_space:
    user_9code=second_alphabet.index(x)
    user_word_uncode=one[user_9code]
    uncode_word.append(user_word_uncode)
print("this is your uncode shhhh, dont let the teacher know ", "".join(uncode_word))