while(True):
    a=int(input())
    if a==0: break
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12: print("%d - %d"%(a,31))
    elif a==2: print("%d - %d"%(a,28))
    elif a>12: print("%d - %d"%(a,99))
    else:print("%d - %d"%(a,30))
