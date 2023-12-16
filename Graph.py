class RootedGraph:
    def __init__(self):
        self.graph=dict()   #Dictionnaire pour les relations entre les noeuds
        self.roots=[]       #Liste des noeuds racines

    def roots(self):
        return self.roots   #Méthode pour retourner une liste des racines noeuds du graph

    def neighbors(self,node):
        return self.graph.get(node,[])  #Méthode pour obtenir une liste des noeuds voisins d'une noeud spécifiée
                                        #Si le noeud n'existe pas ,il retourne une liste vide