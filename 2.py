input_file_1 = open("i2.txt","r")
input_file_2 = open("i1.txt","r")
out=open("o2.txt","w")
d={}
for line in input_file_1.readlines():
    out.write(line)
for line in input_file_2.readlines():
    out.write(line)
    

