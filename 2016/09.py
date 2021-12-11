def decompressed_length(string, recursive=False):
    length,i=0,0
    while i<len(string):
        if string[i]=='(':
            close_index=string.find(')',i)
            char,reps=map(int,string[i+1:close_index].split('x'))
            substr=string[close_index+1:close_index+char+1]
            if recursive:
                new_len=decompressed_length(substr,recursive)
            else:
                new_len=len(substr)
            length+=reps*new_len
            i=close_index+char
        else:
            length+=1
        i+=1
    return length

with open('09.txt') as file:
    data="".join(file.read().split())

print('Part 1:',decompressed_length(data))
print('Part 2:',decompressed_length(data,recursive=True))
