from utils import constants, global_func

class Alpha:
    """Defines a representation for an alphabet"""
    
    def __init__(self, alpha):
        self.alpha = alpha
        self.kind = self.idKind(alpha)

    # identifies the alphabet kind
    def idKind(self, alpha):
        if alpha == constants.ANUSVARA:
            return 'anusvara'
        elif alpha == constants.VISARGA:
            return 'visarga'
        else: # consonant
            return 'consonant'
    
    # pp the alphabet's details 
    def display(self):
        print('Alphabet: {}\nKind: {}\n'.format(self.alpha, self.kind))