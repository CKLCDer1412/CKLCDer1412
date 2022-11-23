def compress(string):
    index = 0
    compressed = ""
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(count) + str(string[index])
        index = index + 1
    return compressed
       
 
string = "AAAABBBCDDDDDDDEEF"
print(compress(string))