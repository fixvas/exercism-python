def is_isogram(word):
    word_lowercase = word.lower()
    for letter in word_lowercase:
        if letter.isalpha() and word_lowercase.count(letter) > 1:
            return False
    return True
