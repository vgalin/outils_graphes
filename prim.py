from graph import Graphe


def prim(graphe: Graphe, sommet_depart):

    cout = [float('infinity') for t in graphe]
    pred = [None for t in graphe]

    cout[sommet_depart] = 0

    F = sorted(graphe.liens(),key=lambda item: item[2]) 
    
    while len(F) != 0:
        t = F.pop()
        F_current = [arete for arete in F if t in arete]

        # for u in F_current:
        #     if cout[u]

        print(f'{t=}')
        # print(f'{F=}')
        # print(f'{F_current=}')
        
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
    
    graphe = Graphe(matrice_indicence=matrice)
    prim(graphe, 0)