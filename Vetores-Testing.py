class Vetor:
    def __init__(self, x, y, z):  #creating a vector with 3 dimensions x, y and z; without intensity
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setZ(self, z):
        self._z = z

    def __add__(self, V2):       #add vector
        return Vetor(self._x + V2._x, self._y + V2._Y, self._y + V2._Z)

    def __sub__(self, V2):       #subtrac. vector
        Vetor_resultante = Vetor(0,0,0)
        Vetor_resultante._x = self._x - V2._x
        Vetor_resultante._Y = self._y - V2._y
        Vetor_resultante._Z = self._z - V2._z
        return Vetor_resultante

    def __mul__(self, V2):
        return self._x * V2._x + self._y * V2._y + self._z * V2._z

    def __rmul__(self, V2):
        return Vetor(self._x, self._y, self._z)

#Classes with vector
#Force (Newton)

class Force(Vetor):
    def __init__(self, x, y, z, intensity):
        super().__init__(x, y, z)
        self._intensity = intensity   #Force atribute

    def getIntensity(self):
        return self._intensity
    def setIntensity(self, intensity):
        self._intensity = intensity



#Velocity (m/s)
