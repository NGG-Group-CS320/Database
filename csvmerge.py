fout=open("out.csv","a")

for line in open("1-perform.csv"):
    line = line.replace('""','0')
    fout.write(line)

for num in range(2,4520):
    f = open(str(num)+"-perform.csv")
    f.next() # skip the header
    for line in f:
         line = line.replace('""','0')
         fout.write(line)
    f.close()
fout.close()
