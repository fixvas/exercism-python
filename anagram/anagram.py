def detect_anagrams(word, candidates):
    anagram = []
    word = list(word.lower())
    for item in candidates:
        symb = list(item.lower())
        if symb != word and sorted(symb) == sorted(word):
                anagram.append(item)
    return anagram
