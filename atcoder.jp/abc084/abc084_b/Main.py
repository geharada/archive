a,b = map(int,input().split())
s = input()
if len(s) == a + b + 1 and s[a] == "-":
    s = s.replace("-","")
    if s.isdecimal() and len(s) == a + b:
        print("Yes")
        exit(0)
print("No")