class Date():
    def __init__(self,j,m,a):
        self.jour = j
        self.mois = m
        self.annee = a
    def __repr__(self):
        return f"{self.jour}/{self.mois}/{self.annee}"    
        