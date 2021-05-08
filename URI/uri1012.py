a, b, c = [float(x) for x in input().split()]
pi = 3.14159


print("TRIANGULO: {:.3f}".format((a*c)/2))
print("CIRCULO: {:.3f}".format(pi * c**2))
print("TRAPEZIO: {:.3f}".format((a+b)*c/2))
print("QUADRADO: {:.3f}".format(b**2))
print("RETANGULO: {:.3f}".format(a*b))
