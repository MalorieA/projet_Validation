class Graph:
    def __init__(self):
        self.graph=dict()   #Dictionnaire pour les relations entre les noeuds
        self.roots=[]       #Liste des noeuds racines

    def roots(self):
        return self.roots   #Méthode pour retourner une liste des racines noeuds du graph