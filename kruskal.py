from graph import Graphe
from disjoint_set import DisjointSet


def kruskal(graphe: Graphe):
    retour = []

    sommets = [sommet for sommet in graphe]

    aretes = graphe.liens(trier=True)

    ds = DisjointSet(sommets)

    for arete in aretes:
        if ds.find(arete[0]) != ds.find(arete[1]):
            retour.append(f'{arete[0]}-{arete[1]}')
            ds.union(arete[0], arete[1])

    return retour

if __name__ == '__main__':

    _ = 0

    # Matrice d'incidence correspondant au graphe donné sur la page
    # https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal

    mat_incid_wiki = [
            #A  #B  #C  #D  #E  #F  #G
            [ _,  7,  _,  5,  _,  _,  _], #A
            [ 7,  _,  8,  9,  7,  _,  _], #B
            [ _,  8,  _,  _,  5,  _,  _], #C
            [ 5,  9,  _,  _, 15,  6,  _], #D
            [ _,  7,  5, 15,  _,  8,  9], #E
            [ _,  _,  _,  6,  8,  _, 11], #F
            [ _,  _,  _,  _,  9, 11,  _], #G
        ]
    
    graphe_wiki = Graphe(matrice_indicence=mat_incid_wiki)
    print('Solution :', kruskal(graphe_wiki))