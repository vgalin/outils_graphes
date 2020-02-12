class Graphe():
    def __init__(self, matrice_indicence=None):
        self._noeuds = {} #sommets

        if matrice_indicence is not None:

            for i in range(len(matrice_indicence[0])):
                self.ajout_noeud(Graphe.to_letter(i))

            for i, ligne in enumerate(matrice_indicence):
                for j, val in enumerate(ligne):
                    if val != 0:
                        self.ajout_lien(
                            depart=Graphe.to_letter(j),
                            destination=Graphe.to_letter(i),
                            distance=val
                        )

    def liens(self, trier=False):
        liens = []
        for depart in self._noeuds:
            for arrivee in self._noeuds[depart]:
                liens.append([depart, arrivee, self._noeuds[depart][arrivee]])

        if trier:
            #trie dans l'ordre croissant en fonction de la valeur du lien/arête
            liens = sorted(liens,key=lambda item: item[2]) 

        return liens

    @staticmethod           
    def to_letter(num):
        return chr(num + 65)

    def __contains__(self, noeud):
        return noeud in self._noeuds

    def __len__(self):
        return len(self._noeuds)

    def __iter__(self):
        return self._noeuds.__iter__()

    def __repr__(self):
        return str(self._noeuds)

    def ajout_noeud(self, noeud):
        if noeud in self:
            raise Exception("Noeud déjà existant")

        #print(f"ajout du noeud {noeud}")
        self._noeuds[noeud] = {}

    def ajout_lien(self, depart, destination, distance, bidirectionnel=False):
        if depart not in self:
            raise Exception(f"Le noeud de départ ({depart}) spécifié n'existe pas")
        if destination not in self:
            raise Exception(f"Le noeud de départ ({destination}) spécifié n'existe pas")

        self._noeuds[depart][destination] = distance

        if bidirectionnel:
            self._noeuds[destination][depart] = distance

if __name__ == '__main__':
    pass
