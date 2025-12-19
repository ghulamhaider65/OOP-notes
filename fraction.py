class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d
        
        
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    

    