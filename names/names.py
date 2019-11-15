import time
import sys
#sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


start_time = time.time()

LinkList1 = DoublyLinkedList()
LinkList2 = DoublyLinkedList

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

duplicates = []

for name_1 in LinkList1:
    for name_2 in LinkList2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# void rec_fun(int i,int n) {
#     if (!(i<n)) return;
#     func(i);
#     rec_fun(i+1,n);
# }
# ...
# rec_fun(0,n);