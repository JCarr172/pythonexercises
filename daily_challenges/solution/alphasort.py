def alphasort(string):
    if ' ' in string:
        words = string.lower().split(' ')
        words = list(set(words))
        words = sorted(words)
        return ' '.join(words)
    else:
        return []
    