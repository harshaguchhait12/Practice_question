# Count vowels and Consonants
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        elif ch.isalpha():
            consonants = consonants + 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

count_vowels_consonants("trvbniuyhjnk")