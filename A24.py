# Find Last Character

def last_character(text):
    print(text[-1])

last_character("kokiyt")


#Approach 2 — Loop

def last_character(text):
    last = ""

    for ch in text:
        last = ch

    print(last)

last_character("Python")