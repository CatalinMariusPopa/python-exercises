#descompunerea in factori primi
print("Introduceti un numar:")
n = input()
d = 2
while int(n)>1:
    p = 0
    while (int(n)%int(d) == 0):
        p = int(p)+1
        n = int(n)/int(d)
    if p:
        print("factorul este:", d, " si puterea este", p)
    d = int(d)+1