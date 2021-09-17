# created a sort method for alphabetical sort

a = []
def stringSorted(a):
    return sorted(a)

def quickString(a):
    if not a:
        return []
    return (quickString([x for x in a[1:] if x <  a[0]])
            + [a[0]] +
            quickString([x for x in a[1:] if x >= a[0]]))

    
## using this to see if the function works
b = ["jib", "hehe"]
print(quickString(b))
