# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    sum=0
    for x in args:
        sum+=x
    return sum


def main():
    # TODO: pass different arguments
    print(addition(10,3,45))

    # TODO: pass an existing list


if __name__ == "__main__":
    main()
