def char_counter(s):
    if len(s)==0:
        return 0
    else:
        if s[len(s)-1]=="x":
            return 1+char_counter(s[0:len(s)-1])
        return char_counter(s[0:len(s)-1])
print(char_counter("xxhixx"))