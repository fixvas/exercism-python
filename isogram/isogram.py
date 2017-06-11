def is_isogram(word):
    word_lowercase = word.lower()
    d = {} 
    for letter in word_lowercase:
        if letter.isalpha():
            if letter in d:
                return False
            else:
                d[letter] = 1
    return True
