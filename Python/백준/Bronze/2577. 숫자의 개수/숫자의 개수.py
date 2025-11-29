a = int(input())
b = int(input())
c = int(input())    

total = str(a * b * c)

def num_count(num):
    return(total.count(num))
    

for i in range(0, 10):
    stri = str(i)
    print(num_count(stri))