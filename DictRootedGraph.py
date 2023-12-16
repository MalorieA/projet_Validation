from RootedGraph import RootedGraph
class DictRootedGraph(RootedGraph): # DictRootedGraph est un Class dérivée qui hérité de RootedGraph
    def __init(self):
        super().__init__()  # Appeler le constructeur de la classe de base en utilisant super

    def roots(self):
        super().roots()     # Appeller la même méthode roots de la classe de base

    def neighbors(self,node):
        super().neighbors()     # Appeller la même méthode neighbors de la classe de base

    def add_new_one(self,u,v):
        self.graph.setdefault(u,[]).append(v)     # Ajoute une arête entre u et v dans le graphe
                                                  # Vérifie si u n'existe pas on l'initialise avec une liste vide avant d'ajouter v


