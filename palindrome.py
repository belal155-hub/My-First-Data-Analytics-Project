def isPalindrome(s):
    s = s.lower()

    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
text = input("Enter a word: ")
print(isPalindrome(text))