import hashlib
door = "cxdnnyjw"
i = 0
password = {}
while len(password) < 8:
    test = door + str(i)
    hash_out = str(hashlib.md5(test.encode()).hexdigest())
    # print(hash_out)
    if hash_out[:5] == '00000':
        print(hash_out)
        if int(hash_out[5], 16) < 8 and hash_out[5] not in password:
            password[int(hash_out[5])] = hash_out[6]
            print(password)
    i += 1
# print(password)
for i in range(0, 8):
    print(password[i], end="")
