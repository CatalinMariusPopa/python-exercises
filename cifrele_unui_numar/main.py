#trebuie sa aflam cifrele unui numar faormat din 3 cifre
n = 274
uc = 0
cz = 0
cs = 0
uc = n % 10
print("Ultima cifra este: ", uc)
n = n / 10
cz = n % 10
print("Cifra zecilor este: ", int(cz))
n = n / 10
cs = n % 10
print("Cifra sutelor este: ", int(cs))
