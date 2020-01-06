import time
from binarysearch import BinarySearchTree
# You've been tasked with speeding up the code
# You may not use the built in Python list, set, or dictionary for this problem
# (Hint: You might try importing a data structure you built during the week)

# Go through homework/classwork for the past week and see which projects
# had no Python built in restrictions - if any
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst = None

for name1 in names_1:
    if bst is None:

        bst = BinarySearchTree(name1)
else:
    bst.insert(name1)

duplicates = []
# for name_1 in names_1:
for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# 0 duplicates
# runtime: 0.01465606689453125 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
