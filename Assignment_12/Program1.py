# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
#Input: a
#Output: Vowel

def is_vowel_or_consonant(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

def main():
    char = input("Enter a character: ")
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
    else:
        result = is_vowel_or_consonant(char)
        print(result)

if __name__ == "__main__":
    main()