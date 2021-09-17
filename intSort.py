# created a sorting method from lowest to highest int
a = []
def intSorted(a):
    return sorted(a)

def intsorter(a):
    if not a:
        return []
    return (intsorter([x for x in a[1:] if x <  a[0]])
            + [a[0]] +
            intsorter([x for x in a[1:] if x >= a[0]]))

b = [4, 5, 1, -2 ,-3 ,4]
print(intsorter(b))