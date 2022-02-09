# ecuatia de gradul 2
import math

print("Acesta este un program ce rezolva ecuatia de gr 2!")
print("Introduceti primul numar:")
a = input()
print("Introduceti al doilea numar:")
b = input()
print("Introduceti al treilea numar:")
c = input()
x1 = 0
x2 = 0
d = int(b) ** 2 - 4 * int(a) * int(c)  # declaram delta
if d > 0:
    x1 = (-int(b) + math.sqrt(d)) / (2 * int(a))
    print("valoarea lui x1 este:", x1)
    x2 = (-int(b) - math.sqrt(d)) / (2 * int(a))
    print("valoarea lui x2 este:", x2)
elif d == 0:
    x1, x2 = -(int(b) / (2 * int(a)))
    print("Valoarea lui x1 respectiv x2 este:", x1, x2)
else:
    print("Ecuatia nu admite valori in multimea numerelor reale")


