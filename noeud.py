class Noeud:
    def __init__(self, n):
        self.nom = n
        self.enfants = None

    def ajouter_enfant(self, noeud):
        self.enfants = noeud

    def afficher(self):
        if self.enfants != None:
            print(f"{self.nom}({self.enfants.afficher()})")
        else: print(self.nom)
