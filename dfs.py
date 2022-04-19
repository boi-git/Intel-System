a =  [4,1,2,5,3]

def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("   "*d + str(a[i]))
    traversed(a, l, d = d+1)

traversed(a)