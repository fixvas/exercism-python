def abbreviate(phrase):
    phrase = phrase.replace('-', ' ')
    acronym = ''
    for word in phrase.split():
        acronym += word[0].upper()
    return acronym
