from functools import reduce
llist = []
index = 0

def lessThan_conprehension(n,lst):
    lst2 = []
    for element in lst:
        if(element < n):
            lst2.append(element)
    return lst2



def lessThan_recursive(n,lst):
    if not lst:
        return []
    if lst[0] < n:
        return [lst[0]] + lessThan_recursive(n, lst[1:])
    return lessThan_recursive(n, lst[1:])

def lessThan_highorder(n,lst):
    return reduce(lambda y,x: x+[y] if y < n  else x,lst,[])

def main():
    
    lst = [5,7,12,-4]

    

    lst1 = lessThan_conprehension(11,lst)
    print(lst1)


    lst1 = lessThan_highorder(11,lst)
    print(lst1)


    lst1 = lessThan_recursive(11,lst)
    print(lst1)


   
    
if __name__ == "__main__":
   main()