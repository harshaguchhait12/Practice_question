# Frequency of a Character

def character_frequency(text, ch):
    count = 0

    for x in text:
        if x == ch:
            count = count + 1

    return count

print(character_frequency("programming", "g"))