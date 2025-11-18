zero_count = int(input())
S_len = int(input())
S = input()

Pn = 'I'
for _ in range(zero_count):
    Pn += "OI"

I, O = 1, 2 

def Hash(answk):
    count = 0
    for i in range(len(answk)):
        if answk[i] == 'I':
            count += I * 31**(len(answk)-i-1)
        else:
            count += O * 31**(len(answk)-i-1)
    return count

Pn_result = Hash(Pn)
count = 0
for i in range(S_len - zero_count-1):
    search = S[i:i+len(Pn)]
    if Hash(search) == Pn_result:
        count += 1

print(count)