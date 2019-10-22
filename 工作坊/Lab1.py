def prod(x,y):
    msg = '{:<d} * {:<d} = {:>d}   '.format(x, y, x*y) 
    return msg
    
for x in range(10): # 0...9 不含 10
    if x >0 :
        print(" ")
        for y in range(10): # 0...9 不含 10
            if y > 0:
                print(prod(x, y), end='')
                 #print(str(x) + "*" + str(y) + "=" + str(x*y) + " ", end='')