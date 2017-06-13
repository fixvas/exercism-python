import string


def is_pangram(sentence):
    s = sentence.lower()
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    return True
