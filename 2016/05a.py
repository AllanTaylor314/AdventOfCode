import hashlib
door = "cxdnnyjw"
i = 0
password = ""
while len(password) < 8:
    test = door + str(i)
    hash_out = str(hashlib.md5(test.encode()).hexdigest())
    # print(hash_out)
    if hash_out[:5] == '00000':
        print(hash_out)
        password += hash_out[5]
        print(password)
    i += 1
print(password)
