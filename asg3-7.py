
def make_acronym(phrase):
    words = phrase.split()
    acronym = ""

    for word in words:
        acronym += word[0].upper()

    return acronym
print(make_acronym("unidentified foreign object"))

