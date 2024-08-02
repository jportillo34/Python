import sys

class complejo:
    def __init__(self, rI, jI):
        self.r = rI
        self.j = jI
    def __add__(self, C):
        return complejo(self.r + C.r, self.j + C.j)
    def __sub__(self, C):
        return complejo(self.r - C.r, self.j - C.j)
    def __str__(self):
        return "({},{})".format(self.r, self.j)

if __name__ == "__main__":
	try:
		P = complejo(3.0, 2.0)
		Q = complejo(4.0, 4.0)
		print("P + Q = {}".format(P + Q))
	except:
		print("Ocurrio un error")
		sys.exit(1)
	sys.exit(0)
