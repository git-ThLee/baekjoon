import sys

trees = {}
tree_num = 0

for line in sys.stdin:
    if line == "\n":
        break
    tree = line.rstrip()
    tree_num += 1
    if tree in trees:
        trees[tree] += 1
    else :
        trees[tree] = 1
        
sorted_trees = sorted(trees.items(), key = lambda x : x[0])

for k, v in sorted_trees:
    precentage = round((v/tree_num)*100,4)
    print(k, '%.4f' %precentage)