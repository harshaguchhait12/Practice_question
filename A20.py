#Remove Spaces

def remove_spaces(text):
    result = ""

    for ch in text:
        if ch != " ":
            result = result + ch

    return result

print(remove_spaces("bengali Language is good"))