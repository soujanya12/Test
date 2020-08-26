def totalWords():
    with open(r'C:\Users\Sgangula2\Desktop\o.txt',"r") as f:
        freqs={}
        for line in f.read().split():
            if  line    not in  freqs:
                freqs[line]=1
            else:
                freqs[line]+=1

        return freqs
print(totalWords())