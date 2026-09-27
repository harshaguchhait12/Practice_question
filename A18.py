# Count Words
def count_words(text):
    count = 1

    for ch in text:
        if ch == " ":
            count = count + 1

    return count

print(count_words("he is a nice guy"))