from string import ascii_lowercase, ascii_uppercase


def rotate(phrase, key):
    coded_phrase = []
    for char in phrase:
        if char.islower():
            x = ascii_lowercase.index(char)
            y = (x + key)
            if y > 25:
                y -= 26
            y = y % 26
            coded_phrase.append(ascii_lowercase[y])
        elif char.isupper():
            x = ascii_uppercase.index(char)
            y = (x + key)
            if y > 26:
                y -= 26
            y = y % 26
            coded_phrase.append(ascii_uppercase[y])
        else:
            coded_phrase.append(char)
    return ''.join(coded_phrase)