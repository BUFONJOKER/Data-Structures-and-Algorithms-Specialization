def lcm(a, b):
    
    less_num = a


    if b<a:
        less_num = b

    multiple = less_num

    while True:

        if multiple % a == 0 and multiple % b == 0:
            break

        multiple+=less_num 
    return multiple

print(lcm(761457, 614573))