#Remove Vowels
def remove_vowels(text):
    result = ""

    for ch in text:
        if ch not in "aeiouAEIOU":
            result = result + ch

    return result

print(remove_vowels("sdfghjkuytfdcvbn"))