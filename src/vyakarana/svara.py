from utils import constants, global_func

class Svara:
    """Defines a representation for a svara"""
    
    def __init__(self, svara):
        self.svara = svara
        self.kind = self.idKind(svara)
        self.breakdown = self.decompose(svara, self.kind)

    # identifies the svara kind
    def idKind(self, svara):
        if svara in constants.HRASVA_SVARA:
            return 'hrasva'
        elif svara in constants.DIRGHA_SVARA:
            return 'dirgha'
        elif svara in constants.COMPOUND_SVARA:
            return 'compound'
        else: # Invalid svara
            return None

    # provides a breakdown ("decomposition") of the svara based on its kind
    def decompose(self, svara, kind):
        if kind == 'dirgha': # A, I, U
            return [svara.lower()]*2
        elif kind == 'compound':
            if svara == 'e':
                return ['a','i']
            elif svara == 'ai':
                return global_func.flatten([self.decompose('e', 'compound')])
            elif svara == 'o':
                return ['a', 'u']
            else: # au
                return global_func.flatten(['a', self.decompose('o', 'compound')])
        elif kind == 'hrasva': # a, i, u
            return [svara]
        else: # Invalid svara
            return None
    
    # pp the svara's details 
    def display(self):
        print('Svara: {}\nKind: {}\nBreakdown: {}\n'.format(self.svara, self.kind, self.breakdown))