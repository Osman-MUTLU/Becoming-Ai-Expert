from operator import length_hint


def main():
    square = lambda x: x**2
    pov = lambda x,y: x**y
    print(square(5))
    print(pov(2,5))
    
    array = [1,2,3,4,5,6]
    result = list(map(square,array))
    print(result)
    
    result = list(map(lambda x: x+5,array))
    print(result)
    
    isOdd = lambda x: x%2 != 0
    result = list(filter(isOdd,array))
    print(result)
    
    array = ["osman","beyza","ogun","arman","suheyla","simay","ecem","doga","omer"]
    result = list(filter(lambda x: len(x)==5,array))
    print(result)
    
    x = [i for i in range(5)]
    print(x)
    
    names = ["hello "+i for i in array]
    print(names)
    
    def find_len(arr):
        for element in arr:
            yield len(element)
    for length in find_len(names):
        print(length)
    
    
if __name__ == '__main__':
    main()