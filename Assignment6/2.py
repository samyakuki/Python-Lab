def encry_fun(str,s):
    result=""

    for i in range(len(str)):
        char=str[i]

        if(char.isupper()): 
            result += chr((ord(char) + s - 64)% 26+ 65 )  
        else:  
            result += chr((ord(char) + s - 96)%26 +97)  
    return result  

str=input("enter the text: ")
s=int(input("enter the shift: "))

print("original text is: " +str)
print("cipher: " + encry_fun(str,s))