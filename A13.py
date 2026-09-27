# Count Consonants
def count_consonants(text):
    count = 0

    for ch in text:
        if ch.isalpha() and ch not in "aeiouAEIOU":
            count = count + 1

    return count

print(count_consonants("sdtyuifghjk"))