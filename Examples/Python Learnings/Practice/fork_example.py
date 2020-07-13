import os
import sys


def child_saying_hello():
    my_pid = os.getpid()
    print("Hello from " + str(my_pid))
    sys.exit(0)


while True:
    choice = input("Enter n for new child Process or any other key for terminate :")
    if choice == 'c':
        new_pid = os.fork()
        if new_pid == 0:
            child_saying_hello()
        else:
            parent_pid = os.getpid()
            print(f"Parent is {parent_pid} and child is {new_pid}")
    else:
        sys.exit(0)
