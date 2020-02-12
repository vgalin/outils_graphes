class DisjointSet:
    def __init__(self, sommets):
        self.sommets = sommets
        self.parents = {sommet: sommet for sommet in sommets}

    def find(self, item):
        if self.parents[item] == item:
            return item
        else:
            return self.find(self.parents[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parents[root1] = root2

    def __repr__(self):
        return f'{self.sommets} \n {self.parents}'


if __name__ == '__main__':
    pass