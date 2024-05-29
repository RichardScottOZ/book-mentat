## check cloud and local

with open('/home/richard/local.txt') as fl:
    l = fl.readlines()

with open('/home/richard/cloud.txt') as fl:
    c = fl.readlines()

for local in l:
    found = False
    for cloud in c:
        if l in c:
            found = True
            break   

    if not found:
        print(l)

   