from RootedGraph import RootedGraph
class DictRootedGraph(RootedGraph): # DictRootedGraph est un Class dérivée qui hérité de RootedGraph
    def __init(self):
        super().__init__()  # Appeler le constructeur de la classe de base en utilisant super

    def roots(self):
        super().roots()     # Appeller la même méthode roots de la classe de base

    def neighbors(self,node):
        super().neighbors()     # Appeller la même méthode neighbors de la classe de base