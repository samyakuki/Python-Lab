input_file = open("i3.txt","r")
out_file= open("o3.txt","w")
word = "city"
for line in input_file.readlines():
    if word in line.split():
        out_file.write(line)
