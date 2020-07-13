from Practice.single_linked_list import *


def linked_list_from_string(s):
    l = SinglyLinkedList()
    for c in s:
        l.append(c)
    return l


def reversed_string(l):
    current = l.head
    prev = None
    next = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    l.head = prev
    return l


s = input("enter the string:")
l = linked_list_from_string(s)
print(f"Reversed String is {reversed_string(l)}")
