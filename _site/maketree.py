import json

leaves = []

for i in range(16):
    leaf = {}
    leaf["data"] = i
    leaves.append(leaf)



with open("./tree") as f:
    json.dump(leaves, f)