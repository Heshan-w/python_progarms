# to store the vowels
vowels_list = []
# to store the consonants
consonants_list = []
string = input("please enter a word : ").strip()

# iterate throught each character in the string entered
for char in string:
    # to see if that character is a vowel and if so add it to the vowels list
    if char.lower() in ("a", "e", "i", "o", "u"):
        vowels_list.append(char)
    # to check if the character is neither a vowel or a consonant
    elif not char.isalpha():
        continue
    # to see if that character is a consonant and if so add it to the consonants list
    else:
        consonants_list.append(char)
print(f"list of vowels : {vowels_list}")
print(f"list of consonants : {consonants_list}")

