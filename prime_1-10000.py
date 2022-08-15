ln=1
un=10000
for i in range(ln,un+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:
                break
        else:
            print(i)


