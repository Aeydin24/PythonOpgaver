import random
# Complex numbers

z = complex(5, 7)
print("Output:", z)
# Output: (5+7j) 

z = complex(3)
print("Output:", z)
# Output: (3+0j)

z = complex()
print("Output:", z)
# Output: 0j

z = complex('1+1j')
print("Output:", z)
# Output: 1+1j

z = complex(1, -4)
print("Output:", z)
# Output: 1-4j

# Eller med en indbygget funktion:

z  = 3 + 4j

print("rigtige del:", z.real)
# rigtige del: 3.0 

print("'falske del' del:", z.imag)
# falske del: 4.0

print("Conjugate value:", z.conjugate())
# Conjugate value: 3 - 4j

# Der kan udføres matematik på disse: 

z1 = 6 + 7j
z2 = 1 + 4j

print("Addition of numbers:", z1 + z2)
print("Subtraction of numbers:", z1 - z2)
print("Multiplication of numbers:", z1 * z2)
print("Division of numbers:", z1 / z2)

#------------------------------------------------------<

# Python Casting:

# Integers:
x = int(1)   # Output = 1
y = int(2.8) # Output = 2
z = int("3") # Output = 3

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings: 
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 

# Python Booleans

# check om expression er true

a = random.randrange(1,100)
b = random.randrange(1,200)

if b < a:
    print("b er mindre end a")
else:
    print("a er mindre end b")
    
print("a = ", a)
print("b = ", b)
    
print(bool("Hej med dig, jeg hedder Kaj, dubi dubi dubi dej"))

# Python Strings

a = """RELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRE
LFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFROLFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELFRELF"""

print("ROLF" in a)
print(len(a))
for h in "Ananananananananas":
    print(h)
    
# Python Operators

# plus
a = 5 + 3
print(a)
# minus
b = 5 - 3
print(b)
# gange
c = 3 * 10
print(c)
# dividere
d = 10 / 5
print(d)
# modulo
f = 10 % 4
print(f)
# exponentiel
g = 10 ** 2
print(g)
# floor division
h = 13 // 5
print(h)
# hurtig plus
b += 25
print(b)

