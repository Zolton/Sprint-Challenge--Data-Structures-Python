import time
import sys
#sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from binary_search_tree import BinarySearchTree


start_time = time.time()




f = open('names_1.txt', 'r')
LinkList1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
LinkList2 = f.read().split("\n")  # List containing 10000 names
f.close()
#print("This is names1: ", names_1)

# Problem is names_1 and 2 are arrays - not necessary since we don't
# care about index numbers or location of any particular name - 
# Only care whether it exists or not

#duplicates = []

# for name_1 in LinkList1:
#     for name_2 in LinkList2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Binary trees really are a brilliant bit of code.  Computer doesn't give a shit whether
# it's sorting numbers or strings - its all the same.  Sort 1 list into a binary
# tree, and traverse it with the second - chopping it in half every operation
# O(logn)

# Prime the pump - start with real name in middle of alphabet, 
# make it fake so it'll never come back, and organize list around it
bst = BinarySearchTree("Mikaelz Mcmahz")

duplicates = []

for name_1 in LinkList1:
    bst.insert(name_1)

for name_2 in LinkList2:
    if bst.contains(name_2) == None:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

