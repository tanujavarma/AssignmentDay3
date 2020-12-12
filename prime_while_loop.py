x=int(input("enter upper value"))
lower=1
while(lower<=x):
    count=0
    i=2
    
    while(i<=lower//2):
        if(lower%i==0):
            count=count+1
            break
        i=i+1

    if(count==0 and lower!=1):
        print("%d" %lower, end=' ')
    lower=lower+1
    
