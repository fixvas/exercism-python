from string import ascii_lowercase, ascii_uppercase


def rotate(phrase, key):
    coded_phrase = []
    for char in phrase:
        if char.islower():
            shift = (ascii_lowercase.index(char) + key)
            code = shift % 26 if shift < 25 else (shift - 26) % 26
            coded_phrase.append(ascii_lowercase[code])
        elif char.isupper():
            shift = (ascii_uppercase.index(char) + key)
            code = shift % 26 if shift < 25 else (shift - 26) % 26
            coded_phrase.append(ascii_uppercase[code])
        else:
            coded_phrase.append(char)
    return ''.join(coded_phrase)