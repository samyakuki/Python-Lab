import operator
inp = input("Enter a string:")
dictionary = {}
for i in inp.split(" "):
    if i.isalpha():
        if i not in dictionary:
            dictionary[i]=1
        else:
            dictionary[i]+=1
sort = sorted(dictionary.items(),key=operator.itemgetter(0))
for i in sort:
    print(i[0],":",i[1])