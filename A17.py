# Cheak Palindrome
def check_palindrome(text):
    reverse = text[::-1]

    if text == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome("madam")