input_file = open("i1.txt",'r')
dictionary={}
for line in input_file.readlines():
    for word in line.split():
        if word not in dictionary:
            dictionary[word]=0
        dictionary[word]+=1
out_file=open("o1.txt","w")
for k,v in dictionary.items():
    out_file.write(f"{k}:{v}\n")
