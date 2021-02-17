import json


class Leaf(dict):
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

tree = []

for i in range(1,17):
    leaf = Leaf()
    leaf.data = i
    tree.append(leaf)
    

#print(tree)

with open('tree.json', 'w') as f:
    json.dump(tree, f, indent=2)


