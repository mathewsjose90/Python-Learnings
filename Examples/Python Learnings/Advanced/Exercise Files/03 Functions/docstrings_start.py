# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    '''
    myFunction(arg1, arg2=None)-->Just prints 
    Parameters:
    arg1:First argument, whatever we like
    arg2: Optional . Defaults to None
    '''
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
