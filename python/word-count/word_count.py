import re
from collections import Counter
def word_count(phrase):
    # pattern match =,eg:can't,a,good,1,23
    pattern = re.compile(r"[a-zA-Z]+'[a-zA-Z]|[a-zA-Z0-9]+")
    words = re.findall(pattern,phrase.lower())
    return dict(Counter(words))
