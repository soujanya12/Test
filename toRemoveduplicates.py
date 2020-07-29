f = open(r"/file/location","r")
contents = f.readlines()
f.close()
f = open(r"/file/location","w")
contents = [1,1,2,1]
for x in contents:
    if contents.count(x) > 1:
        contents.remove(x)
        print(x)
res = contents
for i in res:
    f.write(i)
f.close()





















































