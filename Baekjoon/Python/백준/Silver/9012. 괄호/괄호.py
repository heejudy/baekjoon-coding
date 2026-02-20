for i in range(int(input())):
    b = input()
    c = b.replace("()","")
    if c == "": 
        print("YES")
    else:
        while c != "":
            c = c.replace("()","")
            if c == "":
                print("YES")
            elif "()" not in c:
                print("NO")
                break