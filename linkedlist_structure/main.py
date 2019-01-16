from linkedlist import Linkedlist

linkedlist = Linkedlist()

linkedlist.addFirst(1)
linkedlist.addFirst(2)
linkedlist.addFirst(4)
linkedlist.addFirst(5)
linkedlist.addLast(100)

print (linkedlist.showLinkedlist())
print (linkedlist.getSize())
linkedlist.setVal(3,200)
print (linkedlist.getVal(4))
print (linkedlist.showLinkedlist())

linkedlist.remove(2)
print (linkedlist.showLinkedlist())





