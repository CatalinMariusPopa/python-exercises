#program care executa operatia matematica dorita
print("Alege operatia matematica dorita in scris:")
op = input()
print("Introduce primul numar:")
a = input()
print("Introduce al doilea numar:")
b = input()
c = 0
while True:
    if op == 'adunare':
        c = int(a)+int(b)
        print("Rezultatul este:", c)
        break
    if op == 'scadere':
        c = int(a)-int(b)
        print("Rezultatul este:", c)
        break
    if op == 'inmultire':
        c = int(a)*int(b)
        print("Rezultatul este:", c)
        break
    if op == 'impartire':
        c = int(a)/int(b)
        print("Rezultatul este:", c)
        break
