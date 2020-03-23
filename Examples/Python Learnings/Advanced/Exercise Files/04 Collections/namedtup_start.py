# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point=collections.namedtuple("Point",['x','y'])
    p1=Point(12,33)
    p2=Point(10,20)
    print(p1,p2)
    p1=p1._replace(x=150)
    print(p1,p2)

    # TODO: use _replace to create a new instance
    pass


if __name__ == "__main__":
    main()
