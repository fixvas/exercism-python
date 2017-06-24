def detect_anagrams(word, candidates):
    anagram = []
    word = list(word.lower())
    word_sorted = sorted(word)
    for item in candidates:
        symb = list(item.lower())
        if symb != word and sorted(symb) == word_sorted:
                anagram.append(item)
    return anagram
