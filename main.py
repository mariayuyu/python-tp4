from noeud import Noeud
from arbre import Arbre

n = Noeud("mul")
n1 = Noeud("3")
n2 = Noeud("x")
n.ajouter_enfant(n1)
n.ajouter_enfant(n2)
n.afficher()

a = Arbre(n)
a.afficher()