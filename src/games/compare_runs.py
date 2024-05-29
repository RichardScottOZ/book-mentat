## check cloud and local

with open('/home/richard/localout.txt') as fl:
    l = fl.readlines()

with open('/home/richard/cloudout.txt') as fl:
    c = fl.readlines()

for local in l:
    found = False
    for cloud in c:
        if local in cloud:
            found = True
            break   

    if not found:
        print(local)

   