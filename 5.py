input_file = open("i5.txt","r")
out_file= open("o5.txt","w")
word = "day"
for line in input_file.readlines():
    for word in line[::-1]:
        out_file.write(word)
