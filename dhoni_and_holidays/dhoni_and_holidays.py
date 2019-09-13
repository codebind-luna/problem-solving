n=int(input())
a=list(map(int,input().split()))
r=0
pd=-1
for i in range(0,n):
    if a[i]==0:
        r+=1
        pd=-1
    elif a[i]==1:
        if pd==0:
            r+=1
            pd=-1
        else:
            pd=0
    elif a[i]==2:
        if pd==1:
            r+=1
            pd=-1
        else:
            pd=1
    else:
        if pd==0:
            pd=1
        elif pd==1:
            pd=0
        elif i!=n-1:
            if a[i+1]==2:
                pd=0
            elif a[i+1]==1:
                pd=1
            else:
                pd=-1
print(r)