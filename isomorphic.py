def isomorphic(a,b):
    d = {}
    
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = b[i]
        else:
            if d[a[i]] != b[i]:
                return False
            else:
                return True
    return False
a = 'egg' 
b = 'add'
print (isomorphic(str(a),str(b)))