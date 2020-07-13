# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d=collections.deque(string.ascii_lowercase)
    #print(len(d))

    # TODO: deques support the len() function
    print("Item count is ",len(d))

    # TODO: deques can be iterated over
    for item in d:
        print(item.upper(),end="")
    print()

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(100)
    d.appendleft(99)
    print(d)

    # TODO: rotate the deque
    d.rotate(10)
    print("After rotation :",d)


if __name__ == "__main__":
    main()
