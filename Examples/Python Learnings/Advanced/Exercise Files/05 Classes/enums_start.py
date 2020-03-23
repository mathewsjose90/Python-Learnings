# define enumerations using the Enum base class
from enum import Enum,unique,auto

@unique
class  Fruit(Enum):
    Apple=1
    Banana=2
    Orange=3
    SOMETHING=10
    SOMETHING_ELSE=auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    print(Fruit.Apple.name,Fruit.Apple.value)
    print(type(Fruit.Apple))
    print(repr(Fruit.Apple))
    

    # TODO: enums have name and value properties
    print(Fruit.Apple.name,Fruit.Apple.value)

    # TODO: print the auto-generated value
    print(Fruit.SOMETHING_ELSE.name,":",Fruit.SOMETHING_ELSE.value)

    # TODO: enums are hashable - can be used as keys
    myFruits={}
    myFruits[Fruit.Apple]='Apple value'
    myFruits[Fruit.SOMETHING]='Something intresting'
    print(myFruits.items())


if __name__ == "__main__":
    main()
