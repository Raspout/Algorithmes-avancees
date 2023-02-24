# exo 2
# 1. Implémentez une classe ListeChainee sans utiliser les listes de Python : vous devez donc d’abord
# écrire une classe Noeud, puis utiliser cette classe pour votre ListeChainee.

class Node:
        def __init__(self, value):
                self.value = value
                self.next = None

        def __repr__(self):
                if self.suivant == None :
                        return f"{self.valeur} -> None"
                else:
                        return f"{self.valeur} -> {str(self.suivant)}"

class ListC:
        def __init__(self):
                self.head = None
                self.taille = 0

# 2. Ajoutez les méthodes inserer(valeur, k), supprimer(k), rechercher(valeur), taille() et estVide().

        def insert(self, value):
                Node.value = value



#L=ListC()
#n1, n2 = Node(), Node()
#n1.next = n2
#n2.head = n1
chaine = ListC

print(chaine)
