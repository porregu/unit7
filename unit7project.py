# Guillermo Porres 11/14/2019
#this program let the user choose how many time they want to shift the alphabet in order to get a "code" then the program will show the code word. finally the progra will uncode the word and show the uncode word another time.

def main():
    one = "abcdefghijklmnopqrstuvwxyz"#regular alphabet
    user_shift = int(input("how many times you wanna shift the alphabet "))#will askt he suer how many times want to shift the alphabet
    third = one[0:user_shift]
    rest = one[user_shift:]
    second_alphabet = rest + third#creat a second alphabet with the shifht in the end of the alphabet without repeting any words
    user_word = input("which word you wanna put?")# ask the user what word they want to code
    word_no_space = []
    for x in user_word:#thi loop will tell the code work letter by letter
        user_code = one.index(x)
        user_word_code = second_alphabet[user_code]
        word_no_space.append(user_word_code)
    print("this is your code shhhh " , "".join(word_no_space))
    uncode_word = []
    for x in word_no_space:# this loop will uncode the word letter by letter
        user_9code = second_alphabet.index(x)
        user_word_uncode = one[user_9code]
        uncode_word.append(user_word_uncode)
    print("this is your uncode shhhh", "".join(uncode_word))


main()