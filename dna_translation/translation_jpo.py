inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n","")
seq = seq.replace("\r","")
print(seq)
