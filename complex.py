import sys

class complejo:
	""" Representa a un numero complejo """
	def __init__(self, rI, jI):
		self.r = rI
		self.j = jI
	def __add__(self, C):
        	return complejo(self.r + C.r, self.j + C.j)
	def __sub__(self, C):
		return complejo(self.r - C.r, self.j - C.j)
	def __neg__(self):
		return complejo((-1)*self.r, (-1)*self.j)
	def __str__(self):
		return "({},{})".format(self.r, self.j)

def print_suma_complejos(A, B):
	print("{} + {} = {}".format(A, B, A + B))

def main():
	""" Funcion principal del programa """
	try:
		print_suma_complejos(complejo(3.0, 2.0), complejo(4.0, 4.0))
	except:
		print("Ocurrio un error")
		sys.exit(1)
	sys.exit(0)

if __name__ == "__main__":
	main()
