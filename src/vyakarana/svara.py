# flatten nested lists
def flatten(t):
    return [item for sublist in t for item in sublist]

class Svara:
    """Defines a representation for a svara"""
    
    def __init__(self, svara):
        self.svara = svara
        self.kind = self.idKind(svara)
        self.breakdown = self.decompose(svara, self.kind)

    # identifies the svara kind
    def idKind(self, svara):
        if svara in ['a', 'i', 'u']:
            return 'basic'
        elif svara in ['A', 'I', 'U']:
            return 'long'
        elif svara in ['e', 'ai', 'o', 'au']:
            return 'compound'
        else: # Invalid svara
            return None

    # provides a breakdown ("decomposition") of the svara based on its kind
    def decompose(self, svara, kind):
        if kind == 'long': # A, I, U
            return [svara.lower()]*2
        elif kind == 'compound':
            if svara == 'e':
                return ['a','i']
            elif svara == 'ai':
                return flatten([self.decompose('e', 'compound')])
            elif svara == 'o':
                return ['a', 'u']
            else: # au
                return flatten(['a', self.decompose('o', 'compound')])
        elif kind == 'basic': # a, i, u
            return [svara]
        else: # Invalid svara
            return None
    
    # pp the svara's details 
    def display(self):
        print('Svara: {}\nKind: {}\nBreakdown: {}\n'.format(self.svara, self.kind, self.breakdown))