def print_matrix(matrix):
    for ligne in matrix:
        for val in ligne:
            print(f'{val} ', end='')
        print()
    print()

_ = 0

    mat_incidence_base = [
         #A  #B  #C  #D  #E  #F  #G
        [ _,  _,  _,  _,  _,  _,  _], #A
        [ _,  _,  _,  _,  _,  _,  _], #B
        [ _,  _,  _,  _,  _,  _,  _], #C
        [ _,  _,  _,  _,  _,  _,  _], #D
        [ _,  _,  _,  _,  _,  _,  _], #E
        [ _,  _,  _,  _,  _,  _,  _], #F
        [ _,  _,  _,  _,  _,  _,  _], #G
    ]

    # matrice de https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal
    mat_incidence = [
         #A  #B  #C  #D  #E  #F  #G
        [ _,  7,  _,  5,  _,  _,  _], #A
        [ 7,  _,  8,  9,  7,  _,  _], #B
        [ _,  8,  _,  _,  5,  _,  _], #C
        [ 5,  9,  _,  _, 15,  6,  _], #D
        [ _,  7,  5, 15,  _,  8,  9], #E
        [ _,  _,  _,  6,  8,  _, 11], #F
        [ _,  _,  _,  _,  9, 11,  _], #G
    ]