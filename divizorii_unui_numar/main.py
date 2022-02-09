#program pentru aflarea divizorilor unui numar
print("introduceti un numar:")
n = input()
i = 0
c = 0
while i < int(n):
    i = i + 1
    if int(n)%i == 0:
        print("acesta este divizor", i)
        c = int(n)/i
        print("si acesta este divizor", int(c))
    else:
        print("acesta nu este divizor", i)
