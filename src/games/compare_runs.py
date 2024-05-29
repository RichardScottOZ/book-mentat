## check cloud and local

with open('local.txt') as fl:
    l = fl.readlines()

with open('cloud.txt') as fl:
    c = fl.readlines()

for local in l:
    found = False
    for cloud in c:
        if l in c:
            found = True
            break   

    if not found:
        print(l)

   