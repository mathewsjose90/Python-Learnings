# use iterator functions like enumerate, zip, iter, next
import sys
import os
sys.path.append(os.curdir)

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i=iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel
    with open("/Users/mjose/Documents/Team/Python Learnings/Advanced/Exercise Files/02 BuiltIn Functions/testfile.txt") as f:
        for line in iter(f.readline,''):
            print(line)

    # TODO: use regular interation over the days
    for d in days:
        print(d)

    # TODO: using enumerate reduces code and provides a counter
    for i,d in enumerate(days,start=1):
        print(i,d)

    # TODO: use zip to combine sequences
    for pos,d in enumerate(zip(days,daysFr),start=1):
        print(pos,d[0],"=",d[1]," in French")


if __name__ == "__main__":
    main()
