a=[1,2,3,1,2,4,5,3,4,2,1]
def samle(l):
    counts={}
    for i in l:
        if i in counts:
            counts[i]=counts[i]+1
        else:
            counts[i]=1;
    print (counts)
samle(a)    
