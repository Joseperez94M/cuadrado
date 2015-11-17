class cuadrado:
	def __init__(self, x, y):
        """Este metodo es un constructor python"""
		self.x = x
		self.y = y

	def area(self):
        """Este metodo devuelve el area del cuadrado"""
		return self.x * self.y

    def perimeter(self, x, y):
        """Este metodo devuelve el perimetro del cuadrado"""
	    return (2 * self.x) + (2 * self.y)
