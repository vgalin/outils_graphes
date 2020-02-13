from graph import Graphe


def dijkstra(graphe: Graphe, depart):

    Q = [sommet for sommet in graphe]
    Q2 = graphe.liens(trier=True)[::-1]

    dist = [float('infinity')] * len(Q)
    prev = [None] * len(Q)

    dist[depart] = 0

    while Q2: #tant que Q n'est pas vide
        u = Q2.pop(0)
        voisins_de_u = [u[1]] + [arete[1] for arete in Q2 if arete[0] == u[0]]

        for v in voisins_de_u:
            alt = dist[ord(u[0]) - 65] + graphe.distance(u[0], v)
            if alt < dist[ord(v) - 65]:
                dist[ord(v) - 65] = alt
                prev[ord(v) - 65] = u[0]

    print(f'{dist=}')
    print(f'{prev=}')
    return None



    # dist = []
    # prev = []

    # for v in graphe:
    #     dist[]

if __name__ == '__main__':
    _ = 0

    matrice = [
        #A  #B  #C  #D  #E  #F  #G
        [ _,  7,  _,  5,  _,  _,  _], #A
        [ 7,  _,  8,  9,  7,  _,  _], #B
        [ _,  8,  _,  _,  5,  _,  _], #C
        [ 5,  9,  _,  _, 15,  6,  _], #D
        [ _,  7,  5, 15,  _,  8,  9], #E
        [ _,  _,  _,  6,  8,  _, 11], #F
        [ _,  _,  _,  _,  9, 11,  _], #G
    ]

    matrice_ex6 = [
         #A  #B  #C  #D  #E  #F
        [ _,  3, 10,  _,  _,  _], #A
        [ _,  _, 11, 12,  _,  _], #B
        [ _,  _,  _,  5,  _,  _], #C
        [ _,  _,  _,  _,  2,  8], #D
        [ _,  4,  _,  _,  _,  _], #E
        [ _,  _,  _,  _,  6,  _], #F
    ]

    # matrice_ex1 = [
    #      #A  #B  #C  #D  #E
    #     [ _,  5,  4,  5,  8], #A
    #     [ 5,  _,  2,  3,  4], #B
    #     [ 4,  2,  _,  3,  5], #C
    #     [ 5,  3,  3,  _,  2], #D
    #     [ 8,  4,  5,  2,  _], #E
    # ]
    
    graphe = Graphe(matrice_indicence=matrice_ex6)

    dijkstra(graphe, 0)
    dijkstra(graphe, 2)