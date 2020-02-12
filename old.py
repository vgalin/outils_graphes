import json
# class Tree:
#     def __init__(self, value, branches=None):
#         self.value = value
#         self.branches = []
#         self.branches.append(branches)

#     @property
#     def leaves_values(self):
#         # if self.branches[0] is None:
#         #     return self.value
#         # else:
#         #     return dest.leaves_values for dest in self.branches if dest is not None]
        

        
        

#     def add_branch(self, branch): #branch: Tree
#         if self.branches[0] is None :
#             self.branches[0] = branch
#         else :
#             self.branches.append(branch)
    
#     def __str__(self):
#         return self.representation()

#     def representation(self, level=0):       
#         ret = "\t"*level+repr(self.value) + "\n"
#         for branch in self.branches:
#             if branch is not None:
#                 ret += branch.representation(level + 1)
#         return ret

# class Forest:
    
#     def __init__(self, tree: Tree):
#         self.trees = [tree]

#     def add(self, tree: Tree):
#         for tree in self.trees:
#             pass


#     @property
#     def feuilles():
#         pass

class TreeForest:

    def __init__(self):
        self.forest = {}

    def __add__(self, tree):
        ret = self.forest
        ret[tree] = None
        return ret

    def plant(self, key, value):
        if ord(key) > ord(value):
            key, value = value, key

        added = self._plant(self.forest, key)

        if not added:
            print('not added')
            self.forest[key] = {value: None}

    def _plant(self, obj, key):
        if key in obj: return obj[key]
        for k, v in obj.items():
            if isinstance(v,dict):
                item = _plant(v, key)
                if item is not None:
                    return item


    def __str__(self):
        return json.dumps(self.forest, sort_keys=True, indent=4, separators=(',', ': '))

def to_letter(num):
    return chr(num + 65)

def get_coords(searched, matrix):

    taille = len(matrix[0])
    found = []

    for i in range(0, taille):
        for j in range(i, taille):
            if matrix[i][j] == searched:
                found.append((i, j)) # append tuple

    return found

def is_not_empty(matrix):

    taille = len(matrix[0])

    for i in range(0, taille):
        for j in range(i, taille):
            if matrix[i][j] != 0:
                return True

    return False


def kruskal(matrix):

    taille = len(matrix[0])
    forest = TreeForest()

    while is_not_empty(matrix):

        min = 99_999
        max = -1

        

        for i in range(0, taille):
            for j in range(i, taille):
                val = matrix[i][j]

                min = val if (val < min and val != 0) else min
                max = val if (val > max) else max

        coords_min = get_coords(min, matrix)

        print('-------- min = ', min)

        

        for coord in coords_min:
            x, y = coord
            matrix[x][y] = 0

            
            forest.plant(to_letter(x), to_letter(y))

        
        

        # print_matrix(matrix)
    
    print(forest)

def print_matrix(matrix):
    for ligne in matrix:
        for val in ligne:
            print(f'{val} ', end='')
        print()
    print()


if  __name__ == '__main__':

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

    #kruskal(mat_incidence)

    forest = TreeForest()
    forest.plant('A', 'B')
    forest.plant('A', 'C')
    print(forest)
