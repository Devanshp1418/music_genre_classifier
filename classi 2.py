import math
def clasi(points,p,k=9):
    dist=[]
    gru=[]
    for grp in points:
        gru.append(grp)
        for val in points[grp]:
            eucd = math.sqrt((val[0]-p[0])**2 + (val[1]-p[1])**2)
            dist.append((eucd,grp))
    dist=sorted(dist)[:k]
    f=[]
    for i in range(len(gru)):
        f.append(0)
        
    for d in dist:
        if d[1]==gru[0]:
            f[0]+=1
        elif d[1]==gru[1]:
            f[1]+=1
        elif d[1]==gru[2]:
            f[2]+=1
    greatest=0
    for i in f:
        if i>greatest:
            greatest=i
    ind=f.index(greatest)
    return gru[ind]

if __name__ == "__main__":
    points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}
    a=eval(input("enter a point less than (x,y)=(10,15) :"))
    k=3
    p =a
    print("The Group classified to unknown point({}) is:".format(str(a)), clasi(points, p, k))