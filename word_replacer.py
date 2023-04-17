sentence = 'hi im hungry, hi hi hi hi'
print(f"before replacement : {sentence}")

def word_replacer():
    word_to_replace = input("enter word to replace : ")
    word_replacement = input("enter word replacement : ")
    # optionally we can add a 3rd parameter to the replace function, which is a number indicating the number of 
    # times you'd want the word to be replaced to infact be replaced... eg. "sentence.replace(word_to_replace, word_replacement, 2)"
    # this will replace the first two times the word_to_replace occurs with the word_replacemet in the sentence string
    print(f"after replacement {sentence.replace(word_to_replace, word_replacement)}")


word_replacer()
