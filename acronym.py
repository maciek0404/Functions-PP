def f(name):
    words = name.split()
    return ''.join(word[0] for word in words)