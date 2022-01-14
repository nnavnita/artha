# flatten nested lists
def flatten(t):
    return [item for sublist in t for item in sublist]