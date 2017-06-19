import re


def hey(phrase):
    phrase = phrase.strip()
    if re.search(r'[A-Z]{4}', phrase) or re.search(r'[A-Z]{2}!$', phrase):
        return "Whoa, chill out!"
    elif re.search(r'[?]$', phrase) and not re.search(r'[A-Z]{4}', phrase):
        return "Sure."
    elif phrase == "":
        return "Fine. Be that way!"
    return "Whatever."