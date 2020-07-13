# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x<50


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1=itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # TODO: use count to create a simple counter
    seq_counter=itertools.count(10,5)
    print(next(seq_counter))
    print(next(seq_counter))
    print(next(seq_counter))
    print(next(seq_counter))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc1=list(itertools.accumulate(vals))
    print(acc1)
    acc2=list(itertools.accumulate(vals,max))
    print(acc2)

            
    # TODO: use chain to connect sequences together
    x=itertools.chain('ABCD','12345')
    print(list(x))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction,vals)))
    print(list(itertools.dropwhile(lambda x : x<20,vals)))
    print(list(itertools.takewhile(testFunction,vals)))
    
    
if __name__ == "__main__":
    main()
    