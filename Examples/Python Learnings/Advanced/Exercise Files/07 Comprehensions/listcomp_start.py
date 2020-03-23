# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evensquares=list(map(lambda x: x**2,filter(lambda x : x>4 and x<16 ,evens)))
    print(evensquares)

    # TODO: Derive a new list of numbers frm a given list
    evensquares=[x**2 for x in evens if x>4 and x<16]
    print(evensquares)

    # TODO: Limit the items operated on with a predicate condition


if __name__ == "__main__":
    main()
