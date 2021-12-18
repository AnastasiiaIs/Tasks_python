from random import randint 

def binarysearch(array,key):
    low=0
    upper=len(array)-1
    while low<=upper:
        center=(low+upper)//2
        if array[center]==key:
            return(center)
        elif array[center]>key:
            upper=center-1
        elif array[center]<key:
            low=center+1
    return None


x=sorted([randint(-100,100) for i in range(10)])
print(x)
g=int(input())
print(binarysearch(x,g))

assert binarysearch([2,4,5,6,9,56,78,98],2)==0
assert binarysearch([2,4,5,6,9,56,78,98],4)==1
assert binarysearch([2,4,5,6,9,56,78,98],5)==2
assert binarysearch([2,4,5,6,9,56,78,98],6)==3
assert binarysearch([2,4,5,6,9,56,78,98],98)==7
assert binarysearch([], 42) is None
assert binarysearch([0], 0) == 0
assert binarysearch([0], 1) is None
assert binarysearch([-1, 0, 42], 0) == 1
assert binarysearch([-42, 0, 42], 42) == 2
assert binarysearch([-6, -5, -4, -3, -2, -1], -4) == 2
assert binarysearch([1, 2, 3, 4, 5, 6], 4) == 3
assert binarysearch([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert binarysearch([1, 2, 3, 4, 5], 7) is None
assert binarysearch([1, 2, 3, 4, 5, 6], 7) is None
assert binarysearch([-42, -42, -42, -42, -42], -42) == 0
assert binarysearch([42, 42, 42, 42, 43], 43) == 4
assert binarysearch([41, 42, 42, 42, 42], 41) == 0
assert binarysearch([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert binarysearch([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4






