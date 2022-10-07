def key(di,a): 
    b=di.keys()
    c=[]
    for j in b:
        if di[j]==a:
            c.append(j)
    if len(c)!=0:
        return c
    else:
        d="value not found"
        return d