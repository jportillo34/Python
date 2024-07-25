# ================================================================================= #
#                                                                                   #
# EJEMPLOS DE USO DE ESTRUCTURAS DE DATOS, LIBRERIAS Y FUNCIONES EN LOS LENGUAJES:  #
#        PYTHON, PostgreSQL, Oracle PL/SQL, JAVA, JAVASCRIPT, C, C++, Bash Script,  # 
#        C# (C Sharp), R Language, Wolfram Language, SCHEME(LISP), RUST, KOTLIN,    #
#        GIT, ARITMETICA Y ALGEBRA                                                  #
#                                                                                   #
# ================================================================================= #

#
#
#                                        SECCION DE EJEMPLOS PYTHON                                             #
#
#
# IMPORTANTE: PYTHON puede ser instalado en varios sistemas operativos, entre ellos tenemos: Windows, MacOS, 
# las distribuciones de Linux (UBUNTU, DEBIAN, RedHat) y Android (que esta basado en un Kernel de Linux).
#
#
# IMPORTANTE: Si intentamos ejecutar el interprete PYTHON en el GIT Bash no funcionara. Para que ejecute en dicho entorno 
#             debemos incluir la opcion "-i" en el comando de la manera siguiente,
#
#             $ python -i
#








#
# Como saber la version de PYTHON?
#
# Hay dos maneras:
#
# 1.- Desde la linea de comandos del sistema operativo:
python --version
...Python 3.10.14


# 2.- Desde el interprete de PYTHON:
import sys

sys.version
'3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)]'












#
# Como instalar PIP para instalar paquetes PYTHON?
#
# IMPORTANTE: Las distribuciones de LINUX tiene su propio instalador de paquetes y es recomendable usarlo en lugar que usar el de PYTHON (PIP).
#             El nombre del instalador de paquetes puede variar dependiendo de la distribucion de LINUX,
#
#             - "apt" en DEBIAN, UBUNTU y Linux MINT (apt es "Advance Package Tool")
#             - "yum" en RedHat y CentOS
#             - "dnf" en FEDORA
#
#             Por ejemplo, la manera de instalar algun paquete para PYTHON usando el instalador basico de UBUNTU ("apt") seria,
#
#             sudo apt install <nombre del paquete>
#             ("sudo" es un comando que permite ejecutar con privilegios de superusuario, "superuser...do")
#
#             En las distribuciones de LINUX podemos usar el instalador de paquetes nativo para instalar PIP, por ejemplo en UBUNTU,
#
#             sudo apt install python3-pip
#
#             En windows, PIP YA VIENE INCLUIDO en PYTHON!!
#
# IMPORTANTE: La ventaja de usar PIP es que este comprueba (durante la instalacion de un paquete) que todas las dependencias que el paquete 
#             necesita esten instaladas!!
#
# Como actualizar la herramienta pip.
#
python -m pip install --upgrade pip






#
# Como instalar un paquete usando PIP.
#
pip install <paquete>






#
# Usar pip para desinstalar paquetes en Python.
#
pip uninstall <paquete>

# Tambien puede usarse el comando,
python -m pip uninstall <paquete>









# IMPORTANTE: Con Visual Studio Code es posible crear un virtual environment tal y como se hace en este ejemplo.
#
# Instalar el modulo Virtual Environment en Python.
#
# NOTA: La version actual de Python ya incluye este modulo en su lista de modulos pre-instalados!
#       Para acceder a dicho modulo ejecutar,
#
#       python -m venv <nombre del viertual env>
#
pip install virtualenv










#
# Como crear un virtual environment de Python.
#
$ python -m venv .venv

# El comando creara una carpeta con todo lo necesario para mantener y ejecutar la aplicacion (incluido el interprete Python!!).

#
# Luego para activar el virtual env ejecutamos el comando,
#
$ source .venv/Scripts/activate

#
# Para desactivarlo ejecutamos,
#
deactivate

# Estos scripts se encuentran en la misma carpeta del Virtual Env.

#
# IMPORTANTE: Una vez creado el virtual environment es buena practica el crear un "requirements file" que contendra todas las dependencias 
#             o requisitos necesarios para replicar todo en otro virtual environment distinto:
pip freeze > requirements.txt

#
# Luego, para replicar todo en el otro virtual environment ejecutamos (alla):
pip install -r requirements.txt


#
# A continuacion algunas buenas practicas para los virtual environments (tomadas del curso de Google).
#
As you dive into the world of virtual environments, keep these best practices in mind:

Create a virtual environment for each project: Whenever you start a new project, create a new virtual environment. 
This ensures a clean and isolated workspace.

Use requirements files: To document and manage your project's dependencies, create a requirements.txt file. 
This file lists all the libraries and their versions. You can generate it using pip freeze > requirements.txt and 
later install them in a new environment using pip install -r requirements.txt.

Activate and deactivate: Always activate the appropriate virtual environment before working on a project and 
deactivate it when you're done. This prevents confusion and potential conflicts.

Version control: If you're collaborating with others, include the virtual environment setup instructions in 
your version control system. This ensures everyone is using the same environment.

Upgrade pip and setuptools: When you create a new virtual environment, it's a good practice to upgrade pip and 
setuptools to the latest version. This ensures you're using the most up-to-date tools.






#
# Instalar el paquete de pruebas pytest.
#
pip install -U pytest












#
# Sobre el "shebang" en los scripts Python.
#
# IMPORTANTE: Al igual que con los scripts de BASH, es buena practica el iniciar los scripts PYTHON con una linea Shebang para indicar 
#             al shell que, para ejecutar dicho script, debe usar el interprete PYTHON dentro de un nuevo environment. Para ello se 
#             utiliza el comando "/usr/bin/env":
#!/usr/bin/env python











#
# Sobre los permisos de ejecucion de scripts PYTHON.
#
# IMPORTANTE: Cuando creamos un archivo .py (un script PYTHON) el sistema crea dicho archivo con permisos 600 o parecido; es decir: 
#             sin permiso de ejecucion. Por tanto debemos usar el comando CHMOD para darle permisos de ejecucion:
#
chmod 777 test.py










#
# Como hacer para que un script PYTHON retorne al ambiente desde el cual fue invocado con un codigo de retorno.
#

#!/usr/bin/env python

import sys

if __name__ == "__main__":
   sys.exit(3)              # <---- Retornara con valor 3. Luego, desde la linea de comandos BASH podemos consultar 
                            #       la marca "$?" que muestra el valor retornado por el ultimo comando ejecutado.
                            #       Este valor retornado pudiera ser aprovechado por otros procesos en PIPEs!!










#
# NOTA IMPORTANTE: PYTHON tiene tipos de datos inmutables, por ejemplo: numeric, string, tupla. Estos tipos de datos admiten 
#                  operaciones, tal como +, *. Al ser inmutables, cuando se suman (por ejemplo) dos objetos inmutables PYTHON 
#                  CREA UN NUEVO objeto!!
#
#                  La forma de verificar esto es con el uso de "id()". Al aplicarle esta funcion a un objeto nos muestra su numero 
#                  de identificacion. Ejemplo,
#
#                  x = 3.1416
#                  id(x)   # <---- Ahora solicitamos el ID de este objeto que hemos creado
#                  2588217729616
#
#                  x += 1   # <---- Lo modificamos
#                  id(x)   # <---- Consultamos su ID
#                  2588217732176   # <---- El ID ES DIFERENTE. PYTHON ha creado un objeto nuevo!!











# Sobre los objetos ITERABLES, ITERATORs, la funcion ITER(), los GENERATORs, las GENERATOR EXPRESSIONs, la funcion SUM(), 
# la funcion ALL() y la funcion ANY(). 
#
# El ITERABLE es un tipo de objeto en PYTHON que se caracteriza porque sus elementos pueden ser extraidos o visitados 
# usando un loop FOR o una LIST COMPREHENSION.
#
# Objetos como las LIST, SET, TUPLE, DICTIONARY o STRING son iterables.
#
# La funcion "iter()" toma como parametro un objeto iterable y devuelve un iterator.
#
# El metodo "reader()" del modulo CSV devuelve un objeto iterable, el cual pudieramos convertirlo a una LIST usando 
# la funcion "list()".
#
# Otro ejemplo es la funcion "zip()" toma como parametro varios objetos iterables y devuelve un ITERATOR. 
# Esto se utiliza en PYTHON para hacer iteraciones en paralelo a traves de varios objetos iterables!!!!!
#
# Sobre los objetos que son ITERABLES, INDEXABLES e "SLICIABLES" como los tipo STRING y LIST:
#
# El metodo "index()", por ejemplo, aplica tanto a strings como a lists,
#
# lista_nombres = ['nombre', 'Bernardo', 'Vicente', 'Carolina']   # <---- Ejemplo de LIST.
#
# lista_nombres.index('Carolina')                                 # <---- Devuelve la posicion del elemento.
# 3
#
# lista_nombres[1:]                                               # <---- Hace un slice que ignora el primer elemento ([0]).
# ['Bernardo', 'Vicente', 'Carolina']
#
# t = "Primera Segunda Tercera Cuarta"                            # <---- Ejemplo de STRING.
#
# t.index('Segunda')                                              # <---- Similar al mismo metodo en la LIST!
# 8
#
# t[1:]                                                           # <---- Hace un slice que ignora el primer caracter 'P' ([0]).
# 'rimera Segunda Tercera Cuarta'
#
#
# Las siguientes definiciones fueron tomadas de la documentacion oficial de PYTHON:
#
# ITERABLE
# An object capable of returning its members one at a time. Examples of iterables include all sequence types 
# (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes 
# you define with an __iter__() method or with a __getitem__() method that implements sequence semantics.
#
# Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). 
# When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. 
# This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() 
# or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed 
# variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.
#
# ITERATOR
# An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in 
# function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised 
# instead. At this point, the iterator object is exhausted and any further calls to its __next__() method just raise 
# StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every 
# iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code 
# which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you 
# pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted 
# iterator object used in the previous iteration pass, making it appear like an empty container.
#
# ITER(object, sentinel)
# Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. 
# Without a second argument, object must be a collection object which supports the iterable protocol (the __iter__() method), 
# or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support 
# either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. 
# The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned 
# is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.
#
# GENERATOR
# A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for 
# producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.
#
# Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended 
# meaning isn’t clear, using the full terms avoids ambiguity.
#
# GENERATOR ITERATOR
# An object created by a generator function.
#
# Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending 
# try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start 
# fresh on every invocation).
#
# GENERATOR EXPRESSION
# An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, 
# range, and an optional if clause. The combined expression generates values for an enclosing function:
#
# sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
# 285
#
#
# Sobre SUM() y los GENERATORS: la manera "pythonista" de sumar elementos en un iterable!
#
# En el ejemplo siguiente vemos como podemos sumar los elementos numericos de una lista. En otros lenguajes esto 
# puede hacerse a traves de un for loop. Pero PYTHON ya viene equipado con esta funcion:
>>> sum([1, 2, 3, 4])
10

>>> sum([ x*2 for x in [1, 2, 3] ])   # <---- Aqui para obtener la suma de los numeros de un iterable producido desde 
                                      #       una LIST Comprehension!
12

# Es posible, incluso, hacer la misma SUM anterior para que produzca la suma de una GENERATOR EXPRESSION:
>>> sum(x*2 for x in range(1, 4))     # <---- A (x*2 for x in range(...)) se le conoce como un GENERATOR EXPRESSION.
12


>>> sum(range(4))                     # <---- Aqui usamos SUM aplicada a un range!
6

>>> sum([3.0+2.0j, 4.0+4.0j])         # <---- Sumemos los COMPLEX NUMBERS contenidos en una LIST!!
(7+6j)


#
# Sobre las funciones ALL() y ANY() aplicadas a iterables.
#
# Estas funciones evaluan cada elemento de un iterable (LIST, TUPLA< DICTIONARY) y devuelven un valor veritativo (True o False)
# dependiendo de si todas (en el caso de la funcion "all()") o alguna (en el caso de la funcion "any()") de las sentencias o valores 
# contenidas en el iterable se cumplen o son verdaderas!
#
# Si no existiera la funcion ALL() tendriamos que programar una funcion que iterara a traves del iterable y devolviera True o False,
#
# def evalua(lista):
#    for condicion in lista:
#       if not condicion:
#          return False
#    return True
#
# Las funciones ALL() y ANY() serian la manera "pythonista" de obtener un valor veritativo de un iterable!
#
# Una manera de usar la funcion "all()" es incluir un FOR iterador como argumento de esta funcion como veremos en los ejemplos abajo. 
#
# INFORMACION: https://realpython.com/python-all/
#              https://realpython.com/any-python/
#
# Ejemplos:
condiciones = [5 > 2, 1 == 1, 42 < 50]   # Una lista con sentencias condicionales.

# Aplicamos "all()" para ver si todas son verdaderas. Si alguna es falsa devuelve False:
all(condiciones)
True

# Modificamos alguna sentencia para hacerla falsa:
condiciones[0] = 5 < 2

all(condiciones)
False

# Ahora incluimos un FOR iterador como argumento a la funcion "all()":
condiciones = [5 > 2, 1 == 1, 42 < 50]   # Una lista con sentencias condicionales.

all(condicion for condicion in condiciones)
True

# Pudieramos, incluso, incluir el resultado de una funcion dentro de "all()":
all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns)   # <---- Aqui aplicamos el metodo "re.search()" a 
                                                                                 #       cada uno de los elementos de un iterable 
                                                                                 #       llamado "error_patterns"!!

# aqui tenemos otro ejemplo, ahora usando una lambda function:
all((lambda x : x < 6)(n) for n in [1, 2, 3, 4, 5])
True
all((lambda x : x < 6)(n) for n in [1, 2, 3, 4, 5, 6, 7])
False


# La funcion "any()" solo necesita que alguna se cumpla para devolver True. Si todas son falsas devuelve False!


# Sobre los GENERATORS y como crear uno.
#
# Lo siguiente es tomado de Real Python (https://realpython.com/python-iterators-iterables/)
#
# A Python object is considered an iterator when it implements two special methods collectively known as the iterator protocol. 
# These two methods make Python iterators work. So, if you want to create custom iterator classes, then you must implement 
# the following methods:
# Method 	   Description
# .__iter__() 	Called to initialize the iterator. It must return an iterator object.
# .__next__() 	Called to iterate over the iterator. It must return the next value in the data stream.

# El siguiente ejemplo es tomado de la pagina indicada Real Python. Creamos un fuente llamado "fib_generator.py":
class FibonacciInfIterator:
    def __init__(self):
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current

# Luego, desde el interprete PYTHON importamos el modulo y ejecutamos la iteracion. Esto producira una sucesion infinita
# de numeros Fibonacci. Detenemos la impresion de valores en pantalla con Ctrl + c:
>>> from fib_generator import FibonacciInfIterator
>>>
>>> for fi in FibonacciInfIterator():
...     print(fi)

dis.dis(FibonacciInfIterator)
Disassembly of __init__:
  2           0 RESUME                   0

  3           2 LOAD_CONST               1 (0)
              4 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_index)

  4          16 LOAD_CONST               1 (0)
             18 LOAD_FAST                0 (self)
             20 STORE_ATTR               1 (_current)

  5          30 LOAD_CONST               2 (1)
             32 LOAD_FAST                0 (self)
             34 STORE_ATTR               2 (_next)
             44 RETURN_CONST             0 (None)

Disassembly of __iter__:
  7           0 RESUME                   0

  8           2 LOAD_FAST                0 (self)
              4 RETURN_VALUE

Disassembly of __next__:
 10           0 RESUME                   0

 11           2 LOAD_FAST                0 (self)
              4 COPY                     1
              6 LOAD_ATTR                0 (_index)
             26 LOAD_CONST               1 (1)
             28 BINARY_OP               13 (+=)
             32 SWAP                     2
             34 STORE_ATTR               0 (_index)

 12          44 LOAD_FAST                0 (self)
             46 LOAD_ATTR                2 (_next)
             66 LOAD_FAST                0 (self)
             68 LOAD_ATTR                4 (_current)
             88 LOAD_FAST                0 (self)
             90 LOAD_ATTR                2 (_next)
            110 BINARY_OP                0 (+)
            114 SWAP                     2
            116 LOAD_FAST                0 (self)
            118 STORE_ATTR               2 (_current)
            128 LOAD_FAST                0 (self)
            130 STORE_ATTR               1 (_next)

 13         140 LOAD_FAST                0 (self)
            142 LOAD_ATTR                4 (_current)
            162 RETURN_VALUE


# Sobre el mejor performance de las TUPLAS respecto a otras estructuras similares como las LISTS (tomado de Real Python):
#
# Python’s tuples are a straightforward data structure for grouping arbitrary objects. 
# Tuples are immutable—they can’t be modified once they’ve been created.
#
# Performance-wise, tuples take up slightly less memory than lists in CPython, and they’re also faster to construct.
#
# As you can see in the bytecode disassembly below, constructing a tuple constant takes a single LOAD_CONST opcode, 
# while constructing a list object with the same contents requires several more operations:
#
>>> import dis
>>> dis.dis(compile("(23, 'a', 'b', 'c')", "", "eval"))
      0 LOAD_CONST           4 ((23, "a", "b", "c"))
      3 RETURN_VALUE

>>> dis.dis(compile("[23, 'a', 'b', 'c']", "", "eval"))
      0 LOAD_CONST           0 (23)
      3 LOAD_CONST           1 ('a')
      6 LOAD_CONST           2 ('b')
      9 LOAD_CONST           3 ('c')
     12 BUILD_LIST           4
     15 RETURN_VALUE













# Sobre la sentencia IF en PYTHON.
#
# NOTA: La manera tradicional (de todos los lenguajes estructurados) del IF es,
#
#       if <condicion> accion else accion
#
#       PYTHON ofrece otra manera adicional,
#
#       accion if <condicion> else accion
#
# Ejemplo,
y = 10 if x < 5 else 0   # En este caso la variable "y" se activa con valor 10 si x < 5 o 0 de lo contrario!

# Aplicado a una lambda function:
f = lambda x : x if x == 0 or x == 1 else f(x-2) + f(x-1)













# Sobre la creacion de elementos en un DICTIONARY.
#
# IMPORTANTE: Supongamos que queremos crear un dictionary para llevar una cuenta de el numero de ocurrencias de 
#             palabras en un texto. La estructura de datos DICTIONARY es ideal para este tipo de trabajo porque es 
#             capaz de almacenar un nombre o palabra clave conjuntamente con un contenido o valor asociado 
#
#             <nombre del dictionary>[<clave>] = <valor o elemento asociado>
#
#             Un ejemplo de aplicacion de dictionary seria llevar una cuenta de las ocurrencias de una palabra en 
#             un texto, activando cada clave del dictionary con la palabra a contar y llenando su valor con la cuenta de 
#             las ocurrencias. Ejemplo,
#
#             diccionario[clave] = diccionario[clave] + 1
#
#             En el ejemplo anterior en la sentencia "diccionario[clave]" PYTHON devuelve el valor asociado. Por tanto, 
#             podemos sumar una unidad cada vez que ocurre la palabra en un texto.
#
#             Sin embargo, esta manera directa puede producir un error de jecucion en PYTHON si la clave no existe 
#             en el dictionary!!
#
#             Asi que para evitar problemas, PYTHON ofrece un metodo que permite obtener el valor asociado a una clave,
#
#             ".get(clave, <valor por defecto si la clave no existe>)"
#
#             Con este metodo, la sentencia anterior quedaria asi,
#
#             diccionario[clave] = diccionario.get(clave, 0) + 1
#
#             Con esto, si se da el caso que la clave no existe en el dictionary, PYTHON devuelve cero (0) a la sentencia 
#             y por tanto se asigna uno (1)!!








#
# OJO!!! Revisar los siguientes temas del curso google:
#
# 1.- funcion y metodo "sorted()", ".sort()"
#
# 2.- el metodo .append() para adicionar elementos a una lista siendo esta lista un elemento de un dictionary. Ejemplo:
#
#     L = {"list1": [elem1, elem2, ..., elemn], ..., "xx": ....}
#     L["list1"].append([elem3...])
#











#
# NOTA IMPORTANTE: El metodo ".join" puede recibir como parametro los tipos LIST, TUPLA o SET.
#
# NOTA IMPORTANTE: Para que el metodo ".join" funcione, el parametro que se pase a este, sea una LIST, una TUPLA o un SET, sus elementos
#                  TIENEN QUE SER del tipo caracter. Ejemplo,
#
#                  L = ['1', '2', '3', '4']
#                  "-".join(L)
#                  '1-2-3-4'
#
#                  Si intentamos hacer lo mismo con una LIST cuyos elementos son numeric, PYTHON muestra el siguiente error:
#
#                  L = [1, 2, 3, 4]
#                  "-".join(L)
#                  Traceback (most recent call last):
#                   File "<pyshell#33>", line 1, in <module>
#                      "-".join(L)
#                      TypeError: sequence item 0: expected str instance, int found








#
# Ordenar un diccionario en base a su key o en base a su valor:
#
import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

sorted(fruit.items(), key=operator.itemgetter(0))

[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1))

[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]











#
# Sobre las herramientas de testing en PYTHON: UNITTEST y PYTEST.
#
# NOTA: Algunas paginas con informacion sobre los modulos y buenas practicas de testing en PYTHON son,
#
#       https://realpython.com/python-testing/
#       https://docs.python.org/3/library/unittest.html
#       https://realpython.com/pytest-python-testing/
#
# NOTA: PYTHON ya viene con una sentencia "assert" que permite verificar si una sentencia individual se cumple o no,
#
>>> assert 5 == 6, "ERROR: should be equal"
       Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       AssertionError: ERROR: should be equal      # <---- Mensaje incluido en la sentencia assert!
#
#       Ahora hagamos que se cumpla,
#
>>> assert 5 == 5, "ERROR: should be equal"
#       no devuelve ningun mensaje!!!
#
#       Sin embargo, esta es una accion manual e individual. Podemos, con la ayuda del modulo "unittest" crear un programa 
#       el cual haria las pruebas unitarias. El modulo "unittest" es orientado a objeto y por tanto debemos heredar de una 
#       classe llamada "unittest.TestCase" en nuestro script de pruebas. Vamos a crear un script llamado "test_sum_unittest.py",
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

# Ejecutamos este script de pruebas:
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)

# Vemos como la prueba incluida en el metodo "test_sum_tuple" fallo! y el modulo "unittest" lo advierte!


#
# Otra manera de ejecutar pruebas unitarias con el modulo UNITTEST es a traves de la linea de comandos del sistema:
#
# Para este ejemplo creamos un modulo llamado test.py:
import unittest

def isPar(n):
	return n % 2 == 0

class test_Par(unittest.TestCase):
	def test_esPar(self):
		self.assertEqual(isPar(4), True, "deberia devolver True")
	def test_noPar(self):
		self.assertEqual(isPar(7), False, "deberia devolver False")

# Ahora, desde la linea de comandos del sistema operativo ejecutamos la prueba. De esta manera podemos ordenar la ejecucion 
# de un test unitario con tres niveles de granularidad:
#
# - A nivel del modulo completo
# - A nivel del caso de prueba (la clase derivada de la clase TestCase)
# - A nivel del test individual invocando el metodo "test_...." dentro de una subclase especifica
$ python -m unittest test.test_Par       # <---- En este caso se prueba todo lo contenido en la subclase "test_Par".
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


$ python -m unittest test.test_Par.test_esPar    # <---- En este caso se prueba el metodo "test_esPar" individualmente.
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK




#
# Otro modulo de pruebas es PYTEST. Veamos un ejemplo de como preparar y ejecutar una prueba muy simple.
#
# 1.- Creamos el fuente con las pruebas que llamaremos test_pytest.py (el prefijo test_ debe existir en el nombre!!)
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 2

# 2.- Salvamos este fuente y ejecutamos desde la linea de comandos del sistema operativo (en el mismo directorio donde se 
#     encuentra el fuente) el siguiente comando:
$ pytest test_pytest.py
============================= test session starts =============================
platform win32 -- Python 3.12.0, pytest-8.2.2, pluggy-1.5.0
rootdir: C:\Users\user\Desktop
collected 1 item

test_pytest.py F                                                         [100%]

================================== FAILURES ===================================
______________________________ test_with_fixture ______________________________

example_fixture = 1

    def test_with_fixture(example_fixture):
>       assert example_fixture == 2
E       assert 1 == 2

test_pytest.py:10: AssertionError
=========================== short test summary info ===========================
FAILED test_pytest.py::test_with_fixture - assert 1 == 2
============================== 1 failed in 0.07s ==============================

# Como podemos ver, pytest indica que la prueba ha fallado porque 1 no es igual a 2!!













#
# Sobre los modulos "shutil" y "psutil" para obtener informacion de File Systems, storage y procesos desde PYTHON.
#
# Un ejemplo de uso es el metodo ".disk_usage" que devuelve una Tupla conteniendo tres valores: total, used, free, los cuales pueden 
# asignarse o deconstruirse en tres variables para obtener informacion sobre el uso del espacio en disco:
#
import shutil

total, used, free = shutil.disk_usage('C:')

total
127364259840

used
94033154048

free
33331105792

# Podemos sacar (por ejemplo) el porcentaje de espacio aun libre en disco:
"{:.2f}".format(free / total * 100)
'26.17'


#
# Otro ejemplo es el metodo "cpu_percent" contenido en el modulo "cputil":
import psutil

psutil.cpu_percent()
41.2
psutil.cpu_percent()
28.2
psutil.cpu_percent()
28.0

# Es posible indicarle que muestre el porcentaje para cada CPU (en el caso de sistemas multi-nucleo):
psutil.cpu_percent(interval=1, percpu=True)
[15.6, 10.9, 4.6, 76.2]   # <------- Este sistema tiene 4 Logical Processors !!









#
# Sobre la lectura y escritura desde y hacia la entrada estandar (STDIN) y la salida estandar (STDOUT) en un PIPE usando 
# PYTHON.
#
# En este ejemplo usamos un script PYTHON (no ejecutable .exe). El modulo SYS permite a un script PYTHON
# acceder la entrada estandar. La funcion "print()" permite enviar a la salida estandar STDOUT:
import sys

for line in sys.stdin:
   print(line.strip())   # <---- Usamos el metodo "strip()" para eliminar cualquier espacio blanco en los extremos del mensaje.

# Ahora ejecutamos un "super comando" que procesa una linea de texto leida desde un archivo TXT, incluido nuestro script PYTHON:
$ cat test.txt | python test.py | tr ' ' '\n' | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head
      2 de
      1 una
      1 prueba
      1 linea
      1 esta
      1 es
      1 archivo

# Vemos como en una sola linea de comando invocamos varios "mini comandos" para crear un "super comando".
# El comando "tr" traslada o transforma un caracter en otro. En este ejemplo "tr" toma la salida estandar STDOUT de "cat" y 
# reemplaza todos los espacios blancos por el caracter de nueva linea "\n". Luego, la salida estandar de "tr" es enviada a 
# otra invocacion del mismo comando "tr" ahora para reemplazar las mayusculas por minusculas. Esto se conecta con la entrada 
# estandar del comando "sort" que ordena alfabeticamente las palabras recibidas. Despues, se envia al comando "uniq -c" que 
# tomara sin duplicados cada palabra y las cuenta dando como resultado cada palabra acompanada de el numero de veces que aparece. 
# Esto ultimo se envia esto al comando "sort -nr" que ordena en reverso numericamente y alfanumericamente lo que recibe. Al final 
# se envia el resultado hacia el comando "head" que imprime las primeras lineas de todo lo que recibe. Esta es la filosofia de 
# UNIX!!!!












#
# Sobre el modulo "subprocess" que permite ejecutar y obtener informacion de procesos desde PYTHON.
#
# IMPORTANTE: En Windows, para que el metodo "subprocess.run()" funcione bien es buena practica el pasarle el shell, que 
#             en el caso de Windows pudiera ser "powershell" o el "CMD". Ejemplo con powershell,
#
#             resp = subprocess.run(["powershell" "-command" "ls"], capture_output=True)
#
#             Ejemplo con CMD,
#
#             resp = subprocess.run(["CMD", "/c", "dir"], capture_output=True)
#
# NOTA:       El metodo "subprocess.Popen()" permite al proceso padre (el script PYTHON que inicio la ejecucion) seguir 
#             haciendo cosas, mientras que "subprocess.run()" bloquea el proceso padre hasta que el proceso hijo termina!!
#
import subprocess

#
# Supongamos que tenemos un programa llamado test.cpp y que retorna con codigo 3,
#
# #include <iostream>
#
# int main() { std::cout << "\n\nESTE ES UN PROCESO\n\n"; return 3; }
#

# Ejecutamos el programa desde PYTHON usando el metodo "run()" del modulo subprocess:
result = subprocess.run(["test", ""])

# Ahora, consultamos por el resultado del proceso:
result                                    
CompletedProcess(args=['test', ''], returncode=3)   # <---- Desde PYTHON podemos obtener el codigo de retorno del proceso!

# Tambien podemos obtener cualquier mensaje que dicho proceso haya enviado a la STDOUT. Ejemplo,
result = subprocess.run("test", capture_output=True)   # <---- Indicamos "capture_output=True"

result                                       
CompletedProcess(args='test', returncode=3, stdout=b'\r\n\r\nPROCESO EJECUTADO DESDE PYTHON\r\n\r\n', stderr=b'')

# Luego, podemos consultar cada respuesta a traves de las propiedades del subprocess siguientes:
result.stdout
b'\r\n\r\nPROCESO EJECUTADO DESDE PYTHON\r\n\r\n'   # <---- Esto devuelve el mensaje escrito por el proceso hacia la STDOUT.

# Es posible tambien consultar el standar error:
result.stderr

# Consultar el codigo de retorno devuelto por el comando ejecutado:
result.returncode                                             
3                                                   # <---- Con esta otra propiedad podemos ver el codigo devuelto por el proceso.

# Tambien podemos ejecutar comandos del sistema operativo. Ejemplo, ejecutemos "date" desde PYTHON,
#
subprocess.run(["date"])
Thu Jul 11 12:08:14 RDT 2024
CompletedProcess(args=['date'], returncode=0)

# Ejemplo del metodo "Popen()"
#
resp = subprocess.Popen(['powershell', 'python', 'test.py'], stdout=None, text=True)

# Al ejecutar la sentencia anterior, el script PYTHON puede continuar con su ejecucion. Luego de terminar, el proceso hijo
# activa todas las propiedades devueltas por "subprocess.Popen()". Por ejemplo, justo despues de la ejecucion de la sentencia 
# anterior, el script puede consultar el ID del proceso creado:
resp.pid
11032

# Si el proceso invocado (hijo) produce una salida podemos consultarla desde el script padre usando el metodo "communicate()".
# "communicate()" devuelve dos valores:
#
# resp.communicate()
# ('\nSaturday, July 13, 2024 11:44:56 AM\n\n\n', None)
#
# los cuales podemos asignar a variables dentro del script padre:
#
# t, _ = resp.communicate()
# t
# '\nSaturday, July 13, 2024 11:46:02 AM\n\n\n'
#
resp = subprocess.Popen(['powershell', 'date'], stdout=subprocess.PIPE, text=True)

t, _ = resp.communicate() 

t
'\nSaturday, July 13, 2024 11:46:02 AM\n\n\n'

resp.communicate
<bound method Popen.communicate of <Popen: returncode: None args: ['powershell', 'python', 'test.py']>>

# La manera que tiene nuestro script PYTHON de saber si el proceso hijo ha finalizado es a traves del metodo
# "poll()". Mientras el proceso hijo este en ejecucion "poll()" devuelve None. Luego de la ejecucion del proceso 
# hijo, al consultar "poll()" este devuelve el valor de retorno del proceso hijo (0 si todo salio bien) y esta es 
# la manera de conocer si el proceso hijo ha finalizado!!
#
resp = subprocess.Popen(['powershell', 'python', 'test.py'], stdout=None, text=True)
resp.poll()
resp.poll()   # <---- Aun no ha finalizado la ejecucion!
resp.poll()
resp.poll()
0             # <---- Listo! ha finalizado la ejecucion del proceso hijo!!!
# Tambien se puede consultar dicho codigo de retorno a traves del atributo ".returncode":
resp.returncode
0

#
# OJO!!! PENDIENTE POR CONOCER: Como puedo recibir mensajes provenientes del proceso hijo desde el padre en tiempo real?????
#




# IMPORTANTE: Con el modulo OS es posible, incluso, obtener (dentro del script PYTHON) una copia de las variables del 
#             ambiente. Luego, modificar dichas variables o anadir alguna variable nueva y pasar dicho ambiente a un 
#             proceso hijo ejecutado a traves del modulo SUBPROCESS. Veamos un ejemplo,
import os
import subprocess

my_env = os.environ.copy()   # <---- Obtenemos una copia del ambiente.

# Modificamos la variable de ambiente PATH para adicionar una ruta nueva:
my_env["PATH"] = os.pathsep.join(["\\test\\", my_env["PATH"]])      # <---- os.pathsep devuelve el caracter separador del 
                                                                    #       ambiente. En este ejemplo (Windows 10) es el ";".
                                                                    #       En este ejemplo usamos el metodo join (de String) para 
                                                                    #       obtener un String a partir de la lista conformada por
                                                                    #       la variable PATH y la nueva ruta que queremos incorporar.
                                                                    #       Esta variable PATH nueva puede, entonces, pasarse a un 
                                                                    #       proceso hijo!!

# Consultamos la variable PATH luego de anadir la ruta nueva:
my_env["PATH"]
'\\test\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\...'

type(os.pathsep)
<class 'str'>     # <---- os.pathsep es del tipo STRING!










#
# Como mostrar la hora y fecha del sistema desde PYTHON:
#
import datetime as dt

dt.datetime.now()

Salida:

datetime.datetime(2024, 4, 29, 21, 13, 19, 827137)








#
# Como mostrar la fecha de ultima modificacion de un objeto en el file system.
#
# NOTA: Esto se obtiene con el metodo "os.path.getmtime". Este devuelve la cantidad de segundos desde el inicio (en UNIX 01/01/1970).
#       Luego, para convertir este resultado en una fecha legible usamos el metodo "datetime.fromtimestamp" del modulo datetime!
#
import datetime as dt

dt.datetime.fromtimestamp(os.path.getmtime("test.txt"))
datetime.datetime(2024, 6, 27, 10, 20, 36, 526373)

# Tambien pudieramos convertirlo a string para luego obtener la fecha (ano, mes, dia, etc...)
str(dt.datetime.fromtimestamp(os.path.getmtime("test.txt")))[:10]
'2024-06-27'












#
# Ejemplos de lectura/escritura de archivos desde PYTHON.
#
# IMPORTANTE: Para leer archivos muy grandes es recomendable usar el metodo "readline()" que lee una sola fila 
#             del archivo a la vez.
#

#
# Ejemplo de leer y mostrar el contenido de un archivo texto:
#
F = open(r"test.cpp", "r")

# Lee todas las lineas del archivo y las coloca en una lista PYTHON.
cont = F.readlines()

# Ahora las mostramos:
for l in cont:
   print(l)


# Cerrar el archivo:
F.close()



#
# Lectura y escritura en archivos CSV usando el modulo CSV de PYTHON.
#
# IMPORTANTE: Los metodos reader, DictReader devuelven un objeto ITERABLE con el contenido del archivo leido.
#             El metodo "reader()" devuelve un iterador con cada fila leida desde el archivo como una LIST de sus columnas:
#             ['columna1', 'columna2', ...]. Podemos hacerlo consumible convirtiendolo en una LIST: variable = list(csv.reader(........)).
#             El metodo "DictReader()" devuelve un dictionary.
#
# IMPORTANTE: Para escribir en un archivo CSV desde PYTHON, al momento de hacer el OPEN del archivo debemos indicar "newline=''" para 
#             que PYTHON no incluya lineas en blanco intercaladas entre cada fila escrita!!
#
#!/usr/bin/env python

import os
import csv


def read_csv(filename):
  """
  For some CSV file it returns a dictionary of Departments.
  """
  dept = {}

  with open(filename, "r") as file:
    csv_f = csv.DictReader(file)
    for row in csv_f:
      if row["departamento"] not in dept:
        dept[row["departamento"]] = []
      dept[row["departamento"]].append(row["nombre"])

  return dept

def genera_reporte(departamentos, filename):
  """
  Crea el reporte con la cantidad de usuarios en cada Departamento.
  """
  #with open(filename, "w", newline='') as file:
  #  registro = ""

  for dept in departamentos:
    print("Dept: {} - Empleados: {}".format(dept, departamentos[dept]), end="\n")


os.chdir(r"/home/runner/pythonWorks")

lista_dept = read_csv("test.csv")

genera_reporte(lista_dept, "reporte.txt")





#
# Para escribir el contenido de un diccionario PYTHON en un archivo CSV:
#
import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})




#
# Practica en Quiklabs: Leer un archivo CSV de empleados y departamentos para crear un reporte de cantidad de empleados por 
# departamento!!
#
#!/usr/bin/env python3

import csv

csv.register_dialect('empDialect', skipinicialspace=True, strict=True)

def read_employees(csv_file_location):
   employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

   employee_list = []

   for data in employee_file:
      employee_list.append(dict(data))

   return employee_list


def process_data(employee_list):
   department_list = []

   for employee_data in employee_list:
      department_list.append(employee_data["Department"])

   department_data = {}

   for department_name in set(department_list):
      department_data[department_name] = department_list.count(department_name)

   return department_data


def write_report(dictionary, report_file):
   with open(report_file, "w+") as f:
      for k in sorted(dictionary):
         f.write(str(k) + ':' + str(dictionary[k]) + '\n')
      f.close()


employee_list = read_employees('/home/student/data/employees.csv')

dictionary = process_data(employee_list)

write_report(dictionary, '/home/student/data/report.txt')










#
# Determinar cual es el directorio actual (Get Current Working Directory).
#
import os

os.getcwd()





#
# El metodo "os.path.join" concatena los strings y arma un path de archivo con los separadores adecuados (para cada sistema operativo)
#
os.path.join(os.getcwd(), "test.txt")
'C:\\Users\\user\\Desktop\\test.txt'






#
# Como saber si el nombre es un directorio y no un archivo?
#
os.path.isdir("<nombre del archivo>")






#
# Como saber el tamano de un objeto en el sistema de archivos.
#
os.path.getsize("test.txt")
86





#
# Como renombrar un archivo desde PYTHON.
#
import os

os.rename("<nombre actual>", "<nombre nuevo>")







#
# Como eliminar un archivo desde PYTHON.
#
import os








#
# Conocer el directorio actual de trabajo.
#
import os

os.getcwd()





#
# Cambiar el directorio de trabajo y mostrar su contenido usando el modulo OS que ya viene en el PYTHON:
#
import os

os.chdir(r"C:\Users\user\Desktop")

for i in os.listdir():
      print(i)





#
# Como listar los objetos (archivos, carpetas) segun su nombre.
#
import os

# Indicamos el directorio o carpeta que queremos listar.
for nombre_archivo in os.listdir('.'):
   # Ahora indicamos la extension del archivo.
   if ".py" in nombre: 
      print(nombre)

Salida:

drawing.py
PYTHON_SUBPROCESS.py
QUIKLABS_REGEX.py
script.py
SPECTRE.py
test.py






#
# Como eliminar un directorio?
#
# IMPORTANTE: Al igual que con el comando "rmdir" del sistema operativo, este metodo de PYTHON requiere que el directorio a ser
#             removido deba estar vacio !!!
#
os.rmdir("<nombre del directorio>")








#
# Sobre el uso de la clase "os.environ" para leer las variables del ambiente desde un script PYTHON.
#
import os
import sys

#
# El tipo de dato de "os.environ" es de una class en formato de Dictionary:
#
> type(os.environ)
<class 'os._Environ'>

os.environ   # <---- Devuelve un tipo Dictionary en el cual cada valor de cada clave es un String!
environ({'ACLOCAL_PATH': 'C:\\Program Files\\Git\\mingw64\\share\\aclocal;C:\\Program Files\\Git\\usr\\share\\aclocal', 
         'ALLUSERSPROFILE': 'C:\\ProgramData', 
         'APPDATA': 'C:\\Users\\user\\AppData\\Roaming', 
         'CLASSPATH': 'C:\\Program Files\\Java\\jdk-18.0.2\\bin', ...........


# Cuando solicitamos una variable de emabiente especifica el tipo de dato devuelto es String. A este valor devuelto 
# podemos aplicarle el metodo "split()" para descomponer cada elemento. Por ejemplo, si pedimos el contenido de la variable 
# PATH, luego podemos imprimir cada ruta por separado:
 type(os.environ["PATH"])
<class 'str'>

# Aplicado a la variable PATH el metodo "split() con separador ; (en el caso de este ambiente Windows)"
rutas = os.environ["PATH"].split(";")

rutas   # <---- Es una LIST.
['C:\\Users\\user\\bin', 'C:\\Program Files\\Git\\mingw64\\bin', 'C:\\Program Files\\Git\\usr\\local\\bin', ...]

# Luego, para imprimir las rutas:
for ruta in rutas:
...     print("ruta: {}".format(ruta), end="\n")
...
ruta: C:\Users\user\bin
ruta: C:\Program Files\Git\mingw64\bin
ruta: C:\Program Files\Git\usr\local\bin
ruta: C:\Program Files\Git\usr\bin
ruta: C:\Program Files\Git\usr\bin
ruta: C:\Program Files\Git\mingw64\bin
ruta: C:\Program Files\Git\usr\bin
...










# -------------------------------------------------------------------------------------------------- #
# Lectura y procesamiento de argumentos en la linea de comandos durante la ejecucion de un programa. #
# Ejemplo:                                                                                           #
# C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32>python lineaco.py spam eggs cheese  #
# ['lineaco.py', 'spam', 'eggs', 'cheese']                                                           #
# -------------------------------------------------------------------------------------------------- #

# En el siguiente ejemplo el script pide el valor de la variable de ambiente PATH , descompone el String recibido 
# en una LIST y finalmente itera atraves de la LIST para mostrar todas las rutas que contiene la variable PATH.
#
# Ademas, se ejercita el manejo de argumentos de linea de comandos desde un script PYTHON.
#
import os
import sys

argumentos = sys.argv   # <---- Consulta los argumentos pasados en la linea de comandos.
                        #       El tipo de objeto devuelto es una LIST!!
print("Tipo de dato devuelto por sys.argv: {}".format(type(argumentos)), end="\n\n")

# Iteramos a traves de la LIST devuelta para mostrar cada argumento de la linea de comandos exceptuando el
# nombre del script mismo:
for i in argumentos:
        if i != "test.py": print("Argumento: {}".format(i), end="\n")


# Ahora vamos con el manejo de variables de ambiente desde un script PYTHON:
#
print("Ahora consultamos la variable de ambiente PATH:")

variables = os.environ["PATH"]   # <---- El tipo de objeto devuelto es un String!!

# Descomponemos el String devuelto (el separador en este ambiente Windows es ";"). Obtenemos una LIST.
rutas = variables.split(";")

# Ahora iteramos a traves de la LIST obtenida para mostrar cada ruta incluida en la variable de ambiente PATH:
for ruta in rutas: print("ruta: {}".format(ruta), end="\n")


# Por ultimo, simulamos el retornar con un codigo de error:
#
sys.exit(3)



# Ejecutamos el script desde la linea de comandos BASH indicando algunos parametros:
#
$ python test.py -i par1

# Esta parte del script debe mostrar lo siguiente:
#
Tipo de dato devuelto por sys.argv: <class 'list'>

Argumento: -i
Argumento: par1

Ahora consultamos la variable de ambiente PATH:
ruta: C:\Users\user\bin
ruta: C:\Program Files\Git\mingw64\bin
ruta: C:\Program Files\Git\usr\local\bin
ruta: C:\Program Files\Git\usr\bin
ruta: C:\Program Files\Git\usr\bin
ruta: C:\Program Files\Git\mingw64\bin
ruta: C:\Program Files\Git\usr\bin
....
..

#
# Para ver el codigo retornado por el script:
#
echo $?
3



#
# Esta funcion coloca los pares de argumentos estilo "-name value" (por ejemplo "-i data.txt") y los coloca en un diccionario.
#
def getopts(argv):
	opts = {}         # Diccionario que contendra la lista de argumentos obtenidos desde la linea de comandos.

	# Itera a traves de la lista de argumentos y si consigue alguno del estilo buscado ("-name value") entonces lo coloca en el diccionario.
	while argv:
		if argv[0][0] == '-':              # Busca los pares estilo "-name value".
			opts[argv[0]] = argv[1]        # La key del diccionario es el argumento "-name" (primero del par buscado).
			argv = argv[2:]
		else:
			argv = argv[1:]
	return opts

#
# Funcion main principal del programa.
#
if __name__ == '__main__':

	# se usa la libreria sys.
	from sys import argv

	# Con esta sentencia se pueden mostrar los argumentos leidos en la linea de comandos.
	# (En el atributo argv se guardan dichos argumentos)
	# print(sys.argv)

	myargs = getopts(argv)

	if '-i' in myargs:
		print(myargs['-i'])

	print(myargs)









#
# Leer y filtrar el contenido de un directorio usando wildcards. Para esto se utiliza el modulo "GLOB" que ya viene en el PYTHON.
#
# IMPORTANTE: GLOB admite un parametro ("recursive") que le indicaria si la busqueda debe hacerla de forma recursiva o no; 
#             es decir: si debe traer tambien los contenidos de los subdirectorios. Ejemplo:
#
#             files = glob.glob('/home/geeks/Desktop/gfg/**/*.txt', recursive = True) 
#
import glob

import os

os.chdir(r"C:\Users\user\Desktop")

# Observar que podemos usar wildcards tipo "*", "[0-9]" o "?"
allCPPs = glob.glob(r"*.cpp")

allCPPs

['lispy.cpp', 'test.cpp', 'vectores.cpp']








#
# Como saber si un archivo existe?
#
import os

os.path.exists("<nombre del archivo>")








#
# Como saber el tamano de un archivo?
#
os.path.getsize("<nombre del archivo>")

# retorna el tamano en Bytes.







# This code will provide a unix timestamp for the file
# Devuelve el timestamp de la ultima modificacion del archivo!
os.path.getmtime("spider.txt")

Salida:
1719476436.5263731    # <------ Representa la cantidad de segundos desde el 01/01/1970 !!!!


#This code will provide the date and time for the file in an 
#easy-to-understand format
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)

Salida:
datetime.datetime(2024, 6, 27, 10, 20, 36, 526373)









os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path

Salida:
'C:\\Users\\user\\Desktop\\test.txt'








#
# Uso del modulo "pathlib".
#
from pathlib import Path

path = Path()
WindowsPath('.')

path.parent
WindowsPath('.')
path = Path(os.getcwd())
path
WindowsPath('C:/Users/user/Desktop')
path.parent
WindowsPath('C:/Users/user')
path.parent.absolute()
WindowsPath('C:/Users/user')
print(path.parent.absolute())
C:\Users\user








#
# Como hacer que el script PYTHON retorne con un codigo de error (0, 1, 2, 3,...etc).
#
import sys

sys.exit(3)

# Desde la linea de comandos BASH ejecutamos el script:
python script.py

# Luego, en la linea de comandos del BASH,
echo $?
3       <---- La variable de ambiente "$?" contiene el valor retornado por el ultimo comando ejecutado!














# Ejemplos de uso de EXPRESIONES REGULARES (REGEX) en PYTHON, a traves del modulo "re".
#
# NOTA:       Las Regular Expressions en PYTHON parece que siguen el estandar que siguen comandos como GREP en Unix. Ejemplo,
#
#             $ ls -l | grep -E "(\w+)\.js"
#             -rw-r--r-- 1 user 197121    3744 Jan  8  2019 Ejemplo_itera_array_for_map.js
#             -rw-r--r-- 1 user 197121 1071472 Aug 16  2022 jsonEjercicio.json
#             -rw-r--r-- 1 user 197121     160 Aug  8  2022 jsonTest.json
#             -rw-r--r-- 1 user 197121   17894 Apr  9 19:03 nodef.js
#
#             $ ls -l | grep -E "(\w+)\.js$"
#             -rw-r--r-- 1 user 197121    3744 Jan  8  2019 Ejemplo_itera_array_for_map.js
#             -rw-r--r-- 1 user 197121   17894 Apr  9 19:03 nodef.js
#
#
#             La siguiente nota es tomada de Wikipedia,
#
#             The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene 
#             formalized the concept of a regular language. They came into common use with Unix text-processing utilities. 
#             Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard 
#             and another, widely used, being the Perl syntax. 
#
# IMPORTANTE: En el manejo de las funciones y metodos del modulo RE en PYTHON, cuando indicamos una REGEX siempre debemos indicarla como
#             una raw string, es decir: re.search(r".......", "texto de ejemplo....."). Esto es necesario porque las REGEX pudieran incluir 
#             secuencias como por ejemplo "\n" la cual tiene otro significado en otro contexto de PYTHON (significa newline character)!!!
#
# NOTA:       "\w" significa cualquier caracter alfanumerico (a-z, A-Z, 0-9) o el caracter underscore "_". Veamos un ejemplo,
#
#             re.search("\w*", "Esta es una prueba")   # <---- devolvera "Esta" porque el espacio blanco " " no esta incluido en el conjunto de
#                                                              caracteres representado por "\w" !!!!
#
# NOTA:       "\s" significa caracter espacial (espacio blanco, tab o newline).
#
# NOTA:       "\d" significa un caracter numerico (0-9). Tambien lo es "[0-9]".
#
# NOTA:       La manera de indicar a RE que un determinado caracter o tipo de caracter se repite es con "{n}" o "{n,m}" o "{n,}".
#             Ejemplo,
#
#             re.search(r"\[(\d{5})\]", "El proceso [72623] esta detenido en linea 186")   # <---- Aqui {5} indica a RE que el caracter numerico 
#                                                                                                  anterior se repite cinco veces!
#
# NOTA:       "\b" significa word boundaries. Sirve para indicarle a RE que localice solo las palabras (o secuencias) que cumplan con un patron.
#                  Es decir: palabras individuales (separadas de su texto por espacios). Esto es muy util para el metodo "findall()". 
#                  Ejemplo,
#
#                  re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
#                  ['scary', 'ghost']   # <---- Recordemos que "findall" devuelve una LIST conteniendo los resultados.
#                                               Aqui vemos como "\b" aisla las palabras y ayuda a que RE encuentre UNICAMENTE las palabras que
#                                               complan con la condicion (cinco caracteres). Si no se colocara "\b" RE devolveria tambien "apper"!!!!
#
#                  Otro ejemplo, supongamos que queremos extraer dos palabras (que tienen ciertas caracteristicas) desde un texto,
#
#                  re.findall(r"\b(P\w+|T\w+)\b", "Primera Segunda Tercera y Cuarta")
#                  ['Primera', 'Tercera']   # <---- Observar que utilizamos el operador "|" de alternativa para que RE busque toda palabra 
#                                                   que inicie con "P" O "T". Observar ademas que colocamos toda la expresion dentro de una 
#                                                   Capture Group rodeada de "\b" para que RE localice unicamente palabras individuales!!!
#
#
# NOTA:       El metodo "sub()", una vez que encuentra una secuencia que cumple con el patron buscado la reemplaza con un texto.
#             Su sintaxis es: re.sub(r"<patron de busqueda>", r"<texto de reemplazo>", "<string>"). Ejemplo,
#
#             re.sub(r"([A-Z])\.\s+(\w+)\s+", r"Mr. \2", "A. Weber and B. Bellmas have joined the team.")
#             'Mr. and Mr. have joined the team.'   # <---- Substituye "A. " y "B. " por "Mr. ". El "\2" se llama Backreference y es como una 
#                                                           variable. En este ejemplo, dicha Backreference hace referencia al segundo 
#                                                           Capture Group (en este ejemplo seria el nombre de la persona representado por el patron (\w+))!!!
#
# NOTA:       El metodo "split()" sirve para separar cadenas usando un patron de separacion.
#
#             L = re.split(r"\-", "Primero-Segundo-Tercero-Cuarto")
#             ['Primero', 'Segundo', 'Tercero', 'Cuarto']   # <---- En este ejemplo el patron de separacion es "-". El metodo split devuelve una LIST!!
#             L[1]
#             'Segundo'
#
#
# IMPORTANTE: Hay que entender que las REGEX en PYTHON (y en cualquiera de sus implementaciones ejemplo Unix, Linux) siempre devuelven la 
#             primera coincidencia que encuentran partiendo de izquierda a derecha en el texto. Luego, tenemos el metodo "findall()" que veremos 
#             mas adelante.
#
# NOTA:       El punto "." indica CUALQUIER CARACTER incluido el newline. Es un WILDCARD que indica cualquier caracter, pero SOLO UNO!!
#             Para indicar un carcater pero no cualquiera sino uno con ciertas caracteristicas usamos "Character Classes".
#
#             En las "Character Classes", cuando vamos a buscar coincidencia con UN SOLO CARACTER (como "p" o "P") podemos expresarlo 
#             [pP] o tambien con el signo OR asi [p|P]. La Character Class aplica para un solo caracter. Ejemplo,
#
#             print(re.search("[\d+] [\d+]", "Esta es una 765 123 prueba de numero"))
#             <re.Match object; span=(14, 17), match='5 1'>
#
#             Ahora eliminamos el espacio en medio,
#
#             print(re.search("[\d+][\d+]", "Esta es una 765 123 prueba de numero"))
#             <re.Match object; span=(12, 14), match='76'>
#
# NOTA:       En las expresiones regulares existen los llamados Capturing Groups "(....)". En cada Capturing Group podemos colocar un patron a buscar 
#             para luego extraerlo del resultado a traves de un indice. Ejemplo,
#
#             r = re.search(r"\[(\d+)\]\: (\w+) ", "El codigo del proceso [37262]: ERROR en lectura.")
#
#             # En este ejemplo indicamos a RE dos Capturing Groups: (\d+) y (\w+) correspondientes al codigo del proceso y al mensaje.
#             r
#             <re.Match object; span=(22, 37), match='[37262]: ERROR '>
#
#             r.groups()
#             ('37262', 'ERROR')   # <---- Si invocamos el metodo "groups()" nos devuelve los Capturing Groups del resultado.
#
#             # Luego, para acceder de forma individual a cada Capturing Group:
#             re[0]
#             '[37262]: ERROR '   # <---- Devuelve un string conteniendo todo lo encontrado por RE
#             re[1]               # <---- Ahora solicitamos el primer Capturing Group 
#             '37262'
#             re[2]               # <---- Solicitamos el segundo Capturing Group
#             'ERROR'
#
#             Esto de los Capturing Groups es muy util para, por ejemplo, extraer los elementos de una busqueda de un patron de numero telefonico pero 
#             hay muchos otros casos de uso,
#
#             resultado = re.search(r"(\+\d{2}) (\d{9})", " El numero de telefono es +34 900347156 en Espana.")
#
#             resultado
#             <re.Match object; span=(26, 39), match='+34 900347156'>
#
#             resultado.groups()
#             ('+34', '900347156')   # <---- Nos muestra todos los Capturing Groups contenidos en el hayazgo.
#
#             resultado[0]
#             '+34 900347156'        # <---- En el indice 0 almacena todo el hayazgo en formato string.
#             resultado[1]
#             '+34'                  # <---- El indice 1 almacena el primer Capturing Group (codigo de pais).
#             resultado[2]
#             '900347156'            # <---- El indice 2 almacena el segundo Capturing Group (numero de telefono).
#
# NOTA:       En el ejemplo anterior vimos la sintaxis 
#
# NOTA:       En las expresiones regulares existen los llamados Quantifiers. Los mas usados son * y +. 
#             * representa una, varias o cero coincidencias.
#             El + representa una o varias coincidencias (pero no cero coincidencias). Ejemplos,
#
#             print(re.search("5.* ", "Esta es un texto 55 de prueba"))
#             <re.Match object; span=(17, 23), match='55 de '>   # <---- Devuelve, a partir del caracter "5", el resto del texto. Aqui lo importante es
#                                                                        que el cuantificador indica repeticion del caracter que le precede en la expresion,
#                                                                        en este ejemplo seria el "." que indica uno o mas caracteres. Por tal motivo RE 
#                                                                        devuelve todo el texto a partir del "5" !!!
#
#             Otro ejemplo,
#
#             print(re.search("5\d*", "Esta es un texto 55 de prueba"))
#             <re.Match object; span=(17, 19), match='55'>   # <---- Devuelve, a partir del "5", cualquier repeticion de un digito numerico!!
#
# NOTA:       Otra manera de indicar repeticion de un caracter o character class es "{..}". Ejemplo,
#
#             re.search(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", "El telefono 111-222-3333 es de Soporte Tecnico")
#             <re.Match object; span=(12, 24), match='111-222-3333'>   # <---- El {3} indica secuencia de tres caracteres como indicados en el
#                                                                              character class "[0-9]".
#
# ATENCION:   Hay que ser cuidadosos con estos cuantificadores, en especial ".*" porque representa repeticion de cualquier caracter incluido espacio
#             blanco e incluido ningun caracter (* es uno, varios o ningun caracter). Ejemplo,
#
#             re.search(r"Py.*n", "Python Programming")
#             <re.Match object; span=(0, 17), match='Python Programmin'>   # <---- En este caso RE consigue la secuencia "Py" seguida de varios
#                                                                                  caracteres (incluido el espacio) y llega hasta el ultimo "n"!!!!!!
#
# NOTA:       El caracter especial "?" indica ocurrencia o no ocurrencia de un caracter indicado antes del "?". Ejemplo,
#
#             re.search("p?ar", "Este es una secuencia @sigamos nadie @ la partesera@ y la otra")
#             <re.Match object; span=(42, 45), match='par'>   # <----- Lo encontro! y por tanto devuelve la secuencia indicada
#
#             ahora veamos cuando no hay "p",
#             re.search("p?ar", "Este es una secuencia @sigamos nadie @ la artesera@ y la otra")
#             <re.Match object; span=(42, 44), match='ar'>   # <---- Igual devuelve la secuencia detectada porque la "p" es opcional!!!
#
#
# IMPORTANTE: El OR "|" sirve tambien para encontrar palabras enteras, es decir: <una palabra>|<otra palabra>. Ejemplo,
#
#             re.search("una|otra", "texto.....")
#
#             El resultado de este comando devuelve la primera coincicencia del patron, contando de izquierda a derecha. PERO, si queremos 
#             que RE nos devuelva todas las coincidencias podemos usar el metodo "re.findall()". Ejemplo,
#
#             r = re.findall("perro|gato|gallina", "Este es un gato o una gallina o un perro?")
#             r
#             ['gato', 'gallina', 'perro']   # <---- Devuelve una LIST contenido todas las coincidencias!!!
#
#             r[0]
#             'gato'
#             r[1]
#             'gallina'
#              r[2]
#              'perro'
#
#             Tambien podemos incluir dentro de una Character Class varios rangos: "[a-zA-Z0-9]". En este ejemplo le indicamos a RE que 
#             lo buscado puede coincidir con cualquier caracter alfabetico (mayuscula o minuscula) o con cualquier caracter numerico.
#
#             Para indicarle a RE que queremos una coincidencia negada, es decir que NO sea tal cosa: "[^....tal cosa...]". Esta complementacion 
#             o negacion aplica UNICAMENTE cuando la colocamos dentro de corchetes (bracket espression) [^....] !!!!!!!!!
#
#             Ejemplo, si queremos encontrar algun caracter que NO sea alfanumerico, 
#
#             print(re.search(r"[^a-zA-Z]", "nn Este omienza con vocal"))         
#             <re.Match object; span=(2, 3), match=' '>    # <----- Devuelve el primer espacio blanco que encuentra de izquierda a derecha!
#
#             Pero, si ahora queremos que cuente espacios blancos incluso,
#
#             print(re.search(r"[^a-zA-Z] ", "nn Este omienza con vocal"))   # <---- Incluimos un espacio " " en la Character Class
#             None    # <----- Devuelve "No Value"!!
#
#             Otra cosa que podemos hacer es indicar a RE que encuentre una repeticion de un caracter especifico. Para esto usamos ".*".
#             Ejemplo,
#
# IMPORTANTE: Algunas expresiones regulares funcionan de forma diferente en comandos como GREP y en Python. Ejemplo: "\d" y "[0-9]". Para que 
#             grep acepte todas las expresiones regulares POSIX debemos indicarle la opcion "grep -E" (que significa extendido) o usar el 
#             comando "egrep"!!
#
#             A proposito de GREP, la opcion "-o" le indica a GREP que devuelva el string correspondiente a la coincidencia.
#             Ejemplo,
#
#             $ echo "El numero es +34-618675423" | grep -E "\+[0-9]{2}\-[0-9]{9}" -o
#               +34-618675423
#
#             Mirar la seccion "BASH" mas abajo en esta guia.
#
#
# NOTA:       En RE existe algo llamado "lookahead" que sirve para encontrar una secuencia siempre y cuando dicha secuencia este seguida 
#             de un patron. La sintaxis es re.search(r"patron a buscar(?=<patron que le sigue>)", "<texto>"). "(?=)" es lo que identifica 
#             a una lookahaead. Ejemplo,
#
#             hayazgo = re.search(r"(\w+)\=(?=\[0001\])", "MENSAJE1=[0098], MENSAJE2=[0001], MENSAJE3=[0035]")
#             hayazgo.groups()
#             ('MENSAJE2',)
#             hayazgo[1]
#             'MENSAJE2'   # <---- En este ejemplo vemos como RE encuentra una coincidencia: MENSAJE2 precede al lookahead indicado [0001]
#
# NOTA:       Tambien existe algo llamado "lookbehind" cuya sintaxis es re.search(r"(?<=patron que le precede)<patron a buscar>", "<texto>")
#
#
#
# NOTAS TOMADAS DE LA PAGINA DEL GNU "https://www.gnu.org/software/gawk/manual/html_node/Regexp-Operator-Details.html":
# --------------------------------------------------------------------------------------------------------------------
# . (period)
#
# This matches any single character, including the newline character. For example, ‘.P’ matches any single character followed by a ‘P’ in a string. 
# Using concatenation, we can make a regular expression such as ‘U.A’, which matches any three-character sequence that begins with ‘U’ and ends with ‘A’.
#
# In strict POSIX mode (see Command-Line Options), ‘.’ does not match the NUL character, which is a character with all bits equal to zero. 
# Otherwise, NUL is just another character. Other versions of awk may not be able to match the NUL character.
#
# […]
#
# This is called a bracket expression. It matches any one of the characters that are enclosed in the square brackets. 
# For example, ‘[MVX]’ matches any one of the characters ‘M’, ‘V’, or ‘X’ in a string. A full discussion of what can be inside the square brackets 
# of a bracket expression is given in Using Bracket Expressions.
#
# [^…]
#
# This is a complemented bracket expression. The first character after the ‘[’ must be a ‘^’. It matches any characters except those in the square brackets. 
# For example, ‘[^awk]’ matches any character that is not an ‘a’, ‘w’, or ‘k’.
#
# |
#
# This is the alternation operator and it is used to specify alternatives. The ‘|’ has the lowest precedence of all the regular expression operators. 
# For example, ‘^P|[aeiouy]’ matches any string that matches either ‘^P’ or ‘[aeiouy]’. This means it matches any string that starts with ‘P’ or 
# contains (anywhere within it) a lowercase English vowel.
#
# The alternation applies to the largest possible regexps on either side.
#
# (…)
#
# Parentheses are used for grouping in regular expressions, as in arithmetic. They can be used to concatenate regular expressions containing 
# the alternation operator, ‘|’. For example, ‘@(samp|code)\{[^}]+\}’ matches both ‘@code{foo}’ and ‘@samp{bar}’. 
# (These are Texinfo formatting control sequences. The ‘+’ is explained further on in this list.)
#
# The left or opening parenthesis is always a metacharacter; to match one literally, precede it with a backslash. However, 
# the right or closing parenthesis is only special when paired with a left parenthesis; an unpaired right parenthesis is (silently) treated 
# as a regular character.
#
# *
#
# This symbol means that the preceding regular expression should be repeated as many times as necessary to find a match. For example, ‘ph*’ 
# applies the ‘*’ symbol to the preceding ‘h’ and looks for matches of one ‘p’ followed by any number of ‘h’s. This also matches just ‘p’ 
# if no ‘h’s are present.
#
# There are two subtle points to understand about how ‘*’ works. First, the ‘*’ applies only to the single preceding regular expression component 
# (e.g., in ‘ph*’, it applies just to the ‘h’). To cause ‘*’ to apply to a larger subexpression, use parentheses: ‘(ph)*’ matches ‘ph’, ‘phph’, 
# ‘phphph’, and so on.
#
# Second, ‘*’ finds as many repetitions as possible. If the text to be matched is ‘phhhhhhhhhhhhhhooey’, ‘ph*’ matches all of the ‘h’s.
#
# +
#
# This symbol is similar to ‘*’, except that the preceding expression must be matched at least once. This means that ‘wh+y’ would match 
# ‘why’ and ‘whhy’, but not ‘wy’, whereas ‘wh*y’ would match all three.
#
# ?
#
# This symbol is similar to ‘*’, except that the preceding expression can be matched either once or not at all. For example, ‘fe?d’ matches ‘fed’ 
# and ‘fd’, but nothing else. 
#
# {n}
# {n,}
# {n,m}
#
# One or two numbers inside braces denote an interval expression. If there is one number in the braces, the preceding regexp is repeated n times. 
# If there are two numbers separated by a comma, the preceding regexp is repeated n to m times. If there is one number followed by a comma, 
# then the preceding regexp is repeated at least n times:
#
# wh{3}y
#
# Matches ‘whhhy’, but not ‘why’ or ‘whhhhy’.
#
# wh{3,5}y
#
# Matches ‘whhhy’, ‘whhhhy’, or ‘whhhhhy’ only.
#
# wh{2,}y
#
# Matches ‘whhy’, ‘whhhy’, and so on. 
#
# In regular expressions, the ‘*’, ‘+’, and ‘?’ operators, as well as the braces ‘{’ and ‘}’, have the highest precedence, followed by concatenation, 
# and finally by ‘|’. As in arithmetic, parentheses can change how operators are grouped.
#
# According to the POSIX specification, when ‘*’, ‘+’, ‘?’, or ‘{’ are not preceded by a character, the behavior is “undefined.” In practice, for gawk, 
# the ‘*’, ‘+’, ‘?’ and ‘{’ operators stand for themselves when there is nothing in the regexp that precedes them. For example, /+/ matches 
# a literal plus sign. However, many other versions of awk treat such a usage as a syntax error. 
#
#
#
# ALGUNAS NOTAS TOMADAS DEL CHEAT SHEET del curso Python "Using Python to Interact with the Operating System":
# -----------------------------------------------------------------------------------------------------------
# A regular expression—sometimes called regex—is a string of characters that specifies a pattern to match against some text. 
# In addition to matching patterns, they can search to extract specific parts of text, validate input data, and are supported by code editors 
# and integrated development environments (IDEs). In this reading, you will look at some examples of common regexes used in coding. 
#
# Regex examples
#
# r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.
#
# r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.
#
# r”^(.+)\/([^\/]+)\/” This line of code matches any path and filename.    <----- OJO: Lo probe y tiene un error!!!!!!
#
# Helpful tool
# Sometimes regexes can be complex and difficult to read and understand—even for experienced programmers! 
# There are tools available to help break down the regex and explain what each part of the expression does. 
# A common tool that you can use to help with understanding each stage of a regular expression is:
#
# https://regex101.com/
#
#
# Advanced regular expressions—commonly referred to as advanced regexes—are used by developers to execute complicated pattern matching 
# against strings.
#
# Alterations
#
# An alteration matches any one of the alternatives separated by the pipe | symbol. Let’s look at an example:
#
# r"location.*(London|Berlin|Madrid)" 
#
# This line of code will match the text string location is London, location is Berlin, or location is Madrid.
#
#
# Matching only at the beginning or end
#
# If you use the circumflex symbol (also known as a caret symbol) ^ as the first character of your regex, it will match 
# only if the pattern occurs at the start of the string. Alternatively, if you use the dollar sign symbol $ at the end of a regex, 
# it will match only if the pattern occurs at the end. Let’s look at an example:
#
# r”^My name is (\w+)” 
#
# This line of code will match My name is Asha but not Hello. My name is Asha.
#
#
# Character ranges
#
# Character ranges can be used to match a single character against a set of possibilities. Let’s look at a couple of examples:
#
# r”[A-Z] This will match a single uppercase letter.
#
# r”[0-9$-,.] This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.
#
# The two examples above are often combined with the repetition qualifiers. Let’s look at one more example:
#
# r”([0-9]{3}-[0-9]{3}-[0-9]{4})”
#
# This line of code will match a U.S. phone number such as 888-123-7612.
#
#
# Backreferences
#
# A backreference is used when using re.sub() to substitute the value of a capture group into the output. Let’s look at an example:
#
# >>> re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)
#
# This line of code will produce Ms. Weber and Ms. Bellmas have joined the team.
#
#
# Lookahead
#
# A lookahead matches a pattern only if it’s followed by another pattern. Let’s look at an example:
#
# If the regex was r”(Test\d)-(?=Passed)” and the string was “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:
#
# Test1, Test2, Test4
#
# Key takeaways
#
# The types of advanced regular expressions explained in this reading are just some of the more commonly used ones by developers. 
# They are beneficial in pattern matching, text manipulation, and data validation. For more information, check out the following link:
#
# https://regexcrossword.com/
#
#
#
#
# A continuacion algunos ejemplos hechos por mi cuenta y algunos sacados de los tests del curso:
#
# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains 
# alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, 
# followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular 
# expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, 
# and character classes.
#
import re
def check_web_address(text):
  pattern = r"^[a-zA-Z_-]+\.?[a-zA-Z0-9_-]+\.?[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True



#
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, 
# followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. 
# Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
#
import re
def check_time(text):
  pattern = "^[1]?[0-9]\:[0-5][0-9][ ]?[aA]?[pP]?[mM]$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False




# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
# with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. 
# For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return 
# True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 
#
import re
def contains_acronym(text):
  pattern = "\([A-Z0-9][a-zA-Z]+\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



# An intern implemented a zip code checker, but it works only with five-digit zip codes. Your task is to update the checker so that 
# it includes all nine digits of the zip code; the leading five digits and the optional four after the hyphen. The zip code needs to be 
# preceded by at least one space, and cannot be at the start of the text. Update the regular expression.
import re

def correct_function(text):
  result = re.search(r"^.* [0-9]{5}[\-]?(.*)?[0-9]{4}.*", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False



#
# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
#
import re
def multi_vowel_words(text):
  pattern = r"\b([a-zA-Z]+[aeiou]{3,}[a-zA-Z]+)\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []



#
# The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 
# 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
# Fill in the regular expression to complete this function.
import re
def convert_phone_number(phone):
  result = re.sub(r"(\d{3})\-(\d{3})\-(\d{4}).\$", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



#
# Fill in the code to check if the text passed contains punctuation symbols: 
# commas, periods, colons, semicolons, question marks, and exclamation points.
import re

def check_punctuation (text):
   #
   # En este caso el backslash "\" anula la interpretacion del caracter siguiente. El caracter "|" significa un OR o alternativa.
   #
   result = re.search(r"\.|\,|\:|\;|\?|\!", text)
   return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


#
# Otro ejemplo: buscar si existe el patron <cualquier digito numerico><algun signo de puntuacion como los del ejemplo anterior>
#
print(re.search(r"[0-9][\.|\,|\;|\:|\?|\!]", "Et xenguaje* 56Python +5? es bueno"))
<re.Match object; span=(23, 25), match='5?'>


# Otro ejemplo:
print(re.search(r"\+(\d+) (\d+)", "El numero es +34 601518619 "))
<re.Match object; span=(13, 26), match='+34 601518619'>


# Otro ejemplo, pero ahora colocando en una variable el resultado de la busqueda (en este caso el numero telefonico).
#
# NOTA: Observar que el metodo "groups" devuelve una tupla con los strings encontrados. Luego, convertimos dicha tupla en 
#       un string y lo asignamos a una variable. Este es un ejemplo de cosas que podemos hacer con el modulo "re"!!!
texto = "El numero telefonico es +34 610908765, para todo usuario"
resultado = re.search(r"(\+\d+) (\d+)", texto)   # <---- los parentesis son un "Capture Group" en REGEX!!!
resultado.groups()

('+34', '610908765')    # <--------- DEVUELVE UNA TUPLA!!
resultado.groups()[0]  
'+34'
resultado.groups()[1]
'610908765'

telf = " ".join(resultado.groups())   # <----- Convertimos a string y asignamos a variable.

telf
'+34 610908765'


#
# Otro ejemplo de reconocimiento de digitos numericos:
#
re.search("\d+\.\d+\.\d+\.\d+", "El servidor es: [hostOne] y su ip es 192.168.101.23")
<re.Match object; span=(37, 51), match='192.168.101.23'>

# es equivalente a,

re.search("[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9]", "El servidor es: [hostOne] y su ip es 192.168.101.023")
<re.Match object; span=(37, 51), match='192.168.101.02'>

# y tambien a,

re.search("\d\d\d\.\d\d\d\.\d\d\d\.\d\d", "El servidor es: [hostOne] y su ip es 192.168.101.23")
<re.Match object; span=(37, 51), match='192.168.101.23'>


#
# Otro ejemplo de reconocimiento de caracteres alfabeticos,
#
re.search("\[\w+\]", "El servidor es: [hostOne] y su ip es 192.168.101.023")
<re.Match object; span=(16, 25), match='[hostOne]'>

# es equivalente a,

re.search("\[[a-zA-Z]+\]", "El servidor es: [hostOne] y su ip es 192.168.101.023")
<re.Match object; span=(16, 25), match='[hostOne]'>


#
# Otro ejemplo: usar el metodo "findall" para obtener una LIST conteniendo cada palabra que existe en un texto:
#
L = re.findall("\w+", "Este es un ejemplo de parrafo interesantisimo")
L
['Este', 'es', 'un', 'ejemplo', 'de', 'parrafo', 'interesantisimo']

# Tambien podemos expresar la REGEX asi:
re.findall("[a-zA-Z0-9]+", texto)
['Este', 'es', 'un', 'ejemplo', 'de', 'parrafo', 'interesantisimo']

# Y tambien puediera hacerse asi:
L = re.findall("[a-zA-Z]+| [a-zA-Z]+ | [a-zA-Z]+", texto)
L
['Este', ' es ', 'un', ' ejemplo ', 'de', ' parrafo ', 'interesantisimo']

# Por ultimo le aplicamos el metodo "strip()" para eliminar espacios a izquierda y derecha de cada palabra:
T = []
for l in L: T.append(l.strip())
T
['Este', 'es', 'un', 'ejemplo', 'de', 'parrafo', 'interesantisimo']


# Los tres ejemplos anteriores de uso de una REGEX son equivalentes a usar el metodo "split" sobre un string:
L = "Este es un ejemplo de parrafo interesantisimo".split()
L
['Este', 'es', 'un', 'ejemplo', 'de', 'parrafo', 'interesantisimo']


#
# Ejemplo de uso del metodo "split()". Este metodo sirve para separar cadenas usando un patron de separacion.
#
L = re.split(r"\-", "Primero-Segundo-Tercero-Cuarto")
['Primero', 'Segundo', 'Tercero', 'Cuarto']   # <---- En este ejemplo el patron de separacion es "-". El metodo split devuelve una LIST!!
L[1]
'Segundo'


#
# Otro ejemplo: Encontrar una direccion de correo dentro de un texto:
#
print(re.search("[a-zA-Z0-9\.\_]+@[a-zA-Z\.\_]+", "El email es: pedro.fernandez@gmail.com en este servidor"))
<re.Match object; span=(13, 38), match='pedro.fernandez@gmail.com'>


#
# Otro ejemplo: Encontrar una secuencia consistente en a lo minimo dos grupos de caracteres alfanumericos 
# (incluidas letras, numeros y underscore) y separados por uno o varios espacios blancos.
#
result = re.search(r"\w+\s+\w+", text)


#
# El siguiente ejemplo es tomado de un quitz del curso:
#
# We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. 
# We can read each line of the syslog and pass the contents to the show_time_of_pid function. 
# Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
def show_time_of_pid(line):
  pattern = r"^([a-zA-Z]{3} [0-9]{1,} [0-9]{2}\:[0-9]{2}\:[0-9]{2}) (\w+\.\w+) .+\[([0-9]{5})\]\:"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[3])

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
Jul 6 14:05:01 pid:29440












#
# Sobre la identificacion del modulo principal en PYTHON a traves de la built-in variable "__name__".
#
# COMENTARIO: El modulo ejecutado por el interprete de PYTHON se convierte en el principal. Para dicho modulo, 
#             la variable "__name__" asume el valor "__main__". Si dicha variable es consultada desde un modulo 
#             importado desde otro modulo principal, entonces la variable se activa con el nombre del modulo importado. 
#             En el ejemplo siguiente, se consulta dicha variable tanto desde el modulo principal.py como desde el modulo
#             importado libreria.py.

# Modulo libreria.py (es usado desde el modulo principal.py pero tambien puede ser ejecutado directamente):
sum = lambda x, y : x + y

fib = lambda x : x if x == 0 or x == 1 else fib(x-1) + fib(x-2)

def iden() : print(f"\n\nNombre desde libreria.py: {__name__}")

iden()



# Modulo principal.py:
import libreria

total = 0

def suma(n) : global total; total = total + n

def main() :
   #print(" 3 + 2 = " + str(lib.sum(2, 3)))
   #suma(16)
   #print("\n\nTotal = " + str(total))
   #print(f"\n\nTotal = {total}")
   print(f"El Fibonacci de 7 = {libreria.fib(7)}\n\n")

if __name__ == "__main__" : main()



# Ejecutamos el modulo principal.py:
$ python principal.py

Nombre desde libreria.py: libreria
El Fibonacci de 7 = 13

Nombre del modulo: __main__

Nombre desde libreria.py: libreria


# Ahora ejecutamos el modulo libreria.py:
$ python libreria.py

Nombre desde libreria.py: __main__












#
# Ejemplo de manejo de archivos texto con Python.
#
# Las opciones van desde "w" hasta "r" pasando por "w+" (lectura y escritura) y "a" (append).
# El caracter "r" (al inicio del nombre del archivo) evita que Python interprete caracteres especiales en el nombre o path.
# El "with" incluye la ejecucion de una sentencia close(), asi que no hay necesidad de hacerla explicita. Ademas, es una 
# manera elegante de englobar las operaciones sobre el archivo que se abre.
with open(r"prueba.txt", "w") as f:
   # Ejemplo de escritura de multiples lineas en un archivo texto. Se crea una lista conteniendo las lineas.
   L = ["(define (fib n)", "	    (cond ((= n 0) 0)", "	    	  ((= n 1) 1)", "	    	  (else (+ (fib (- n 1)) (fib (- n 2))))))"]

   for line in L:
      # Existen tambien los metodos write y read.
      f.writelines(line + '\n')

f.close()

Resultado:
~/pyWorks$ cat prueba.txt

(define (fib n)
        (cond ((= n 0) 0)
              ((= n 1) 1)
              (else (+ (fib (- n 1)) (fib (- n 2))))))












#
# Ejemplo de asserts.
#
>>> number = 42
>>> assert number > 0

>>> number = -42
>>> assert number > 0
Traceback (most recent call last):
    ...
AssertionError














#
# Instalar el modulo openpyxl para manejar hojas Excel desde Python!
#
# IMPORTANTE: La libreria PANDAS tambien tiene capacidad para almacenar un Dataframe en un archivo Excel con "to_excel(...)"!!!
#
pip install openpyxl

Collecting openpyxl
  Downloading openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
     ---------------------------------------- 250.0/250.0 kB 1.5 MB/s eta 0:00:00
Collecting et-xmlfile (from openpyxl)
  Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-1.1.0 openpyxl-3.1.2

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip


#
# Ejemplo de uso del modulo openpyxl para crear una hoja Excel con algunas formulas.
#
from openpyxl import Workbook

filename = "miHoja.xlsx"
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "=3+2"
sheet["B1"] = "26"

workbook.save(filename=filename)













# IMPORTANTE: PYTHON NO TIENE un tipo array. En su lugar podemos usar LISTs.
#
# Como inicializar una LIST con un numero determinado de elementos (como si fuera un array).
#
A = [0]*10

# La sentencia anterior creara una LIST con diez elementos!
A
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]











#
# Como llenar una lista con una sucesion de valores en PYTHON:
#
# Aqui creamos una lista con los numeros naturales entre 0 y 9:
A = list[range(10)]













#
# Como leer un JSON desde una URL. Es una forma equivalente al "fetch().then().then()" en javaScript
#
# El modulo requests posiblemente no viene con PYTHON. Se debe instalar usando "pip install requests"
#
import requests
import json

url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json"

response = requests.get(url)

#
# Ahora convertimos el JSON leido
data_json = response.json()

# El resultado es una LIST conteniendo los elementos del JSON leido. Luego podemos iterar, tal y como se hace en el ejemplo siguiente:

# Otro ejemplo pero usando el modulo urllib.request
from urllib.request import urlopen
import json

url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json"

response = urlopen(url)

data_json = json.loads(response.read())

# el metodo "loads" devuelve una lista en la cual cada elemento es un dictionary:
# [{'country': 'Afghanistan'}, {'country': 'Albania'}, {'country': 'Algeria'}, {'country': 'American Samoa'}, ...........
#
# Entonces, para mostrar la lista de paises iteramos a traves de la lista:
for country in data_json:
    for key, value in country.items():   # Descomponemos el dictionary en curso.
        print(value)                     # Mostramos el valor del elemento (el nombre del pais en este ejemplo).











#
# Como leer desde la entrada estandar en PYTHON.
#
numero = input("Introduzca el numero: ")
Introduzca el numero: 6
numero
'6'
a = int(numero)
a
6
print(a)
6




#
# Como mostrar en pantalla con formato en PYTHON.
#
a = 13
b = 8

print("\n\na = {} y b = {}\n\n".format(a, b))

a = 13 y b = 8

# o mejor aun:
print(f"\n\na = {a} y b = {b}\n\n")













# Los siguientes son ejemplos de como definir una expresion recursiva anonima en PYTHON.
# Tomadas de:
#
# https://stackoverflow.com/questions/481692/can-a-lambda-function-call-itself-recursively-in-python
#
# 1.- Fibonacci anonima:

#1.1.- 
(lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v))))(lambda f : (lambda i : f(i-1) + f(i-2) if i > 1 else 1))(5)

#o 

#1.2.-
(lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v))))(lambda f : (lambda i : i if i == 0 or i == 1 else f(i-1) + f(i-2)))(7)

#o

#1.3.- Utilizando el walrus operator := PERO no seria ANONIMA!
#
# IMPORTANTE: En javascript hay una expresion parecida. Ejemplo:
#
#             (f = (x) => !x || x == 1 ? x : f(x-1) + f(x-2))(7)
#
#             Luego, al consultar al interprete de javascript que es f, este devuelve:
#
#             (x) => !x || x == 1 ? x : f(x-1) + f(x-2)
#
#             Ver mas sobre este tipo de expresiones en la seccion javaScript mas abajo en este documento.
#
(f := lambda x : x if x == 0 or x == 1 else f(x-1) + f(x-2))(7)
13
#
# OBSERVAR que es posible en Python (al igual que en javaScript) definir/nombrar una LAMBDA expression y utilizarla. Todo en la misma linea!!
#

# Luego, al consultar al interprete quien es f, este devuelve:

<function <lambda> at 0x0000012408D7ED40>

# Entonces, no es anonima!



(f := lambda x : x if x == 0 or x == 1 else f(x-1) + f(x-2))
<function <lambda> at 0x0000028DFB4CAD40>
dis.dis(f)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_CONST               1 (0)
              6 COMPARE_OP              40 (==)
             10 POP_JUMP_IF_TRUE         5 (to 22)
             12 LOAD_FAST                0 (x)
             14 LOAD_CONST               2 (1)
             16 COMPARE_OP              40 (==)
             20 POP_JUMP_IF_FALSE        2 (to 26)
        >>   22 LOAD_FAST                0 (x)
             24 RETURN_VALUE
        >>   26 LOAD_GLOBAL              1 (NULL + f)
             36 LOAD_FAST                0 (x)
             38 LOAD_CONST               2 (1)
             40 BINARY_OP               10 (-)
             44 CALL                     1
             52 LOAD_GLOBAL              1 (NULL + f)
             62 LOAD_FAST                0 (x)
             64 LOAD_CONST               3 (2)
             66 BINARY_OP               10 (-)
             70 CALL                     1
             78 BINARY_OP                0 (+)
             82 RETURN_VALUE




# Vamos a desglosar 1.2.-:
(lambda f : 
            (lambda x : 
                        f(lambda v : x(x)(v))
            )
            (lambda x : 
                        f(lambda v : x(x)(v))
            )
)
(lambda f : 
            (lambda i : i if i == 0 or i == 1 else f(i-1) + f(i-2))
)
(7)




# 2.-
(lambda a : lambda v : a(a, v))(lambda s, x : 1 if x == 0 else x * s(s, x-1))(10)

# 2.-
## 2.1.-
Y = (lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v))))
## 2.2.-
fact = (lambda f : (lambda i : 1 if (i == 0) else i * f(i-1)))
## Combinacion de 2.1 y 2.2
(lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v))))(lambda f : (lambda i : 1 if (i == 0) else i * f(i-1)))(10)











# Iterating With Python Lambdas 

# list of numbers 
l1 = [4, 2, 13, 21, 5] 

# list of square of odd numbers 
# lambda function is used to iterate over list l1 
# filter is used to find odd numbers 
l2 = list(map(lambda v: v ** 2, filter(lambda u: u % 2, l1))) 

# print list 
print(l2) 





format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))











#
# Python es capaz de manejar NUMEROS COMPLEJOS de forma natural (una de los pocos lenguajes que puede hacerlo sin librerias adicionales).
#
a = 1+2j

a
(1+2j)

type(a)
<class 'complex'>

b = 2+3j
b
(2+3j)

a + b
(3+5j)

a.real
1.0

a.imag
2.0


z1 = 2.5 + 3.0j
z2 = 1.2 + 4.5j

z1 + z2
(3.7+7.5j)


z1 = 6 + 7j
z2 = 1 + 4j

print("Addition of numbers:", z1 + z2)
print("Subtraction of numbers:", z1 - z2)
print("Multiplication of numbers:", z1 * z2)
print("Division of numbers:", z1 / z2)

Addition of numbers: (7+11j)
Subtraction of numbers: (5+3j)
Multiplication of numbers: (-22+31j)
Division of numbers: (2-1j)








#
# Ejemplo de uso del modulo cmath para operaciones y constantes matematicas en Python.
#
import cmath

z = 4 + 2j

# Power and log functions like log2, log10, sqrt
# Power function
print("e^z:", cmath.exp(z))

# Logarithm function
print("log2(z):", cmath.log(z, 2))

# Trigonometric functions
# For sine value
print("Sine Value:", cmath.sin(z))

# For cosine value
print("Arc Sine Value:", cmath.asin(z))

# Hyperbolic functions
# For hyperbolic sine value
print("Hyperbolic Sine Value:", cmath.sinh(z))

# For Inverse hyperbolic sine value
print("Inverse Hyperbolic Sine Value:", cmath.asinh(z))


e^z: (-22.720847417619233+49.645957334580565j)
log2(z): (2.1609640474436813+0.6689021062254881j)
Sine Value: (-2.8472390868488278-2.3706741693520015j)
Arc Sine Value: (1.096921548830143+2.183585216564564j)
Hyperbolic Sine Value: (-11.356612711218174+24.83130584894638j)
Inverse Hyperbolic Sine Value: (2.198573027920936+0.4538702099631225j)

# Value of pi
print("pi:", cmath.pi)

# Value of e
print("e:", cmath.e)

# Positive Infinity
print("Positive infinity:", cmath.inf)

# Complex number: zero real part and positive infinity imaginary part
print("Positive complex infinity:", cmath.infj)

# Not a number value
print("NaN value:", cmath.nan)

# Complex number: zero real part and NaN imaginary part
print("NaN complex value:", cmath.nanj)

pi: 3.141592653589793
e: 2.718281828459045
Positive infinity: inf
Positive complex infinity: infj
NaN value: nan
NaN complex value: nanj









#
# Ejemplo de LAMBDA function en Python.
#
pow = lambda x : x*x
pow

<function <lambda> at 0x00000254F2FFCEE0>

pow(2)
4


fib = lambda x : x if x == 0 or x == 1 else fib(x - 1) + fib(x - 2)

fib
<function <lambda> at 0x00000254F2A9E040>

fib(7)
13


#
# Ejemplo de LAMBDA aplicada a una LIST COMPREHENSION!
#
A = [1, 2, 3, 4, 5]

D = [(lambda x : 3*x)(x) for x in A]
D
[3, 6, 9, 12, 15]



#
# Ahora aplicando una misma operacion a todos los elementos de una LIST usando LAMBDA y las funciones list() y map()!
#
A = [0, 1, 2, 3, 4, 5]

A = list(map(lambda x : 2*x, A))

A
[0, 2, 4, 6, 8, 10]



#
# IMPORTANTE: En Python es posible pasar como argumento una LAMBDA function durante la invocacion de una funcion, tal y como 
#             se hace en LISP (ver seccion de SCHEME y LISP abajo en este mismo documento).
#             Tambien, una funcion puede retornar una LAMBDA function como respuesta.
#

# Paso de una LAMBDA en la invocacion de una funcion:
def pow (x):
    return x*x

pow((lambda y, z : y+z)(2, 3))
25

# Ahora creamos una funcion que retorna una LAMBDA como respuesta:
def sum (x1, x2):
    return ((lambda x, y : x+y)(x1, x2))

sum(5, 6)
11






#
# Ejemplo de clase con sobrecarga de operadores suma, resta y multiplicacion. Para este ejemplo creamos una clase del tipo
# par ordenado.
#
#
class parOrd:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, p):
		return self.x + p.x, self.y + p.y
	def __sub__(self, p):
		return self.x - p.x, self.y - p.y
	def __mul__(self, k):
		return parOrd(k*self.x, k*self.y)


# IMPORTANTE: Cuando intentamos multiplicar (por ejemplo) un par ordenado por un escalar, si intentamos hacerlo colocando
#             el escalar a la izquierda del par ordenado Python muestra un mensaje de error!!
#
#             p2 = 2 * p1
#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    c = 2 * a
#TypeError: unsupported operand type(s) for *: 'int' and 'parOrd'
#
#
# Aqui esta una descripcion del problema y de la solucion a traves del operador rmul:
#
# https://www.geeksforgeeks.org/__rmul__-in-python/
#
#
class parOrd:
   def __init__(self, x, y):
            self.x = x
            self.y = y
   def __add__(self, p):
            return self.x + p.x, self.y + p.y
   def __sub__(self, p):
            return self.x - p.x, self.y - p.y
   def __mul__(self, other):
            if isinstance(other, parOrd):
                x = self.x * other.x
                y = self.y * other.y
                return parOrd(x, y)
            elif isinstance(other, int):
                x = self.x * other
                y = self.y * other
                return parOrd(x, y)
   def __rmul__(self, other):
      return self.__mul__(other)


p1 = parOrd(2, 2)
p2 = parOrd(3, 6)
p3 = p1 + p2
p3
(5, 8)

p3 = p1 * p2
p3
<__main__.parOrd object at 0x0000024AD8C1C910>

p3.x
6

p3.y
12


#
# Aqui esta la traduccion en codigo de maquina PYTHON de la clase parOrd:
#
dis.dis(parOrd)
Disassembly of __add__:
  5           0 RESUME                   0

  6           2 LOAD_FAST                0 (self)
              4 LOAD_ATTR                0 (x)
             24 LOAD_FAST                1 (p)
             26 LOAD_ATTR                0 (x)
             46 BINARY_OP                0 (+)
             50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                2 (y)
             72 LOAD_FAST                1 (p)
             74 LOAD_ATTR                2 (y)
             94 BINARY_OP                0 (+)
             98 BUILD_TUPLE              2
            100 RETURN_VALUE

Disassembly of __init__:
  2           0 RESUME                   0

  3           2 LOAD_FAST                1 (x)
              4 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (x)

  4          16 LOAD_FAST                2 (y)
             18 LOAD_FAST                0 (self)
             20 STORE_ATTR               1 (y)
             30 RETURN_CONST             0 (None)

Disassembly of __mul__:
  9           0 RESUME                   0

 10           2 LOAD_GLOBAL              1 (NULL + isinstance)
             12 LOAD_FAST                1 (other)
             14 LOAD_GLOBAL              2 (parOrd)
             24 CALL                     2
             32 POP_JUMP_IF_FALSE       62 (to 158)

 11          34 LOAD_FAST                0 (self)
             36 LOAD_ATTR                4 (x)
             56 LOAD_FAST                1 (other)
             58 LOAD_ATTR                4 (x)
             78 BINARY_OP                5 (*)
             82 STORE_FAST               2 (x)

 12          84 LOAD_FAST                0 (self)
             86 LOAD_ATTR                6 (y)
            106 LOAD_FAST                1 (other)
            108 LOAD_ATTR                6 (y)
            128 BINARY_OP                5 (*)
            132 STORE_FAST               3 (y)

 13         134 LOAD_GLOBAL              3 (NULL + parOrd)
            144 LOAD_FAST                2 (x)
            146 LOAD_FAST                3 (y)
            148 CALL                     2
            156 RETURN_VALUE

 14     >>  158 LOAD_GLOBAL              1 (NULL + isinstance)
            168 LOAD_FAST                1 (other)
            170 LOAD_GLOBAL              8 (int)
            180 CALL                     2
            188 POP_JUMP_IF_FALSE       42 (to 274)

 15         190 LOAD_FAST                0 (self)
            192 LOAD_ATTR                4 (x)
            212 LOAD_FAST                1 (other)
            214 BINARY_OP                5 (*)
            218 STORE_FAST               2 (x)

 16         220 LOAD_FAST                0 (self)
            222 LOAD_ATTR                6 (y)
            242 LOAD_FAST                1 (other)
            244 BINARY_OP                5 (*)
            248 STORE_FAST               3 (y)

 17         250 LOAD_GLOBAL              3 (NULL + parOrd)
            260 LOAD_FAST                2 (x)
            262 LOAD_FAST                3 (y)
            264 CALL                     2
            272 RETURN_VALUE

 14     >>  274 RETURN_CONST             0 (None)

Disassembly of __rmul__:
 18           0 RESUME                   0

 19           2 LOAD_FAST                0 (self)
              4 LOAD_ATTR                1 (NULL|self + __mul__)
             24 LOAD_FAST                1 (other)
             26 CALL                     1
             34 RETURN_VALUE

Disassembly of __sub__:
  7           0 RESUME                   0

  8           2 LOAD_FAST                0 (self)
              4 LOAD_ATTR                0 (x)
             24 LOAD_FAST                1 (p)
             26 LOAD_ATTR                0 (x)
             46 BINARY_OP               10 (-)
             50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                2 (y)
             72 LOAD_FAST                1 (p)
             74 LOAD_ATTR                2 (y)
             94 BINARY_OP               10 (-)
             98 BUILD_TUPLE              2
            100 RETURN_VALUE











#
# Ejemplo de creacion de una LIST de objetos. Tomaremos como ejemplo la clase par ordenado de arriba.
#
A = []

A.append(parOrd(5, 5))

A
[<__main__.parOrd object at 0x0000024ADF419AC0>]

A[0].x
5
A[0].y
5

#Anadimos un nuevo elemento par ordenado a la lista:
A.append(parOrd(10, 4))


for i in A:
	print('x=' + str(i.x) + ', y=' + str(i.y))
	
x=5, y=5
x=10, y=4





#
# Ejemplos de NUMPY.
#
# IMPORTANTE: Para descargar la libreria NUMPY,
#
#             pip install numpy

#
import numpy as np


# Creacion de matriz 6-dimensional.
x = np.arange(729).reshape((3, 3, 3, 3, 3, 3))

print('Array es: ')

print(x)

# Traspuesta de la matriz.
xT = x.T

print('Traspuesta es: ')

print(xT)

# Vector de 3 elementos o componentes.
A = [1, 3, 5]

# Creacion de un nuevo vector con 3*A.
B = [3*n for n in A]

print(B)

# Creacion de dos matrices con numpy.
C = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
D = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

# Suma de ambas matrices.
E = C + D

print(E)



#
# EJEMPLOS DE MATRICES NUMPY CON NUMEROS REALES Y NUMEROS COMPLEJOS!
#
import numpy as np

# creating matrix of complex number
x = np.array([2+3j, 4+5j])

print("Printing First matrix:")
print(x)

y = np.array([8+7j, 5+6j])

print("Printing Second matrix:")
print(y)

# vector dot product of two matrices
z = np.vdot(x, y)

print("Product of first and second matrices are:")
print(z)


# 2-Dimensional matrix

# creating matrix of complex number
x = np.array([[2+3j, 4+5j], [4+5j, 6+7j]])

print("Printing First matrix:")
print(x)

y = np.array([[8+7j, 5+6j], [9+10j, 1+2j]])

print("Printing Second matrix:")
print(y)

# vector dot product of two matrices
z = np.vdot(x, y)

print("Product of first and second matrices are:")
print(z)



#
# Ejemplo de MULTIPLICACION DE POLINOMIOS CON NUMPY!
#
# importing package
import numpy

# define the polynomials
# p(x) = 5(x**2) + (-2)x +5

px = (5, -2, 5)
# q(x) = 2(x**2) + (-5)x +2
qx = (2, -5, 2)

# mul the polynomials
rx = numpy.polynomial.polynomial.polymul(px, qx)

# print the resultant polynomial
print(rx)











#
# Ejemplos de uso de la libreria MATPLOTLIB.
#
# Ejemplo de trazado de grafico 2D de una funcion:   3      2
#                                                  4X  +  2X   +   5X
#
import numpy as np
import matplotlib.pyplot as plt

#
# linspace produce una sucesion de numeros igualmente espaciados desde un inicio (-5 en este caso) hasta un fin (5 en este caso). El tercer 
# argumento indica el numero de elementos a generar.
#
x_ = np.linspace(-5, 5, 5)
x_ = np.linspace(-5, 5, 10)

y_ = 4 * (x_**3) + 2 * (x_**2) + 5 * x_

plt.plot(x_, y_)
[<matplotlib.lines.Line2D object at 0x000001916DE4FE30>]
plt.show()
x_
array([-5.        , -3.88888889, -2.77777778, -1.66666667, -0.55555556,
        0.55555556,  1.66666667,  2.77777778,  3.88888889,  5.        ])
y_
array([-475.        , -224.45130316,  -84.19067215,  -21.2962963 ,
         -2.84636488,    4.08093278,   32.40740741,  115.05486968,
        284.94513032,  575.        ])





#
# Aqui hay otro ejemplo de la funcion linspace:
#
A = np.linspace(start=1.0, stop=30.5, num=15)

A
array([ 1.        ,  3.10714286,  5.21428571,  7.32142857,  9.42857143,
       11.53571429, 13.64285714, 15.75      , 17.85714286, 19.96428571,
       22.07142857, 24.17857143, 26.28571429, 28.39285714, 30.5       ])






# Otro ejemplo. Genera un grafico 3D que puede rotarse con el mouse:
#
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

ax = plt.figure().add_subplot(projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')

ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')

plt.show()











#
# Ejemplos PANDAS: manejo de datos (Datasets en un Dataframe) y de lectura/escritura desde/hacia archivos CSV y Excel para salvar el trabajo!!
#
# IMPORTANTE: Para descargar la libreria PANDAS,
#
#             pip install pandas
#
# NOTA IMPORTANTE: PANDAS es capaz de leer fuentes de datos tipo CSV, Excel, JSON. Es capaz de leer varios archivos con diferentes formatos
#                  en una misma sesion o programa PYTHON!!
#
# NOTA IMPORTANTE: Con PANDAS es posible hacer consultas o filtrar los registros (a traves del metodo QUERY) de una tabla Excel 
#                  tal y como lo hariamos en Excel usando los Filtros Avanzados!!!!
#
import numpy as np
import pandas as pd


#
# Como primer ejemplo vamos a crear un DataFRame PANDAS conteniendo el numero de visitantes a un sitio web durante cinco dias conjuntamente 
# con los errores que se detectan durante cada dia y usando como cabeceras los nombres de los dias desde lunes a viernes:
visitors = [1234, 6526, 786, 1235, 3788]
errors = [23, 45, 12, 68, 42]

# Ahora creamos el DataFrame,
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])

# Ahora mostramos el dataFrame
print(df)
      visitors  errors
Mon       1234      23
Tues      6526      45
Wed        786      12
Thu       1235      68
Fri       3788      42

# Con este DataFrame podemos usar algun metodo para hacer calculos. Por ejemplo, podemos usar el metodo mean para mostrar la media aritmetica 
# de la columna "errors"
df["errors"].mean()
38.0




#
# Otro ejemplo de creacion de un Data Frame desde un Dictionary de Python!
#
df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)

df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo


#
# Ejemplo de almacenamiento de un Dataframe en un archivo CSV con separador TAB!
#
df2.to_csv(r"C:\Users\user\Desktop\pandas.csv", sep='\t')




#
# Creacion de un DataFrame en la cual se indica los valores del indice del DataSet:
#
df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index = [1, 2, 3])

df
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12


# Ahora veamos un ejemplo de filtro. Observar como cada condicion debe ir dentro de parentesis:
#
subC = df[(df.a > 4) & (df.c == 12)]

subC
   a  b   c
3  6  9  12

# Mismo resultado obtendremos al usar QUERY. Observar que se usa la palabra "and" en lugar de "&":
#
subQuery = df.query('a > 4 and c == 12')

subQuery
   a  b   c
3  6  9  12


# Otro ejemplo de filtro. Esta vez con el condicional OR "|":
subOR = df[(df.a == 4) | (df.a == 6)]

subOR
   a  b   c
1  4  7  10
3  6  9  12





#
# Otro ejemplo de creacion de un Dataframe:
#
dates = pd.date_range("20130101", periods=6)

#
# Ejemplo de creacion de un Data Frame
#
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df
                   A         B         C         D
2013-01-01 -0.032335  0.016063  0.823220  1.513305
2013-01-02 -0.673649  0.435033 -1.625516  0.180959
2013-01-03 -0.991528  1.571661  0.940232 -1.267361
2013-01-04  0.114470 -0.394647 -0.371690 -0.145988
2013-01-05 -0.164062  0.438835  1.272382 -1.248339
2013-01-06 -0.079109 -0.341629  0.140775 -0.259579



#
# Ejemplo de almacenamiento del Data Frame en un archivo CSV
#
df.to_csv(r"C:\Users\user\Desktop\pandas.csv", sep=',')


#
# Ejemplo de lectura (recuperacion) de un Data Frame desde un archivo CSV
#
pandasData = pd.read_csv(r"C:\Users\user\Desktop\pandas.csv")
pandasData
   Unnamed: 0         A         B         C         D
0  2013-01-01 -0.032335  0.016063  0.823220  1.513305
1  2013-01-02 -0.673649  0.435033 -1.625516  0.180959
2  2013-01-03 -0.991528  1.571661  0.940232 -1.267361
3  2013-01-04  0.114470 -0.394647 -0.371690 -0.145988
4  2013-01-05 -0.164062  0.438835  1.272382 -1.248339
5  2013-01-06 -0.079109 -0.341629  0.140775 -0.259579



#
# Ejemplo de query con condiciones!
#
# Ejemplo de lectura de un CSV desde la internet:
df = pd.read_csv("https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv", usecols=range(1,17))


# Ejemplo de query con condiciones y el operador logico "&" (tambien puede utilizarse "and"):
df.query('year == 2013 & day < 27 & air_time == 160')
        year  month  day  dep_time  ...  air_time  distance  hour minute
2       2013      1    1     542.0  ...     160.0      1089   5.0   42.0
135     2013      1    1     826.0  ...     160.0      1089   8.0   26.0
137     2013      1    1     828.0  ...     160.0       740   8.0   28.0
225     2013      1    1    1009.0  ...     160.0      1020  10.0    9.0
296     2013      1    1    1155.0  ...     160.0      1076  11.0   55.0
...      ...    ...  ...       ...  ...       ...       ...   ...    ...
330432  2013      9   24     807.0  ...     160.0      1131   8.0    7.0
331381  2013      9   25     759.0  ...     160.0      1182   7.0   59.0
331757  2013      9   25    1450.0  ...     160.0      1182  14.0   50.0
331996  2013      9   25    1820.0  ...     160.0      1076  18.0   20.0
332251  2013      9   26     631.0  ...     160.0      1008   6.0   31.0

[1127 rows x 16 columns]

# OJO!!!!!!!!
# NOTA IMPORTANTE: Como vemos en esta salida, PANDAS trunca u oculta las columnas con "...". Para que muestre todas las columnas y 
#                  mostrarlas todas en una sola linea (sin wrapping) ejecute los siguientes comandos:
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 9999)


# Ejemplo de como mostrar los primeros/ultimos registros de un Dataframe:
df.head()
df.tail()


#
# Otro ejemplo, ahora leyendo un archivo EXCEL:
#
# IMPORTANTE: Para almacenar en un archivo Excel se utiliza "to_excel(...)"
#
base = pd.read_excel(r"C:\Users\user\Desktop\sample-salesv3.xlsx")


# IMPORTANTE: Es posible pedir a PANDAS que nos muestre los tipos de datos de cada columna de la tabla leida:
base.dtypes

account number      int64
name               object
sku                object
quantity            int64
unit price        float64
ext price         float64
date               object
dtype: object



# Ahora instruimos a PANDAS para que muestre todas las columnas de la tabla Excel y sin picarlas en dos partes (wrapping):
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 9999)

# Pedimos a PANDAS que nos muestre los primeros registros (filas) de la tabla:
base.head()

   account number                         name       sku  quantity  unit price  ext price                 date
0          740150                   Barton LLC  B1-20000        39       86.69    3380.91  2014-01-01 07:21:51
1          714466              Trantow-Barrows  S2-77896        -1       63.16     -63.16  2014-01-01 10:00:47
2          218895                    Kulas Inc  B1-69924        23       90.70    2086.10  2014-01-01 13:24:58
3          307599  Kassulke, Ondricka and Metz  S1-65481        41       21.05     863.05  2014-01-01 15:05:22
4          412290                Jerde-Hilpert  S2-34077         6       83.21     499.26  2014-01-01 23:26:55


#
# IMPORTANTE: Es posible instruir a PANDAS para que ordene la tabla (en su memoria...no afecta el origen de los datos) segun una columna:
base = base.sort_values(by='quantity')

# Veamos como quedaron los primeros registros luego del sort:
base.head()
      account number              name       sku  quantity  unit price  ext price                 date
670           424914     White-Trantow  S1-30248        -1       76.46     -76.46  2014-06-05 04:10:34
1151          527099  Sanford and Sons  B1-69924        -1       57.76     -57.76  2014-10-04 06:20:29
459           740150        Barton LLC  B1-69924        -1       65.45     -65.45  2014-04-17 08:46:36
745           218895         Kulas Inc  B1-38851        -1       56.89     -56.89  2014-06-24 00:59:41
146           688981       Keeling LLC  B1-20000        -1       72.18     -72.18  2014-02-04 07:43:51

# Y como quedaron los ultimos registros luego del sort:
base.tail()
      account number                             name       sku  quantity  unit price  ext price                 date
514           688981                      Keeling LLC  S1-65481        49       37.23    1824.27  2014-04-29 23:37:42
511           257198  Cronin, Oberbrunner and Spencer  B1-33364        49       17.71     867.79  2014-04-29 09:37:34
1401          786968         Frami, Hills and Schmidt  S1-65481        49       30.33    1486.17  2014-12-07 11:34:55
440           729833                        Koepp Ltd  B1-65551        49       18.43     903.07  2014-04-14 03:44:48
330           688981                      Keeling LLC  S2-34077        49       91.80    4498.20  2014-03-21 19:20:17


# Ahora hagamos un query:
base[base["account number"] == 527099]

      account number              name       sku  quantity  unit price  ext price                 date
1151          527099  Sanford and Sons  B1-69924        -1       57.76     -57.76  2014-10-04 06:20:29
689           527099  Sanford and Sons  B1-04202        -1       33.04     -33.04  2014-06-11 06:16:44
878           527099  Sanford and Sons  S2-16558        -1       89.45     -89.45  2014-07-24 17:46:26
1092          527099  Sanford and Sons  B1-50809         2       29.04      58.08  2014-09-19 19:10:52
533           527099  Sanford and Sons  B1-05914         3       58.75     176.25  2014-05-05 15:27:15
...              ...               ...       ...       ...         ...        ...                  ...
883           527099  Sanford and Sons  B1-20000        45       66.28    2982.60  2014-07-26 04:38:08
477           527099  Sanford and Sons  B1-50809        45       86.60    3897.00  2014-04-22 09:13:36
697           527099  Sanford and Sons  S1-30248        45       50.50    2272.50  2014-06-13 12:43:00
526           527099  Sanford and Sons  S1-82801        46       44.45    2044.70  2014-05-03 06:59:30
35            527099  Sanford and Sons  S1-27722        48       43.40    2083.20  2014-01-10 10:59:39





#
# Ahora vamor a leer un archivo JSON desde PANDAS:
df2 = pn.read_json(r"C:\Users\user\Desktop\jsonEjercicio.json")

df2
      albumId    id                                              title                                     url                            thumbnailUrl
0           1     1  accusamus beatae ad facilis cum similique qui ...  https://via.placeholder.com/600/92c952  https://via.placeholder.com/150/92c952
1           1     2             reprehenderit est deserunt velit ipsam  https://via.placeholder.com/600/771796  https://via.placeholder.com/150/771796
2           1     3     officia porro iure quia iusto qui ipsa ut modi  https://via.placeholder.com/600/24f355  https://via.placeholder.com/150/24f355
3           1     4  culpa odio esse rerum omnis laboriosam volupta...  https://via.placeholder.com/600/d32776  https://via.placeholder.com/150/d32776
4           1     5  natus nisi omnis corporis facere molestiae rer...  https://via.placeholder.com/600/f66b97  https://via.placeholder.com/150/f66b97
...       ...   ...                                                ...                                     ...                                     ...
4995      100  4996  voluptatem ab aliquam dolorum vel voluptas qui...  https://via.placeholder.com/600/b3db9a  https://via.placeholder.com/150/b3db9a
4996      100  4997    sunt amet autem exercitationem fuga consequatur  https://via.placeholder.com/600/13454b  https://via.placeholder.com/150/13454b
4997      100  4998             qui quo cumque distinctio aut voluptas  https://via.placeholder.com/600/315aa6  https://via.placeholder.com/150/315aa6
4998      100  4999         in voluptate sit officia non nesciunt quis  https://via.placeholder.com/600/1b9d08  https://via.placeholder.com/150/1b9d08
4999      100  5000  error quasi sunt cupiditate voluptate ea odit ...  https://via.placeholder.com/600/6dd9cb  https://via.placeholder.com/150/6dd9cb




#
# Ejemplo de iteracion a traves de un PANDAS Dataframe (usando el JSON leido arriba). En cada iteracion mostraremos las columnas 
# "albumId" y "id":
#
for i in df2.index:
    print(df2['albumId'][i], df2['id'][i])













# ----------------------------------------------------------------------------------------- #
# Ejemplo del metodo "sort" para ordenar una lista (arreglo) de elementos de tipo numerico. #
# ----------------------------------------------------------------------------------------- #
lista = [90, 23, 5, 109, 12, 22, 67, 34]

>>> lista
[90, 23, 5, 109, 12, 22, 67, 34]
>>> 

lista.sort()

>>> 
>>> lista
[5, 12, 22, 23, 34, 67, 90, 109]








# ----------------------------------------------------------------------------------------- #
# Ejemplo de arbol binario para manejos de la estructura de una frase o formula matematica. #
# ----------------------------------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Esta clase representa a un nodo cualquiera del arbol binario. #
# ------------------------------------------------------------- #
class Nodo:
    def __init__(self, data):
        self.izq = None
        self.der = None
        self.data = data

    # ------------------------------- #
    # Metodo para insercion de nodos. #
    # ------------------------------- #
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.izq is None:
                    self.izq = Nodo(data)
                else:
                    self.izq.insert(data)
            elif data > self.data:
                if self.der is None:
                    self.der = Nodo(data)
                else:
                    self.der.insert(data)
        else:
            self.data = data

    # ----------------------------------------------------------------------------- #
    # Metodo para localizar un nodo con valor especifico (dentro del arbol binario. #
    # ----------------------------------------------------------------------------- #
    def encValor(self, valEnc):
        if valEnc < self.data:
            if self.izq is None:
                return str(valEnc)+" Not Found"
            return self.izq.encValor(valEnc)
        elif valEnc > self.data:
            if self.der is None:
                return str(valEnc)+" Not Found"
            return self.der.encValor(valEnc)
        else:
            print(str(self.data) + ' is found')

    # ------------------------------------- #
    # Metodo para mostrar el arbol binario. #
    # ------------------------------------- #
    def muestraArb(self):
        if self.izq:
            self.izq.muestraArb()

        print( self.data)

        if self.der:
            self.der.muestraArb()
# ---------------------- FIN - Clase Nodo ------------------------ #


# -------------------------------------------------------- #
#                  Principal del programa.                 #
# -------------------------------------------------------- #
root = Nodo(12)

root.insert(6)

root.insert(14)

root.insert(3)

print(root.encValor(7))
print(root.encValor(14))

root.muestraArb()
# -------------------------------------------------------- #


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)



TRADUCCION DE UNA EXPRESION LISP HACIA EL ASSEMBLER SPECTRE MAP:
================================================================
                    Jose Portillo L. - 2018


PASO 1 - Expresion LISP: (+ 6 (- (+ 4 (* 3 7))(/ 5 (+ 3 4))))


PASO 2 - Arbol sintactico (en parentesis directo desde LISP):
(+  
    6 
    (- 
        (+ 
            4 
            (* 
                3 
                7
            )
        )
        (/ 
            5 
            (+ 
                3 
                4
            )
        )
    )
)


PASO 3 - Recorrido del arbol sintactico en post-order: 6 4 3 7 * + 5 3 4 + / - +


PASO 4 - Comprobacion del calculo:
6 4 21 + 5 3 4 + / - +

6 25 5 3 4 + / - +

6 25 5 7 / - +

6 25 5/7 - +

6 25-(5/7) +

Post order valido: 6 4 3 7 * + 5 3 4 + / - +


PASO 5 - Traduccion usando la tabla de traslacion a instrucciones de maquina SPECTRE:

ETIQUETA    OP      OPER    Comentarios
--------    ---     ----    -----------
INICIO      LDQ     3       T1 = 3 * 7
            MPY     7
            STQ     T1
            CLA     4       T2 = 4 + T1
            ADD     T1
            STO     T2
            CLA     3       T3 = 3 + 4
            ADD     4
            STO     T3
            LDQ     5       T3 = 5 / T3
            DIV     T3
            STQ     T3
            CLA     T2      T3 = T2 - T3
            SUB     T3
            STO     T3
            CLA     6       T1 = 6 + T3
            ADD     T3
            STO     T1


ANEXO - Maquina SPECTRE:
=======================
Registros internos......:   A, Q
Memoria.................:   T1, ..., Tn
Unidad Aritmetica/Logica:   A <- Tn | Const  A <- A + Tn | Const  A <- A - Tn | Const
                            Q <- Tn | Const  Q <- Q * Tn | Const  Q <- Q / Tn | Const
Micro-codigo............:   LDQ  CLA  STQ  STO  ADD  SUB  MPY  DIV


# ---------------------------------------------------------- #
# Genera instrucciones en assembler para la maquina SPECTRE. #
# ---------------------------------------------------------- #
class SPECTRE_Assembler:

    # Codigos de operacion.
    opcodes = ["     CLA     op1,     ADD     op2,     STO     T#",
               "     CLA     op1,     SUB     op2,     STO     T#",
               "     LDQ     op1,     MPY     op2,     STQ     T#",
               "     LDQ     op1,     DIV     op2,     STQ     T#",
               "     CLA     op2,     STO     op1"
            ]

    def genera_codigo(self, ietiq, operando, fetiq):
        if ietiq and operando != "=":
            print("")
            print("")
            print(ietiq)
        if operando == "+":
            for sum in self.opcodes[0].split(","):
                print(sum)
        elif operando == "-":
            for res in self.opcodes[1].split(","):
                print(res)
        elif operando == "*":
            for mul in self.opcodes[2].split(","):
                print(mul)
        elif operando == "/":
            for div in self.opcodes[3].split(","):
                print(div)
        elif operando == "=":
            for igual in self.opcodes[4].split(","):
                print(igual)
        if fetiq:
            print('     ' + fetiq + '     ' + ietiq)


# Ejemplo de generacion de codigo.
varSimtab = SPECTRE_Assembler()

varSimtab.genera_codigo("FUNC1", "+", "")
varSimtab.genera_codigo("", "+", "")
varSimtab.genera_codigo("FUNC1", "=", "END")

varSimtab.genera_codigo("MAIN", "+", "")
varSimtab.genera_codigo("", "*", "")
varSimtab.genera_codigo("", "/", "")
varSimtab.genera_codigo("", "+", "")
varSimtab.genera_codigo("", "-", "")
varSimtab.genera_codigo("MAIN", "=", "END")

Y Aqui esta el codigo generado por el ejemplo:

FUNC1
     CLA     op1
     ADD     op2
     STO     T#
     CLA     op1
     ADD     op2
     STO     T#
     CLA     op2
     STO     op1
     END     FUNC1
MAIN
     CLA     op1
     ADD     op2
     STO     T#
     LDQ     op1
     MPY     op2
     STQ     T#
     LDQ     op1
     DIV     op2
     STQ     T#
     CLA     op1
     ADD     op2
     STO     T#
     CLA     op1
     SUB     op2
     STO     T#
     CLA     op2
     STO     op1
     END     MAIN



# ----------------------------------------------- #
# Conversion de notacion desde infija a postfija. #
# ----------------------------------------------- #
def infix_to_postfix(infix_expr):
    prec = {}

    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    op_stack = Stack()

    postfix_list = []

    #
    # Adaptacion: Se incluye tokenizacion de los simbolos "(" y ")".
    #
    token_list = infix_expr.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()

            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())

            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

# Ejemplos de conversion.
print(infix_to_postfix("A * B + C * D"))

print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))



# ------------------------ #
# Ejemlo de arbol binario. #
# ------------------------ #
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

def post_order(tree):
    if tree != None:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_val())


def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree  = BinaryTree('')


    p_stack.push(e_tree)
    current_tree = e_tree

    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError

    return e_tree

# Ejemplo de parse y conversion a postorder de una expresion algebraica.
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")

post_order(pt)

# Muestra el codigo assempler generado por la compilacion que hace Python sobre la funcion "build_parse_tree".
build_parse_tree.__code__.co_code
b'|\x00\x00j\x00\x00\x83\x00\x00}\x01\x00t\x01\x00\x83\x00\x00}\x02\x00t\x02\x00d\x01\x00\x83\x01\x00}\x03\x00|\x02\x00j\x03\x00|\x03\x00\x83\x01\x00\x01|\x03\x00}\x04\x00x\xda\x00|\x01\x00D]\xd2\x00}\x05\x00|\x05\x00d\x02\x00k\x02\x00rv\x00|\x04\x00j\x04\x00d\x01\x00\x83\x01\x00\x01|\x02\x00j\x03\x00|\x04\x00\x83\x01\x00\x01|\x04\x00j\x05\x00\x83\x00\x00}\x04\x00q;\x00|\x05\x00d\x08\x00k\x07\x00r\xaa\x00|\x04\x00j\x06\x00t\x07\x00|\x05\x00\x83\x01\x00\x83\x01\x00\x01|\x02\x00j\x08\x00\x83\x00\x00}\x06\x00|\x06\x00}\x04\x00q;\x00|\x05\x00d\t\x00k\x06\x00r\xec\x00|\x04\x00j\x06\x00|\x05\x00\x83\x01\x00\x01|\x04\x00j\t\x00d\x01\x00\x83\x01\x00\x01|\x02\x00j\x03\x00|\x04\x00\x83\x01\x00\x01|\x04\x00j\n\x00\x83\x00\x00}\x04\x00q;\x00|\x05\x00d\x07\x00k\x02\x00r\x07\x01|\x02\x00j\x08\x00\x83\x00\x00}\x04\x00q;\x00t\x0b\x00\x82\x01\x00q;\x00W|\x03\x00S'




# ---------------------------------------- #
# Ejemplo de uso de base de datos SQLite3. #
# ---------------------------------------- #
import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()

c.execute('create table portfolio (symbol text, shares integer, price real)')
<sqlite3.Cursor object at 0x02E29D60>

db.commit()

stocks = [
          ('GOOG', 100, 490.1),
          ('AAPL', 50, 545.75),
          ('FB', 150, 7.45),
          ('HPQ', 75, 33.2),
         ]

c.executemany('insert into portfolio values (?,?,?)', stocks)
<sqlite3.Cursor object at 0x02E29D60>

db.commit()

for row in db.execute('SELECT * FROM portfolio'):
	print(row)

('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
('FB', 150, 7.45)
('HPQ', 75, 33.2)

for row in db.execute('SELECT * FROM portfolio WHERE symbol = "FB"'):
	print(row)

('FB', 150, 7.45)




# Prueba de __iter__().
nums = [1, 2, 3]

i_num = nums.__iter__()

print(i_num)
print(dir(i_num))

# for i_num in nums:
#     print (num)

while True:
    if dat1 <= 3:
        print('Es menor que tres')
    else:
        break



# Ejemplo de uso de REDUCE.
# Python tiene una libreria llamada "operator". En lugar de usar una expresion lambda 
# se puede usar el operator deseado dentro de una sentencia reduce:
One example is in the use of the reduce() function:

>>> import operator
>>> a = [2, 3, 4, 5]
>>> reduce(lambda x, y: x + y, a)
14
>>> reduce(operator.add, a)
14




# ----------------------------------------------------------------------------------------------------------------------- #
# En Python las funciones son first-class objects. Esto quiere decir que las funciones pueden (al igual que los integers, #
# strings y otros tipos de datos) ser pasadas como parametros a otra funcion. Esto es un concepto que viene del LISP      #
# (Scheme). El siguiente es un ejemplo en Scheme y luego lo implementamos en Python:                                      #
#                                                                                                                         #
# (define (suma a b)                                                                                                      #
#         (+ a b))                                                                                                        #
#                                                                                                                         #
# (define (mult a b)                                                                                                      #
#         (* a b))                                                                                                        #
#                                                                                                                         #
# Ahora definimos una funcion que recibe como parametros dos funciones basicas:                                           #
#                                                                                                                         #
# (define (formula oper1 oper2 a b)                                                                                       #
#         (oper1 (oper2 a 2) (oper2 b 3)))                                                                                #
#                                                                                                                         #
# Luego, se invoca de la siguiente manera:                                                                                #
#                                          (formula suma mult 3 2)                                                        #
# ----------------------------------------------------------------------------------------------------------------------- #
def suma(a, b):
	return a + b

def mult(a, b):
	return a * b

def formula(oper1, oper2, a, b):
	return oper1(oper2(a, 2), oper2(a, 3))

>>> print(formula(suma, mult, 3, 2))
15



# -------------------------------------------------------------------------------------------------------------------- #
# POSTGRESQL: Ejemplo de uso desde Python.                                                                             #
#                                                                                                                      #
# NOTA: El paquete psycopg2 se importa con el comando "pip". Dicho comando se ejecuta desde la command line Python 3.7:#
#                                                                                                                      #
#       C:\...\pip install psycopg2                                                                                    #
#                                                                                                                      #
#       Para instalarlo dentro de Jupyter se utiliza el NEW/Terminal (menu superior derecho en Jupyter)                #
#                                                                                                                      #
# NOTA: Para consultar las columnas de una tabla en POSTGRESQL se usa la siguiente consulta:                           #
#                                                                                                                      #
#       SELECT table_name, column_name, data_type FROM information_schema.columns                                      #
#                                                 WHERE table_name = 'empleados'                                       #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #
import psycopg2

conexion = psycopg2.connect(
                            host     = "localhost",
                            database = "inventario",
                            user     = "postgres",
                            password = "apollo2134")


cursor = conexion.cursor()

# Invoca la ejecucion de la sentencia SQL:
cursor.execute("SELECT * FROM empleados")

rows = cursor.fetchall()

>>> for row in rows:
	   print("ID: " + str(row[0]) + " | Nombre: " + row[2] + " | Apellido: " + row[1] + " | Dept: " + str(row[3]))

ID: 1 | Nombre: Jose            | Apellido: Portillo        | Dept: 12
ID: 3 | Nombre: Fernando        | Apellido: Lozano          | Dept: 10
ID: 18 | Nombre: Isabel          | Apellido: Portillo        | Dept: 11
ID: 9 | Nombre: Maria           | Apellido: Gonzalez        | Dept: 14
ID: 7 | Nombre: Alexis          | Apellido: Aponte          | Dept: 70
ID: 20 | Nombre: Donald          | Apellido: Knuth           | Dept: 80


# Invocar la ejecucion de un Stored Procedure desde Python (abajo aparece un ejemplo de creacion de dicho Stored Procedure).
# Mas adelante, en la seccion de manejo de diccionarios en Python veremos otros ejemplos de interaccion con PostgreSQL.
cursor.execute("CALL insert_into_empleados(%s, %s, %s, %s);", (90, 'Miletos', 'Thales de', 15))

# Y una vez que se ha realizado la insercion de la fila nueva se debe hacer COMMIT:
conexion.commit()

# Con esta libreria se puede imprimir cualquier lista de forma mas elegante en pantalla.
import pprint

>>> pprint.pprint(rows)

[(1, 'Portillo       ', 'Jose           ', 12),
 (3, 'Lozano         ', 'Fernando       ', 10),
 (18, 'Portillo       ', 'Isabel         ', 11),
 (9, 'Gonzalez       ', 'Maria          ', 14),
 (7, 'Aponte         ', 'Alexis         ', 70),
 (20, 'Knuth          ', 'Donald         ', 80),
 (90, 'Miletos        ', 'Thales de      ', 15)]


# Invocar la ejecucion de una function PostgreSQL y colocar el valor devuelto en una variable:
cursor.execute("SELECT empl_total_records()")

respuesta = cursor.fetchall()

# Devuelve el valor en una estructura tipo lista de tuplas.
>>> respuesta
[(7,)]


# PostgreSQL permite hacer cargas (Bulk copy) masivas hacia (y desde) la base de datos a traves del comando COPY.
# Este comando es ejecutado desde el cliente SQL y permite, incluso, cargar (y descargar) archivos CSV.
#
# NOTA: La tabla debe estar creada previamente a la operacion.
#
# NOTA IMPORTANTE: Esta operacion la hace el servidor de base de datos. En el caso del sistema Windows, si el archivo a 
#                  leer (o escribir) se encuentra en el disco "C:" Windows no permite escribir archivos en ese disco por 
#                  este un disco del sistema, excepto que el usuario que utilice el servidor PostgreSQL tenga privilegios 
#                  de super usuario en Windows. El tipo de mensaje de error que muestra PostgreSQL seria:
#
#                  "HINT:  COPY FROM instructs the PostgreSQL server process to read a file. 
#                         You may want a client-side facility such as psql's \copy. SQL state: 58P01"
#
#                  Una forma de evitar este error seria usar un disco (ejemplo "D:") distinto al "C:" del sistema.
#
# Unos ejemplos de carga y descarga masiva de datos desde un archivo CSV:

# Cargar datos desde un archivo CSV hacia una tabla en PostgreSQL.
COPY persons(first_name, last_name, dob, email) 
FROM 'D:\persons.csv' DELIMITER ',' CSV HEADER;

# Descargar datos desde una tabla PostgreSQL hacia un archivo CSV:
COPY (SELECT * FROM persons) TO 'D:\prueba.csv'


#
# NOTA: Otros metodos de psycopg2,
#
#     - cursor.rowcount() : This read-only attribute which returns the total number of database rows 
#                           that have been modified, inserted, or deleted by the last last execute.
#
#     - cursor.fetchone() : This method fetches the next row of a query result set, returning a single sequence, 
#                           or None when no more data is available.
#

# Cierra el cursor y la sesion con PostgreSQL:
cursor.close()
conexion.close()



# ----------------------------------------------------------------------------------------------------- #
#                                 Ejemplos de sentencias en PostgreSQL                                  #
# ----------------------------------------------------------------------------------------------------- #

# Ejemplo de creacion de un schema:
CREATE SCHEMA repositorio;

# Creacion de una tabla dentro de este nuevo schema:
CREATE TABLE repositorio.compania
(
	ID          INT           NOT NULL,
	nombre      VARCHAR(20)   NOT NULL,
	direccion   VARCHAR(25),
	PRIMARY KEY(ID)
);

# Ejemplo de consulta basica:
SELECT * FROM repositorio.compania;


# Como listar los nombres de las columnas de una tabla:
SELECT table_name, column_name, data_type FROM information_schema.columns
WHERE table_name = 'empleados';


SELECT * FROM empleados
         WHERE (apellido = 'Portillo' OR apellido = 'Lozano') AND (nombre = 'Jose' OR nombre = 'Fernando');

# Otro ejemplo de creacion de tabla:
CREATE TABLE departamentos (
	ID		INT PRIMARY KEY NOT NULL,
	NOMBRE	CHAR(30)        NOT NULL,
	ZONA	INT				NOT NULL);

# Para alterar la definicion de algun campo(s):
ALTER TABLE google_stock_data
ALTER COLUMN abierto TYPE NUMERIC,
ALTER COLUMN alto TYPE NUMERIC,
ALTER COLUMN bajo TYPE NUMERIC,
ALTER COLUMN cerrado TYPE NUMERIC,
ALTER COLUMN ceradjn TYPE NUMERIC;

#
# NOTA: PostgreSQL almacena las fechas en formato "yyyy-mm-dd". Para mostrar (en una consulta) los valores en otro formato, 
#       ejemplo "dd-mm-yyyy" puede usar la siguiente sintaxis en la consulta. Aqui la columna "fecha" es tipo DATE:
SELECT TO_CHAR(fecha, 'dd-mm-yyyy'), abierto, alto, bajo, cerrado, volumen, ceradjn FROM google_stock_data;


SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'departamentos';

INSERT INTO departamentos VALUES (12, 'Tecnologia', 20);
INSERT INTO departamentos VALUES (10, 'Contabilidad', 30);
INSERT INTO departamentos VALUES (11, 'Recursos Humanos', 40);
INSERT INTO departamentos VALUES (14, 'Mercadeo', 50);


# Ejemplo de SELECT FROM IN:
SELECT * FROM empleados
         WHERE Dept IN (SELECT ID FROM departamentos);


# Ejemplo de una Inner Join (interseccion de dos tablas en relacion a un campo). En este ejemplo la consulta devuelve 
# todos los registros de la tabla empleados cuyo departamento coincida con algun departamento existente en la tabla 
# departamentos. La interseccion aqui es el mismo concepto de la interseccion de conjuntos.
SELECT empleados.nombre, empleados.apellido FROM empleados
INNER JOIN departamentos ON empleados.dept = departamentos.id;


# Tambien es posible hacer Inner Joins (intersecciones) entre tres tablas. Ejemplo:
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM (
	  (Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID) 
	  INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
     ); 


# Es posible hacer UNION entre tablas pero tomando las siguientes consideraciones:
#    - Cada sentencia SELECT (dentro de la UNION) debe tener el mismo numero de columnas consultadas.
#    - Dichas columnas deben tener el mismo tipo de dato.
#    - Dichas columnas deben aparecer (en ambos SELECT) en el mismo orden.
SELECT dept FROM empleados
UNION
SELECT id FROM departamentos;


# Tip importante sobre el uso de "GROUP BY" en sentencias SQL:
#
# La sección GROUP BY debe incluir TODOS los campos que aparecen en la consulta. Ejemplo,

SELECT CAMPO1, CAMPO2, COUNT(*) AS NUMTXN, CAMPO3
FROM   TABLA
GROUP BY CAMPO1, CAMPO2, CAMPO3


# Ejemplo de Update a una tabla:
UPDATE empleados SET Dept = 70 WHERE ID = 7;


# La siguiente sentencia devuelve el timestamp del sistema de base de datos (incluida la time zone):
SELECT CURRENT_TIMESTAMP;


# Ejemplo de conteo de registros:
SELECT COUNT(*) FROM empleados;


# Ejemplo de creacion de Stored Procedure PL/pgSQL:
CREATE PROCEDURE insert_into_empleados(vid integer, apel varchar(15), nom varchar(15), dep integer)

LANGUAGE SQL

AS $BODY$
      INSERT INTO empleados(id, apellido, nombre, dept)
             VALUES(vid, apel, nom, dep);
   $BODY$;


# Invocacion del Stored Procedure:
CALL insert_into_empleados (20, 'Knuth', 'Donald', 80);


# Ejemplo de creacion de una function PL/pgSQL:
CREATE OR REPLACE FUNCTION empl_total_records()
RETURNS integer AS $totalEmp$

DECLARE
   totalEmp integer;

-- Cuerpo de la funcion.
BEGIN
   SELECT COUNT(*) INTO totalEmp FROM empleados;
   
   RETURN totalEmp;
END;
$totalEmp$ LANGUAGE plpgsql;


-- Le asigna como propietario al usuario "postgres".
ALTER FUNCTION empl_total_records OWNER TO postgres;


# Luego, para ejecutar la funcion que hemos creado:
SELECT empl_total_records();

# Resultado devuelto:
7


# Es posible crear bloques anonimos con PL/pgSQL. Aqui el comando "DO" ejecutara todo lo que esta entre $$.
DO
$$
DECLARE
   varnom   VARCHAR(15) := '';   -- Nombre del empleado.
   varapl   VARCHAR(15) := '';   -- Apellido del empleado.
   vardep   INTEGER     := 0;    -- Departamento al cual pertenece el empleado.
BEGIN
   -- Hacemos la consulta
   SELECT nombre, apellido, dept INTO varnom, varapl, vardep FROM empleados
          WHERE apellido = 'Lozano';
   
   RAISE NOTICE 'Empleado: % %', varnom, varapl;
END
$$


OJO!!!!!!  HACER UN EJEMPLO DE ESTO: How to Develop a PL/pgSQL Function That Returns a Table
To define a function that returns a table, you use the following form of the create function statement:

create or replace function function_name (
   parameter_list
) 
returns table ( column_list ) 
language plpgsql
as $$
declare 
-- variable declaration
begin
-- body
end; $$ 

Instead of returning a single value, this syntax allows you to return a table with a specified column list




# Operaciones aritmeticas en PostgreSQL. Usar la linea de comandos SQL como calculadora (el "AS ..." es opcional):
SELECT (15 + 6) AS ADDITION;

SELECT (5 * 3) AS MULT;

SELECT ((200 * 2) / 100) AS PERCENTAGE;

# NOTA: En ORACLE, el mismo calculo se hace usando una tabla dummy llamada "DUAL",
#
#       SELECT (15 + 6) FROM DUAL;


# Para consultar la fecha u hora actual del servidor PostgrSQL:
SELECT NOW()::date;   # Para consultar la fecha.
SELECT NOW()::time;   # Para consultar la hora (hh:mm:sssssss).

# Otra manera de consultar la fecha actual del servidor PostgreSQL:
SELECT CURRENT_DATE;

# Consultar la hora:
SELECT CURRENT_TIME;

       timetz
--------------------
 08:01:34.656+05:30

# Se puede extraer (de todo el timestamp) valores como dia, mes y agno:
SELECT EXTRACT(CENTURY FROM TIMESTAMP '2000-12-16 12:21:13');

 date_part
-----------
        20

SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');
 date_part
-----------
        16

# Tambien es posible hacer calculo de diferencia entre dos fechas a traves de "AGE":
SELECT AGE(timestamp '2001-04-10', timestamp '1957-06-13');

# Dara como resultado la siguiente diferencia (en agnos, meses y dias):
           age
-------------------------
 43 years 9 mons 27 days



# Creacion y uso de una SEQUENCE (generador de secuencias) y ejemplo de uso en un query:
CREATE SEQUENCE secuencia
INCREMENT 1
START 1;

SELECT TO_CHAR(nextval('secuencia'), '0000000000');

NOTA: Se usa la capacidad de la funcion TO_CHAR para completar con ceros a la izquierda, pero si no se requiere completar 
      con ceros, entonces no hace falta.








# --------------------------------------------------------------------- #
# Ejemplo de calculo de tiempo de ejecucion de una funcion (o proceso). #
# --------------------------------------------------------------------- #
import time

#
# El metodo "time" devuelve la cantidad de segundos que han transcurrido desde el 1ro de Enero de 1970 ("Unix Epoch").
# El valor devuelto es de tipo float.
#
>>> time.time()
1603742948.0051677

# Ejemplo de procesamiento del producto de los primeros 100.000 numeros.
def calcula():
	producto = 1
	
	for i in range(1, 100000):
		producto *= i

	return producto

# Ahora ejecutamos esta funcion pero incluyendo el tomar la metrica del tiempo transcurrido durante su ejecucion:
tiempo_ini = time.time(); result = calcula(); tiempo_fin = time.time()

# Calculamos la diferencia y la colocamos en una variable para luego mostrarla:
tiempo_en_segundos = tiempo_fin - tiempo_ini

# Tardo casi 13 segundos la ejecucion!
>>> tiempo_en_segundos
12.797472476959229



# ------------------------------------------------ #
# Ejemplo de creacion de pagina HTML desde Python. #
# Ejemplo de control del browser desde Python.     #
# ------------------------------------------------ #
import webbrowser

f = open('pagina.html', 'w')

hypercode = """<html>
<head><head>
<body><p>Pagina generada esde Python!</p></body>
</html>"""

f.write(hypercode)
f.close()

webbrowser.open_new_tab('pagina.html')




# ---------------------------------------------------------------------------------------------------------- #
# Uso de numpy/PANDAS para graficar datos colocados en formato CSV en una URL dada y desde JUPYTER.          #
#                                                                                                            #
# NOTA: Antes de ejecutar estas sentencias usted debe instalar Panda y Plotlib desde el Terminal en Jupyter: #
#                                                                                                            #
#       pip install pandas matplotlib                                                                        #
#                                                                                                            #
# NOTA: PANDAS esta basado en Numpy (libreria de manejo de arreglos multidimensionales).                     #
# ---------------------------------------------------------------------------------------------------------- #
import pandas as pd

# URL donde esta el CSV.
download_url = (
                "https://raw.githubusercontent.com/fivethirtyeight/"
                "data/master/college-majors/recent-grads.csv"
)

# Lee el CSV desde esa direccion.
df = pd.read_csv(download_url)

type(df)     # Muestra el tipo.

pd.set_option("display.max.columns", None)

df.head()      # Con esta funcion se toma una muestra de las primeras 5 filas del CSV (sin ordenar).


# Se activa el graficador en Jupyter.
%matplotlib

# Al ejecutar la siguiente sentencia PANDAS muestra el grafico en una ventana a parte.
# df.plot(x="Rank", y=["P25th", "Median", "P75th"])

# Las siguientes sentencias muestran un grafico histograma de la columna Median. 
# NOTA: Para visualizar este grafico debe comentar la sentencia anterior.
# median_column = df["Median"]
# type(median_column)
# median_column.plot(kind="hist")

# Ahora vamos a crear un grafico de barras. Primero tomamos otra muestra ordenada por columna Median en forma ascendente del top 5.
top_5 = df.sort_values(by="Median", ascending=False).head()

# Mostramos el grafico de tipo barras verticales.
#top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)

# Ahora veamos un grafico de todos los empleados cuyo salario minimo esta por encima de los $60.000.
# NOTA: En este ejemplo vemos como puede incluirse condiciones del tipo < o >.
top_medians = df[df["Median"] > 60000].sort_values("Median")

top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")

# NOTA: Para armar una vista (igual que en base de datos) usando un criterio de seleccion:
#
#       subCon2 = data_leida.loc[data_leida["Median"] < 50000, ["P25th", "Median", "P75th"]]
#
#       En este ejemplo, de todo el DataFrame leido desde la URL, se seleccionan unicamente las columnas P25th, Median y P75th pero
#       unicamente las filas donde el valor Median sea menor que 50.000. La funcion "loc" hace esto.



# ------------------------------------------------- #
# Trabajar con archivos CSV desde PANDAS en Python. #
# ------------------------------------------------- #
import pandas as pd

# Ejemplo de lectura de datos contenidos en archivo CSV desde PANDAS.
data_frame = pd.read_csv(r'C:\Users\jportillo34\Desktop\airtravel.csv')

# Adicionalmente puede colocarle (dentro de su programa Python los headers a las columnas en caso de que el archivo CSV no las traiga):
#
# col_names = ['Id',
#              'Survived',
#              'Passenger Class',
#              'Full Name',
#              'Gender',
#              'Age',
#              'SibSp',
#              'Parch',
#              'Ticket Number',
#              'Price', 'Cabin',
#              'Station']
#
# titanic_data = pd.read_csv(r'E:\Datasets\titanic.csv', names=col_names, header=None)

# Ejemplo de creacion de archivo CSV desde PANDAS.
city = data_frame.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])

#
# NOTA: En la siguiente sentencia de creacion es necesario colocar el atributo "index" para que PANDAS no incluya en el archivo CSV
#       una numeracion en primera columna.
#
city.to_csv(r'C:\Users\jportillo34\Desktop\city.csv', index=False)




# ---------------------------------------------- #
# Trabajar con archivos CSV desde Python nativo. #
# ---------------------------------------------- #
import csv
 
path = r"C:\Users\jportillo34\Desktop\google_stock_data.csv"
 
# Listamos los modulos, clases y funciones que contiene la libreria csv.
print(dir(csv))
>> ['Dialect', 'DictReader', 'DictWriter', 'Error', 'OrderedDict', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 
 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', 
 '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 
 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 
 'unregister_dialect', 'writer']
 
# NOTA: Aqui solo se usan las funciones "reader" y "writer". Tambien hay para excel.

# Preparamos el archivo e indicamos que no cuente los caracteres newline.
archivo = open(path, newline='')

# Cargamos los datos desde el archivo CSV.
reader = csv.reader(archivo)

# Colocamos en una variable a parte la primera fila de cabeceras de columnas.
header = next(reader)

# Ahora colocamos los datos en otra variable.
#
# NOTA: Los datos vienen como strings de caracteres. Por tal motivo hay que trabajarlos
#       para que asuman su tipo de dato original (date, integer, float, etc.).
#       En el CSV de este ejemplo contiene siete columnas:
#       Date, Open, High, Low, Close, Volume y Adj. Close. Date es de tipo fecha
#       mientras que Open, High, Low, Close y Adj. Close son tipo float y Volume es integer.
#       Para manejar el tipo Datetime se debe importar dicho modulo:
from datetime import datetime

# Declaramos la variable que contendra los datos.
data = []

# La cargamos con los datos (crudos en principio).
for row in reader:
	# row = [Date, Open, High, Low, Close, volume, Adj. Close]
	date = datetime.strptime(row[0], '%m/%d/%Y')  # El segundo argumento es el formato.
	open_price = float(row[1])                    # Convierte a float.
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])                          # Convierte a integer.
	adj_close = float(row[6])
	data.append([date, open_price, high, low, close, volume, adj_close])


print(data[0])   # Imprimimos ejemplo de la primera fila.
>> [datetime.datetime(2014, 8, 19, 0, 0), 585.002622, 587.342658, 584.002627, 586.862643, 978600, 586.862643]

# NOTA: Como vemos ya todas las columnas tienen su tipo de datos del origen.

# Cerramos el archivo.
archivo.close()

#
# Ahora veamos un ejemplo de grabar datos en un archivo CSV. Para ello vamos a hacer unos calculos con la data leida.
#

# Calcule y grabe el Daily Stock Price a partir de los datos leidos.
returns_path = r"C:\Users\jportillo34\Desktop\google_returns.csv"

archivo = open(returns_path, 'w')

writer = csv.writer(archivo)

# Grabamos la primera linea de cabeceras de columnas.
writer.writerow(["Date", "Return"])

# Creamos un for loop con un indice con la cantidad de datos.
for i in range(len(data) - 1):
	# El -1 se coloca por cuestion del algoritmo de los calculos (es solo un ejemplo).
	todays_row = data[i]
	todays_date = todays_row[0]
	todays_price = todays_row[-1]  # El -1 tiene el efecto que devuelve el primer elemento.
	yesterdays_row = data[i+1]  # Esto es porque las fechas estan en orden decreciente.
	yesterdays_price = yesterdays_row[-1]
	# Ahora calculamos el Daily Return.
	daily_return = (todays_price - yesterdays_price) / yesterdays_price
	# Y grabamos la data en el archivo CSV.
	writer.writerow([todays_date, daily_return])

# Cerramos el archivo.
archivo.close()




# ------------------------------------------------- #
# Ejemplo de creacion de archivo JSON desde Python. #
# ------------------------------------------------- #
import json
 
data = {}

data['personal'] = []

# Se adicionan objetos.
data['personal'].append({
	'name': 'Scott',
	'website': 'stackabuse',
	'from': 'Nebraska'
})
data['personal'].append({
	'name': 'Larry',
	'website': 'google',
	'from': 'Michigan'
})
data['personal'].append({
	'name': 'Tim',
	'website': 'apple',
	'from': 'Alabama'
})

# Se crea el archivo y se convierte "data" a formato JSON. Luego se graba la sream JSON.

# En la siguiente sentencia es necesario colocar "r" antes del string. Esto se debe a que, al ver Python el simbolo "\"
# lo interpreta como una secuencia de escape Unicode al estilo \U00014...
#
with open(r'C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32\empleados.json', 'w') as outfile:
	json.dump(data, outfile)


# ----------------------------------------------------------------------------------------------------- #
# Ejemplo de lectura de un archivo JSON hacia Python y conversion del stream JSON en estructura Python. #
# ----------------------------------------------------------------------------------------------------- #

# En la siguiente sentencia es necesario colocar "r" antes del string. Esto se debe a que, al ver Python el simbolo "\"
# lo interpreta como una secuencia de escape Unicode al estilo \U00014...
#
with open(r'C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32\empleados.json') as json_file:
	data = json.load(json_file)

# Muestra los registros.
for p in data['people']:
	print('Name: ' + p['name'])
	print('Website: ' + p['website'])
	print('From: ' + p['from'])
	print(' -------------------- ')











# ---------------------------------------------------------------------------- #
# Importar un programa (o modulo) python desde otro programa python principal. #
# Hacer uso de funciones definidas en otro modulo                              #
# ---------------------------------------------------------------------------- #
#
# NOTA: Cuando el interprete Python es invocado (pasando como argumento el nombre de un programa .py) este hace dos cosas:
#
#       1.- Inicializa algunas variables especiales; entre ellas esta "__name__" y la carga con el nombre del modulo o
#           programa que ejecutara. Si el programa es uno solo (sin importar otros programas), entonces carga esta variable
#           con el valor "__main__".
#
#       2.- Ejecuta todas las sentencias en el programa.
#
#       Cuando se importa un programa desde un programa (o modulo) principal, si se consulta dentro del primero el valor
#       de la variable "__name__" este contiene el nombre del programa (o modulo) importado desde el modulo principal.
#
# NOTA: Desde un programa (o modulo) python se puede hacer uso de cualquier otro programa .py incluyendo una sentencia
#       "import <nombre del programa>". Esto le indicara al interprete python que incluya este programa y ejecute todo su
#       codigo.
#
# NOTA: En caso que se desee hacer uso de algunas funciones definidas dentro de un programa (o modulo) externo, debe 
#       indicarlo de la siguiente manera:
#
#       from <nombre del modulo externo> import <funcion1>, <funcion2>, ... <funcionN>
#
# Algunos ejemplos de los descrito arriba:
#

#
# El siguiente es el programa funciones.py que contiene dos funciones a ser usadas dentro del programa principal principal.py
#
import math

def functionA():
    print("Function A")

def functionB():
    print("Function B {}".format(math.sqrt(100)))

#
# NOTA: Es posible incluir (dentro de este modulo secundario) una condicion para verificar si es ejecutado como modulo 
#       principal y asi ejecutar otra funcionalidad interna del mismo que no debe ejecutarse cuando es utilizado solo 
#       como modulo secundario (o como libreria de funciones) de otro programa principal.
#
#       Ejemplo:

# Verifica si este programa (funciones.py) fue ejecutado como programa principal "...\python funciones.py"
if '__name__' == '__main__':

	# Si fue ejecutado como programa principal, entonces ejecute el siguiente codigo.
	#.......
	#...


#
# El siguiente es el programa principal principal.py dentro del cual se hace uso de las funciones definidas en funciones.py
#
from funciones import funcionA, functionB

# Invoca la functionA.
functionA()

# Invoca la functionB.
functionB()

# Es posible consultar el valor de la variable especial "__name__" para saber si este programa es el principal o main.
if __name__ == '__main__':

	# se usa la libreria sys.
	from sys import argv

	myargs = getopts(argv)

	if '-i' in myargs:
		print(myargs['-i'])

	print(myargs)













# ----------------------------------------------------------------------------------------- #
# Como acceder a las variables de ambiente del sistema (como PATH o CLASSPATH) desde Python #
# y encontrar en ellas algun path especifico. Usando a Python como scripting language!      #
#                                                                                           #
# NOTA: El objeto "os.environ" es un dictionary. Por tal motivo podemos usar el metodo get  #
#       para obtener algun elemento de dicho dictionary O podemos acceder al mismo usando   #
#       la sintaxis normal de acceso a elementos a traves de sus claves:                    #
#                                                                                           #
#       os.environ.get("<clave del elemento>") O os.environ["<clave del elemento>"]         #
#                                                                                           #
# NOTA: Python puede usarse como un utility de scripting en estos casos. La unica           #
#       diferencia con utilities como AWK y SEED es que se debe ingresar al interprete de   #
#       Python desde la linea de comandos del sistema y ejecutar lo siguiente desde alli.   #
# ----------------------------------------------------------------------------------------- #
import os

# Para estos ejemplos el contenido de la variable del sistema "PATH" es:
# C:\\Users\\jportillo34\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\pywin32_system32;
# C:\\Program Files (x86)\\Common Files\\Orcle\\Java\\javapath;C:\\MinGW\\bin;C:\\MinGW\\libexec\\gcc\\x86_64-pc-mingw32\\4.9.2;
# C:\\ProgramData\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\WINDOWS;C:\\WINDOWS\\System32\\Wbem;
# C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\QuickTime\\QTSystem\\;
# C:\\Program File(x86)\\MiKTeX 2.9\\miktex\\bin\\;C:\\Program Files\\Microsoft SQL Server\\120\\Tools\\Binn\\;
# C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Bin\\;C:\\Program Files\\Java\\jdk1.8.0_101;
# C:\\Program Files\\Java\\jre1.8.0_101\\bin;C:\\MinGW\\msys\\1.0\\bin;C:\\eigen\\Eigen;
# C:\\Users\\jportillo3\\AppData\\Local\\Programs\\Python\\Python35-32\\include;C:\\MATLAB7\\bin\\win32;
# C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Gradle\\bin;C:\\rogram Files\\Java\\jdk1.8.0_171\\bin;
# C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319;C:\\Program Files\\nodejs\\;C:\\Program Files\\dotnet\\;C:\jdk-15\\bin;
# C:\\Users\\jportillo34\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\;
# C:\\Users\\jportillo34\\AppData\\Local\\Programs\\Python\Python37-32\\;C:\\Program Files (x86)\\Microsoft VS Code\\bin;
# C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319;C:\\Users\\jportillo34\\AppData\\Raming\\npm

#
# el metodo "environ" devuelve el contenido de una variable del sistema (indicada). Y el comando find devuelve la posicion
# del substring indicado.
#
>>> print(os.environ['PATH'].find("jdk"))
568
>>> print(os.environ['PATH'].find("dotnet"))
937
>>> print(os.environ['PATH'].find("eigen"))
645
>>>

# Ahora, si queremos que Python no solo encuentre la ocurrencia de un substring (dentro de la variable del sistema), sino tambien
# que nos devuelva el substring completo (en este ejemplo seria algun path dentro de la variable "PATH"), entonces podemos usar
# la siguiente sentencia. Es un poco compleja pero funciona (utiliza el slicing de strings en Python). En el caso especifico de 
# este ejemplo se conoce (previamente) cual es el substring el cual necesitamos saber si esta (y como aparece) en la variable del
# sistema "PATH". Por ejemplo, queremos saber si el JDK de Java esta instalado (o al menos que su ruta esta declarada):
#
>>> subs = os.environ['PATH']      # Se coloca el contenido de la variable del sistema "PATH" en una variable en Python.

>>> print(pth[pth.find("C:\jdk-15") : pth.find("C:\jdk") + 13])

# En la sentencia anterior se pidio a Python que imprimiera el substring (slicing) de la variable "subs" que empieza en la 
# posicion devuelta por el metodo "find" del string y contando 13 caracteres hacia adelante (tambien usando "find" para esto).
# Es decir:
#           pth[<posicion de inicio del substring> : <posicion de inicio del substring + n caracteres>]
#
# Claro, previamente debemos saber como es (mas o menos) el path que estamos buscando (en este caso sabemos que seria algo asi 
# como 'jdk-15\bin' para el JDK de Java). El substring extraido pudo haberse colocado, tambien, en otra variable para usarlo 
# en otro procesamiento de tipo scripting.
#
C:\jdk-15\bin




# ------------------------------------------------------------------- #
# Trabajar con DICTIONARY (como si fueran tablas de base de datos).   #
#                                                                     #
# NOTA: Aqui se usa la idea de diccionarios anidados: cada item del   #
#       diccionario "empleados" es un sub-diccionario conteniendo     #
#       los datos del empleado.                                       #
# ------------------------------------------------------------------- #

# Este modulo tiene un metodo para imprimir de forma mas ordenada el contenido de un diccionario.
import pprint


# Se crea un diccionario con registros basicos (esto no es necesario; pudiera haberse declarado vacio "empleados = {}").
empleados = {'01':{'nombre':'Jose', 'apellido':'Portillo', 'departamento':'tecnologia'},
	         '02':{'nombre':'Alix', 'apellido':'Portillo', 'departamento':'finanzas'},
	         '03':{'nombre':'Fernando', 'apellido':'Lozano', 'departamento':'administracion'},
	         '04':{'nombre':'Merce', 'apellido':'Holskin', 'departamento':'enfermeria'},
	         '05':{'nombre':'Renato', 'apellido':'Rodriguez', 'departamento':'ingenieria'},
	         '06':{'nombre':'Luis', 'apellido':'Uchuya', 'departamento':'arquitectura'}
	         }


# El metodo "pprint" (del modulo pprint) imprime de forma mas ordenada un diccionario.
>>> pprint.pprint(empleados)
{'01': {'apellido': 'Portillo', 'departamento': 'tecnologia', 'nombre': 'Jose'},
 '02': {'apellido': 'Portillo', 'departamento': 'finanzas', 'nombre': 'Alix'},
 '03': {'apellido': 'Lozano',
        'departamento': 'administracion',
        'nombre': 'Fernando'},
 '04': {'apellido': 'Holskin', 'departamento': 'enfermeria', 'nombre': 'Merce'},
 '05': {'apellido': 'Rodriguez',
        'departamento': 'ingenieria',
        'nombre': 'Renato'},
 '06': {'apellido': 'Uchuya', 'departamento': 'arquitectura', 'nombre': 'Luis'}}


# Para mostrar solo la columna "departamento" de nuestra "tabla" de empleados:
>>> for row in empleados:
	   print(empleados[row]['departamento'])

tecnologia
finanzas
administracion
enfermeria
ingenieria
arquitectura


# Ahora, para adicionar un "registro" nuevo dentro de este diccionario:
empleados['07'] = {'nombre':'Perico', 'apellido':'Los Palotes', 'departamento':'vagabunderia'}

# Para actualizar uno existente es igual:
empleados['01'] = {'nombre': 'Rafael', 'apellido': 'Lugo', 'departamento': 'tecnologia'}

#
# Para hacer un "QUERY" en nuestra "tabla" usamos el metodo items() de la siguiente manera:
#
# Primero hagamos un "SELECT * FROM empleados":
>>> for k, v in empleados.items():
    #
    # IMPORTANTE: se usan dos variables (k y v) porque el metodo "items" puede devolver por separado la key y el value.
	print(k + " " + str(v))

01 {'nombre': 'Rafael', 'apellido': 'Lugo', 'departamento': 'tecnologia'}
02 {'nombre': 'Alix', 'apellido': 'Portillo', 'departamento': 'finanzas'}
03 {'nombre': 'Fernando', 'apellido': 'Lozano', 'departamento': 'administracion'}
04 {'nombre': 'Merce', 'apellido': 'Holskin', 'departamento': 'enfermeria'}
05 {'nombre': 'Renato', 'apellido': 'Rodriguez', 'departamento': 'ingenieria'}
06 {'nombre': 'Luis', 'apellido': 'Uchuya', 'departamento': 'arquitectura'}
07 {'nombre': 'Perico', 'apellido': 'Los Palotes', 'departamento': 'vagabunderia'}


# Ahora hagamos un "SELECT * FROM empleados WHERE departamento = 'ingenieria':
>>> for k, v in empleados.items():
	if v['departamento'] == 'ingenieria':
		print(k + " " + str(v))

05 {'nombre': 'Renato', 'apellido': 'Rodriguez', 'departamento': 'ingenieria'}


#
# Integracion entre Base de datos PostgreSQL y un diccionario Python. Vamos a leer una tabla desde PostgreSQL y llenar un
# diccionario con los datos.
#
import psycopg2

empleados = {}

conexion = psycopg2.connect(
	                        host = 'localhost',
                            database = 'inventario',
                            user = 'postgres',
                            password = 'apollo2134'
			               )

cursor = conexion.cursor()

cursor.execute("SELECT * FROM empleados")

rows = cursor.fetchall()

# Cargamos el diccionario con los datos leidos desde PostgreSQL.
for row in rows:
    # Para cada fila se convierten los tipos de datos a sus originales en PostgreSQL (DateTime, Integer, etc.).
	numIden  = int(row[0])      # Convierte a Integer.
	dept     = int(row[3])      # Convierte a Integer. 
	nombre   = row[2].strip()   # Elimina los espacios al inicio y fin.
	apellido = row[1].strip()

    # Se llena el "registro" en el diccionario.
	empleados[numIden] = {'nombre':nombre, 'apellido':apellido, 'departamento':dept}


# Hacemos un query "SELECT * FROM..." para verificar que los datos fueron cargados.
#
# NOTA: Observar que para imprimir los datos Integer se debe usar la funcion "srt()".
#
>>> for k, v in empleados.items():
	print("ID: " + str(k) + " | Nombre: " + v['nombre'] + " | Apellido: " + v['apellido'] + " | dept: " + str(v['departamento']))

ID: 1 | Nombre: Jose | Apellido: Portillo | dept: 12
ID: 3 | Nombre: Fernando | Apellido: Lozano | dept: 10
ID: 18 | Nombre: Isabel | Apellido: Portillo | dept: 11
ID: 9 | Nombre: Maria | Apellido: Gonzalez | dept: 14
ID: 7 | Nombre: Alexis | Apellido: Aponte | dept: 70

# Ahora hacemos un "SELECT * FROM... WHERE...":
>>> for k,v in empleados.items():
	if v['departamento'] == 14:
		print("ID: " + str(k) + " | Nombre: " + v['nombre'] + " | Apellido: " + v['apellido'] + " | Dept: " + str(v['departamento']))
	
ID: 9 | Nombre: Maria | Apellido: Gonzalez | Dept: 14



import getpass
import telnetlib


HOST     = "localhost"
user     = "jportillo34"
password = "A--pollo123"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")

tn.write(user + b"\n")

tn.read_until(b"Password: ")

tn.write(password + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))




# ----------------------------- #
# Envio de emails desde Python. #
#                               #
# OJO: En estudio!!!!!          #
#      AUN NO ESTA LISTO!!!!!!! #
# ----------------------------- #
import smtplib, ssl
>>> 
>>> from email.message import EmailMessage
>>> 
>>> msg = EmailMessage()
>>> 
>>> msg.set_content("Hola, como estas?")
>>> msg["Subject"] = "email de prueba desde Python"
>>> msg["From"] = "jportillo34@gmail.com"
>>> msg["To"] = "jportillo34@gmail.com"
>>> 
>>> context = ssl.create_default_context()
>>>
>>> with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
	smtp.starttls(context=context)
	smtp.login(msg["From"], "programador")
	smtp.send_message(msg)

(220, b'2.0.0 Ready to start TLS')
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    smtp.login(msg["From"], "programador")
  File "C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 730, in login
    raise last_exception
  File "C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "C:\Users\jportillo34\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials g1sm150869qtp.74 - gsmtp')




# -------------------------------------------------------------------------------------------------------- #
# Ejemplo de disassembly con "dis" en Python (muestra el codigo assembler para la Python virtual machine). #
# -------------------------------------------------------------------------------------------------------- #
NOTA: Disassembly de una funcion escrita en Python. Se hace con la funcion dis.dis(). 
      Primero, hay que hacer ">>>import dis" para poder usar dicha funcion. 
      A la funcion dis.dis hay que pasarle como argumento el nombre de la funcion 
      a hacer el disassembly colocandole ".__code__". 

      Para ver el codigo que genera una sentencia (sin compilar ni crear un programa completo) usar:

>>> dis.dis(compile("[23, 'a', 'b', 'c']", "", "eval"))
  1           0 LOAD_CONST               0 (23)
              2 LOAD_CONST               1 ('a')
              4 LOAD_CONST               2 ('b')
              6 LOAD_CONST               3 ('c')
              8 BUILD_LIST               4
             10 RETURN_VALUE

      Aqui "compile" compila la sentencia y luego "dis" genera el codigo en assembler.


Estos otros ejemplos muestran el codigo devuelve "dis" para un programa ya compilado:

def suma():
    var1 = 2
    var2 = 3
    var4 = (var1 + var2) / 100

>>> import dis

>>> dis.dis(suma.__code__)
  2           0 LOAD_CONST               1 (2)
              3 STORE_FAST               0 (var1)
  3           6 LOAD_CONST               2 (3)
              9 STORE_FAST               1 (var2)
  5          12 LOAD_FAST                0 (var1)
             15 LOAD_FAST                1 (var2)
             18 BINARY_ADD
             19 LOAD_CONST               3 (100)
             22 BINARY_TRUE_DIVIDE
             23 STORE_FAST               2 (var4)
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE


Otro ejemplo (EVAL de un interprete de Scheme LISP):

def eval(x, env=global_env):
...     "Evaluate an expression in an environment."
...     if isinstance(x, Symbol):      # variable reference
...         return env.find(x)[x]
...     elif not isinstance(x, List):  # constant literal
...         return x                
...     elif x[0] == 'quote':          # (quote exp)
...         (_, exp) = x
...         return exp
...     elif x[0] == 'if':             # (if test conseq alt)
...         (_, test, conseq, alt) = x
...         exp = (conseq if eval(test, env) else alt)
...         return eval(exp, env)
...     elif x[0] == 'define':         # (define var exp)
...         (_, var, exp) = x
...         env[var] = eval(exp, env)
...     elif x[0] == 'set!':           # (set! var exp)
...         (_, var, exp) = x
...         env.find(var)[var] = eval(exp, env)
...     elif x[0] == 'lambda':         # (lambda (var...) body)
...         (_, parms, body) = x
...         return Procedure(parms, body, env)
...     else:                          # (proc arg...)
...         proc = eval(x[0], env)
...         args = [eval(exp, env) for exp in x[1:]]
...         return proc(*args)
... 
>>> dis.dis(eval.__code__)
122           0 LOAD_GLOBAL              0 (isinstance)
              3 LOAD_FAST                0 (x)
              6 LOAD_GLOBAL              1 (Symbol)
              9 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             12 POP_JUMP_IF_FALSE       32
123          15 LOAD_DEREF               0 (env)
             18 LOAD_ATTR                2 (find)
             21 LOAD_FAST                0 (x)
             24 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             27 LOAD_FAST                0 (x)
             30 BINARY_SUBSCR
             31 RETURN_VALUE
124     >>   32 LOAD_GLOBAL              0 (isinstance)
             35 LOAD_FAST                0 (x)
             38 LOAD_GLOBAL              3 (List)
             41 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             44 POP_JUMP_IF_TRUE        51
125          47 LOAD_FAST                0 (x)
             50 RETURN_VALUE
126     >>   51 LOAD_FAST                0 (x)
             54 LOAD_CONST               1 (0)
             57 BINARY_SUBSCR
             58 LOAD_CONST               2 ('quote')
             61 COMPARE_OP               2 (==)
             64 POP_JUMP_IF_FALSE       83
127          67 LOAD_FAST                0 (x)
             70 UNPACK_SEQUENCE          2
             73 STORE_FAST               2 (_)
             76 STORE_FAST               3 (exp)
128          79 LOAD_FAST                3 (exp)
             82 RETURN_VALUE
129     >>   83 LOAD_FAST                0 (x)
             86 LOAD_CONST               1 (0)
             89 BINARY_SUBSCR
             90 LOAD_CONST               3 ('if')
             93 COMPARE_OP               2 (==)
             96 POP_JUMP_IF_FALSE      157
130          99 LOAD_FAST                0 (x)
            102 UNPACK_SEQUENCE          4
            105 STORE_FAST               2 (_)
            108 STORE_FAST               4 (test)
            111 STORE_FAST               5 (conseq)
            114 STORE_FAST               6 (alt)
131         117 LOAD_GLOBAL              4 (eval)
            120 LOAD_FAST                4 (test)
            123 LOAD_DEREF               0 (env)
            126 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            129 POP_JUMP_IF_FALSE      138
            132 LOAD_FAST                5 (conseq)
            135 JUMP_FORWARD             3 (to 141)
        >>  138 LOAD_FAST                6 (alt)
        >>  141 STORE_FAST               3 (exp)
132         144 LOAD_GLOBAL              4 (eval)
            147 LOAD_FAST                3 (exp)
            150 LOAD_DEREF               0 (env)
            153 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            156 RETURN_VALUE
133     >>  157 LOAD_FAST                0 (x)
            160 LOAD_CONST               1 (0)
            163 BINARY_SUBSCR
            164 LOAD_CONST               4 ('define')
            167 COMPARE_OP               2 (==)
            170 POP_JUMP_IF_FALSE      210
134         173 LOAD_FAST                0 (x)
            176 UNPACK_SEQUENCE          3
            179 STORE_FAST               2 (_)
            182 STORE_FAST               7 (var)
            185 STORE_FAST               3 (exp)
135         188 LOAD_GLOBAL              4 (eval)
            191 LOAD_FAST                3 (exp)
            194 LOAD_DEREF               0 (env)
            197 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            200 LOAD_DEREF               0 (env)
            203 LOAD_FAST                7 (var)
            206 STORE_SUBSCR
            207 JUMP_FORWARD           173 (to 383)
136     >>  210 LOAD_FAST                0 (x)
            213 LOAD_CONST               1 (0)
            216 BINARY_SUBSCR
            217 LOAD_CONST               5 ('set!')
            220 COMPARE_OP               2 (==)
            223 POP_JUMP_IF_FALSE      272
137         226 LOAD_FAST                0 (x)
            229 UNPACK_SEQUENCE          3
            232 STORE_FAST               2 (_)
            235 STORE_FAST               7 (var)
            238 STORE_FAST               3 (exp)
138         241 LOAD_GLOBAL              4 (eval)
            244 LOAD_FAST                3 (exp)
            247 LOAD_DEREF               0 (env)
            250 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            253 LOAD_DEREF               0 (env)
            256 LOAD_ATTR                2 (find)
            259 LOAD_FAST                7 (var)
            262 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
            265 LOAD_FAST                7 (var)
            268 STORE_SUBSCR
            269 JUMP_FORWARD           111 (to 383)
139     >>  272 LOAD_FAST                0 (x)


Otro ejemplo (la clase de generacion de codigo SPECTRE):

class SPECTRE_Assembler:

    # Codigos de operacion.
    opcodes = ["     CLA     op1,     ADD     op2,     STO     T#",
               "     CLA     op1,     SUB     op2,     STO     T#",
               "     LDQ     op1,     MPY     op2,     STQ     T#",
               "     LDQ     op1,     DIV     op2,     STQ     T#",
               "     CLA     op2,     STO     op1"
            ]

    def genera_codigo(self, ietiq, operando, fetiq):
        if ietiq and operando != "=":
            print("")
            print("")
            print(ietiq)
        if operando == "+":
            for sum in self.opcodes[0].split(","):
                print(sum)
        elif operando == "-":
            for res in self.opcodes[1].split(","):
                print(res)
        elif operando == "*":
            for mul in self.opcodes[2].split(","):
                print(mul)
        elif operando == "/":
            for div in self.opcodes[3].split(","):
                print(div)
        elif operando == "=":
            for igual in self.opcodes[4].split(","):
                print(igual)
        if fetiq:
            print('     ' + fetiq + '     ' + ietiq)

>>> dis.dis(SPECTRE_Assembler)
Disassembly of genera_codigo:
 12           0 LOAD_FAST                1 (ietiq)
              2 POP_JUMP_IF_FALSE       36
              4 LOAD_FAST                2 (operando)
              6 LOAD_CONST               1 ('=')
              8 COMPARE_OP               3 (!=)
             10 POP_JUMP_IF_FALSE       36
 13          12 LOAD_GLOBAL              0 (print)
             14 LOAD_CONST               2 ('')
             16 CALL_FUNCTION            1
             18 POP_TOP
 14          20 LOAD_GLOBAL              0 (print)
             22 LOAD_CONST               2 ('')
             24 CALL_FUNCTION            1
             26 POP_TOP
 15          28 LOAD_GLOBAL              0 (print)
             30 LOAD_FAST                1 (ietiq)
             32 CALL_FUNCTION            1
             34 POP_TOP
 16     >>   36 LOAD_FAST                2 (operando)
             38 LOAD_CONST               3 ('+')
             40 COMPARE_OP               2 (==)
             42 POP_JUMP_IF_FALSE       80
 17          44 SETUP_LOOP             208 (to 254)
             46 LOAD_FAST                0 (self)
             48 LOAD_ATTR                1 (opcodes)
             50 LOAD_CONST               4 (0)
             52 BINARY_SUBSCR
             54 LOAD_METHOD              2 (split)
             56 LOAD_CONST               5 (',')
             58 CALL_METHOD              1
             60 GET_ITER
        >>   62 FOR_ITER                12 (to 76)
             64 STORE_FAST               4 (sum)
 18          66 LOAD_GLOBAL              0 (print)
             68 LOAD_FAST                4 (sum)
             70 CALL_FUNCTION            1
             72 POP_TOP
             74 JUMP_ABSOLUTE           62
        >>   76 POP_BLOCK
             78 JUMP_FORWARD           174 (to 254)
 19     >>   80 LOAD_FAST                2 (operando)
             82 LOAD_CONST               6 ('-')
             84 COMPARE_OP               2 (==)
             86 POP_JUMP_IF_FALSE      124
 20          88 SETUP_LOOP             164 (to 254)
             90 LOAD_FAST                0 (self)
             92 LOAD_ATTR                1 (opcodes)
             94 LOAD_CONST               7 (1)
             96 BINARY_SUBSCR
             98 LOAD_METHOD              2 (split)
            100 LOAD_CONST               5 (',')
            102 CALL_METHOD              1
            104 GET_ITER
        >>  106 FOR_ITER                12 (to 120)
            108 STORE_FAST               5 (res)
 21         110 LOAD_GLOBAL              0 (print)
            112 LOAD_FAST                5 (res)
            114 CALL_FUNCTION            1
            116 POP_TOP
            118 JUMP_ABSOLUTE          106
        >>  120 POP_BLOCK
            122 JUMP_FORWARD           130 (to 254)
 22     >>  124 LOAD_FAST                2 (operando)
            126 LOAD_CONST               8 ('*')
            128 COMPARE_OP               2 (==)
            130 POP_JUMP_IF_FALSE      168
 23         132 SETUP_LOOP             120 (to 254)
            134 LOAD_FAST                0 (self)
            136 LOAD_ATTR                1 (opcodes)
            138 LOAD_CONST               9 (2)
            140 BINARY_SUBSCR
            142 LOAD_METHOD              2 (split)
            144 LOAD_CONST               5 (',')
            146 CALL_METHOD              1
            148 GET_ITER
        >>  150 FOR_ITER                12 (to 164)
            152 STORE_FAST               6 (mul)
 24         154 LOAD_GLOBAL              0 (print)
            156 LOAD_FAST                6 (mul)
            158 CALL_FUNCTION            1
            160 POP_TOP
            162 JUMP_ABSOLUTE          150
        >>  164 POP_BLOCK
            166 JUMP_FORWARD            86 (to 254)
 25     >>  168 LOAD_FAST                2 (operando)
            170 LOAD_CONST              10 ('/')
            172 COMPARE_OP               2 (==)
            174 POP_JUMP_IF_FALSE      212
 26         176 SETUP_LOOP              76 (to 254)
            178 LOAD_FAST                0 (self)
            180 LOAD_ATTR                1 (opcodes)
            182 LOAD_CONST              11 (3)
            184 BINARY_SUBSCR
            186 LOAD_METHOD              2 (split)
            188 LOAD_CONST               5 (',')
            190 CALL_METHOD              1
            192 GET_ITER
        >>  194 FOR_ITER                12 (to 208)
            196 STORE_FAST               7 (div)
 27         198 LOAD_GLOBAL              0 (print)
            200 LOAD_FAST                7 (div)
            202 CALL_FUNCTION            1
            204 POP_TOP
            206 JUMP_ABSOLUTE          194
        >>  208 POP_BLOCK
            210 JUMP_FORWARD            42 (to 254)
 28     >>  212 LOAD_FAST                2 (operando)
            214 LOAD_CONST               1 ('=')
            216 COMPARE_OP               2 (==)
            218 POP_JUMP_IF_FALSE      254
 29         220 SETUP_LOOP              32 (to 254)
            222 LOAD_FAST                0 (self)
            224 LOAD_ATTR                1 (opcodes)
            226 LOAD_CONST              12 (4)
            228 BINARY_SUBSCR
            230 LOAD_METHOD              2 (split)
            232 LOAD_CONST               5 (',')
            234 CALL_METHOD              1
            236 GET_ITER
        >>  238 FOR_ITER                12 (to 252)
            240 STORE_FAST               8 (igual)
 30         242 LOAD_GLOBAL              0 (print)
            244 LOAD_FAST                8 (igual)
            246 CALL_FUNCTION            1
            248 POP_TOP
            250 JUMP_ABSOLUTE          238
        >>  252 POP_BLOCK
 31     >>  254 LOAD_FAST                3 (fetiq)
            256 EXTENDED_ARG             1
            258 POP_JUMP_IF_FALSE      280
 32         260 LOAD_GLOBAL              0 (print)
            262 LOAD_CONST              13 ('     ')
            264 LOAD_FAST                3 (fetiq)
            266 BINARY_ADD
            268 LOAD_CONST              13 ('     ')
            270 BINARY_ADD
            272 LOAD_FAST                1 (ietiq)
            274 BINARY_ADD
            276 CALL_FUNCTION            1
            278 POP_TOP
        >>  280 LOAD_CONST               0 (None)
            282 RETURN_VALUE



# ------------------------------------------------------------ #
# Ejemplo de modificacion de los byte-code en tiempo real.     #
# Python permite modificar un programa compilado en byte-code. #
# ------------------------------------------------------------ #

# Funcion de ejemplo:
def fact(n):
	if n <= 1: return 1
	return n * fact(n - 1)

# Aplicamos "dis" para ver el codigo assembler generado:
>>> import dis
>>> 
>>> dis.dis(fact)
  2           0 LOAD_FAST                0 (n)
              2 LOAD_CONST               1 (1)
              4 COMPARE_OP               1 (<=)
              6 POP_JUMP_IF_FALSE       12
              8 LOAD_CONST               1 (1)
             10 RETURN_VALUE

  3     >>   12 LOAD_FAST                0 (n)
             14 LOAD_GLOBAL              0 (fact)
             16 LOAD_FAST                0 (n)
             18 LOAD_CONST               1 (1)
             20 BINARY_SUBTRACT
             22 CALL_FUNCTION            1
             24 BINARY_MULTIPLY
             26 RETURN_VALUE

# Ahora veamos los byte-codes:
>>> fact.__code__.co_code
b'|\x00d\x01k\x01r\x0cd\x01S\x00|\x00t\x00|\x00d\x01\x18\x00\x83\x01\x14\x00S\x00'

# NOTA: En el archivo de cabecera "opcode.h" de la distribucion CPython los codigos de operacion aparecen en decimal, mientras
#       que los codigos de operacion en "co_code" se muestran en hexadecimal.

# Vamos a cambiar la instruccion "BINARY_SUBTRACT" (en la posicion 20) por la instruccion "BINARY_ADD":
from types import CodeType

def fix_function(func, payload):
	fn_code = func.__code__
	func.__code__ = CodeType(fn_code.co_argcount,
				 fn_code.co_kwonlyargcount,
				 fn_code.co_nlocals,
				 fn_code.co_stacksize,
				 fn_code.co_flags,
				 payload,
				 fn_code.co_consts,
				 fn_code.co_names,
				 fn_code.co_varnames,
				 fn_code.co_filename,
				 fn_code.co_name,
				 fn_code.co_firstlineno,
				 fn_code.co_lnotab,
				 fn_code.co_freevars,
				 fn_code.co_cellvars,
				 )

# la variable payload contendra el string retornado por fact.__code__.co_code (tal como se ve arriba). Queremos suplantar 
# (en la posicion 20) el codigo de operacion "18" por el "17" (que corresponde al nemonico "BINARY_ADD").
payload = fact.__code__.co_code

add_opcode = dis.opmap['BINARY_ADD'].to_bytes(1, byteorder='little')   # Obtiene (del Python) el codigo de operacion de BINARY_ADD

payload = payload[0:20] + add_opcode + payload[21:]    # Concatena el nuevo codigo de operacion dentro del string

# Mostramos primero el string para confirmar que el codigo de operacion de BINARY_SUBTRACT fue sustituido:
>>> payload
b'|\x00d\x01k\x01r\x0cd\x01S\x00|\x00t\x00|\x00d\x01\x17\x00\x83\x01\x14\x00S\x00'

# Ahora aplicamos el cambio en "__code__" de la funcion fact compilada:
fix_function(fact, payload)

# Verificamos el codigo assembler de nuevo:
>>> dis.dis(fact)
  2           0 LOAD_FAST                0 (n)
              2 LOAD_CONST               1 (1)
              4 COMPARE_OP               1 (<=)
              6 POP_JUMP_IF_FALSE       12
              8 LOAD_CONST               1 (1)
             10 RETURN_VALUE

  3     >>   12 LOAD_FAST                0 (n)
             14 LOAD_GLOBAL              0 (fact)
             16 LOAD_FAST                0 (n)
             18 LOAD_CONST               1 (1)
             20 BINARY_ADD                          <--------- Ya lo cambio!
             22 CALL_FUNCTION            1
             24 BINARY_MULTIPLY
             26 RETURN_VALUE




#
#
#                                        SECCION DE EJEMPLOS JAVA                                              #
#
#

#
# NOTA: Para activar la variable de ambiente PATH del sistema (para acceder a las aplicaciones javac, javap, jshell, etc),
#       debe ir al Advance System Settings de Windows. Alli debe editar la variable PATH que se encuentra en "System Variables"
#       y adicionar el path "C:\...\bin" hasta el directorio bin del JDK instalado.
#
#       La otra variable de ambiente que se debe crear (para que el compilador javac pueda acceder a las librerias .jar) es la
#       variable CLASSPATH. Si no existe debe crearla e incluir en ella el directorio donde se encuentran los .jar. Abajo ahi
#       un ejemplo de esto usando la libreria JDBC.
#
# NOTA: Al momento de compilar un programa Java usted debe indicar la extension (.java) del nombre del programa. De lo contrario 
#       recibira el siguiente mensaje de error del compilador:
#
#       error: Class names, 'prueba', are only accepted if annotation processing is explicitly requested
#
# NOTA: Para ejecutar un programa Java (.class) cuando la carpeta donde se encuentra dicho programa no esta incluida en la variable 
#       CLASSPATH, usted debe incluir el parametro -cp y la ruta hacia dicha carpeta. De lo contrario la Java Virtual Machine mostrara 
#       el siguiente mensaje de error:
#
#       Error: Could not find or load main class prueba
#              Caused by: java.lang.ClassNotFoundException: prueba
#
#       Ejemplo, supongamos que el archivo .class se encuentra en el Desktop:
#
#       C:\Users\user\Desktop>java -cp C:\Users\user\Desktop prueba
#
# NOTA: Hay veces que al intentar ejecutar un programa Java, si dicho programa se compilo con una version mas reciente del compilador, 
#       entonces la virtual machine protesta con el siguiente mensaje:
#
#       Error: A JNI error has occurred, please check your installation and try again
#       Exception in thread "main" java.lang.UnsupportedClassVersionError: ... has been compiled 
#       by a more recent version of the Java Runtime...
#
#       Para evitar este tipo de errores se debe tener el buen habito de actualizar la virtual machine (o tener una sola version).
#
# NOTA: El interprete JSHELL viene ahora dentro del JDK. Permite crear programas y ejecutarlos online.
#       Para salir del shell se ejecuta "jshell>/exit".
#
# MEJORA EN JAVA (version >= 13): En el caso de la sentencia switch...case ya no se necesita usar el comando "break"
#                                 para salir del switch. Ahora se usa un comando arrow (->). En el caso de opciones
#                                 que necesiten ejecutar mas de una sentencia estas deben encerrarse entre llaves
#                                 como cualquier bloque Java. Ejemplo:
#
#                                 // JDK 13 (Preview) introduces "arrow labels"
#                                 String day = "Thursday";
#
#                                 switch (day) 
#                                 {
#                                    case "Monday" ->
#                                       System.out.println("1");                // use '->' and no break needed
#
#                                    case "Tuesday", "Wednesday", "Thursday" -> // multiple labels are commas separated
#                                       System.out.println("2 or 3 or 4");
#
#                                    case "Friday" ->
#                                       System.out.println("5");
#
#                                    default -> 
#                                    {                               // braces needed for block
#                                       System.out.println("others");
#                                       System.out.println("try again");
#                                    }
#                                 }
#
# NOTA: Cualquier metodo que sea declarado en la clase principal de un fuente, para que pueda ser invocado desde el metodo main 
#       este debe ser declarado "static".
#
# NOTA: JAVA no ofrece la posibilidad de operator overloading!
#
# NOTA SOBRE EL MODIFICADOR STATIC: 
#       Un programa JAVA puede hacer uso de los campos y metodos de una clase UNICAMENTE cuando dicha clase es 
#       instanciada (a traves del objeto creado en el programa mismo). Si se quiere hacer uso (invocar) un 
#       campo o variable o metodo declarado dentro de una clase, dicho elemento debe incluir el modificador static.
#
#       Ejemplo,
#
#public class ejemplo {
#   int miFuncion(int a) { return(a*a); }
#
#   public static void main(String args[]) {
#      System.out.println(miFuncion(2));
#   }
#}
#
#       La compilacion de este ejemplo dara un error porque el metodo miFuncion no tiene el modificador static. Para solventar 
#       esta situacion podemos hacer dos cosas: 1) declarar el metodo como 
#
#       static int miFuncion(int a)...
#
#       o instanciar la clase ejemplo y luego SI podremos invocar el metodo desde el objeto creado:
#
#   public static void main(String args[]) {
#      ejemplo miEje = new ejemplo();
#
#      System.out.println(miEje.miFuncion(2));
#   }

/* Ejemplo de uso de clases. Ejemplo de creacion de un vector (ArrayList) de objetos de una clase creada por el usuario. Ejemplo 
   de propiedades con tipo de dato de una clase creada por el usuario (en el ejemplo abajo seria del tipo "punto" dentro de una 
   clase que representa el plano cartesiano.                                                                                     */

import java.io.DataOutputStream;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Arrays;
import java.lang.Math;

public class prueba
{
   /* Representa un punto del plano cartesiano. */
   static class punto
   {
      double x;
      double y;

      public punto(double px, double py) { x = px; y = py; }
   }

   /* Representa un plano cartesiano. */
   static public class plano
   {
      private punto p;
      private punto q;

      /* Constructor. */
      public plano() { p = new punto(0.00, 0.00); q = new punto(0.00, 0.00); p.x = 0.0; p.y = 0.0; q.x = 0.0; q.y = 0.0; }

      public void setP(double parx, double pary) { p.x = parx; p.y = pary; }
      public void setQ(double parx, double pary) { q.x = parx; q.y = pary; }
      public double getPx() { return(p.x); }
      public double getPy() { return(p.y); }
      public double getQx() { return(q.x); }
      public double getQy() { return(q.y); }

      /* Distancia entre dos puntos del plano (Utiliza las funciones de la libreria java.lang.Math). */
      public double distancia() {
                                   double a = q.x - p.x;
                                   double b = q.y - p.y;
                                   return(Math.sqrt(a*a + b*b));
                                }
   }

   /* Ejemplo de clase conteniendo una propiedad de tipo arreglo. */
   static class linea
   {
      public int id;
      ArrayList<punto> vector = new ArrayList<punto>();
   }


   public static void main(String[] args)
   {
      plano miPlano;

      miPlano = new plano();

      miPlano.setQ(4.0, 2.0);
      System.out.println("p.x=" + miPlano.getPx() + ", p.y=" + miPlano.getPy() + ", q.x=" + miPlano.getQx() + ", q.y=" + miPlano.getQy());
      System.out.println("...y Distancia=" + miPlano.distancia());

      /* Creamos una instancia de linea. */
      linea miLinea = new linea();

      miLinea.id = 10;   // asignamos el ID de la linea.

      /* Alimentamos la linea con algunos puntos. Observar como se usa el metodo new. */
      miLinea.vector.add(0, new punto(2.00, 4.00));
      miLinea.vector.add(1, new punto(3.00, 5.00));
      miLinea.vector.add(2, new punto(15.00, 25.00));

      /* Acceso a traves de una expresion LAMBDA. */
      miLinea.vector.forEach((x) -> { System.out.println(x.x); });   // Esta es una funcion LAMBDA EXPRESSION.

      /* Acceso a traves de un Iterator. */
      Iterator<punto> lineaIt = miLinea.vector.iterator();
      while(lineaIt.hasNext()) System.out.println(lineaIt.next().x);

      /* Acceso individual a cada objeto del vector.*/
      System.out.println("ID:" + miLinea.id + ", x:" + miLinea.vector.get(0).x + ", y:" + miLinea.vector.get(0).y);
      System.out.println("ID:" + miLinea.id + ", x:" + miLinea.vector.get(1).x + ", y:" + miLinea.vector.get(1).y);
      System.out.println("ID:" + miLinea.id + ", x:" + miLinea.vector.get(2).x + ", y:" + miLinea.vector.get(2).y);
   }
}



/* ----------------------------------------------------------------------------------- */
/* Para ejecutar esta clase escribiendo estas sentencias dentro del interprete JSHELL, */
/* se debe escribir "jshell>prueba.main(new String[0])".                               */
/*                                                                                     */
/* Para generar el .class (p-codes) "C:\...\bin>javac prueba.java".                         */
/*                                                                                     */
/* Para generar el listado assembler de p-codes "C:\...\bin>javap -c prueba > prueba.s"*/
/* ----------------------------------------------------------------------------------- */
public class prueba 
{
	// El atributo static es necesario aqui para poder invocar este metodo desde el main.
	public static int calcula(int a, int b)
	{
		return((a + b) / 2);
	}

	public static void main(String[] args)
	{
		int a = 50;
		int b = 100;
		int c = calcula(a, b);


		int varAle = (int)((Math.random() * 100) + 1);

		System.out.println("Valor aleatorio: " + varAle + " y resultado del calculo: " + c);
	}
}

# Ejemplo de codigo assembler p-code generado (para la java virtual machine) del ejemplo anterior:

Compiled from "prueba.java"
public class prueba {
  public prueba();
       0: ALOAD_0
       1: INVOKESPECIAL #1                  // METHOD JAVA/LANG/OBJECT."<INIT>":()V
       4: RETURN
  public static int calcula(int, int);
       0: ILOAD_0
       1: ILOAD_1
       2: IADD
       3: ICONST_2
       4: IDIV
       5: IRETURN
  public static void main(java.lang.String[]);
       0: BIPUSH        50
       2: ISTORE_1
       3: BIPUSH        100
       5: ISTORE_2
       6: ILOAD_1
       7: ILOAD_2
       8: INVOKESTATIC  #7                  // METHOD CALCULA:(II)I
      11: ISTORE_3
      12: INVOKESTATIC  #13                 // METHOD JAVA/LANG/MATH.RANDOM:()D
      15: LDC2_W        #19                 // DOUBLE 100.0D
      18: DMUL
      19: DCONST_1
      20: DADD
      21: D2I
      22: ISTORE        4
      24: GETSTATIC     #21                 // FIELD JAVA/LANG/SYSTEM.OUT:LJAVA/IO/PRINTSTREAM;
      27: ILOAD         4
      29: ILOAD_3
      30: INVOKEDYNAMIC #27,  0             // INVOKEDYNAMIC #0:MAKECONCATWITHCONSTANTS:(II)LJAVA/LANG/STRING;
      35: INVOKEVIRTUAL #31                 // METHOD JAVA/IO/PRINTSTREAM.PRINTLN:(LJAVA/LANG/STRING;)V
      38: RETURN
}



/* ---------------------------------------------------------------- */
/* Ejemplo de paso de argumentos (desde la linea de comandos) hacia */
/* un programa Java. En este ejemplo se ejecuta:                    */
/*                                                                  */
/*                              C:\jdk-15\bin>java fibonaci 10      */
/*                                                                  */
/* y se obtiene el siguiente resultado:                             */
/*                                                                  */
/*                                      Valor del fibonaci: 55      */
/*                                                                  */
/* NOTA: La numeracion de los argumentos empieza en cero y no       */
/*       incluye "java" ni el nombre del programa:                  */
/*                                                                  */
/*       \..>java ejemplo   2       4       6                       */
/*                        args[0] args[1] args[2] ...               */
/* ---------------------------------------------------------------- */
public class fibonaci
{
    public static int fib(int n)
    {
        if (n == 0) return(0);
        if (n == 1) return(1);
        return(fib(n - 1) + fib(n - 2));
    }

    public static void main(String[] args)
    {
    	int n = Integer.parseInt(args[0]);  // Se debe convertir a integer el argumento (su tipo original es String).

        System.out.println("Valor del fibonaci: " + fib(n));
    }
}


Otro ejemplo:

public class fib
{
   static int fibFunction(int x) { if(x == 0 || x == 1) return(x); return(fibFunction(x - 1) + fibFunction(x - 2)); }

   public static void main(String[] args) { int i = Integer.parseInt(args[0]); System.out.println(fibFunction(i)); }
}




/* ------------------------------------------------------------------------------------------------------------------ */
/* Ejemplo de uso del metodo sort para ordenar arrays cuyos elementos son de un tipo de dato basico (int en este caso). */
/*                                                                                                                    */
/* En el proximo ejemplo (abajo) usamos una collection del tipo ArrayList para representar objetos de cualquier clase */
/* y ordenarlos con su metodo "sort".                                                                                 */
/*                                                                                                                    */
/* Tambien se incluye un ejemplo de uso del "for each" en JAVA para iterar a traves de los elementos de un array.     */
/* ------------------------------------------------------------------------------------------------------------------ */
import java.util.Arrays;

public class prueba
{
   public static void main(String[] args)
   {
      // Ejemplo de metodo "sort".
      int [] lista = new int [] {90, 23, 5, 109, 12, 22, 67, 34};

      for(int elemento: lista) System.out.println("Antes del sort: " + elemento);

      // Para usar este metodo debemos importar la libreria "java.util.Arrays".
      Arrays.sort(lista);

      for(int elemento: lista) System.out.println("Despues del sort: " + elemento);
   }
}




/* --------------------------------------------------------------------------------- */
/* Ejemplo de collection del tipo ArrayList de objetos, iteradores, uso de Generics, */
/* sobrecarga de metodos y simulacion de apuntadores (en JAVA no existe ese concepto)*/
/* Se crea un ArrayList de objetos tipo "elemento" (una clase).                      */
/* --------------------------------------------------------------------------------- */
import java.util.ArrayList;
import java.util.Iterator;


public class prueba
{
   static class elemento
   {
      public int atr1;

      public elemento(int parm) { atr1 = parm; }

      public int getElemento() { return(atr1); }
   }

   // Ejemplo de uso de Generics.
   static public class Vector<Item>
   {
      private Item arrSt;

      public Vector(Item arrPar) { arrSt = arrPar; }

      public Item getVector() { return(arrSt); }
   }

   /* Ejemplo de sobrecarga de metodos. Dos o mas metodos pudieran tener el mismo nombre pero manejar tipos de datos
      diferentes. El compilador de Java se encarga de detectar cual metodo invocar dependiendo del tipo de dato usado 
      como argumento en la invocacion.                                                                                */
   static int suma(int oper1, int oper2) { return(oper1 + oper2); }
   static double suma(double oper1, double oper2) { return(oper1 + oper2); }

   public static void main(String[] args)
   {
      // Ejemplo de ArrayList y uso de iteradores.
      ArrayList<String> cars = new ArrayList<String>();

      cars.add("Volvo");
      cars.add("BMW");
      cars.add("Ford");
      cars.add("Mazda");

      Iterator<String> it = cars.iterator();

      while(it.hasNext()) System.out.println(it.next());


      ArrayList<elemento> elementos = new ArrayList<elemento>();

      // Cada vez que se adiciona un elemento, se debe invocar el constructor (es decir: usar "new...").
      elementos.add(new elemento(10));
      elementos.add(new elemento(15));
      elementos.add(new elemento(20));

      Iterator<elemento> it2 = elementos.iterator();

      while(it2.hasNext()) System.out.println("Elemento[0]: " + it2.next().getElemento());


      // Ejemplo de sobrecarga de metodos.
      System.out.println("Resultado: " + suma(2.4, 3.9));


      // Simulacion de apuntadores. En JAVA no existe ese concepto.
      elemento a;
      elemento b;

      a = new elemento(40);
      b = new elemento(60);

      a = b;   // Asigna la direccion de la segunda instancia de la clase elementos (b) a la primera instancia (a).

      System.out.println("Valor de a: " + a.getElemento());

      // int[] a = {1, 2, 3, 4, 5, 6, 7, 8};

      // Vector<int[]> v = new Vector<int[]>(a);

      // System.out.println("Valor del vector s: " + v.getVector()[0]);
   }
}





/* --------------------------------------------------------------------------------------------------------------- */
/* Ejemplo de sobrecarga de metodos. Dos o mas metodos pudieran tener el mismo nombre pero manejar tipos de datos  */
/* diferentes. El compilador de Java se encarga de detectar cual metodo invocar dependiendo del tipo de dato usado */
/* como argumento en la invocacion.                                                                                */
/* --------------------------------------------------------------------------------------------------------------- */
   static int    suma(int oper1, int oper2)       { return(oper1 + oper2); }
   static double suma(double oper1, double oper2) { return(oper1 + oper2); }

   public static void main(String[] args)
   {
      System.out.println("Resultado: " + suma(2.4, 3.9));
   }



/* ---------------------------------------------------------------------------------------------------- */
/* En JAVA no existe el concepto de pointer a una posicion de memoria. Es posible, sin embargo, simular */
/* esto usando clases (objetos). Aqui hay un ejemplo de como, al declarar una instancia de una clase,   */
/* luego es posible asignar a otra instancia de la misma clase la instancia creada primero. Esto hace   */
/* el efecto de asignar la direccion de memoria de la primera instancia a la segunda instancia.         */
/* ---------------------------------------------------------------------------------------------------- */
   static class elemento
   {
      public int atr1;

      public elemento(int parm) { atr1 = parm; }

      public int getElemento() { return(atr1); }
   }

   public static void main(String[] args)
   {
      elemento a;
      elemento b;

      a = new elemento(40);
      b = new elemento(60);

      a = b;

      System.out.println("Valor de a: " + a.getElemento());


    El resultado que se imprime es 60, es decir: el valor asignado al atributo de la segunda instancia!




/* -------------------------------------- */
/* Ejemplo de lectura de archivo en JAVA. */
/* -------------------------------------- */
import java.io.File;                   // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner;              // Import the Scanner class to read text files

public class herencia {
   public static void main(String[] args) {
      try {
         File myObj = new File("jsonTEst.json");
         Scanner myReader = new Scanner(myObj);

         while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            System.out.println(data);
         }

         myReader.close();
      } catch (FileNotFoundException e) {
         System.out.println("An error occurred.");
         e.printStackTrace();
      }
   }
}




/* ------------------------------------------------------------------------ */
/* Como se fuerza terminar (desde un punto especifico) un programa en JAVA. */
/* ------------------------------------------------------------------------ */
System.exit(0);





/* ------------------------------- */
/* Como se simula el goto en JAVA. */
/* ------------------------------- */
break salida;
..
..
..
salida:




/* ---------------------------------------------------------------------------------------------------- */
/* Como copiar (y utilizar luego) el contenido de una variable tipo String en un arreglo de caracteres. */
/* ---------------------------------------------------------------------------------------------------- */
import java.util.*;

public class herencia {
   public static void main(String[] args) {
      String muestra = "Esta es una prueba";

      char caracteres[] = new char[muestra.length()];

      for(int i = 0; i < muestra.length(); i++) caracteres[i] = muestra.charAt(i);

      // Modo tradicional de iterar un arreglo: for(int i = 0; i < caracteres.length; i++) System.out.print(caracteres[i]);
      for(char c : caracteres) System.out.print(c);   // Usando for each...
   }
}





/* -------------------------------------------------------------------------- */
/* Ejemplo de conexion hacia POSTGRESQL desde Java utilizando el driver JDBC. */
/*                                                                            */
/* NOTA: Para hacer esta integracion debe descargar el driver JDBC. Para el   */
/*       momento de crear este ejemplo el nombre del archivo (.jar) que       */
/*       contiene el driver es "postgresql-42.2.18.jar" (varia con version).  */
/*                                                                            */
/* NOTA: Luego de descargar este archivo (.jar) debe colocarlo en una carpeta */
/*       del JDK. Para este ejemplo se coloco en "C:\jdk-15\bin".             */
/*                                                                            */
/*       Una vez que se tenga dicho archivo colocado en esa carpeta, debe     */
/*       actualizar (o crear si no existe) la variable de ambiente CLASSPATH. */
/*       Para hacer esto vaya a las "System Variables" en System Properties   */
/*       de Windows. Alli debe crear una variable nueva (de no existir)       */
/*       llamada "CLASSPATH" e incluir en ella lo siguiente:                  */
/*                                                                            */
/*       .;C:\jdk-15\bin;C:\jdk-15\bin\postgresql-42.2.18.jar                 */
/*                                                                            */
/*       En esta sintaxis se le indica a la Java Virtual Machine donde esta   */
/*       localizado el driver JDBC. Guardar el cambio de ambiente.            */
/*                                                                            */
/* NOTA: Luego, compilar el siguiente programa de forma normal:               */
/*                                                                            */
/*       C:\jdk-15\bin>javac prueba.java                                      */
/*                                                                            */
/* NOTA: Por ultimo para ejecutar esta prueba de conexion y consulta SQL:     */
/*                                                                            */
/*       C:\jdk-15\bin>java -Djdbc.drivers=org.postgresql.Driver prueba       */
/*                                                                            */
/*       Con la opcion "-D" se indica el nombre del driver JDBC a usar.       */
/*       Esta "D" debe ir pegada al identificador "jdbc.drivers"!!            */
/* -------------------------------------------------------------------------- */

// Estas librerias son necesarias para usar el JDBC.
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;


public class PostgreJDBC 
{
	public static void main(String[] args)
	{
		Connection c   = null;        // Declaramos la instancia de conexion.
        Statement stmt = null;        // Declaramos la instancia de sentencia SQL.

		try {
			// Class.forName("org.postgresql.Driver"); // Esta sentencia hace lo mismo que la opcion "-D" arriba. No es necesaria.

            // Realiza la conexion a la base de datos "inventario" con el user y password indicados.
			c = DriverManager.getConnection("jdbc:postgresql://localhost:5432/inventario", "postgres", "apollo2134");

			c.setAutoCommit(false);

            System.out.println("Se conecto a la base de datos de forma exitosa!");

            // Ahora creamos un statement.
            stmt = c.createStatement();

            // Ejecutamos la sentencia SQL y colocamos el resultado en este cursor.
            ResultSet rs = stmt.executeQuery("SELECT * FROM empleados;");

            // Iteramos a traves del cursor.
            while(rs.next())
            {
                // Colocamos los valores de cada campo en variables manteniendo su tipo de dato.
            	int    id       = rs.getInt("id");
            	String name     = rs.getString("nombre");
            	String apellido = rs.getString("apellido");
            	int    dept     = rs.getInt("dept");

                // Imprimimos el resultado de la consulta.
            	System.out.println("ID: " + id); 
            	System.out.println("Nombre: " + name); 
            	System.out.println("Apellido: " + apellido);
            	System.out.println("Departamento: " + dept);
            	System.out.println();
            }

            // Cerramos todas las instancias de conexion, statement y cursor.
            rs.close();
            stmt.close();
            c.close();
		} catch (Exception e) {
			e.printStackTrace();
			System.err.println(e.getClass().getName() + ": " + e.getMessage());
			System.exit(0);
		}

		System.out.println("FIN de la consulta.");
	}
}


# El resultado de la ejecucion arroja:
C:\jdk-15\bin>java -Djdbc.drivers=org.postgresql.Driver prueba

Se conecto a la base de datos de forma exitosa!
ID: 1
Nombre: Jose
Apellido: Portillo
Departamento: 12

ID: 3
Nombre: Fernando
Apellido: Lozano
Departamento: 10

ID: 18
Nombre: Isabel
Apellido: Portillo
Departamento: 11

ID: 9
Nombre: Maria
Apellido: Gonzalez
Departamento: 14

ID: 7
Nombre: Alexis
Apellido: Aponte
Departamento: 70

ID: 20
Nombre: Donald
Apellido: Knuth
Departamento: 80

ID: 90
Nombre: Thales de
Apellido: Miletos
Departamento: 15

FIN de la consulta.






/* ----------------------------------- */
/* Uso de la palabra "STATIC" en JAVA. */
/* ----------------------------------- */
NOTAS: La palabra STATIC existe para declarar una parte del programa (variable, clase o  bloque anonimo) y que el mismo sea accesible 
       sin necesidad de pertenecer a una clase instanciada en un objeto. Este es el caso del metodo "main". La JVM carga y ejecuta 
       el metodo "main" sin necesidad de instanciar la clase a la cual este pertenece. PERO es el unico metodo que tiene este 
       privilegio. Es posible dar este privilegio a un bloque especifico declarandolo con "static" como veremos en el ejemplo.

       En JAVA, toda clase debe ser instanciada excepto aquellas que son declaradas STATIC. 

       Ademas, es posible (a traves del uso de la palabra STATIC) crear un bloque que ejecute justo al inicio del programa incluso 
       antes que la ejecucion del main.

       IMPORTANTE: La ejecucion y uso de variables y bloques declarados STATIC es en el orden de aparicion dentro del programa!

class herencia {
   int fib(int x) { if(x == 0 || x == 1) return(x); return(fib(x - 1) + fib(x - 2)); }

   int funcion(int x) { return(x*x); }


   static {
      System.out.println("EJECUTA PRIMERO!");
   }

   public static void main(String args[]) {
      herencia miHer = new herencia();

      System.out.println("cuadrado de x: " + miHer.funcion(2));
      System.out.println("Fibonacci de " + 7 + " es: " + miHer.fib(7));
   }
}

Resultado de la ejecucion:

C:\Users\user\Desktop> javac herencia.java
PS C:\Users\user\Desktop> java -cp C:\Users\user\Desktop herencia
EJECUTA PRIMERO!
cuadrado de x: 4
Fibonacci de 7 es: 13









#
#
#                                  SECCION DE EJEMPLOS HTML, CSS, JAVASCRIPT Y NODE.js                                             #
#
# IMPORTANTE: El programa node, al ser ejecutado sin argumentos funciona como un interprete (shell) de sentencias javaScript!!
#             Para finalizar una sesion con este shell puede ejecutar el comando ".exit" y la ayuda con el comando ".help".
#
# IMPORTANTE: Para Ejecutar un archivo JavaScript con NODE.js,
#
#             C:\node <archivo>.js
#
# IMPORTANTE: En JavaScript los objetos son "class-free"; esto quiere decir que la creacion de objetos puede hacerse sin que exista 
#             una declaracion de clase.
#
# IMPORTANTE: En JavaScript todos los objetos son propiedades derivadas de un objeto mayor llamado "Object". Ejemplo: podemos crear 
#             un objeto de la siguiente manera,
#
#             Object.prototype.miobjeto = {} que seria equivalente a crearlo de la siguiente manera tradicional miobjeto = {}
#
#             Un metodo importante (dentro del objeto "Object") es "keys()" que devuelve un arreglo con las propiedades del objeto en cuestion. 
#             De tal modo que podemos usar dicho metodo para iterar a traves de las propiedades de un objeto combinando este metodo con 
#             el metodo "forEach" del objeto "Array" como veremos en los ejemplos a continuacion.
#
# IMPORTANTE: Las propiedades y metodos de los objetos basicos (de fabrica) de JavaScript pueden ser listados usando la siguiente sentencia,
#
#             Object.prototype (para el caso del objeto "Object") o Array.prototype (para el caso del objeto "Array"). La salida seria algo asi
#
# >> Object.prototype
#    Object { … }
#​
#__defineGetter__: function __defineGetter__()
#​
#__defineSetter__: function __defineSetter__()
#constructor: function Object()
#​​
#assign: function assign()
#is: function is()
#​​
#keys: function keys()
#​​
#length: 1
#​​
#name: "Object"
#
#             Observar que, entre los metodos, aparece el metodo "keys()". Igual seria con el objeto "Array".
#
# IMPORTANTE: En JavaScript usted puede crear un objeto sin propiedades para, luego, adicionar propiedades al objeto. Ejemplo:
#
#             let miobjeto = {}
#
#             miobjeto.id = "0001"
#             miobjeto.desc = "Llave de tubo"
#             miobjeto.getId = function() {
#                                            return this.id
#                                         }
#
#             El resultado de estas dos ultimas sentencias sera un objeto con dos propiedades nuevas,
#
#             miobjeto = {
#                           id:   "0001",
#                           desc: "Llave de tubo",
#                           getId = function() { return this.id }
#                        }
#
<!-- ------------------------------------------------------------------- -->
<!-- Ejemplo de objeto en al cual una de sus propiedades es una funcion. -->
<!-- Ejemplo de array en el cual uno de sus elementos es una funcion.    -->
<!-- ------------------------------------------------------------------- -->
<script>
       // Ejemplo de objeto en el cual una de sus propiedades es una funcion. En este contexto a dicha funcion se le llama Metodo.
       // Este objeto representa dos puntos p y q en el plano cartesiano, equipados con una funcion Distancia "pitagoreana" 
       // entre los puntos
       //                              .----------------------------.
       //                              |          2              2  |
       //                   d(p, q) = \| (x2 - x1)   +  (y2 - y1)
       //                              v
       // En matematica, este plano cartesiano, equipado con la funcion Distancia es un conjunto al cual se le ha añadido 
       // una propiedad especial: una metrica o funcion distancia. Esto convierte este conjunto en un Espacio.

       let dosPts = {
                       p: {x: 0, y: 0},
                       q: {x: 1, y: 1},
                       dist: function() {
                                           let a = this.q.x - this.p.x;
                                           let b = this.q.y - this.p.y;

                                           return Math.sqrt(a*a + b*b);
                                        }
                    }

       console.log(dosPts.dist())

       // Ejemplo de arreglo en el cual uno de sus elementos es una funcion.
       let points = [
                       {x: 0, y: 0},
                       {x: 1, y: 1},

                       function() {
                                     let p = this[0];
                                     let q = this[1];
                                     let a  = q.x - p.x;
                                     let b  = q.y - p.y;

                                     return Math.sqrt(a*a + b*b);
                                }
                    ]

       console.log(points[2]())
</script>





/* ------------------------------------------ *
 * Ejemplo de uso del metodo map en arreglos. *
 * ------------------------------------------ */
>>let data = [8, 7, 6, 5, 4, 3, 2]

>>let dobles = data.map((x) => x*x)

>>var fib = (x) => (x == 0 || x == 1) ? x : (fib(x - 1) + fib(x - 2))

>>fib(7)
13

>>let miFib = data.map((x) => fib(x))

>>miFib
Array(7) [ 21, 13, 8, 5, 3, 2, 1 ]






/* ------------------------------------------------------------------------------------------------------ *
 * Ejemplo de Arrow functions (LAMBDA) en javaScript. Se muestra un ejemplo de una Arrow function ANONIMA *
 * (SIN SER ASIGNADA A NINGUNA VARIABLE COMO PUEDE HACERSE EN LISP).                                      *
 * ------------------------------------------------------------------------------------------------------ */
((x, y) => x + y)(3, 2)

Resultado:
5

// Un ejemplo de LAMBDA recursiva. No es anonima porque hay que nombrar la expresion obligatoriamente:

(f = (x) => !x || x == 1 ? x : f(x-1) + f(x-2))(7)

// Luego, al consultar al interprete de javascript que es f, este devuelve:

(x) => !x || x == 1 ? x : f(x-1) + f(x-2)

// En PYTHON se puede crear una LAMBDA anonima parecida de la siguiente manera:
(f := lambda x : x if x == 0 or x == 1 else f(x-1) + f(x-2))(7)







/* -------------------------------------------------------------------------------- */
/* Ejemplo de uso de first class functions: en Javascript las funciones son objetos */
/* que pueden ser asignados a variables, que pueden ser pasadas como parametros a   */
/* otras funciones (callback function), que pueden ser elementos de un arreglo.     */
/*                                                                                  */
/* Ejemplo de arrow functions.                                                      */
/*                                                                                  */
/* Ejemplo de como Javascript maneja los parametros a funciones de forma variable.  */
/* La funcion "muestra" pudiera recibir uno o dos parametros. Javascript se encarga */
/* de manejar la cantidad de parametros para cada caso (sqr solo necesita uno, pero */
/* suma y mult necesitan dos).                                                      */
/* -------------------------------------------------------------------------------- */
var suma = (x, y) => { return x + y; }
var mult = (x, y) => { return x * y; }
var sqr  = (x)    => { return x*x; }

var muestra = (calculo, parm1, parm2) => { console.log(calculo(parm1, parm2)); }

muestra(sqr, 2);

/* ------------------------------------------------------------------------------------------ */
/* Ejemplo de arreglo de funciones y como invocarlas. Cada elemento del array es una funcion. */
/* ------------------------------------------------------------------------------------------ */
array2 = [ 
           op1 = (x, y) => { return x + y },
           op2 = (x, y) => { return x * y },
           op3 = (x)    => { return 2 * x }
         ]

console.log(array2[0](4, 6))
console.log(array2[1](2, 5))
console.log(array2[2](3))



/* --------------------------------------------------------------------------------- */
/* Ejemplo de map, forEach, reduce y filter en arreglos.                             */
/*                                                                                   */
/* map sirve para ejecutar una funcion (callback function) por cada uno de los       */
/* elementos de un arreglo y devolver el arreglo modificado para asignarse a una     */
/* variable tipo arreglo. Esto ultimo no es necesario: usted pudiera usar map para   */
/* iterar a traves del arreglo y ejecutar alguna sentencia (ejemplo console.log)     */
/* sobre cada elemento del arreglo.                                                  */
/*                                                                                   */
/* map permite, ademas, que la salida de un map sea la entrada a otra map!           */
/*                                                                                   */
/* forEach sirve para iterar a traves de los elementos de un arreglo, ejecutando una */
/* funcion (callback function) por cada elemento del arreglo. No devuelve valor      */
/* alguno y, por tanto, no debe asignarse a una variable (de hacerlo este devolvera  */
/* "undefined").                                                                     */
/* --------------------------------------------------------------------------------- */
var serie = [2, 3, 4, 5, 6]

// Devuelve el arreglo "serie" modificado. Lo puede usted asignar a alguna variable de tipo arreglo.
var doble = serie.map((x) => { return 2*x; })

console.log(serie)
console.log(doble)

// Ejecuta unas sentencias o una funcion, pero no devuelve valor alguno.
serie.forEach((x) => { if(x > 4) console.log(2*x); })

// Tambien puede hacer la sentencia anterior con map (no asignando a una variable).
serie.map((x) => { if(x > 4) console.log(2*x); })

// Dos maps en secuencia: suma 10 a cada elemento y, luego, convierte a string cada elemento.
var concatenada = serie.map((x) => { return x + 10; }).map((x) => { return x.toString(); })

console.log(concatenada)

// Calcula la suma total de los numeros contenidos en el arreglo.
const inicial = 0
const total   = serie.reduce((previo, enCurso) => previo + enCurso, inicial)

console.log(total)

// Filtra los elementos del arreglo y toma solo los que son menores que 4.
const ltCuatro = serie.filter((x) => x < 4)

console.log(ltCuatro)




/* ------------------------------------------------------------------------------------------------------*/
/* Ejemplo de como iterar a traves de las propiedades de un objeto. Imaginemos un objeto que almacena el */
/* resultado de una consulta SQL (o el ejemplo abajo que es mas simple). La iteracion la podemos hacer   */
/* usando "forEach". Pero este solo opera en arrays. Para que funcione (en casos como este) debemos      */
/* convertir el objeto en un arreglo. Para ello usamos "Object.keys" que devuelve un array con las propiedades */
/* del objeto indicado.                                                                                  */
/*                                                                                                       */
/* Ademas, podemos usar "for" para iterar a traves del objeto. Segun algunas referencias este metodo "for"*/
/* es mas rapido que el "ForEach".                                                                       */
/* ------------------------------------------------------------------------------------------------------*/
const plano = {
                 p: {x: 0, y: 0},
                 q: {x: 1, y: 1}
              }

// Convertimos en array al objeto. Luego, por cada propiedad, ejecutamos alguna sentencia.
Object.keys(plano).forEach(key => {
  let punto = plano[key]   // Asignamos la propiedad en curso a una variable.

  // Imprimimos tanto la propiedad como las propiedades de esa propiedad (en este caso se trata de un objeto de objetos).
  console.log(key, punto.x, punto.y)
});

// Otro ejemplo de iteracion a traves de las propiedades de un objeto pero esta vez usando "for":
for(const key in plano) { 
   let elemento = plano[key]; console.log(elemento) 
}





/* ----------------------------------*/
/* Ejemplo de uso del metodo reverse */
/* ----------------------------------*/
// Este archivo JSON contiene un array de objetos con la siguiente estructura:
//
// [
//  ...
//  ..
//  {
//    "albumId": 100,
//    "id": 5000,
//    "title": "error quasi sunt cupiditate voluptate ea odit beatae",
//    "url": "https://via.placeholder.com/600/6dd9cb",
//    "thumbnailUrl": "https://via.placeholder.com/150/6dd9cb"
//  }
// ]
const array1 = JSON.parse(fs.readFileSync('\\Users\\user\\Desktop\\jsonEjercicio.json', 'utf8'));

console.log('array1:', array1[0].albumId);

// Reversa el orden del array. NOTA: reverse altera el arreglo original!
const reversed = array1.reverse();

console.log('reversed:', reversed[0].albumId);




/* ------------------------------------------------------------------------------- */
/* Ejemplo de arreglo de objetos. Ejemplo de adicionar un objeto a dicho arreglo.  */
/* Ejemplo de arrow function para devolver una propiedad de los objetos contenidos */
/* en ese arreglo.                                                                 */
/* ------------------------------------------------------------------------------- */
var objetos = [
                 {id: "0001", desc: "objeto_1"},
                 {id: "0002", desc: "objeto_2"},
                 {id: "0003", desc: "objeto_3"},
              ]

objetos.push({id: "0004", desc: "objeto_4"})

console.log(objetos.map((elemento) => { return elemento.id; }))




/* -------------------------------------------------------------------------------------------- */
/* Ejemplo del metodo sort aplicado a un arreglo tomando en cuenta una propiedad de los objetos */
/* que conforman dicho arreglo.                                                                 */
/*                                                                                              */
/* NOTA IMPORTANTE: Este metodo (por default) ordena convirtiendo cualquier elemento numerico   */
/*                  en formato String y comparando sus valores UNICODE.                         */
/*                  Por tal motivo, si deseamos ordenar un arreglo cuyos elementos son numeros  */
/*                  debemos alimentar el metodo sort con una funcion de ordenamiento. Para el   */
/*                  caso de elementos de tipo numerico bastaria con que dicha funcion devuelva  */
/*                  el resultado de la resta entre dos elementos (esta operacion convertira     */
/*                  los elementos en tipo numerico).                                            */
/* -------------------------------------------------------------------------------------------- */

// Ejemplo de array con elementos de tipo numerico. Se debe proveer a sort con una funcion de comparacion (en este caso devuelve una resta).
let lista = [13, 5, 27, 2]

lista.sort((x, y) => { return x - y })   // El resultado sera [ 2, 5, 13, 27 ]

// Si queremos ordenarlos en modo inverso (de mayor a menor).
lista.sort((x, y) => { return y - x })   // El resultado sera [ 27, 13, 5, 2 ]

// Otro ejemplo, ahora con un array de objetos.
var objs = [
              { first_nom: 'Lazslo', last_nom: 'Jamf' },
              { first_nom: 'Pig',    last_nom: 'Bodine'},
              { first_nom: 'Pirate', last_nom: 'Prentice' }
           ]

console.log(objs)

// IMPORTANTE: El metodo sort altera el arreglo al cual se aplica!
objs.sort((a, b) => (a.last_nom > b.last_nom) ? 1 : ((b.last_nom > a.last_nom) ? -1 : 0))

// objs.sort((a, b) => a.last_nom - b.last_nom); // b - a for reverse sort

console.log(objs)





/* -------------------------------------------------------------------------------- */
/* Ejemplo de un vector de objetos (cada objeto conteniendo atributos y funciones). */
/* -------------------------------------------------------------------------------- */
// Define un objeto plano cartesiano.
let plane = {
               p: {x: 0, y: 0},
               q: {x: 0, y: 0},
               distancia: function() {
                                        let a = this.q.x - this.p.x;
                                        let b = this.q.y - this.p.y; 
                                        return  Math.sqrt(a*a + b*b);
                                     }
            }

/* Se crea un vector basico. */
let vector = []

// Introduce un primer elemento (tipo objeto plane) en el vector.
vector.push(plane)

// Ejecuta el metodo-funcion en el elemento vector[0].
console.log("Ejecucion de vector[0].distancia():" + vector[0].distancia())
console.log("")

// OJO: EN LA CONSOLA DEL NAVEGADOR FIREFOX ESTE PUSH NO FUNCIONA!! INVESTIGAR!!
// Introduce un segundo elemento (tipo objeto plane) en el vector.
plane.p.x = 1
plane.p.y = 2
plane.q.x = 6
plane.q.y = 4
vector.push(plane)

// Ejecuta el metodo-funcion en el elemento vector[1].
console.log("Ejecucion de vector[1].distancia():" + vector[1].distancia())





/* ----------------------------------*/
/* Ejemplo de uso del metodo reverse */
/* ----------------------------------*/
// Este archivo JSON contiene un array de objetos con la siguiente estructura:
//
// [
//  ...
//  ..
//  {
//    "albumId": 100,
//    "id": 5000,
//    "title": "error quasi sunt cupiditate voluptate ea odit beatae",
//    "url": "https://via.placeholder.com/600/6dd9cb",
//    "thumbnailUrl": "https://via.placeholder.com/150/6dd9cb"
//  }
// ]
const array1 = JSON.parse(fs.readFileSync('\\Users\\user\\Desktop\\jsonEjercicio.json', 'utf8'));

console.log('array1:', array1[0].albumId);

// Reversa el orden del array. NOTA: reverse altera el arreglo original!
const reversed = array1.reverse();

console.log('reversed:', reversed[0].albumId);




/* ---------------------------------------------------------------- */
/* Implementar un stack es muy facil en Javacript: usar un arreglo. */
/* ---------------------------------------------------------------- */
let stack = []

stack.push({numCon: "00000001", mnt: 25.3})
stack.push({numCon: "00000002", mnt: 160.0})
stack.push({numCon: "00000003", mnt: 18.00})

console.log(stack)

console.log("Contratos:")

stack.forEach((x) => console.log(x.numCon))

let lastEle = stack.pop()

console.log(lastEle.numCon)

console.log("Nuevamente Contratos:")

stack.forEach((x) => console.log(x.numCon))





/* ------------------------------------------------------- */
/* Ejemplo de funciones recursivas: factorial y fibonacci. */
/* ------------------------------------------------------- */
function fact(x) { if(x === 0 || x === 1) return(1); return(x * fact(x - 1)); }

// o con arrow notation.
let fact = (x) => { if(!x || x === 1) return 1; return(x * fact(x - 1)); }

// o con ternary conditional ? : notation.
let fact = (x) => x <= 1 ? 1 : x * fact(x - 1)


function fib(x) { if(x === 0 || x === 1) return(x); return(fib(x - 1) + fib(x - 2)); }

// o con arrow notation.
let fib = (x) => { if(!x || x === 1) return x; return(fib(x -1) + fib(x - 2)); }


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(x => console.log(x + " ---> " + fact(x)));

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(x => console.log(x + " ---> " + fib(x)))









<!-- --------------------------------------------------------------------------------- -->
<!-- Ejemplo de la API XMLHttpRequest para hacer requerimientos HTTP desde javaScript. -->
<!-- Ejemplo de la API "fetch" (actualmente es nativo en los navegadores).             -->
<!-- Ejemplo de como leer un JSON desde una URL.                                       -->
<!-- --------------------------------------------------------------------------------- -->
   <script>
      //
      // Aqui se muestra como desde javscript podemos hacer un requerimiento HTTP (GET en este caso), tal y como se hace arriba:
      //
      var requerimiento = new XMLHttpRequest();
      requerimiento.open('GET', 'https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json', true);
      requerimiento.onload = () => { 
                                      // Valida el codigo de respuesta enviado por el servidor:
                                      if (request.status >= 200 && request.status < 400) {
                                         var data = JSON.parse(requerimiento.responseText);    // Convierte el JSON en objeto javaScript.
                                         console.log(data);
                                      }
                                   }
      requerimiento.send();   // Inicia el requerimiento HTTP!


      //
      // Ahora vamos a ver ejemplos del mismo requerimiento HTTP pero usando el API "fetch" (es nativo en el javscript engine en los navegadores):
      //
      async function leeJSON() {
        const response = await fetch("https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json");
        const paises = await response.json();
        for(i = 0; i < paises.length; i++) document.body.innerHTML += '<h1>' + paises[i].country + '</h1>';
        console.log(paises);
        // Para mostrar en la consola los nombres de los paises:
        Object.keys(paises).forEach(x => console.log(paises[x].country))
        // Tambien puede ser:
        for(i in paises) console.log(paises[i].country)
      }
      leeJSON();


      // Misma funcion pero ahora como arrow:
      getCountries = async () => {
        const resp = await fetch("https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json");
        const paises = await resp.json();
        console.log(paises)
      }

      // Misma operacion pero ahora sin async await. Solo usa fetch y sus .then...
      F = () => fetch("https://gist.githubusercontent.com/almost/7748738/raw/575f851d945e2a9e6859fb2308e95a3697bea115/countries.json")
                .then((resp) => resp.json())
                .then((paises) => { for(let i in paises) console.log(paises[i].name) });
    </script>




//
// Ahora mostramos como se lee un JSON desde una URL usando la libreria jQuery:
//
<!DOCTYPE html>
   <html lang="en">

   <head>
      <meta charset="utf-8">
      <title>Prueba de lectura JSON - Paises del mundo</title>

      <!-- Utilizamos JQUERY. -->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   </head>

   <body>
        <!-- Area en la pagina HTML para mostrar la lista de paises (de lo que trata el ejemplo) -->
        <textarea id="countries" style="width:1000px;height:1000px"></textarea>

    	<script>
    		// Lee el JSON en la siguiente URL. El parametro de la callback function sera de tipo object.
    		$.getJSON('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json', function(data) {

                var text = "";     // Variable que contendra la lista de paises.

                //
                // Itera a traves del objeto data.
                //
                for(var i = 0; i < data.length; i++) {
                	var pais = data[i];


                	for(property in pais) {
                		// text += property + ": " + pais[property] + "\n";
                		text += pais[property] + ",";      // Lo convierte en un stream CSV.
                	}
				}

				$("#countries").val(text);

				var arreglo_paises = [];

				arreglo_paises = text.split(",");    // El stream CSV creado lo convierte en un arreglo.

				console.log(arreglo_paises);
    		});
    	</script>
   </body>
</html>









//
// Ejemplos de tablas, forms, botones y estilos en una pagina HTML usando la libreria BOOTSTRAP y la seccion STYLES.
// Tambien se muestra las diferentes maneras de leer y escribir el contenido de un elemento (DIV) en una pagina HTML.
//
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>replit</title>
    <style>
      #valores {
        font-family: Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }
      #valores td, #valores th {
        border: 1px solid #ddd;
        padding: 8px;
      }
      #valores th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #04AA6D;
        color: white;
      }
      #valores tr:nth-child(even){background-color: #f2f2f2;}
      #valores tr:hover {background-color: #ddd;}

      /* body { background-image: url('https://img.freepik.com/free-vector/realistic-neon-lights-background_23-2148907367.jpg') } */
      /* body { background-color: rgb(28, 111, 199)} */
      #f8 { background-color: red }
      #f7 { background-color: blue }
      #ent { background-color: green }
      .test { display: table-cell; border: solid; border-width: thin; padding-left: 5px; padding-right: 5px; width: 30%; }
    </style>
  </head>
  <body>
    <script>
      f = x => !x || x === 1 ? x : f(x-2) + f(x-1)

      // Construye en tiempo de ejecucion los elementos HTML:
      document.body.innerHTML = '<div id="f8" class="test"></div><div id="f7" class="test"></div><div id="ent" class="test">987</div><div id="sal" class="test"></div>'

      // Existen dos maneras de cambiar el contenido de un elemento de la pagina HTML:
      document.querySelector('#f8').innerHTML = 'Fibonacci de 8: ' + f(8)   // En querySelector se usa el selctor CSS del elemento!
      document.getElementById('f7').innerHTML = 'Fibonacci de 7: ' + f(7)   // En getElementById se usa el ID del elemento!

      // Tambien pudieramos asignar el objeto a una variable y hacer el mismo acceso a traves de la variable:
      //const elemento = document.querySelector('#calculo');
      //elemento.textContent = f(7);
      //elemento.innerHTML = f(7);

      // Ejemplo de leer un elemento para alimentar a otro con el contenido leido:
      let a = document.querySelector("#ent").innerHTML
      document.querySelector("#sal").innerHTML = 'Valor leido es: ' + a
    </script>


    <div style="background-image: url('https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cd29c175759573.5c55ad2cec53f.jpg'); background-size: cover; height:480px; padding-top:80px;"></div>


    <table id="valores">
      <tr>
        <th>Descripcion</th>
        <th>Valor</th>
      </tr>
      <tr>
        <td>Fibonacci de 8</td>
        <td>21</td>
      </tr>
      <tr>
        <td>Fibonacci de 7</td>
        <td>13</td>
      </tr>
      <tr>
        <td>Valor existente</td>
        <td>987</td>
      </tr>
      <tr>
        <td>Valor leido es</td>
        <td>987</td>
      </tr>
    </table>

    <table class="table table-dark">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Handle</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </table>



<!-- ALGUNOS EJEMPLOS DE BOOTSTRAP -->
    <button type="button" class="btn btn-primary">Primary</button>
    <button type="button" class="btn btn-secondary">Secondary</button>
    <button type="button" class="btn btn-success">Success</button>
    <button type="button" class="btn btn-danger">Danger</button>
    <button type="button" class="btn btn-warning">Warning</button>
    <button type="button" class="btn btn-info">Info</button>
    <button type="button" class="btn btn-light">Light</button>
    <button type="button" class="btn btn-dark">Dark</button>    
    <button type="button" class="btn btn-link">Link</button>


    <button type="button" class="btn btn-primary btn-lg btn-block">Block level button</button>
    <button type="button" class="btn btn-secondary btn-lg btn-block">Block level button</button>


    <form>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <div class="form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>



    <div class="jumbotron">
      <h1 class="display-4">Hello, world!</h1>
      <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
      <hr class="my-4">
      <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
      <p class="lead">
        <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
      </p>
    </div>


    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand" href="#">Hidden brand</a>
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>


<!-- BARRA DE PROGRESO -->
    <div class="progress">
      <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
    </div>


    <div class="container">
      <div class="row">
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
      </div>
    </div>
  </body>
</html>
















/* ---------------------------------------------------------------------------------------- */
/* Ejemplo de NODE.js para ejecutar operaciones en el lado del servidor con Javascript.     */
/*                                                                                          */
/* NOTA: NODE.js puede funcionar como un servidor HTTP y permitir invocar una pagina HTML   */
/*       desde la URL del navegador como en el siguiente ejemplo.                           */
/*                                                                                          */
/* IMPORTANTE: El servidor HTML implementado con Node.js no tiene capacidad para enviar al  */
/*             navegador imagenes o href incluidas en la pagina html solicitada. Para que   */
/*             dichas referencias puedan ser usadas desde el navegador, estas deben publicarse*/
/*             en algun sitio web (no sirve colocarlas en la carpeta local donde recide la  */
/*             pagina html!                                                                 */
/*                                                                                          */
/*       Ademas, NODE incluye un conjunto de modulos que permiten hacer operaciones en el   */
/*       servidor tal como leer y escribir en archivos, etc.                                */
/* ---------------------------------------------------------------------------------------- */

// NOTA: El siguiente es un ejemplo de uso del modulo "fs" de NODE.js. En este ejemplo asumimos que NODE.js 
//       ya esta instalado en la maquina local.
//       El modulo "fs" permite leer, escribir, actualizar y eliminar archivos locales. En este ejemplo especifico se 
//       combina el uso de este modulo con otro modulo (tambien muy util) llamado "http" que convierte a NODE.js en un 
//       servidor HTTP local que estara escuchando a traves de un puerto HTTP indicado y que mostrara el contenido de 
//       un archivo (leido a traves del modulo "fs"), que en el caso de este ejemplo se trata de una pagina HTML y que 
//       al enviarla al browser ejecutara cualquier script Javascript contenida en dicha pagina. En esta modalidad 
//       NODE.js no es un servidor HTTP de la calidad de un Apache; sin embargo, sirve para ofrecer un servidor Web sencillo.

// 1.- Se crea un script para manejar el NODE.js. En este ejemplo el script se llamara myNode.js y tiene el siguiente contenido:

// Utiliza el modulo http para iniciar un servidor HTTP.
var http = require('http');

// Utiliza el modulo de manejo del file system que permite leer, escribir, actualizar y eliminar archivos 
// y desplegar paginas HTML (en caso que el archivo leido sea un ".html") en el browser.

/* NOTA: The Node.js file system module allows you to work with the file system on your computer. *
 *       To include the File System module, use the require() method.                             */
var fs   = require('fs');

// Ser crea un servidor HTTP. Observar que el comando "listen(8080)" al final inicia el servidor HTTP que estara escuchando
// requerimientos (desde un browser) a traves del puerto local 8080.
http.createServer(function(req, res) {

	// Se lee y ejecuta la pagina "jsontest.html" de ejemplo, la cual lee un JSON desde una URL (ver ejemplo arriba).
	fs.readFile('jsontest.html', function(err, data) {
      // Para servir un archivo JSON debe usar como content type 'application/json'.
      // Para servir un archivo CSV debe usar como content type 'text/csv'.
		res.writeHead(200, {'Content-Type': 'text/html'});
		res.write(data);

		return res.end();
	})
}).listen(8080);


// 2.- Para ejecutar este ejemplo de servidor HTTP vamos a la linea de comandos del sistema y ejecutamos el NODE indicando 
//     como argumento el nombre del script "js". Es importante que tanto la pagina HTML referida como este script se encuentren 
//     en el mismo directorio donde se ejecuta el NODE.

C:\Users\jportillo34\Desktop>node myNode.js


// 3.- Una vez ejecutado el comando anterior NODE quedara en escucha a traves de ese puerto ("8080"). Vamos al browser y 
//     en la URL invocamos la pagina principal de nuestro "HTTP server" local:

htt://localhost:8080

// Al teclear ENTER NODE ejecutara nuestro script, el cual mostrara la pagina HTML del ejemplo arriba. En caso de que el archivo 
// leido no sea una pagina HTML sino cualquier otro archivo (como un CSV, TXT o JSON), entonces se vera el contenido de dicho 
// archivo en la ventana del navegador.



/* -------------------------------------- */
/* Otro ejemplo de web server con Node.js */
/* -------------------------------------- */
let indexFile;

const http = require("http");

// Utiliza el modulo de manejo del file system que permite leer, escribir, actualizar y eliminar archivos 
// y desplegar paginas HTML (en caso que el archivo leido sea un ".html") en el browser.
const fs   = require('fs').promises;

const host = 'localhost';
const port = 8080;

// Ser crea un servidor HTTP. Observar que el comando "listen(8080)" al final inicia el servidor HTTP que estara escuchando
// requerimientos (desde un browser) a traves del puerto local 8080.

const requestListener = function(req, res) {
   res.setHeader("Content-Type", "text/html");
   res.writeHead(200);
   res.end(indexFile);
};

const server = http.createServer(requestListener);

fs.readFile("index.html")
   .then(contents => {
      indexFile = contents;
      server.listen(port, host, () => {
         console.log("Server is running on http://${host}:${port}");
      });
   })
   .catch(err => {
      console.error("No pudo leer index.html");
      process.exit(1);
   });






Otro ejemplo de Node JS:

/* ------------------------------------------------------------------------ */
/* Ejemplo de Node JS para leer y escribir el contenido de un archivo.      */
/*                                                                          */
/* Ejecutar desde la consola de comandos de node,                           */
/*                                                                          */
/* node nodef.js                                                            */
/* ------------------------------------------------------------------------ */
const fs = require('fs');


// Ejemplo de lectura de archivo TXT.
fs.readFile('\\Users\\user\\Desktop\\jsonTest.txt', 'utf8', (err, data) => {
   if (err) { console.error(err); return; }
   console.log(data);
});

// ejemplo de lectura de archivo JSON contenido en el servidor local.
// El archivo JSON contiene un arreglo con nombres de paises:
// [
//  {"country": "Afghanistan"},
//  {"country": "Albania"},
//  {"country": "Algeria"},
//  {"country": "American Samoa"},
//  {"country": "Andorra"},
//  {"country": "Angola"}
// ]
var obj = JSON.parse(fs.readFileSync('\\Users\\user\\Desktop\\jsonTest.json', 'utf8'));

var paises = "";

for(var i = 0; i < obj.length; i++) paises += obj[i].country + ',';

var paisPrint = []

Se separa la lista de paises y se elimina el ultimo elemento del arreglo, por estar en blanco.
paisPrint = paises.split(",").slice(0, -1);

for(var i = 0; i < paisPrint.length; i++) console.log(paisPrint[i]);


// Otro ejemplo de lectura de archivo JSON. Esta vez se trata de un registro con nombre de empresa, datos basicos y un erreglo con 
// el nombre de cada empleado:
// {
//    "empresa": "Tecnomed",
//    "datos": {
//                "direccion":"xxxxxx,xxxxxx,xxxxxxxx",
//                "telefono":"60854263",
//                "codPost":"1050"
//             },
//    "empleados": [
//                    "Fernando",
//                    "Isabel",
//                    "Pedro",
//                    "Maria"
//                 ]
// }
// El archivo JSON esta local en el servidor.
var obj = JSON.parse(fs.readFileSync('\\Users\\user\\Desktop\\jsonTest.json', 'utf8'));

console.log(obj.empresa);
console.log(obj.datos.direccion);
console.log(obj.datos.telefono);
console.log(obj.datos.codPost);

// Para imprimir los nombres de los empleados, al tratarse de un arreglo, debemos iterar a traves de este.
for(var i = 0; i < obj.empleados.length; i++) console.log(obj.empleados[i]);


// Ejemplo de escritura de archivo.
const content = '{"empresa":"Tecnomed","datos":{"direccion":"xxxxxx,xxxxxx,xxxxxxxx","telefono":"60854263","codPost":"1050"},"empleados":["Fernando","Isabel","Pedro","Maria"]}';

fs.writeFile('\\Users\\user\\Desktop\\jsonTest.json', content, err => {
if (err) {
   console.error(err);
}
  // file written successfully
});









/* -----------------------------------------------------------------------------------*
 * Ejemplo de manejo de eventos y refreso automatico de pagina HTML desde javascript. *
 * Ejemplo de reloj que se actualiza (refresca) en la pagina automaticamente.         *
 * Ejemplo de LAMBDA expression en manejo de eventos DOM.                             *
 * Ejemplo de multiples new lines en HTML.                                            *
 * -----------------------------------------------------------------------------------*/
<!DOCTYPE html>
<html>
	<head>
		<title>Digital Clock</title>
		<style>
			#clock {
				      font: bold 24px sans-serif;
				      background: rgb(212, 212, 236);
				      padding: 15px;
				      border: solid black 2px;
				      /*border-radius: 10px;*/
			       }

			#mensaje {
                  font: bold 24px sans-serif;
						background: rgb(212, 212, 236);
						padding: 15px;
						border: solid black 2px;
						border-radius: 10px;
			         }

            h1     {
                      background-color: red;
			       }

			body   {
				      background-color: rgb(153, 183, 193);
			       }
		</style>
	</head>

	<body>
		<h1>Digital Clock</h1>	
		<span id="clock"></span>
		<br style="line-height:3">
		<button id="boton">Click Me!</button>
		<br style="line-height:8">
		<span id="mensaje"></span>
		<script>
			//let reloj = () => {
			//	                 let clock = document.querySelector("#clock");
			//	                 let now   = new Date();

			//	                 clock.textContent = now.toLocaleTimeString();
			//                  }

			//reloj()
			//setInterval(reloj, 1000);

            document.getElementById("boton").addEventListener("click", () => {
				                                                                //document.getElementById("mensaje").innerHTML = "PRUEBA!"; 
				                                                                let mns = document.querySelector("#mensaje");
			                                                                    mns.textContent = "PRUEBA!";
                                                                              })

            // Usando una funcion anonima (LAMBDA).
			setInterval(() => { 
                                 let clock = document.querySelector("#clock"); 
                                 let now = new Date(); 
                                 clock.textContent = now.toLocaleTimeString(); 
                              }, 1000)
		</script>
	</body>
</html>








/* ------------------------------------------------------------- *
 * Ejemplo de uso de la libreria de numeros complejos en Node.js *
 * ------------------------------------------------------------- */
import { create, all } from 'mathjs'

const math = create(all)

const A = math.complex(3.0, 2.0)
const B = math.complex(4.0, 5.0)
let C = math.add(A, B)
console.log('A = ' + A)
console.log('B = ' + B)
console.log('A + B = ' + C)












#
#
#                                        SECCION DE EJEMPLOS LENGUAJE C                                      #
#
# IMPORTANTE: Hay una carpeta de proyecto llamada gestFlota. Hay ejemplos de uso de typedef, const, enum y el uso de 
#             vectores de registros (struct) simulando en C estandar los objetos clases. Tambien, hay ejemplo de Tipos de datos
#             abstractos (TAD o ADT) usando modulos (archivo .cpp con su cabecera archivo .h).
#
# IMPORTANTE: Ejemplo de compilacion de un programa multimodulo (varios .cpp y varios .h). Para este ejemplo tomaremos el programa GestFlota. 
#             Este programa consta de los fuentes puerto.cpp, puerto.h, calendario.cpp, calendario.h, buque.cpp, buque.h, GestFlota.cpp (este ultimo 
#             contiene el main()):
#
#             1.- Compilar cada modulo por separado (puede usar tambien g++),
#
#             c++ -c -std=c++11 puerto.cpp
#             c++ -c -std=c++11 calendario.cpp
#             c++ -c -std=c++11 buque.cpp
#             c++ -c -std=c++11 GestFlota.cpp
#
#             Por ultimo, generar el ejecutable (indicando el nombre que tendra el ejecutable),
#
#             c++ -o GestFlota puerto.o calendario.o buque.o GestFlota.o
#
# IMPORTANTE: El compilador g++ puede generar el fuente en assembler correspondiente al fuente en C. Para ello debe indicar (ejemplo),
#
#             g++ -S <nombreFuente.c> -o <nombreArchivo.s>
#
#             Ademas, puede generar el listado conteniendo el codigo de maquina y el assembler. Para ello debe,
#
#             1.- Generar solo el objeto correspondiente al fuente en C con el comando,
#
#             g++ -c <nombreFuente.c>
#
#             Esto producira un archivo con extension .o
#
#             2.- Generar el dump conteniendo el codigo de maquina y el assembler,
#
#             objdump -D <nombreObjeto.o> > <archivo.dump>
#

/* ----------------------------------------------------------------------------------------------------------------------------------------- *
 * Ejemplo de generacion de listado en codigo de maquina y assembler correspondiente a un fuente en C (suando los comandos antes indicados). *
 * ----------------------------------------------------------------------------------------------------------------------------------------- */
Fuente ejemplo llamado fib.c,


#include<stdio.h>

int fib(int x) { if(x == 0 || x == 1) return(x); else return(fib(x-1) + fib(x-2)); }

int main() {
  int n = fib(7);
  printf("El Fibonacci de 7 es: %d", n);
  return(0);
}

Ejecutamos el comando de compiplacion pero solo para generar el fuente objeto (no el ejecutable .exe),

g++ -c fib.c

Si queremos ver un dump del contenido (en hexadecimal y en ascii) de este archivo objeto,

objdump -s fib.o

El comando producira el siguiente dump:

fib.o:     file format pe-i386

Contents of section .text:
 0000 5589e553 83ec148b 450885c0 74088b45  U..S....E...t..E
 0010 0883f801 75058b45 08eb208b 450883e8  ....u..E.. .E...
 0020 01890424 e8d7ffff ff89c38b 450883e8  ...$........E...
 0030 02890424 e8c7ffff ff01d883 c4145b5d  ...$..........[]
 0040 c35589e5 83e4f083 ec20e800 000000c7  .U....... ......
 0050 04240700 0000e8a5 ffffff89 44241c8b  .$..........D$..
 0060 44241c89 442404c7 04240000 0000e800  D$..D$...$......
 0070 000000b8 00000000 c9c39090           ............
Contents of section .rdata:
 0000 456c2046 69626f6e 61636369 20646520  El Fibonacci de
 0010 37206573 3a202564 00000000           7 es: %d....
Contents of section .rdata$zzz:
 0000 4743433a 20284d69 6e47572e 6f726720  GCC: (MinGW.org
 0010 4743432d 362e332e 302d3129 20362e33  GCC-6.3.0-1) 6.3
 0020 2e300000                             .0..
Contents of section .eh_frame:
 0000 14000000 00000000 017a5200 017c0801  .........zR..|..
 0010 1b0c0404 88010000 20000000 1c000000  ........ .......
 0020 04000000 41000000 00410e08 8502420d  ....A....A....B.
 0030 05448303 78c341c5 0c040400 1c000000  .D..x.A.........
 0040 40000000 45000000 39000000 00410e08  @...E...9....A..
 0050 8502420d 0575c50c 04040000           ..B..u......


Ahora generaremos el listado en codigo de maquina y en assembler con el comando,

objdump -D fib.o > fib.asm

Esto ultimo generara lo siguiente:

fib.o:     file format pe-i386


Disassembly of section .text:

00000000 <__Z3fibi>:
   0:	55                   	push   %ebp
   1:	89 e5                	mov    %esp,%ebp
   3:	53                   	push   %ebx
   4:	83 ec 14             	sub    $0x14,%esp
   7:	8b 45 08             	mov    0x8(%ebp),%eax
   a:	85 c0                	test   %eax,%eax
   c:	74 08                	je     16 <__Z3fibi+0x16>
   e:	8b 45 08             	mov    0x8(%ebp),%eax
  11:	83 f8 01             	cmp    $0x1,%eax
  14:	75 05                	jne    1b <__Z3fibi+0x1b>
  16:	8b 45 08             	mov    0x8(%ebp),%eax
  19:	eb 20                	jmp    3b <__Z3fibi+0x3b>
  1b:	8b 45 08             	mov    0x8(%ebp),%eax
  1e:	83 e8 01             	sub    $0x1,%eax
  21:	89 04 24             	mov    %eax,(%esp)
  24:	e8 d7 ff ff ff       	call   0 <__Z3fibi>
  29:	89 c3                	mov    %eax,%ebx
  2b:	8b 45 08             	mov    0x8(%ebp),%eax
  2e:	83 e8 02             	sub    $0x2,%eax
  31:	89 04 24             	mov    %eax,(%esp)
  34:	e8 c7 ff ff ff       	call   0 <__Z3fibi>
  39:	01 d8                	add    %ebx,%eax
  3b:	83 c4 14             	add    $0x14,%esp
  3e:	5b                   	pop    %ebx
  3f:	5d                   	pop    %ebp
  40:	c3                   	ret    

00000041 <_main>:
  41:	55                   	push   %ebp
  42:	89 e5                	mov    %esp,%ebp
  44:	83 e4 f0             	and    $0xfffffff0,%esp
  47:	83 ec 20             	sub    $0x20,%esp
  4a:	e8 00 00 00 00       	call   4f <_main+0xe>
  4f:	c7 04 24 07 00 00 00 	movl   $0x7,(%esp)
  56:	e8 a5 ff ff ff       	call   0 <__Z3fibi>
  5b:	89 44 24 1c          	mov    %eax,0x1c(%esp)
  5f:	8b 44 24 1c          	mov    0x1c(%esp),%eax
  63:	89 44 24 04          	mov    %eax,0x4(%esp)
  67:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
  6e:	e8 00 00 00 00       	call   73 <_main+0x32>
  73:	b8 00 00 00 00       	mov    $0x0,%eax
  78:	c9                   	leave  
  79:	c3                   	ret    
  7a:	90                   	nop
  7b:	90                   	nop

Disassembly of section .rdata:


NOTA IMPORTANTE: La siguente seccion contiene la data, es decir el mensaje que imprimira la instruccion printf: 
Contents of section .rdata:
 0000 456c2046 69626f6e 61636369 20646520  El Fibonacci de
 0010 37206573 3a202564 00000000           7 es: %d....


00000000 <.rdata>:
   0:	45                   	inc    %ebp
   1:	6c                   	insb   (%dx),%es:(%edi)
   2:	20 46 69             	and    %al,0x69(%esi)
   5:	62 6f 6e             	bound  %ebp,0x6e(%edi)
   8:	61                   	popa   
   9:	63 63 69             	arpl   %sp,0x69(%ebx)
   c:	20 64 65 20          	and    %ah,0x20(%ebp,%eiz,2)
  10:	37                   	aaa    
  11:	20 65 73             	and    %ah,0x73(%ebp)
  14:	3a 20                	cmp    (%eax),%ah
  16:	25 64 00 00 00       	and    $0x64,%eax
	...

Disassembly of section .rdata$zzz:

00000000 <.rdata$zzz>:
   0:	47                   	inc    %edi
   1:	43                   	inc    %ebx
   2:	43                   	inc    %ebx
   3:	3a 20                	cmp    (%eax),%ah
   5:	28 4d 69             	sub    %cl,0x69(%ebp)
   8:	6e                   	outsb  %ds:(%esi),(%dx)
   9:	47                   	inc    %edi
   a:	57                   	push   %edi
   b:	2e 6f                	outsl  %cs:(%esi),(%dx)
   d:	72 67                	jb     76 <_main+0x35>
   f:	20 47 43             	and    %al,0x43(%edi)
  12:	43                   	inc    %ebx
  13:	2d 36 2e 33 2e       	sub    $0x2e332e36,%eax
  18:	30 2d 31 29 20 36    	xor    %ch,0x36202931
  1e:	2e 33 2e             	xor    %cs:(%esi),%ebp
  21:	30 00                	xor    %al,(%eax)
	...

Disassembly of section .eh_frame:

00000000 <.eh_frame>:
   0:	14 00                	adc    $0x0,%al
   2:	00 00                	add    %al,(%eax)
   4:	00 00                	add    %al,(%eax)
   6:	00 00                	add    %al,(%eax)
   8:	01 7a 52             	add    %edi,0x52(%edx)
   b:	00 01                	add    %al,(%ecx)
   d:	7c 08                	jl     17 <.eh_frame+0x17>
   f:	01 1b                	add    %ebx,(%ebx)
  11:	0c 04                	or     $0x4,%al
  13:	04 88                	add    $0x88,%al
  15:	01 00                	add    %eax,(%eax)
  17:	00 20                	add    %ah,(%eax)
  19:	00 00                	add    %al,(%eax)
  1b:	00 1c 00             	add    %bl,(%eax,%eax,1)
  1e:	00 00                	add    %al,(%eax)
  20:	04 00                	add    $0x0,%al
  22:	00 00                	add    %al,(%eax)
  24:	41                   	inc    %ecx
  25:	00 00                	add    %al,(%eax)
  27:	00 00                	add    %al,(%eax)
  29:	41                   	inc    %ecx
  2a:	0e                   	push   %cs
  2b:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
  31:	44                   	inc    %esp
  32:	83 03 78             	addl   $0x78,(%ebx)
  35:	c3                   	ret    
  36:	41                   	inc    %ecx
  37:	c5 0c 04             	lds    (%esp,%eax,1),%ecx
  3a:	04 00                	add    $0x0,%al
  3c:	1c 00                	sbb    $0x0,%al
  3e:	00 00                	add    %al,(%eax)
  40:	40                   	inc    %eax
  41:	00 00                	add    %al,(%eax)
  43:	00 45 00             	add    %al,0x0(%ebp)
  46:	00 00                	add    %al,(%eax)
  48:	39 00                	cmp    %eax,(%eax)
  4a:	00 00                	add    %al,(%eax)
  4c:	00 41 0e             	add    %al,0xe(%ecx)
  4f:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
  55:	75 c5                	jne    1c <.eh_frame+0x1c>
  57:	0c 04                	or     $0x4,%al
  59:	04 00                	add    $0x0,%al
	...

       





/* --------------------------------------------------------------------------- *
 * Ejemplos de uso de directivas al preporcesador y definicion de macros en C. *
 * --------------------------------------------------------------------------- */
#define __MICONSTANTE__

/*
#ifndef __MICONSTANTE__
#define resta(x, y) x - y
#else
#define suma(x, y) x + y
#endif
*/

#if (defined __MICONSTANTE__)
#define suma(x, y) x + y
#endif

#if !(defined __MICONSTANTE__)
#define resta(x, y) x - y
#endif








/* ----------------------------------------------------------------------------------------------------------------------- *
 * Un programa C o C++ puede leer las variables del ambiente (Shell) en el cual se ejecuta. Para ello debe usar la funcion *
 * getenv contenida en la libreria stdlib.h.                                                                               *
 * ----------------------------------------------------------------------------------------------------------------------- */
#include <iostream>
#include <stdlib.h>

int main(int argc, char *argv[]) {
        char *libvar = getenv("PWD");
        std::cout << "\n\nLa variable PWD = " << libvar << "\n\n";
        return 0;
}








/* -------------------------------------------------------------------- *
 * Ejemplo de manejo de memoria dinamica usando MALLOC, REALLOC y FREE. *
 *                                                                      *
 * IMPORTANTE: Ver ejemplo (mas abajo) sobre casting (void *) de las    *
 *             funciones malloc, realloc, etc.                          *
 * -------------------------------------------------------------------- */
#include<stdio.h>
#include<stdlib.h>

struct punto {
      void setX(int parX) { x = parX; }
      void setY(int parY) { y = parY; }
      int getX() { return(x); }
      int getY() { return(y); }
   private:
      int x;
      int y;
};

int main() {
   puntos misPuntos;

   punto * miDyna = (punto *) malloc(20 * sizeof(punto));


   for(int i = 0; i < 20; i++) { miDyna[i].setX(i); miDyna[i].setY(i+2); }
   for(int j = 0; j < 20; j++) printf("x:%d, y:%d\n", miDyna[j].getX(), miDyna[j].getY());

   printf("\n\nrealocamos...");

   // Solicitamos mas espacio de memoria!
   miDyna = (punto *) realloc(miDyna, 40 * sizeof(punto));

   printf("\n\n...luego de la realocacion...\n");

   for(int i = 20; i < 40; i++) { miDyna[i].setX(i); miDyna[i].setY(i+2); }
   for(int j = 0; j < 40; j++) printf("x:%d, y:%d\n", miDyna[j].getX(), miDyna[j].getY());

   printf("\n\n...liberamos espacio reservado");

   free(miDyna);

   return(0);
}







/* --------------------------------------------------------------------------------------------- *
 * Ejemplo de apuntador a funcion en C estandar.                                                 *
 *                                                                                               *
 * NOTA: C++ tiene otra forma de hacer esta declaracion, a parte de aceptar esta del C estandar. *
 * --------------------------------------------------------------------------------------------- */
int fun(int parX, int parY) { return(parX + parY); }

int main() {
   int (*fun_ptr)(int, int) = &fun;

   printf("El resultado de sumar parX + parY es: %d", (*fun_ptr)(6, 12));

   return(0);
}







/* ----------------------------------------------------------------- *
 * Ejemplo de codigo de maquina incluido en un fuente en lenguaje C. *
 * ----------------------------------------------------------------- */
typedef int (*fnptr)(void);   // Definimos un tipo de apuntador a funcion para hacer mas claro todo.

// Algunos ejemplos de instrucciones de maquina (i386) en hexadecimal dentro de un array.
const unsigned char bytes[]={0x31, 0xd2, 0xc3};

// Otro ejemplo.
const unsigned char subrt[] = {0xb8, 0x03, 0x00, 0x00, 0x00, 
                               0x83, 0xc0, 0x02,
                               0x89, 0x44, 0x24, 0x1c,
                               0xc3};

int main() {
   // Se declara un apuntador a funcion alimentadolo con la direccion del array "byte" que contiene las instrucciones de maquina.
   fnptr f = (fnptr)bytes;

   // La sentencia siguiente ejecuta las instrucciones de maquina incluidas en el array "bytes"!
   f();

/* Este es un ejemplo de inline assembler.
   int first = 0;
   int second = 0;
   int tercer = 0;

   __asm__ __volatile__ ( "MOVL   $3,    %EAX;"
                          "ADDL   $2,    %EAX;"
                          "MOVL   %EAX,  0x28(%ESP);"
                          "MOVL   $10,   %EBX;"
                          "MOVL   %EBX,  0x24(%ESP);"
                          "MOVL   $7,    %EAX;"
                          "MOVL   %EAX,  0x20(%ESP);"      
                          //: "=a" (first), "=b" (second), "=c" (tercer) : "a" (first), "b" (second), "c" (tercer)
   );

   printf("\n\n\nfirst=%d y second=%d y tercer=%d\n\n\n", first, second, tercer);
*/

  return 0;
}











/* ------------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: Sobre comparar valores reales (punto flotante) en C, C++ y otros lenguajes como javaScript. *
 *             Por el tema de la precision comparaciones como la siguiente                                 *
 *                                                                                                         *
 *             0.2 + 0.1 == 0.3                                                                            *
 *                                                                                                         *
 *             pudieran dar un valor False                                                                 *
 *                                                                                                         *
 *             Para comparar dos valores reales podemos restar ambos valores (resta aritmetica) y comparar *
 *             el resultado contra 0.0.                                                                    *
 *                                                                                                         *
 *             Por tal motivo hay que establecer un valor de tolerancia para comparar contra este.         *
 *             Pudieramos decir 1e-8 (es necesario determinar ese valor de tolerancia de acuerdo al caso). *
 *                                                                                                         *
 * IMPORTANTE: Se puede observar la precision a traves de las macros de la libraria float.h (abajo se      *
 *             muestra un ejemplo usando dichas macros o sin ellas. En todos los casos se utiliza la       *
 *             funcion printf y el calificador %xxe.                                                       *
 *             Para mas informacion sobre la precision en C y la libreria float.h consultar:               *
 *                                                                                                         *
 * https://pubs.opengroup.org/onlinepubs/009604599/basedefs/float.h.html                                   *
 * https://stackoverflow.com/questions/16839658/printf-width-specifier-to-maintain-precision-of-floating-point-value *
 * ------------------------------------------------------------------------------------------------------- */
#include <stdbool.h>    // <---- NECESARIA para usar Booleans.

float a = 0.2;
float b = 0.1;
float t = 0.3;
bool r;                // <---- DECLARAMOS BOOL.

//r = 0.2 + 0.1 == 0.3;
r = ((0.2 + 0.1) - 0.3) == 0.0;

printf("\n\nr=%d\n\n", r);


Salida:

r=0

Le colocamos un valor de tolerancia:

 r = ((0.2 + 0.1) - 0.3) < 1e-8;

printf("\n\nr=%d\n\n", r);


Salida:

r=0


/* Ahora usamos la funcion printf para mostrar la precision usada y como afecta el valor de tolerancia de antes.
   Vemos como usando una precision de 16 digitos el valor de la resta no es igual a cero!                        

   De hecho, si evaluamos la resta como ((0.2 + 0.1) - 0.3) > 0 SI DA VERDADERO!
*/

#include <float.h>

int Digs = DBL_DECIMAL_DIG;   //DECIMAL_DIG;

printf("LA PRECISION DE 02. + 0.1 es........:   %.*e\n", Digs, (0.2 + 0.1));
printf("LA PRECISION DE 0.3 es..............:   %.*e\n\n", Digs, 0.3);
printf("LA PRECISION DE (0.2 + 0.1) - 0.3 es:   %.*e\n\n", Digs, ((0.2 + 0.1) - 0.3));

printf("LA PRECISION DE 02. + 0.1 es........:   %.16e\n", (0.2 + 0.1));
printf("LA PRECISION DE 0.3 es..............:   %.16e\n\n", 0.3);
printf("LA PRECISION DE (0.2 + 0.1) - 0.3 es:   %.16e\n\n", ((0.2 + 0.1) - 0.3));

// Salida:
LA PRECISION DE 02. + 0.1 es........:   3.00000000000000044e-01
LA PRECISION DE 0.3 es..............:   2.99999999999999989e-01

LA PRECISION DE (0.2 + 0.1) - 0.3 es:   5.55111512312578270e-17

LA PRECISION DE 02. + 0.1 es........:   3.0000000000000004e-01
LA PRECISION DE 0.3 es..............:   2.9999999999999999e-01

LA PRECISION DE (0.2 + 0.1) - 0.3 es:   5.5511151231257827e-17





En javascript seria algo asi:

let f1 = 1000000.1 + 0.2;
let f2 = 1000000.3;
let miTolerancia = 1e-8;


let calcDifference =  Math.abs(f1 - f2);
let compareResult = calcDifference < miTolerancia;

console.log(" ")

console.log(compareResult)






/* -------------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: Las FUNCIONES en lenguaje C son GLOBALES por defecto. Cuando son declaradas STATIC se limita * 
 *             su ambito al mismo source file que las contiene!!                                            *
 *                                                                                                          *
 * IMPORTANTE: Cuando se define una variable STATIC su ambito es el de la funcion que la contiene PERO su   *
 *             tiempo de vida NO termina cuando termina la ejecucion de la funcion. Esta variable conserva  *
 *             su valor hasta que termina el programa! Es util, por ejemplo, como variable para contar el   *
 *             numero de veces que se invoca una funcion en el programa!                                    *
 * -------------------------------------------------------------------------------------------------------- */
#include <stdio.h>

void miFun() {
      static int x = 0;

      x++;
      printf("valor de x: %d", x);
}

int main() {
      mifun();
      miFun();
      return(0);
}

resultado:
valor de x: 1
valor de x: 2








/* --------------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: Sobre la precedencia del operador ++ (en su forma postfix) sobre el operador * de referencia. *
 * --------------------------------------------------------------------------------------------------------- */
int s[] = {1, 2, 3, 4, 5, 6, 7, 8};

int* ptr = s;            // Se declara un apuntador al arreglo s de enteros.

*ptr++;       // Aqui el operador ++ esta en modo postfix, el cual tiene una precedencia mayor que *. Entonces, se incrementa
              // el valor del apuntador (su direccion) y el * no tiene ningun uso aqui.
              // Si en lugar de esta sentencia hubiesemos asignado esta expresion a una variable (ejemplo int temp = *ptr++), entonces 
              // PRIMERO se asigna el contenido de memoria apuntada por ptr y luego se incrementa dicho apuntador!!!


printf("\n\ntemp:%d , *ptr:%d\n\n", temp, *ptr);


Salida:

temp:1 , *ptr:2










/* --------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: Sobre los apuntadores a void (void *ptr). DEBE hacer casting para poder asignar valores *
 *             a este tipo de apuntadores!                                                             *
 *                                                                                                     *
 *             Un ejemplo importante de esto es la funcion malloc que devuelve un apuntador a void.    *
 *             Por tal motivo se debe hacer casting cuando se emplea esta funcion!                     *
 * --------------------------------------------------------------------------------------------------- */
int var1 = 28;

void *ptr2;


ptr2 = &var1;

printf("\n\n*ptr2:%d\n\n", *(int *) ptr2);    // <---- Hay que hacer casting para poder utilizar este apuntador a void!



/* A continuacion un ejemplo de la funcion malloc donde puede observar el uso del casting que requiere dicha funcion. */
char nombre[]  = "Jose Maria";
char destino[] = "Jose";

nombre = (char *) malloc(15);   // Prueba de malloc.

strcpy(nombre, "Jose Maria");   // Prueba de string copy usando la libreria standard de C.










/* -------------------------------------------------------------------------------------------------- *
 * Ejemplo de la funcion STRCPY. Esta funcion copia el contenido de un string sobre otro sustituyendo *
 * el contenido del string destino! Es decir: modifica el string destino. Tambien devuelve el mismo   * 
 * string copiado que puede asignarse a una variable de tipo char*.                                   *
 * -------------------------------------------------------------------------------------------------- */
#include<string.h>

char src[] = "Cadena Origen";     // Cadena origen.
char dst[] = "ESPACIOVACIOAQUI";  // Cadena destino.
char *resp;                       // Valor devuelto por la funcion strcpy.

resp = strcpy(dst, src);

printf("\nsrc:%s , dst:%s , resp:%s\n", src, dst, resp);


Resultado:
src:Cadena Origen , dst:Cadena Origen , resp:Cadena Origen








/* ----------------------------------------- *
 * Ejemplo de hilos (threads) en C estandar. *
 * ----------------------------------------- */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //Header file for sleep(). man 3 sleep for details.
#include <pthread.h>

// A normal C function that is executed as a thread
// when its name is specified in pthread_create()
void *myThreadFun(void *vargp)
{
	sleep(1);
	printf("Printing GeeksQuiz from Thread \n");
	return NULL;
}

int main()
{
	pthread_t thread_id;
	printf("Before Thread\n");
	pthread_create(&thread_id, NULL, myThreadFun, NULL);
	pthread_join(thread_id, NULL);
	printf("After Thread\n");
	exit(0);
}









# ----------------------------------------------------------------------------------------------------- #
# Aritmetica de apuntadores y arrays: la suma es conmutativa!                                           #
#                                                                                                       #
# NOTA: En este ejemplo vemos que es lo mismo a[n] que n[a] dado que *(a + n) es lo mismo que *(n + a). #
#------------------------------------------------------------------------------------------------------ #
int a[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 24};

printf("\n\na[3] = %d y 3[a] = %d\n\n", a[3], 3[a]);









#
# - Ejemplo de formato de impresion con printf.
# - Ejemplo de array anidado dentro de otro array.
#
# IMPORTANTE: En C++ el formato tipo "%-10s" no funciona. Entonces, en C++ hayq que usar el formateador "setw" incluido 
#             en la libreria "iomanip". PERO tambien puede aplicarse FORMATO con la libreria Boost (Boost.format). Ver 
#             ejemplos en la seccion de C++ mas abajo.

   char *arraySt[3] = {"Titulo1", "Titulo2", "Titulo3"};
   int arrayNm[3][3] = {{45, 12, 1}, {98, 57, 3}, {4, 26, 70}};


   printf("\n\n\n");
   for(int i = 0; i < 3; i++) printf("%-10s", arraySt[i]);
   printf("\n");
   for(int i = 0; i < 3; i++) printf("%-10s", "=======");
   printf("\n");
   for(int i = 0; i < 3; i++) {
     for(int j = 0; j < 3; j++) printf("%-10d", arrayNm[i][j]);
     printf("\n");
   }
   printf("\n\n");


Salida:

Titulo1   Titulo2   Titulo3   Titulo4   
=======   =======   =======   =======   
45        12        1         
98        57        3         
4         26        70











# --------------------------------------------------------------------------------------------- #
# Ejemplo de creacion de un ADT (Abstract Data Type), usando el tipo "struct" (no POO classes). #
# La diferencia entre esta forma de implementar ADTs y las POO classes es que aqui no existe la #
# herencia. En este ejemplo, el tipo "plano" no hereda el tipo "punto" (se simula mediante la   #
# declaracion de dos elementos tipo "punto" dentro de la estructura "plano").                   #
# --------------------------------------------------------------------------------------------- #

#include<stdio.h>
#include<math.h>

/* =================== TAD punto ==================== */
typedef struct punto {
   void   setX(float xI);
   void   setY(float yI);
   float  getX();
   float  getY();
private:
   float  x;
   float  y;
};

void  punto::setX(float xI) { x = xI; }
void  punto::setY(float yI) { y = yI; }
float punto::getX() { return x; }
float punto::getY() { return y; }
/* =================== TAD punto ==================== */

/* ================================================= Espacio R^2 ================================================= */
/* El siguiente tipo abstracto (con su funcion Distancia), representa el conjunto producto RxR (plano cartesiano), *
 * equipado con una funcion Distancia "pitagoreana" entre los puntos p y q                                         *
 *                              .----------------------------.                                                     *
 *                              |          2              2  |                                                     *
 *                   d(p, q) = \| (x2 - x1)   +  (y2 - y1)                                                         *
 *                              v                                                                                  *
 * En matematica, este plano cartesiano, equipado con la funcion Distancia es un conjunto al cual se le ha añadido *
 * una propiedad especial: una metrica o funcion distancia. Esto convierte a este conjunto en un Espacio (finito). */
/* ================================================= TAD plano =================================================== */
typedef struct plano {
   punto p;
   punto q;

   float Distancia(punto p1, punto p2);
};

float plano::Distancia(punto p1, punto p2) {
   return sqrt(powf((p2.getX()-p1.getX()), 2) + powf((p2.getY()-p1.getY()), 2));
}
/* ================================================= TAD plano =================================================== */
/* ================================================= Espacio R^2 ================================================= */

int main() {
   plano miPlano;

   miPlano.p.setX(1.0);
   miPlano.p.setY(1.0);

   miPlano.q.setX(5.0);
   miPlano.q.setY(5.0);

   printf("\nDistancia = %f\n\n", miPlano.Distancia(miPlano.p, miPlano.q));
}



 /* ------------------------------------------------------------------------------------------------------------ *
 * Ejemplo de programa de consola MS-DOS en Windows (compilado con el MinGW gcc). Es un programa para el manejo 
 * de un sistema de puertos y buques. 
 *
 * Ejemplo de declaracion de tipos con typedef. 
 * Ejemplo de uso de scanf, fgets y sus detalles. 
 * Ejemplo de uso de system("cls") para limpiar la pantalla en el MS-DOS. 
 * Ejemplo de uso de tipo de dato enum.
 * Ejemplo de ADT (Abstract Data Type) usando struct. Cada ADT puede ser colocado en un modulo a parte. Con modulo 
 * se entiende un conjunto de fuentes de archivo de cabecera (.h) y los fuentes de programa del modulo (.c o .cpp).
 * 
 * NOTA IMPORTANTE sobre el uso de los procedures scanf y fgets del lenguaje C y el buffer input:
 *
 * scanf, luego de su ejecucion, deja en el buffer de entrada del programa un caracter "\n". 
 * Si la sentencia siguiente al scanf fuera un fgets o scanf, dicho procedure leera el caracter "\n"
 * en el buffer y producira efectos extranos. Ademas, scanf (de forma normal) no lee bien las cadenas de caracter 
 * que tiene espacios blancos intercalados, ejemplo "Hola, como estas". 
 *
 * scanf no maneja el buffer overflow ni tampoco maneja espacios blancos. 
 *
 * Por lo tanto, es necesario colocarle un control de formato en el primer parametro del scanf de la siguiente manera,
 *
 * typedef char string[20];
 * string str;
 *
 * scanf("%19[^\n]s", str);
 *
 * De esta manera, scanf leera 20 caracteres o hasta que encuentre el caracter "\n" sin incluirlo.write. Sin embrago, hay
 * el caracter "\n" aun seguira en el buffer luego de la ejecucion del scanf. De tal manera que cualquier sentencia de contratos
 * lectura estandar que se ejecute a continuacion se encontrata con dicho caracter "\n" al inicio, dando resultados errados.
 * Para limpiar el buffer de entrada (stdin) es necesario usar el procedimiento, 
 *
 * fflush(stdin);
 *
 * A veces sirve con colocar un getchar() para limpiar el caracter "\n" del buffer. Si se desea limpiar todo el compilador
 * buffer (como lo hace fflush) podriamos iterar con el getchar(),
 *
 * while((getchar()) != '\n');
 * ------------------------------------------------------------------------------------------------------------- */
#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

/* ==================INICIO ============================ TAD PUERTO ===================================================== */
/* Tipo de puerto. */
typedef enum tipoPuerto {yacimiento, refineria, deposito, sinAsignacion};

/* Tipo basico para el nombre de puerto. */
const int longNpuerto = 20;   /* Longitud de nombre del Puerto. */
typedef char nomPrt[longNpuerto];


/* --------------- *
 * Elemento Puerto *
 * --------------- */
typedef struct puerto {
   int          id;     /* Identificacion del puerto: 1..20. */
   nomPrt       nomP;   /* Nombre del puerto. */
   tipoPuerto   tipo;   /* Tipo de puerto. */
};


/* Numero de puertos disponibles en el sistema. */
const int numPuertos = 10;

/* ------------------------------------------------------------------------------------------------------------------------ *
 * Lista de puertos                                                                                                         *
 *                                                                                                                          *
 * Comentarios: - Si un Puerto tiene Id con caracter '0' indica que dicho puerto no existe en el sistema y puede ser creado.*
 * ------------------------------------------------------------------------------------------------------------------------ */
typedef puerto puertos[numPuertos];
puertos listaPuertos;

/* Procedimiento para inicializar la lista de puertos. */
void iniciaListaPuertos();
void iniciaListaPuertos() {
   nomPrt nomIni = "";

   for(int i = 0; i < numPuertos; i++) {
      listaPuertos[i].id = 0;
      for(int j = 0; j < longNpuerto-1; j++) {
         /* Asigna nombre del puerto. */
         listaPuertos[i].nomP[j] = nomIni[j];
      }
      listaPuertos[i].tipo = sinAsignacion;
   }
}


/* Procedimiento para asignar un Puerto. */
void asignaPuerto();
void asignaPuerto(int pId, nomPrt pNom, tipoPuerto pTip) {
   int i = pId - 1;   /* Activa el indice para el vector de puertos. */

   listaPuertos[i].id = pId;   /* Asigna Id del Puerto. */

   for(int j = 0; j < longNpuerto-1; j++) {
      /* Asigna nombre del Puerto. */
      listaPuertos[i].nomP[j] = pNom[j];
   }

   listaPuertos[i].tipo = pTip;   /* Asigna el tipo de Puerto. */
}


/* Procedimiento de tratamiento de la opcion "Editar Puerto". */
void editaPuerto() {
   int        idPuerto = 0;
   nomPrt     nombre;
   char       tipoOpc;
   tipoPuerto tipo;
   char       resp = ' ';

   system("cls");
   printf("Editar Puerto:\n\n");

   /* Lee el Id del Puerto. */
   printf("       Identificador(numero entre 1 y 10)?");
   scanf("%d", &idPuerto);
   getchar(); /* Para consumir el caracter nueva linea que deja scanf en el buffer. */
   // while((getchar()) != '\n') {};

   /* Lee el nombre del Puerto. */
   printf("       Nombre(entre 1 y 20 caracteres)?");
   fgets(nombre, longNpuerto, stdin);
   while((getchar()) != '\n') {};
   nombre[strcspn(nombre, "\n")] = 0; /* Elimina el caracter '\n' que deja el ENTER del usuario */

   /* Lee el tipo del Puerto. */
   printf("       Tipo(Y-Yacimiento, R-Refineria, D-deposito)?");
   tipoOpc = toupper(getchar());

   /* Limpia la pantalla y consulta al usuario. */
   while(resp != 'S' && resp != 'N') {
      system("cls");
      printf("Id....: %d\n", idPuerto);
      printf("Nombre: %s\n", nombre);
      printf("Tipo..: %c", tipoOpc);
      printf("\n\nIMPORTANTE: Esta opcion borra los datos anteriores.\n");
      printf("Son correctos los nuevos datos(S/N)?");
      resp = toupper(getchar());
   }

   if(resp == 'S') {
      /* Tipo de Puerto. */
      switch(tipoOpc) {
         case 'Y': tipo = yacimiento;
                   break;
         case 'R': tipo = refineria;
                   break;
         case 'D': tipo = deposito;
                   break;
      }

      /* Asigna el Puerto usando los datos leidos. */
      asignaPuerto(idPuerto, nombre, tipo);



/*DEBUG - Muestra la lista de puertos.*/
      for(int k = 0; k < numPuertos; k++) {
         printf("Id: %d,   ", listaPuertos[k].id);
         printf("Nombre: %s,   ", listaPuertos[k].nomP);
         printf("Tipo: ");
         switch(listaPuertos[k].tipo) {
            case yacimiento: printf("Yacimiento");
                             break;
            case refineria:  printf("Refineria");
                             break;
            case deposito:   printf("Deposito");
                             break;
         }
         printf("\n");
      }
/*DEBUG - Muestra la lista de puertos.*/


      getchar();
   }
}
/* =================FIN ============================== TAD PUERTO ====================================================== */




/* ========== INICIO ================================= TAD BUQUE ====================================================== */
/* Id del Buque. */
typedef enum idBuque {A, B, C, D, E};

/* Tipo de carga. */
typedef enum tipoCarga {crudo, fuel, gasoil, gasolina, vacio};

/* Tipo basico para el nombre de puerto o de buque: 1..20 caracteres. */
const int longNbuque = 20;   /* Longitud de nombre del Buque. */
typedef char nomBuq[longNbuque];

/* ---------------------------------------------------------------------------------------------------------------- *
 * Elemento Buque                                                                                                   *
 *                                                                                                                  *
 * Comentarios: - Este programa no funciona en tiempo real para la operacion del Buque.                             *
 *                El estado de un Buque (si esta en puerto o en traslado; si ha llegado al puerto destino;          *
 *                si esta cargado o vacio; todo esto se establece cuando el usuario elige la opcion "Operar buque". *
 * ---------------------------------------------------------------------------------------------------------------- */
typedef struct buque {
   idBuque      id;       /* Identificacion del buque: A, B, C, D, E. */
   nomBuq       nomB;     /* Nombre del buque. */
   tipoCarga    carga;    /* Carga del buque. */
   int          puertoI;  /* Puerto de inicio o puerto base. */
   int          puertoD;  /* Puerto destino. */
   int          duraC;    /* Duracion (en dias) de la operacion Cargar. */
   int          duraT;    /* Duracion (en dias) de la operacion Trasladar. */
   int          duraD;    /* Duracion (en dias) de la operacion Descargar. */

   /* Fecha inicio de operacion. */
   int          diaI;     /* Dia inicio. */
   int          mesI;     /* Mes inicio. */
   int          anoI;     /* Anno inicio. */

   /* Fecha fin de la operacion. */
   int          diaF;     /* Dia fin. */
   int          mesF;     /* Mes fin. */
   int          anoF;     /* anno fin. */
};


/* Numero de buques disponibles en el sistema. */
const int numBuques = 5;

/* ------------------------------------------------------------------------------------------------------------------ *
 * Lista de buques                                                                                                    *
 *                                                                                                                    *
 * Comentarios: - Si un Buque tiene Id con valor 0 indica que dicho buque no existe en el sistema y puede ser creado. *
 * ------------------------------------------------------------------------------------------------------------------ */
typedef buque buques[numBuques];
buques listaBuques;

/* Procedimiento para inicializar la lista de buques. */
void iniciaListaBuques();
void iniciaListaBuques() {
   nomBuq nomIni = " ";

   for(int i = 0; i < numBuques; i++) {
      listaBuques[i].id = A;
      for(int j = 0; j < longNbuque-1; j++) {
         /* Asigna nombre del Buque. */
         listaBuques[i].nomB[j] = nomIni[j];
      }
      listaBuques[i].carga = vacio;
      listaBuques[i].puertoI = 0;
      listaBuques[i].puertoD = 0;
      listaBuques[i].duraC = 0;
      listaBuques[i].duraT = 0;
      listaBuques[i].duraD = 0;
      listaBuques[i].diaI = 0;
      listaBuques[i].mesI = 0;
      listaBuques[i].anoI = 0;
      listaBuques[i].diaF = 0;
      listaBuques[i].mesF = 0;
      listaBuques[i].anoF = 0;
   }
}

/* Procedimiento para asignar un Buque. */
void asignaBuque();
void asignaBuque(idBuque bId, nomBuq bNom) {
   int i = bId;   /* Activa el indice para el vector de buques. */

   listaBuques[i].id = bId;   /* Asigna Id del Buque. */

   for(int j = 0; j < longNbuque-1; j++) {
      /* Asigna nombre del Buque. */
      listaBuques[i].nomB[j] = bNom[j];
   }
}

/* Procedimiento de tratamiento de la opcion "Editar Buque". */
void editaBuque();
void editaBuque() {
   idBuque    idB;
   char       idBq;
   nomBuq     nombre;
   char       tipoOpc;
   char       resp = ' ';
   int        diaIni;
   int        mesIni;
   int        anoIni;
   int        puertoI;

   system("cls");
   printf("Editar Buque:\n\n");

   /* Lee el Id del Buque. */
   getchar();
   printf("       Identificador(letra entre A y E)?");
   idBq = toupper(getchar());
   getchar(); /* Para consumir el caracter nueva linea que deja scanf en el buffer. */

   /* Lee el nombre del Puerto. */
   printf("       Nombre(entre 1 y 20 caracteres)?");
   fgets(nombre, longNbuque, stdin);
   //while((getchar()) != '\n') {};
   nombre[strcspn(nombre, "\n")] = 0; /* Elimina el caracter '\n' que deja el ENTER del usuario */

   /* Lee Fecha inicio: Dia. */
   printf("       Fecha inicio: Dia?");
   scanf("%d", &diaIni);
   while((getchar()) != '\n') {};

   /* Lee Fecha inicio: Mes. */
   printf("       Fecha inicio: Mes?");
   scanf("%d", &mesIni);
   while((getchar()) != '\n') {};

   /* Lee Fecha inicio: Anno. */
   printf("       Fecha inicio: Anno?");
   scanf("%d", &anoIni);
   while((getchar()) != '\n') {};

   /* Lee el Puerto de Inicio. */
   printf("Puertos posibles para la ubicacion inicial del buque:\n");

   /* Muestra la lista de puertos disponibles. */
   for(int k = 0; k < numPuertos; k++) {
      if(listaPuertos[k].id != 0) {
         printf("     %d-", listaPuertos[k].id);
         printf("%s   ", listaPuertos[k].nomP);
         printf("Tipo: ");
         switch(listaPuertos[k].tipo) {
            case yacimiento: printf("Yacimiento");
                             break;
            case refineria:  printf("Refineria");
                             break;
            case deposito:   printf("Deposito");
                             break;
         }
         printf("\n");
      }
   }
   printf("Identificador de puerto inicio?");
   scanf("%d", &puertoI);
   while((getchar()) != '\n') {};


   /* Limpia la pantalla y consulta al usuario. */
   while(resp != 'S' && resp != 'N') {
      system("cls");
      printf("\n\nId....: %c\n", idBq);
      printf("Nombre: %s\n", nombre);
      printf("Dia Inicio: %d\n", diaIni);
      printf("Mes Inicio: %d\n", mesIni);
      printf("Anno Inicio: %d\n", anoIni);
      printf("\n\nIMPORTANTE: Esta opcion borra los datos anteriores.\n");
      printf("Son correctos los nuevos datos(S/N)?");
      resp = toupper(getchar());
   }

   if(resp == 'S') {
      switch(idBq) {
         case 'A': idB = A;
                   break;
         case 'B': idB = B;
                   break;
         case 'C': idB = C;
                   break;
         case 'D': idB = D;
                   break;
         case 'E': idB = E;
                   break;
      }

      /* Asigna el Buque usando los datos leidos. */
      asignaBuque(idB, nombre);



/*DEBUG - Muestra la lista de buques.*/
      for(int k = 0; k < numBuques; k++) {
         printf("Id: %d,   ", listaBuques[k].id);
         printf("Nombre: %s", listaBuques[k].nomB);
         printf("\n");
      }
/*DEBUG - Muestra la lista de puertos.*/


      getchar();
   }
}
/* ========== FIN ==================================== TAD BUQUE ====================================================== */


/* ----------------------------------------------------------------------------- *
 * Programa: GestFlota - Gestiona los Movimientos de una Flota                   *
 *                                                                               *
 * Comentarios: - Se asume que los Puertos y Buques existen durante la ejecucion *
 *                del programa. No se hace uso del almacenamiento en disco.      *
 *                                                                               *
 *              - Este programa utiliza el procedimiento system() para ejecutar  *
 *                el comando "cls" de MSDOS para limpiar la pantalla.            *
 * ----------------------------------------------------------------------------- */
int main() {
   char resp = ' ';   /* Opcion seleccionada por el usuario. */

   /* Inicializa las listas de puertos y buques. */
   iniciaListaPuertos();
   iniciaListaBuques();

   /* Limpia la pantalla y consulta al usuario. */
   while(resp != 'S') {
      /* Muestra menu principal de GestFlota. */
      system("cls");
      printf("\n\nGestFlota: Gestion de Movimientos de una Flota\n");
      printf("==============================================\n\n");
      printf("       Editar Puerto                      (Pulsar P)\n");
      printf("       Editar Buque                       (Pulsar B)\n");
      printf("       Estado Buques                      (Pulsar E)\n");
      printf("       Operar Buque                       (Pulsar O)\n");
      printf("       Resumen Mensual Buque              (Pulsar R)\n");
      printf("       Salir                              (Pulsar S)\n\n");
      printf("Teclear una opcion valida (P|B|E|O|R|S)?");

      resp = toupper(getchar());

      switch(resp) {
         case 'P': editaPuerto();   /* Tratamiento de Puerto. */
                   break;
         case 'B': editaBuque();    /* Tratamiento de Buque. */
                   break;
         case 'S': return 0;        /* Termina el programa. */
                   break;
      }

      getchar();

      resp = ' ';
   }
}





/* ------------------------------------------------------------------------------- *
 * Ejemplo de lectura de un archivo texto desde un programa en C.                  *
 *                                                                                 *
 * NOTA: getc reconoce los caracteres blancos. fscanf no los reconoce por defecto. *
 *       Para la escritura se utiliza la funcion putc y fopen con "w".             *
 * ------------------------------------------------------------------------------- */
#include <stdio.h>

int main(int argc, char *argv[]) {
   char linea;

   FILE *inArch = fopen("prueba.txt", "r");

   if(inArch) {
      while((linea = getc(inArch)) != EOF) printf("%c", linea);
   }else printf("No abrio el archivo!");

   fclose(inArch);

   return(0);
}








/* ------------------------------- *
 * Aplicacion que dibuja un rombo. *
 * ------------------------------- */
#include<stdio.h>

/* Ajusta con espacios a la izquierda para una fila especifica. */
void ajustaConEspacios(int limite) {
   for(int i = 1; i <= limite; i++) {
      printf(" ");
   }
}

/* Construye el triangulo superior del rombo. */
void trianguloSuperior(int altura) {
   char c = ' ';     /* Almacena el tipo de caracter a imprimir (@, 0, .). */
   int e = 0;        /* Para la seleccion del caracter a imprimir. */

   /* Triangulo superior. */
   for(int k = 2; k <= altura; k++) {
      /* Ajusta con espacios la figura del triangulo. */
      ajustaConEspacios(altura - k);

      /* Imprime el triangulo superior izquierdo. */
      for(int pos = 0; pos <= k-1; pos++) {
         /* Selecciona el caracter a imprimir. */
         e = pos % 4;

         if(e == 0) {
            c = '@';
         }else if(e == 1 || e == 3) {
            c = '.';
         }else {
            c = 'o';
         }

         printf("%c", c);      /* Imprime el caracter*/
      }

      /* Imprime el triangulo superior derecho. */
      for(int pos = k-2; pos >=0 ; pos--) {
         /* Selecciona el caracter a imprimir. */
         e = pos % 4;

         if(e == 0) {
            c = '@';
         }else if(e == 1 || e == 3) {
            c = '.';
         }else {
            c = 'o';
         }

         printf("%c", c);   /* Imprime el caracter*/
      }

      printf("\n");   /* Nueva linea. */
   }
}

/* Construye el triangulo inferior del rombo. */
void trianguloInferior(int altura) {
   char c = ' ';     /* Almacena el tipo de caracter a imprimir (@, 0, .). */
   int e = 0;        /* Para la seleccion del caracter a imprimir. */


   for(int k = altura-1; k >= 1; k--) {
      /* Ajusta con espacios la figura del triangulo. */
      ajustaConEspacios(altura - k);

      /* Imprime el triangulo inferior izquierdo. */
      for(int pos = 0; pos <= k-1; pos++) {
         /* Selecciona el caracter a imprimir. */
         e = pos % 4;

         if(e == 0) {
            c = '@';
         }else if(e == 1 || e == 3) {
            c = '.';
         }else {
            c = 'o';
         }

         printf("%c", c);      /* Imprime el caracter*/
      }

      /* Imprime el triangulo inferior derecho. */
      for(int pos = k-2; pos >=0 ; pos--) {
         /* Selecciona el caracter a imprimir. */
         e = pos % 4;

         if(e == 0) {
            c = '@';
         }else if(e == 1 || e == 3) {
            c = '.';
         }else {
            c = 'o';
         }

         printf("%c", c);   /* Imprime el caracter*/
      }

      printf("\n");   /* Nueva linea. */
   }
}

/*------------------------------------------------------------------*
* Programa: Dibuja un rombo en base a su altura.                    *
*                                                                   *
* Descripcion: La construccion del rombo se divide en               *
*    - Contruccion de un triangulo                                  *
*    - Construccion de un triangulo invertido y similar al primero  *
*      (pero compartiendo la base)                                  *
* ------------------------------------------------------------------*/
int main() {
   int altura = 0;   /* Altura del rombo. */

   /* Solicita el lado del rombo. */
   printf("Lado del rombo?");
   scanf("%d", &altura);

   /* Construye el rombo con el lado solicitado. */
   if(altura > 0 && altura <= 20) {
      /* Ajusta con espacios el vertice superior del rombo. */
      ajustaConEspacios(altura - 1);

      printf("@\n");

      if(altura > 1) {
         /* Construye el triangulo superior. */
         trianguloSuperior(altura);

         /* Construye el triangulo inferior. */
         trianguloInferior(altura);
      }
   }
}










#
#
#                                        SECCION DE EJEMPLOS C++                                             #
#
#

# -------------------------------------------------------------------------------------------------------- #
# IMPORTANTE: los comandos de compilacion (GNU) son g++ y gcc. Para compilar un programa C++ con gcc debe  #
#             incluir, luego del nombre del fuente, la opcion -lstdc++ como se muestra aqui,               #
#                                                                                                          #
#             gcc -std=c++17 test.cpp -lstdc++ -o test                                                     #
#                                                                                                          #
#             Explicacion tomada de                                                                        #
#             https://stackoverflow.com/questions/28236870/error-undefined-reference-to-stdcout),          #
#             "as cout is present in the C++ standard library, which would need explicit linking           #
#              with -lstdc++ when using gcc; g++ links the standard library by default."                   #
#                                                                                                          #
# IMPORTANTE: Algunos autores indican que NO DEBE USARSE "using namespace std" dado que esta sentencia,    #
#                                                                                                          #
# -cita"The statement using namespace std is generally considered bad practice. The alternative to this    #
#       statement is to specify the namespace to which the identifier belongs using the scope operator(::) #
#       each time we declare a type.                                                                       #
#       Although the statement saves us from typing std:: whenever we wish to access a class or type       #
#       defined in the std namespace, it imports the entirety of the std namespace into the current        #
#       namespace of the program."                                                                         #
#                                                                                                          #
# NOTA: Para compilar un programa con el GNU C++:                                                          #
#            c++ -std=c++11 <nombre del fuente .cpp> -o <nombre del compilado ejecutable> o tambien        #
#            g++ -std=c++11 .................                                                              #
# NOTA: Para hacer DEBUG de un programa C++ se utiliza el DEBUGER "gdb" que viene con la distribucion GNU. #
#       Antes de hacer debug de un programa se debe compilar dicho programa con la opcion "-g". Luego,     #
#       para hacer el debug:                                                                               #
#                            ...>gdb <nombre del programa>                                                 #
#                                                                                                          #
#       Dentro del debuger se puede listar el fuente con "l". Se ejecuta con "r". Se puede colocar un      #
#       breakpoint con "break <nombre de la funcion>", ejemplo: (gdb)break main. Puede ejecutar paso a     #
#       paso con "n" (que pasa por encima de las llamadas de bajo nivel) o "step" que entra, incluso,      #
#       hasta las funciones dentro de las dll del sistema. Con "print" podemos visualizar cualquier        #
#       variable o expresion: (gdb)print salida o (gdb)print (char*)l-> dato                               #
#       Para salir del debuger se usa "quit". Hay muchas otras opciones de analisis (ver manual).          #
# -------------------------------------------------------------------------------------------------------- #

/* ----------------------------------------------------------------------------- *
 * Ejemplos de uso de directivas al preporcesador y definicion de macros en C++. *
 * ----------------------------------------------------------------------------- */
#define __MICONSTANTE__

/*
#ifndef __MICONSTANTE__
#define resta(x, y) x - y
#else
#define suma(x, y) x + y
#endif
*/

#if (defined __MICONSTANTE__)
#define suma(x, y) x + y
#endif

#if !(defined __MICONSTANTE__)
#define resta(x, y) x - y
#endif









/* -------------------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: En C++ es posible crear bloques (scopes) que crean un ambito para la existencia de variables, etc. *
 *             Aqui hay un ejemplo usando tres variables con mismo nombre.                                        *
 * -------------------------------------------------------------------------------------------------------------- */
{
                int x = 1;

                {
                        int x = 2;

                        {
                                int x = 3;
                                std::cout << "\nx interior = " << x << "\n";
                        }
                        std::cout << "\nx medio = " << x << "\n";
                }
                std::cout << "\nx exterior = " << x << "\n";
}

// Salida:
x interior = 3

x medio = 2

x exterior = 1













/* ---------------------------------------------------------------------------------------------------- *
 * IMPORTANTE: C++, al igual que C, permite operaciones a nivel de bits como desplazamiento ">>" y "<<" *
 * -----------------------------------------------------------------------------------------------------*/
unsigned int N = 2;

std::cout << "\nN = " << N << "\n";
N = N << 1;
std::cout << "\nN = " << N << "\n";

// Salida:
N = 2

N = 4












/* ---------------------------------------------------------------------------------------------- * 
 * IMPORTANTE: Acceso (desde una clase derivada) a miembros declarados private en una clase base: *
 *                                                                                                *
 * In C++, there are three access specifiers:                                                     *
 *                                                                                                *
 *   public    - members are accessible from outside the class                                    *
 *   private   - members cannot be accessed (or viewed) from outside the class                    *
 *   protected - members cannot be accessed from outside the class, however, they can be accessed *
 *               in inherited classes. You will learn more about Inheritance later.               *
 * ---------------------------------------------------------------------------------------------- */













/* --------------------------------------------------------------------------------------------------------------------------------- *
 * Sobre los constructores, destructores, bloques (scopes), structs y clases.                                                        *
 *                                                                                                                                   *
 * IMPORTANTE: Los STRUCT al igual que las CLASS pueden tener modificadores de acceso a los miembros: public, private y protected!!! *
 *             Tambien pueden tener constructor y destructor como se muestra en el ejemplo siguiente.                                *
 *                                                                                                                                   *
 *             Los destructores se ejecutan al momento en que el bloque (scope) en el cual se instancia la STRUCT o la CLASS termina.*
 *                                                                                                                                   *
 * IMPORTANTE: Observar que, para mostrar la ejecucion de los constructores y los destructores se colocaron ambas instancias dentro  *
 *             de bloques (scopes)!!!                                                                                                *
 * --------------------------------------------------------------------------------------------------------------------------------- */
#include <iostream>

class base {
        public:
                int x;
                base(int xP) { this->x = xP; std::cout << "\nEjecuta el constructor!\n"; }
                ~base() { std::cout << "\nEjecuta el destructor!\n"; }
};

struct segunda {
        public:
                int y;
                segunda() { std::cout << "\nConstructor de segunda!\n"; }
                ~segunda() { std::cout << "\nDestructor de segunda!\n"; }
};

int main() {
        // Creamos un bloque (scope).
        {
                base miInst(2);
        }

        // Creamos un bloque (scope).
        {
                segunda miSeg;
        }

        std::cout << "\nSale del main!\n";
        return 0;
}

// Salida:
Ejecuta el constructor!

Ejecuta el destructor!

Constructor de segunda!

Destructor de segunda!

Sale del main!













#
# Sobre la lectura (STDIN) y escritura (STDOUT) desde y hacia PIPES con otros programas y comandos del sistema.
#
# Supongamos que queremos desarrollar un programa nativo (.exe, no script PYTHON) que lea desde una PIPE de salida de otro
# programa (como en el ejemplo anterior). Para esto creamos un fuente en lenguaje C o C++:
#
#include <iostream>

int main() {
        std::string linea = "";
        std::getline(std::cin, linea);   // La funcion "getline" puede leer la STDIN para recibir el mensaje enviado via PIPE.
        std::cout << linea;              // Luego, enviamos al STDOUT el mismo mensaje para que, via PIPE, lo lea otro programa.
        return 0;
}

# Compilamos este programa para crear el ejecutable que pudieramos llamar "test.exe". Ahora incluimos este programa dentro de 
# la secuencia de PIPES en el ejemplo anterior:
$ g++ -std=c++17 test.cpp -o test

# Repetimos el "super comando" incluyendo el programa nuevo:
$ cat test.txt | ./test | tr ' ' '\n' | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head
      2 de
      1 una
      1 prueba
      1 linea
      1 esta
      1 es
      1 archivo

# Vemos como en una sola linea de comando invocamos varios "mini comandos" para crear un "super comando".
# El comando "tr" traslada o transforma un caracter en otro. En este ejemplo "tr" toma la salida estandar STDOUT de "cat" y 
# reemplaza todos los espacios blancos por el caracter de nueva linea "\n". Luego, la salida estandar de "tr" es enviada a 
# otra invocacion del mismo comando "tr" ahora para reemplazar las mayusculas por minusculas. Esto se conecta con la entrada 
# estandar del comando "sort" que ordena alfabeticamente las palabras recibidas. Despues, se envia al comando "uniq -c" que 
# tomara sin duplicados cada palabra y las cuenta dando como resultado cada palabra acompanada de el numero de veces que aparece. 
# Esto ultimo se envia esto al comando "sort -nr" que ordena en reverso numericamente y alfanumericamente lo que recibe. Al final 
# se envia el resultado hacia el comando "head" que imprime las primeras lineas de todo lo que recibe. Esta es la filosofia de 
# UNIX!!!!












/* ---------------------------------------------------------------------------------------------------------------------- *
 * IMPORTNTE: Un vector puede inicializarse:                                                                              *
 *            1) Usando una lista de valores como se mestra en los siguientes ejemplo (ambos validos en C++)              *
 *            2) Usando el nombre de un vector previamente creado. El nuevo vector contendra un copia del vector original *
 * ---------------------------------------------------------------------------------------------------------------------- */
std::vector<int> miVector = {1, 2, 3, 4, 5, 6, 7, 8, 9};
// tambien:
std::vector<int> miVector({1, 2, 3, 4, 5, 6, 7, 8, 9});

// Haciendo una copia de un vector:
std::vector<int> copiaVector(miVector);   // Crea una copia del vector original.


/* ------------------------------------------------------------------ *
 * OTRAS funciones sobre vectores disponibles en la libreria <vector> *
 * ------------------------------------------------------------------ */
Iterators
    begin() – Returns an iterator pointing to the first element in the vector
    end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector
    rbegin() – Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
    rend() – Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
    cbegin() – Returns a constant iterator pointing to the first element in the vector.
    cend() – Returns a constant iterator pointing to the theoretical element that follows the last element in the vector.
    crbegin() – Returns a constant reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
    crend() – Returns a constant reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)

Capacity
    size() – Returns the number of elements in the vector.
    max_size() – Returns the maximum number of elements that the vector can hold.
    capacity() – Returns the size of the storage space currently allocated to the vector expressed as number of elements.
    resize(n) – Resizes the container so that it contains ‘n’ elements.
    empty() – Returns whether the container is empty.
    shrink_to_fit() – Reduces the capacity of the container to fit its size and destroys all elements beyond the capacity.
    reserve() – Requests that the vector capacity be at least enough to contain n elements.

Element access
    reference operator [g] – Returns a reference to the element at position ‘g’ in the vector
    at(g) – Returns a reference to the element at position ‘g’ in the vector
    front() – Returns a reference to the first element in the vector
    back() – Returns a reference to the last element in the vector
    data() – Returns a direct pointer to the memory array used internally by the vector to store its owned elements.

Modifiers
    assign() – It assigns new value to the vector elements by replacing old ones
    push_back() – It push the elements into a vector from the back
    pop_back() – It is used to pop or remove elements from a vector from the back.
    insert() – It inserts new elements before the element at the specified position
    erase() – It is used to remove elements from a container from the specified position or range.
    swap() – It is used to swap the contents of one vector with another vector of same type. Sizes may differ.
    clear() – It is used to remove all the elements of the vector container
    emplace() – It extends the container by inserting new element at position
    emplace_back() – It is used to insert a new element into the vector container, the new element is added to the end of the vector











/* ---------------------------------------------------------------------------------------------------------------------- *
 * Algoritmos como FIND devuelven un valor tipo iterator apuntando a la posicion del vector donde ocurre la coincidencia! *
 *                                                                                                                        *
 * IMPORTANTE: Si queremos mostrar la "direccion" o valor del iterador DEBEMOS usar el metodo std::distance como se       *
 *             muestra en el ejemplo.                                                                                     * 
 * -----------------------------------------------------------------------------------------------------------------------*/
std::vector<int>::iterator i = std::find(std::begin(V), std::end(V), valorBuscado);

// Para mostrar la posicion (no el contenido de lo apuntado por) el iterador:
std::cout << std::distance(i, std::begin(V));













/* ----------------------------------------------------------------------------------------------------------------------------- *
 * Ejemplo de Smart Pointers en C++. Con este tipo de apuntadores se evita el problema de memory leack!                          *
 *                                                                                                                               *
 * En este ejemplo se muestra un tipo de los varios tipos de Smart Pointers que existen en C++.                                  *
 * Es "unique" porque solo se puede tener un solo apuntador a un objeto. Se libera el apuntador y se asigna el objeto apuntado   *
 * a otro apuntador con la funcion "move".                                                                                       *
 *                                                                                                                               *
 * El tipo "shared_ptr" si permite a mas de un pointer apuntar a un mismo objeto. Este tipo de pointer lleva un contador de      *
 * referencias a un mismo objeto que puede consultarse a traves de la funcion "use_count". Esto ultimo indica que C++ establece  *
 * un registro de referencias durante todo el tiempo de existencia del objeto.                                                   *
 *                                                                                                                               *
 * El tipo "weak_ptr" es similar al "shared_ptr" pero C++ no lleva un contador de referencias y como resultado el sistema de     *
 * apuntadores es mas parecido al de C (solo objeto y pointers que apuntan al objeto).                                           *
 *                                                                                                                               *
 * NOTA: Debe declarar la libreria "memory".                                                                                     *
 * ----------------------------------------------------------------------------------------------------------------------------- */
#include <iostream>
#include <memory>

class rectangle {
        int length;
        int breadth;
        public:
        rectangle(int l, int b) : length(l), breadth(b) {}
        int area() { return this->length * this->breadth; }
};

int main() {
        std::unique_ptr<rectangle> P(new rectangle(10, 5));
        std::cout << "\n\nArea = " << P->area() << "\n\n";
        std::unique_ptr<rectangle> P2;
        P2 = std::move(P);
        return 0;
}
















/* ----------------------------------------------------------------------------------------------------------------------- *
 * Un programa C o C++ puede leer las variables del ambiente (Shell) en el cual se ejecuta. Para ello debe usar la funcion *
 * getenv contenida en la libreria stdlib.h.                                                                               *
 * ----------------------------------------------------------------------------------------------------------------------- */
#include <iostream>
#include <stdlib.h>

int main(int argc, char *argv[]) {
        char *libvar = getenv("PWD");
        std::cout << "\n\nLa variable PWD = " << libvar << "\n\n";
        return 0;
}







/* ----------------------------------------------------------------------------------------------------------------------*
 * IMPORTANTE EN C++: Se puede precindir de la sentencia "using namespace std". SIN EMBARGO, en esa situacion usted debe *
 *                    colocar el prefijo "std::" A TODO!!! INCLUIDOS: std::vector, etc.                                  *
 * --------------------------------------------------------------------------------------------------------------------- */









/* --------------------------------------------------------------------------------------------------- *
 * Ejemplo de uso de "this" en C++.                                                                    *
 * Ejemplo de creacion de un tipo de dato (con "using") de una clase individual (no arreglo o vector). *
 *                                                                                                     *
 * NOTA: En C++ el "this" es un apuntador a un atributo de una clase (o struct).                       *
 *       Como todo apuntador se utiliza a traves del operador "->"!!!                                  *
 * --------------------------------------------------------------------------------------------------- */
#include <iostream>

template<typename T> class parOr {
        private:
        T x;
        T y;
        public:
        parOr() : x(0), y(0) {}
        parOr(T xP, T yP) : x(xP), y(yP) {}
        void setX(T xP) { this->x = xP; }
        void setY(T yP) { this->y = yP; }
        T getX() { return this->x; }
        T getY() { return this->y; }
        parOr operator+(parOr oper) { return parOr(this->x+oper.x, this->y+oper.y); }
        parOr operator*(T k) { return parOr(k*this->x, k*this->y); }
};

using tipoPar = parOr<int>;   // OJO: observar como se declara un tipo de dato nuevo para una clase individual (no un vector o arreglo de...)!!!

int main() {
        tipoPar p(2, 3);
        tipoPar q(4, 4);


        std::cout << "\n\np.x = " << p.getX() << " , p.y = " << p.getY() << "\n\n";
        return 0;
}


# A continuacion otro ejemplo de "using":



/* --------------------------------------------------------------------------------------------------------- *
 * En C++ moderno es posible crear tipos de datos con "using" al igual que con "typedef". Veamos un ejemplo. *
 * ----------------------------------------------------------------------------------------------------------*/
int miFun(int x, int y) { return x + y; }

// Declaramos un apuntador a funcion en C++ moderno.
using FP = int (*)(int, int);

int main() {
   FP funPtr = miFun;

   std::cout << "\n\nfunPtr(3, 2) = " << funPtr(3, 2) << "\n\n";

   return 0;
}


// Ahora veamos un ejemplo de declaracion de tipo de un array de objetos (par ordenado en este ejemplo):
template<typename T> class parOr {
   public:
      parOr()           : x(0), y(0), dumyX(0), dumyY(0) {}
      parOr(T pX, T pY) : x(pX), y(pY), dumyX(0), dumyY(0) {}

      void setX(T pX)               { x = pX; }
      void setY(T pY)               { y = pY; }
      T getX()                      { return x; }
      T getY()                      { return y; }
      parOr operator + (parOr pPar) { dumyX += pPar.x; dumyY += pPar.y; return(parOr(dumyX, dumyY)); }
      parOr operator * (T n)        { dumyX = n*x; dumyY = n*y; return(parOr(dumyX, dumyY)); }
   private:
      T   x;
      T   y;
      T   dumyX;
      T   dumyY;
};

// Observar la manera de declarar un tipo array de objeto con template int!!!
using plano = parOr<int>[50];


// Luego, en main():
plano miPlano;

miPlano[0] = parOr<int>(0, 0);

miPlano[0].setX(5);
miPlano[0].setY(6);
miPlano[1] = miPlano[0] * 3;   // Obervar como el producto escalar (tal y como se definio) devuelve un objeto parOr!!

std::cout << "\n\n\nmiPlano[0].x = " << miPlano[0].getX() << ", miPlano[0].y = " << miPlano[0].getY() << "\n\n\n";
std::cout << "miPlano[1].x = " << miPlano[1].getX() << " y miPlano[1].y = " << miPlano[1].getY() << "\n\n\n";









/* ------------------------------------------------------------------------------------------------ *
 * IMPORTANTE: A partir de C++17 la sentencia if puede contener una variable con su inicializacion! *
 * ------------------------------------------------------------------------------------------------ */
if(int x = 4; x > V[0]) {
   std::cout << "\n\n\n X ES MENOR QUE V[0]! \n\n\n\n";
}else{
   std::cout << "\n\n\n X NO ES MENOR QUE V[0]!! \n\n\n\n";
}








/* ----------------------------------------------------------------- */
/* Como pasar argumentos (desde la linea de comandos) a un programa. */
/*                                                                   */
/* NOTA: argc es un contador de argumentos, siendo el 1 el nombre    */
/*       del programa y 2 o mayor los argumentos al programa.        */
/*       argv es un vector de a puntadores a char que incluye los    */
/*       argumentos, siendo argv[0] el nombre del programa.          */
/* ----------------------------------------------------------------- */
#include<iostream>

int fact(int x) { if(!x || (x == 1)) return(1); return(x * fact(x - 1)); }

int main(int argc, char *argv[]) { 

   if(argc < 2) { 
      std::cout << "Debe indicar un argumento..." << endl; 
   }else {
      int num = stoi(argv[1]);   // Convierte a int el numero al cual se le calculara el factorial.

      std::cout << "Factorial de " << num << endl;
   }

   return(0);
}





/* ------------------------------------------------------------------------------------------------------------------------- *
 * Ejemplo de uso de la libreria chrono para tomar el TIEMPO real con C++. Para medir tiempo de ejecucion en milisegundos!!! *
 *                                                                                                                           *
 * Ejemplo de uso del metodo SLEEP (de la libreria unistd.h o windows.h) para hacer espera en segundos!!!                    *
 * ------------------------------------------------------------------------------------------------------------------------- */
#include<iostream>
#include<chrono>

// Esta libreria se usa para LINUX. Para WINDOWS se usa windows.h !!!!!!!
#include<unistd.h>

int main() {
   auto start = std::chrono::high_resolution_clock::now();
   sleep(5);   // IMPORTANTE: "sleep" (todo minuscula en Unix/Linux); "Sleep" ("S" en mayuscula) para Windows!!!!!!!
   auto stop = std::chrono::high_resolution_clock::now();

  std::cout << "tiempo: " << std::chrono::duration_cast<std::chrono::milliseconds>(stop - start).count() << " milliseconds\n";

  return 0;
}








#include<iostream>

using namespace std;

int euclides(int a, int b) {
   if(!b) return(a);
   else return(b, a%b);
}

int main() {
   cout << euclides(6, 2) << endl;

   return(0);
}









/* ---------------------- *
 * Sobre LVALUE y RVALUE. *
 * ---------------------- */
Tomado de https://stackoverflow.com/questions/5481539/what-does-t-double-ampersand-mean-in-c11

  t declares an rvalue reference (standards proposal doc).

  Here's an introduction to rvalue references.

  Here's a fantastic in-depth look at rvalue references by one of Microsoft's standard library developers.

      CAUTION: the linked article on MSDN ("Rvalue References: C++0x Features in VC10, Part 2") is a very clear introduction to Rvalue references, but makes statements about Rvalue references that were once true in the draft C++11 standard, but are not true for the final one! Specifically, it says at various points that rvalue references can bind to lvalues, which was once true, but was changed.(e.g. int x; int &&rrx = x; no longer compiles in GCC) – drewbarbs Jul 13 '14 at 16:12

  The biggest difference between a C++03 reference (now called an lvalue reference in C++11) is that it can bind to an rvalue like a temporary without having to be const. Thus, this syntax is now legal:

  T&& r = T();

  rvalue references primarily provide for the following:

  Move semantics. A move constructor and move assignment operator can now be defined that takes an rvalue reference instead of the usual const-lvalue reference. A move functions like a copy, except it is not obliged to keep the source unchanged; in fact, it usually modifies the source such that it no longer owns the moved resources. This is great for eliminating extraneous copies, especially in standard library implementations.

  For example, a copy constructor might look like this:

  foo(foo const& other)
  {
      this->length = other.length;
      this->ptr = new int[other.length];
      copy(other.ptr, other.ptr + other.length, this->ptr);
  }

  If this constructor were passed a temporary, the copy would be unnecessary because we know the temporary will just be destroyed; why not make use of the resources the temporary already allocated? In C++03, there's no way to prevent the copy as we cannot determine whether we were passed a temporary. In C++11, we can overload a move constructor:

  foo(foo&& other)
  {
     this->length = other.length;
     this->ptr = other.ptr;
     other.length = 0;
     other.ptr = nullptr;
  }

  Notice the big difference here: the move constructor actually modifies its argument. This would effectively "move" the temporary into the object being constructed, thereby eliminating the unnecessary copy.

  The move constructor would be used for temporaries and for non-const lvalue references that are explicitly converted to rvalue references using the std::move function (it just performs the conversion). The following code both invoke the move constructor for f1 and f2:

  foo f1((foo())); // Move a temporary into f1; temporary becomes "empty"
  foo f2 = std::move(f1); // Move f1 into f2; f1 is now "empty"

  Perfect forwarding. rvalue references allow us to properly forward arguments for templated functions. Take for example this factory function:

  template <typename T, typename A1>
  std::unique_ptr<T> factory(A1& a1)
  {
      return std::unique_ptr<T>(new T(a1));
  }

  If we called factory<foo>(5), the argument will be deduced to be int&, which will not bind to a literal 5, even if foo's constructor takes an int. Well, we could instead use A1 const&, but what if foo takes the constructor argument by non-const reference? To make a truly generic factory function, we would have to overload factory on A1& and on A1 const&. That might be fine if factory takes 1 parameter type, but each additional parameter type would multiply the necessary overload set by 2. That's very quickly unmaintainable.

  rvalue references fix this problem by allowing the standard library to define a std::forward function that can properly forward lvalue/rvalue references. For more information about how std::forward works, see this excellent answer.

  This enables us to define the factory function like this:

  template <typename T, typename A1>
  std::unique_ptr<T> factory(A1&& a1)
  {
      return std::unique_ptr<T>(new T(std::forward<A1>(a1)));
  }

  Now the argument's rvalue/lvalue-ness is preserved when passed to T's constructor. That means that if factory is called with an rvalue, T's constructor is called with an rvalue. If factory is called with an lvalue, T's constructor is called with an lvalue. The improved factory function works because of one special rule:

      When the function parameter type is of the form T&& where T is a template parameter, and the function argument is an lvalue of type A, the type A& is used for template argument deduction.

  Thus, we can use factory like so:

  auto p1 = factory<foo>(foo()); // calls foo(foo&&)
  auto p2 = factory<foo>(*p1);   // calls foo(foo const&)

  Important rvalue reference properties:

      For overload resolution, lvalues prefer binding to lvalue references and rvalues prefer binding to rvalue references. Hence why temporaries prefer invoking a move constructor / move assignment operator over a copy constructor / assignment operator.
      rvalue references will implicitly bind to rvalues and to temporaries that are the result of an implicit conversion. i.e. float f = 0f; int&& i = f; is well formed because float is implicitly convertible to int; the reference would be to a temporary that is the result of the conversion.
      Named rvalue references are lvalues. Unnamed rvalue references are rvalues. This is important to understand why the std::move call is necessary in: foo&& r = foo(); foo f = std::move(r);











/* --------------------------------------------------------------------------------------- *
 * IMPORTANTE: C++ no admite hacer formatos complejos con printf o scanf tales como %-15s. *
 *             Por tal motivo hay que utilizar "cout" pero tomando en cuenta lo siguiente: *
 *                                                                                         *
 * - Como imprimir CON FORMATO una tabla de valores en C++?                                *
 * - Ejemplo de array anidado dentro de otro array!!                                       *
 * - Ejemplo de calculo del numero de elementos de un array de strings
 *                                                                                         *
 * IMPORTANTE: Debe incluir la libreria "iomanip"!                                         *
 *             PERO tambien puede aplicarse FORMATO con la libreria Boost (Boost.format)!! *
 * --------------------------------------------------------------------------------------- */
#include <iomanip>

   string arrStrg[4] = {"Titulo1", "Titulo2", "Titulo3", "Titulo4"};

   // Ejemplo de array anidado dentro de otro array.
   int arrDatos[4][4] = {{36, 20, 100, 72}, {240, 65, 89, 12}, {90, 53, 76, 18}, {17, 16, 15, 14}};


   //
   // IMPORTANTE: sizeof devuelve el tamano en Bytes. Por tanto, se debe dividir el tamano total del array entre el 
   //             tamano de un tipo de dato (int o string por ejemplo) para conocer la cantidad de elementos del array. Esto se hace SOLO 
   //             en caso de que no se sepa (a priori) el numero de elementos del array!!
   //
   for(int i = 0; i < (sizeof(arrStrg)/sizeof(string)); i++) cout << setw(10) << arrStrg[i];
   cout << endl;
   for(int i = 0; i < (sizeof(arrStrg)/sizeof(string)); i++) cout << setw(10) << "========";
   cout << endl;
   for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) cout << setw(10) << arrDatos[i][j];
      cout << endl;
   }

   cout << "\n\n\n";



Salida:

   Titulo1   Titulo2   Titulo3   Titulo4
  ========  ========  ========  ========
        36        20       100        72
       240        65        89        12
        90        53        76        18
        17        16        15        14










/* -------------------------------------------------------------------------------------------------- */
/* Como modificar la precision (en la salida estandar) de los valores numericos double y long double. */
/*                                                                                                    */
/* NOTA: Ver notas arriba sobre la libreria "iomanip" y sobre el posible uso de las librarias Boost.  */
/* -------------------------------------------------------------------------------------------------- */
#include <iomanip>

cout << fixed << showpoint;   // Con esta sentencia se instruye a la salida estandar que muestre el punto.
cout << setprecision(9);      // Esta sentencia activa la precision a nueve digitos decimales. Sin embargo, hay truncamiento.

// Este es solo un ejemplo.
for(vector<contrato>::iterator i = vecSIX.begin(); i != vecSIX.end(); i++) cout << "Contrato: " << i->getNumCon() << ",   Monto: " << i->getMonto() << endl;










/* --------------------------------------------------------------------------------------------------------------------- *
 * Forward declaration de una struct en C++.                                                                             *
 *                                                                                                                       *
 * IMPORTANTE: En los casos en que el programador necesite declarar un elemento de una struct con un tipo                *
 *             que no haya sido definido previamente (como veremos en el ejemplo abajo), entonces debe hacer una         *
 *             forward declaration del tipo de dato antes. PERO, esto UNICAMENTE ES POSIBLE si el elemento que se        *
 *             declara es un APUNTADOR a ese tipo: NO PUEDE SER UNA VARIABLE O ATRIBUTO porque el compilador no tiene    *
 *             manera de conocer cuanto espacio de memoria debe apartar para ese tipo (cuando se declara un apuntador el *
 *             compilador no necesita conocer esto porque es solo un apuntador a "algo").                                *
 * --------------------------------------------------------------------------------------------------------------------- */

// El siguiente ejemplo da un error en la compilacion porque la variable no es un apuntador!
struct str_base;

struct str_utiliza {
   int indice;
   str_base stBase;   // <---- NO ES UN APUNTADOR A str_base. Forward declaration no funciona en este caso!
};


struct str_base {
   int x;
   int y;
};

~/cppWorks$ g++ -std=c++17 main.cpp -o main
main.cpp:65:13: error: field ‘stBase’ has incomplete type ‘str_base’
   65 |    str_base stBase;
      |             ^~~~~~
main.cpp:61:8: note: forward declaration of ‘struct str_base’
   61 | struct str_base;
      |        ^~~~~~~~


// Para que compile bien, debemos declarar un apuntador al tipo str_base!
struct str_base;

struct str_utiliza {
   int indice;
   str_base *stBase;   // <---- APUNTADOR A str_base!
};


struct str_base {
   int x;
   int y;
};








/* --------------------------------------------------------------------------------------------------------------------- *
 * Ejemplos de funciones matematicas.                                                                                    *
 *                                                                                                                       *
 * IMPORTANTE: Las funciones trigonometricas esperan el parametro en RADIANES. Por tal motivo se debe convertir el valor *
 *             de grados a RADIANES como se muestra en el ejemplo.                                                       *
 * --------------------------------------------------------------------------------------------------------------------- */
#include <iostream>
#include <math.h>

using namespace std;

#define PI 3.141592

int main()
{
	double x = 2.3;

	cout << "Sine value of x=2.3 : " << sin(x*PI/180) << endl;
	cout << "Cosine value of x=2.3 : " << cos(x*PI/180) << endl;
	cout << "Tangent value of x=2.3 : " << tan(x*PI/180) << endl;

	double y = 0.25;

	cout << "Square root value of y=0.25 : " << sqrt(y)
		<< endl;

	int z = -10;

	cout << "Absolute value of z=-10 : " << abs(z) << endl;
	cout << "Power value: x^y = (2.3^0.25) : " << pow(x, y)
		<< endl;

	x = 3.0;
	y = 4.0;

	cout << "Hypotenuse having other two sides as x=3.0 and"
		<< " y=4.0 : " << hypot(x, y) << endl;

	x = 4.56;

	cout << "Floor value of x=4.56 is : " << floor(x)
		<< endl;

	x = -4.57;

	cout << "Absolute value of x=-4.57 is : " << fabs(x)
		<< endl;

	x = 1.0;

	cout << "Arc Cosine value of x=1.0 : " << acos(x)
		<< endl;
	cout << "Arc Sine value of x=1.0 : " << asin(x) << endl;
	cout << "Arc Tangent value of x=1.0 : " << atan(x)
		<< endl;

	y = 12.3;

	cout << "Ceiling value of y=12.3 : " << ceil(y) << endl;

	x = 57.3; // in radians

	cout << "Hyperbolic Cosine of x=57.3 : " << cosh(x)
		<< endl;
	cout << "Hyperbolic tangent of x=57.3 : " << tanh(x)
		<< endl;

	y = 100.0;
	// Natural base with 'e'

	cout << "Log value of y=100.0 is : " << log(y) << endl;

   // Logarithm base 10.
   cout << "Logarithmo base 10 de 6: " << log10(6) << endl;

	return 0;
}









/* ------------------------------------ *
 * Ejemplo de numeros complejos en C++. *
 * ------------------------------------ */

// En este ejemplo definimos un vector de numeros complejos.
#include <iostream>
#include <complex>
#include <vector>
#include <iomanip>

// Creamos tipos de datos tanto para el numero complejo como para el vector de complejos:
using complejo = std::complex<double>;
using plano = std::vector<complejo>;

int main() {
        // Observar como definimos y llenamos (de forma sencilla) el vector de complejos:
        plano planoComplejo = {complejo(3.25, 2.16), complejo(4.218, 5.65)};

        // Activamos la precision para mostrar todos los digitos (parte entera y parte decimal) de cada numero!
        std::cout << std::setprecision(4);

        // Mostramos tanto la parte real como la parte imaginaria de cada numero dentro del vector.
        std::cout << "planoComplejo[0]->parte real: " << std::real(planoComplejo[0]) << "\n";
        std::cout << "planoComplejo[0]->parte imaginaria: " << std::imag(planoComplejo[0]) << "\n";
        std::cout << "planoComplejo[1]->parte real: " << std::real(planoComplejo[1]) << "\n";
        std::cout << "planoComplejo[1]->parte imaginaria: " << std::imag(planoComplejo[1]) << "\n";
        return 0;
}

// Aqui hay otro ejemplo:

#include <iostream>	
#include <complex>	

using namespace std;

int main()
{
   complex<double> v1(2.0, 3.0);   // <---- 2,0 + 3,0j
   complex<double> v2(4.0, 5.0);   // <---- 4,0 + 5,0j
   complex<double> v3(0.0, 0.0);   // <---- 0,0 + 0,0j

   v3 = v1 + v2;

   cout << "v3 =" << v3 << endl;

   
   std::complex<double> mycomplex(10.0, 2.0);

   // Muestra parte real y parte imaginaria de un complejo.
   cout << "Real part: " << real(mycomplex) << endl;
   cout << "Imaginary part: " << imag(mycomplex) << endl;

   return 0;
}







/* ----------------------------------------------------------------------------------------------------- *
 * Ejemplo de LAMBDA en C++.                                                                             *
 *                                                                                                       *
 * IMPORTANTE: Para que una funcion recursiva funcione con LAMBDA se debe compilar en C++14 como minimo, *
 *                                                                                                       *
 *             g++ -std=c++14 xxx.cpp -o xxx                                                             *
 * ----------------------------------------------------------------------------------------------------- */

// Una funcion normal *no recursiva).
auto ADD = [](int x, int y) -> int { return x + y; };

cout << "\n\n\nResultado de lambda ADD 3, 2: " << ADD(3, 2) << endl;


// Ahora veamos una funcion recursiva.
auto fib = [](int x, auto &&fib) -> int { return (!x || x == 1) ? x : fib(x-2, fib) + fib(x-1, fib); };

std::cout << "\n\nfib(x) = " << fib(7, fib) << std::endl;

// Tambien:
// auto lambFib = [](int x, auto &&lambFib) { if (!x || x == 1) return x; return(lambFib(x - 1, lambFib) + lambFib(x - 2, lambFib)); };
// cout << "\n\nlambFib(7) = " << lambFib(7, lambFib) << endl;








/* --------------------------------------------------------------------------------------------------------------------- *
 * Ejemplo de vector de apuntadores a funciones en C++ (usando LAMBDA functions!!!                                       *
 *                                                                                                                       *
 * NOTA IMPORTANTE: Como se vera mas adelante (seccion de javascript), en javascript es mucho mas facil implementar este *
 *                  tipo de areglos de funciones LAMBDA. Por ejemplo,                                                    *
 *                                                                                                                       *
 *                  F = [(x, y) => x+y, (x) => x*x]                                                                      *
 *                                                                                                                       *
 *                  Luego, se puede invocar cada funcion de la siguiente manera (comparar esto con este en C++),         *
 *                                                                                                                       *
 *                  F[0](3, 2) o tambien F[1](4)                                                                         *
 *                                                                                                                       *
 * NOTA IMPORTANTE: Observar que, al momento de invocar cada funcion, el iterador debe seguir esta sintaxis,             *
 *                                                                                                                       *
 *                  (*<nombreIterador>)(<lista de parametros>)                                                           *
 * --------------------------------------------------------------------------------------------------------------------- */
  std::vector<int (*)(int, int)> funciones = {[](int x, int y) { return 2*x; }, [](int x, int y) { return x+y; }};

  //funciones.push_back([](int x, int y) { return 2*x; });
  //funciones.push_back([](int x, int y) { return x+y; });

  // vector<int (*)(int, int)>::iterator fibIt = funciones.begin();
  for(vector<int (*)(int, int)>::iterator i = funciones.begin(); i != funciones.end(); i++)
    std::cout << "\n\nfunciones[0] retorna: " << (*i)(3, 2) << "\n";
  
  // std::cout << "\n\nfunciones[0] retorna: " << funciones[0](3, 0) << "\n";
  // std::cout << "\n\nfunciones[1] retorna: " << funciones[1](3, 2) << "\n";

  // Otro ejemplo de vector de apuntadores a funciones.
  std::vector<int (*)(int, int)> funcTions = {
                                                [](int x, int y) -> int { return x+y; },
                                                [](int x, int y) -> int { std::cout << "mensaje!" << "\n\n"; return 0; },
                                                [](int x, int y) -> int { return x*x; }
                                             };

  for(std::vector<int (*)(int, int)>::iterator i = funcTions.begin(); i != funcTions.end(); i++)
     std::cout << "funcTions[n]: " << (*i)(3, 2) << "\n";









/* ------------------------------------------------------------------------------------------------------- *
 * A partir del C++17 es posible invocar una LAMBDA function de forma anonima en sitio, tal y como se hace *
 * en LISP. Para ello se utiliza "std::invoke" que recibe como argumento el nombre de una funcion          *
 * (o el cuerpo de una LAMBDA function) y sus argumentos respectivos (los de la funcion).                  *
 *                                                                                                         *
 * Con esta libreria tambien es posible crear objetos tipo "function". Instancias de estos objetos pueden  *
 * contener referencias a funciones e incluso a LAMBDA functions y estas instancias pueden incluso         *
 * asignarse a otras instancias (crear una copia de...).                                                   *
 *                                                                                                         *
 * IMPORTANTE: Hay algunos compiladores C++ que requieren el uso de la libreria "functional" mientras que  *
 *             otros no la necesitan para "invoke".                                                        *
 * --------------------------------------------------------------------------------------------------------*/
#include <iostream>
#include <functional>

int main() {
   //
   // En este ejemplo se invoca una LAMBDA function que recibe dos parametros y hace la suma. Inmediatamente se la invoca 
   // y se le pasan dos argumentos!!
   std::cout << "\n\n3 + 2 = " << std::invoke([](int x, int y) -> int { return x+y; }, 3, 2) << "\n\n";


   //
   // Ejemplo de creacion de una instancia del objeto "function" al cual le asignamos una LAMBDA function!
   //
   std::function<int(int)> miFun = [](int x) -> int { return 2*x; };
   //
   // Ahora creamos otra instancia de prueba a la cual le asignaremos la instancia "miFun"!
   std::function<int(int)> segundaF;

   segundaF = miFun;  // Una copia de la instancia "miFun" se copia en la instancia "segundaF"!

   std::cout << "\n\n2*x = " << miFun(3) << "\n\n";

   std::cout << "\n\nsegunda funcion = " << segundaF(8) << "\n\n";   // Ejecutamos la segunda instancia.

   return 0;
}











/* ------------------------------------------------------------------------------------------------------------------------------------ *
 * Ejemplo de LAMBDA function en los algoritmos sort y find_if con iterador. Se declara un vector de int y queremos iniciar el iterador *
 * con el primer elemento del vector cuyo valor sea mayor que 10.                                                                       *
 *                                                                                                                                      *
 * Ejemplo del algorithmo for_each (parecido al de javascript) para aplicar una LAMBDA function a un grupo de elementos.                *
 *                                                                                                                                      *
 * Ejemplo del algoritmo TRANSFORM que cumple misma funcion que MAP en javascript o python.                                             *
 *                                                                                                                                      *
 * Tambien existe una funcion llamada std::plus<tipodedato> que, incluida como ultimo argumento del algoritmo TRANSFORM.                *
 *                                                                                                                                      *
 * NOTA: Es mejor compilar con C++14 o C++17 o C++20,                                                                                   *
 *                                      g++ -std=c++14 main.cpp -o main                                                                 *
 * ------------------------------------------------------------------------------------------------------------------------------------ */
#include <iostream>
#include <algorithm>

// Los elementos de este vector no estan ordenados. Vamos a probar el algoritmo sort sobre el!
vector<int> V = {2, 1, 5, 4, 3, 6, 10, 8, 9, 7, 11, 16, 13, 14, 15, 12, 17, 18, 19, 20};


// Aplicamos el algoritmo sort sobre el vector (usando una LAMBDA function como argumento!).
sort(V.begin(), V.end(), [](int x, int y) -> bool { return x < y; });


// Ahora vamos a mostrar un subconjunto del vector cuyos valores son mayor que 10.
// La funcion que se implementa seria: bool isGt8(int i) { return i > 8; }
// En este ejemplo, dicha funcion la escribimos como una LAMBDA function que se pasa como argumento al algoritmo find_if.
vector<int>::iterator i = find_if(V.begin(), V.end(), [](int i) -> bool { return i > 10; });


// Ahora mostramos el subconjunto con todos los elementos mayores que 10.
// En este for no es necesario iniciar el iterador (ya viene iniciado desde el algoritmo find_if).
for(; i < V.end(); i++) cout << "\n" << *i << endl;

// NOTA: Lo anterior pudiera haber sido implementado sin algoritmo, solo con un while y un if (el vector habria que inicializarlo) de la siguiente manera:

vector<int>::iterator i = V.begin();

# Notar el uso del operador ++ en el iterador.
while(i++ < V.end()) if(*i > 10) cout << "\n" << *i << endl;


// Ejemplo de uso del algorithmo for_each que invoca una LAMBDA function.
std::vector<int> V = {1, 2, 3, 4, 5 ,6, 7, 8};
std::for_each(V.begin(), V.end(), [](int x) -> void { std::cout << x << "\n"; });


// Ejemplo del algorithmo TRANSFORM. Cumple la misma funcion que MAP en javascript y python!!
auto unary_op = [](int num) {return std::pow(num, 2);};   // Definimos una funcion que se aplicara a cada elemento del vector.

// Debe indicar: a) inicio del array o vector, b) fin del array o vector y c) objeto donde se almacenara el array o vector modificado.
std::transform(V.begin(), V.end(), V.begin(), unary_op);   // TRANSFORM equivalente a MAP.

cout << "\n\nV luego del algoritmo transform:\n";
for (vector<int>::iterator i = V.begin(); i < V.end(); i++) cout << *i << ", ";


// Ejemplo del uso de la funcion std::plus<xxxx> dentro del algoritmo transform para sumar los elementos de dos arrays (pudiera hacerse con vectores)!!!!
// C++ program to illustrate std::plus 
// by adding the respective elements of 2 arrays 
#include <iostream> // std::cout 
#include <functional> // std::plus 
#include <algorithm> // std::transform 

int main() 
{ 
	// First array 
	int first[] = { 1, 2, 3, 4, 5 }; 

	// Second array 
	int second[] = { 10, 20, 30, 40, 50 }; 

	// Result array 
	int results[5]; 

	// std::transform applies std::plus to the whole array 
	std::transform(first, first + 5, second, results, std::plus<int>()); 

	// Printing the result array 
	for (int i = 0; i < 5; i++) 
		std::cout << results[i] << " "; 

	return 0; 
} 







/* -------------------------------------------------------------------------------------------------------- *
 * A continuacion unos ejemplos de algoritmos C++ que utilizan LAMBDA expressions. Tomado de GeeksforGeeks! *
 * -------------------------------------------------------------------------------------------------------- */

// Function to print vector
void printVector(vector<int> v)
{
	// lambda expression to print vector
	for_each(v.begin(), v.end(), [](int i)
	{
		std::cout << i << " ";
	});
	cout << endl;
}

int main()
{
	vector<int> v {4, 1, 3, 5, 2, 3, 1, 7};

	printVector(v);

	// below snippet find first number greater than 4
	// find_if searches for an element for which
	// function(third argument) returns true
	vector<int>:: iterator p = find_if(v.begin(), v.end(), [](int i)
	{
		return i > 4;
	});
	cout << "First number greater than 4 is : " << *p << endl;


	// function to sort vector, lambda expression is for sorting in
	// non-increasing order Compiler can make out return type as
	// bool, but shown here just for explanation
	sort(v.begin(), v.end(), [](const int& a, const int& b) -> bool
	{
		return a > b;
	});

	printVector(v);

	// function to count numbers greater than or equal to 5
	int count_5 = count_if(v.begin(), v.end(), [](int a)
	{
		return (a >= 5);
	});
	cout << "The number of elements greater than or equal to 5 is : "
		<< count_5 << endl;

	// function for removing duplicate element (after sorting all
	// duplicate comes together)
	p = unique(v.begin(), v.end(), [](int a, int b)
	{
		return a == b;
	});

	// resizing vector to make size equal to total different number
	v.resize(distance(v.begin(), p));
	printVector(v);

	// accumulate function accumulate the container on the basis of
	// function provided as third argument
	int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int f = accumulate(arr, arr + 10, 1, [](int i, int j)
	{
		return i * j;
	});

	cout << "Factorial of 10 is : " << f << endl;

	//	 We can also access function by storing this into variable
	auto square = [](int i)
	{
		return i * i;
	};

	cout << "Square of 5 is : " << square(5) << endl;
}









/* ---------------------------------------------------------------------- *
 * Sobre los apuntadores y arreglos y arreglos de apuntadores a funcion!! *
 * ---------------------------------------------------------------------- */
MIRAR ESTA EXPLICACION tomada de : 
https: // stackoverflow.com/questions/5093090/whats-the-syntax-for-declaring-an-array-of-function-pointers-without-using-a-se

arr               // arr
arr[]             // is an array (so index it)
*arr[]            // of pointers (so dereference them)
(*arr[])()        // to functions taking nothing (so call them with ())
void (*arr[])()   // returning void

so your answer is

void (*arr[])() = {};

But naturally, this is a bad practice, just use typedefs :)

Extra: Wonder how to declare an array of 3 pointers to functions taking int and returning a pointer 
       to an array of 4 pointers to functions taking double and returning char? (how cool is that, huh? :))

arr                                       //arr
arr [3]                                   //is an array of 3 (index it)
* arr [3]                                 //pointers
(* arr [3])(int)                          //to functions taking int (call it) and
*(* arr [3])(int)                         //returning a pointer (dereference it)
(*(* arr [3])(int))[4]                    //to an array of 4
*(*(* arr [3])(int))[4]                   //pointers
(*(*(* arr [3])(int))[4])(double)         //to functions taking double and
char  (*(*(* arr [3])(int))[4])(double)   //returning char











/* ----------------------------------------------------------------------------------------- *
 * Ejemplo de hilos (threads) en C++.                                                        *
 *                                                                                           *
 * IMPORTANTE: Para compilar este programa,                                                  *
 *                                                                                           *
 * g++ -std=c++14 thread.cpp -o thread                                                       *
 *                                                                                           *
 * A partir del c++11 no es necesario incluir el parametro -pthread en el compilador.        *
 *                                                                                           *
 * IMPORTANTE: el metodo "join" es necesario para que el thread funcione y no de error.      *
 * ----------------------------------------------------------------------------------------- */
#include <iostream>
#include <thread>

using namespace std;


// A dummy function
void foo(int Z)
{
	for (int i = 0; i < Z; i++) { cout << "Thread using function" " pointer as callable\n"; }
}

// A callable object
class thread_obj {
public:
	void operator()(int x)
	{
		for (int i = 0; i < x; i++) cout << "Thread using function" " object as callable\n";
	}
};

// class definition
class Base {
public:
	// non-static member function
	void foo()
	{
		cout << "Thread using non-static member function " "as callable" << endl;
	}
	// static member function
	static void foo1()
	{
		cout << "Thread using static member function as " "callable" << endl;
	}
};

// Driver code
int main()
{
	cout << "Threads 1 and 2 and 3 " "operating independently" << endl;

	// This thread is launched by using
	// function pointer as callable
	thread th1(foo, 3);

	// This thread is launched by using
	// function object as callable
	thread th2(thread_obj(), 3);

	// Define a Lambda Expression
	auto f = [](int x) {
		for (int i = 0; i < x; i++) cout << "Thread using lambda" " expression as callable\n";
	};

	// This thread is launched by using
	// lambda expression as callable
	thread th3(f, 3);

	// object of Base Class
	Base b;

	thread th4(&Base::foo, &b);

	thread th5(&Base::foo1);

	// Wait for the threads to finish
	// Wait for thread t1 to finish
	th1.join();

	// Wait for thread t2 to finish
	th2.join();

	// Wait for thread t3 to finish
	th3.join();

	// Wait for thread t4 to finish
	th4.join();

	// Wait for thread t4 to finish
	th5.join();

	return 0;
}



Salida del programa:
Threads 1 and 2 and 3 operating independently
Thread using lambda expression as callable
Thread using lambda expression as callable
Thread using lambda expression as callable
Thread using static member function as callable
Thread using non-static member function as callable
Thread using function pointer as callable
Thread using function pointer as callable
Thread using function pointer as callable
Thread using function object as callable
Thread using function object as callable
Thread using function object as callable










/* -------------------------------------------------------------------- *
 * Ejemplo de uso de argumentos desde la linea de comandos del sistema. *
 * Se muestran dos ejemplos: uno en C++ usando vectores y otro en C     *
 * standard usando un array.                                            *
 *                                                                      *
 * NOTA: En C++ la funcion main tiene dos argumentos: el primero es un  *
 *       contador de argumentos y el segundo es un string que contiene  *
 *       la lista de argumentos terminada en "0":                       *
 *                                                                      *
 *       ...>programa argu1 argu2                                       *
 *                                                                      *
 *       Dentro del programa: int main(int argc, char* argv[]), donde   *
 *       argc cuenta toda la linea incluido el nombre del programa.     *
 *       Es decir, la lista de argumentos comienza en argv[1].          *
 * -------------------------------------------------------------------- */

// EJEMPLO EN C++ USANDO VECTORES:
#include<iostream>
#include<vector>

using namespace std;

// Descompone la lista de argumentos que viene desde la linea de comandos.
vector<string> procArgs(int argc, char* argv[])
{
	vector<string> args;

	for(int i = 0; i != argc; i++) args.push_back(argv[i]); return(args);
}

int main(int argc, char* argv[])
{
	vector<string> parametros;   // Incluira la lista de parametros.

	// Descarta cuando el usuario invoca el programa pero sin parametros.
	if(argc > 1) parametros = procArgs(argc, argv);   // Llena un vector con los parametros al programa.

	// Muestra en pantalla los parametros leidos desde la linea de comandos, exceptuando el nombre del propio programa (argv[0]).
	cout << endl << "Lista de parametros indicados por el usuario:" << endl << endl;
	for(vector<string>::iterator i = parametros.begin() + 1; i != parametros.end(); i++) cout << *i << endl;
}


// EJEMPLO EN C STANDARD USANDO UN ARRAY Y APUNTADORES:
#include<stdio.h>

int main(int argc, char* argv[])
{
	char* parametros[10];   // Contendra la lista de parametros.

	// Descarta cuando el usuario invoca el programa pero sin parametros.
	if(argc > 1)
	{
		for(int i = 1; i < argc; i++) parametros[i] = *++argv;

	    // Muestra en pantalla los parametros leidos desde la linea de comandos, exceptuando el nombre del propio programa (argv[0]).
		printf("Parametros leidos: \n");
		for(int i = 1; i < argc; i++) printf("%s\n", parametros[i]);
	}
}





/* ---------------------------------------------------------------------------------------- *
 * Ejemplo de apuntador a funcion en C++.                                                   *
 *                                                                                          *
 * NOTA: En C++ puede declararse igual que en C estandar. Tambien puede hacerse con "auto". *
 * ---------------------------------------------------------------------------------------- */
int fun(int parX, int parY) { return (parX + parY); }

auto ptrFun = &fun;

cout << "\n\nptrFun(2, 3) = " << ptrFun(2, 3) << endl;





/* ---------------------------------------------------- *
 * Ejemplo de apuntador a funcion miembro de una clase! *
 * ---------------------------------------------------- */

// Las siguientes clases son solo de ejemplo!
class base {
  virtual int miFuncion(int x, int y) = 0;
};

class primeraDerivada : public base {
public:
  primeraDerivada(int iniX, int iniY) {
    x = iniX;
    y = iniY;
  }
  int miFuncion(int parX, int parY) {
    x = parX;
    y = parY;
    return (x + y);
  }

protected:
  int x;
  int y;
};

// Este es un ejemplo de paso de apuntador a funcion miembro de una clase a una funcion normal.
// IMPORTANTE notar que es necesario pasar tambien un apuntador a la clase!!
// Luego, la invocacion de esta funcion se haria de la siguiente manera,
//
// func002(3, 2, &segundaInstancia, &primeraDerivada::miFuncion)
//
int func002(int a, int b, primeraDerivada *P, int (primeraDerivada::*f)(int, int)) {
   return((P->*f)(a, b));
}


int main() {
  primeraDerivada segundaInstancia(0, 0);   // Se instancia la clase ejemplo.

  //primeraDerivada *ptrDerivada;

  //int (primeraDerivada::*funcPtr)(int, int);
  //auto funcPtr = segundaInstancia.miFuncion(3, 2);

  //cout << "\n\n\n\nfuncPtr(3, 2) = " << funcPtr << "\n\n\n" << endl;
  //cout << "\n\n\n\nfuncPtr(3, 2) = " << (ptrDerivada->*funcPtr)(3, 2) << "\n\n\n" << endl;
  //cout << "\n\n\n\nfuncion(3, 2) = " << func002(3, 2, &segundaInstancia, &primeraDerivada::miFuncion) << "\n\n\n" << endl;


  // Se define un apuntador a la clase y se inicia con la direccion de la instancia creada arriba.
  primeraDerivada *P = &segundaInstancia;

  // Creamos el apuntador a funcion, indicando que lo apuntado es un miembro de la clase primeraDerivada. Luego, asignamos 
  // la direccion de la funcion miembro miFuncion!!
  int (primeraDerivada::*f)(int, int) = &primeraDerivada::miFuncion; 

  // Invocamos la funcion apuntada (P->*f)!!
  cout << "\n\n\napuntadorMiembro(3, 2) = " <<  (P->*f)(3, 2) << "\n\n\n" << endl;

  return (0);
}







/* --------------------------------------------------------------------------- *
 * Ejemplo de uso del ternary operator de C: condicion ? statement : statement *
 * --------------------------------------------------------------------------- */
int miFib(int x) { return((x == 0 || x == 1) ? x : (miFib(x - 1) + miFib(x - 2))); }





/* ----------------------------------------------------------- *
 * Ejemplo de apuntador a estructura en C y su arrow operator. *
 * ----------------------------------------------------------- */
// Declaramos primero un tipo estructura de ejemplo.
typedef struct {
   int i;
   int j;
} prueba;

int main() {
   prueba estPrueba;   // Creamos una variable con el tipo de estructura de ejemplo.

   prueba *apuntador;   // Ahora creamos un apuntador al tipo de estructura de ejemplo.

   apuntador = &estPrueba;   // Asignamos la direccion de la variable creada.

   // Ejemplo del operador arrow.
   apuntador->i = 5; apuntador->j = 7;

   printf("\n\ni:%d, j:%d\n\n", apuntador->i, apuntador->j);


   return(0);
}






/* ------------------------------------- *
 * Ejemplo de una pure virtual function. *
 * ------------------------------------- */
class base {
   virtual int miFuncion(int x, int y) = 0;
};

class primeraDerivada : public base {
public:
   primeraDerivada(int iniX, int iniY) { x = iniX; y = iniY; }
   int miFuncion(int parX, int parY) { x += parX; y += parY; return(x + y); }

protected:
   int x;
   int y;
};


class segundaDerivada : public base {
public:
   segundaDerivada(int iniZ, int iniK) { z = iniZ; k = iniK; }
   int miFuncion(int parX, int parY) { return(parX - parY); }

protected:
   int z;
   int k;
};

int main() {

   // Instanciamos la clase derivada (en la cual se implementa la pure virtual function).
   primeraDerivada primeraInstancia(3, 2);

   cout << "primeraInstancia.miFuncion: " << primeraInstancia.miFuncion(10, 20) << endl;

   return(0);
}






/* ------------------------------------------------------------------ *
 * Ejemplo de una aplicacion conformada por mas de un archivo fuente. *
 * Para invocar una funcion definida en un fuente A desde un fuente   *
 * B, es buena practica usar un header file (.h) en el cual se declara*
 * la funcion a ser usada por varios fuentes. A continuacion se da el *
 * ejemplo de dos fuentes (uno principal con la funcion main) y el    *
 * otro conteniendo la definicion de la funcion. En el header file se *
 * coloca la declaracion de dicha funcion y se coloca, ademas, una    *
 * proteccion (basada en #ifndef) para que la funcion no sea declarada*
 * en mas de un fuente. Veamos el ejemplo:                            *
 *                                                                    *
 * IMPORTANTE: Mirar tambien el ejemplo de modulos multiples en la    *
 *             aplicacion GestFlota (se hace referencia a esta en     *
 *             la seccion Lenguaje C arriba.)                         *
 * ------------------------------------------------------------------ */

 // FUENTE DONDE SE DEFINE LA FUNCION:
 #include<iostream>
#include "comun.h"

using namespace std;


void imprime()
{
	cout << "Mensaje desde stros2.cpp" << endl;
}

// HEADER FILE comun.h (conteniendo la declaracion de la funcion a ser usada por todos los fuentes):
#ifndef COMUN_H   // Asegura que la funcion se declara en un solo sitio.
#define COMUN_H

void imprime();

#endif

// FUENTE PRINCIPAL (con la funcion main y desde el cual se invoca la funcion):
#ifndef COMUN_H   // Verifica si la funcion esta declarada en algun otro fuente.
void imprime();
#endif

#include "comun.h"

using namespace std;

int main() 
{
    imprime();

    return 0;
}




/* ------------------------------------------------------------- *
 * Ejemplo de estructura con su constructor y funciones miembro. *
 * ------------------------------------------------------------- */

// NOTA: La struct es como una class en la cual todos sus miembros son public.
struct compleja
{
	int campo1;
	int campo2;

    // Constructor.
	compleja(int parm1, int parm2) { campo1 = parm1; campo2 = parm2; }

	// Funciones miembro.
	void funcion1(int parm1) { campo1 = (parm1 + 50) * 100; }
	void funcion2(int parm2) { campo2 = (parm2 + 36) * 10; }
};

void main()
{
    compleja complejidad(0, 0);   // Al declarar esta "instancia" se ejecuta el Constructor e inicia los campos del Struct.

	cout << "Antes de... campo1 = " << complejidad.campo1 << " y atributo2 = " << complejidad.campo2 << endl;
	complejidad.funcion1(20);   // Invoca las funciones miembro.
	complejidad.funcion2(80);
	cout << "Despues de... campo1 = " << complejidad.campo1 << " y campo2 = " << complejidad.campo2 << endl;
}



/* ------------------------------------------------------------------------------------------------------- *
 * Ejemplo de Template Class con sus constructores, miembros y sobrecarga de operadores. Se crea una clase *
 * vector 2-dimensional (como un par ordenado) equipado con dos operaciones basicas: adicion de vectores y *
 * producto de un vector por un escalar. Tambien, se crea una Template Class representando a una Matriz,   *
 * en la cual cada fila esta representada por una Template Class de vector 2-dimensional (la clase matriz  *
 * hereda la clase vector).                                                                                *
 *                                                                                                         *
 * NOTA: Al usar la sobrecarga de operadores es importante que, al momento de realizar alguna sentancia    *
 *       que involucre dicho operador, el primer operando de la expresion DEBE ser de la misma clase que   *
 *       el objeto. Ejemplo, suponiendo que hacemos un producto escalar por un vector, la siguiente        *
 *       sentencia producira un error de compilacion:                                                      *
 *                                                                                                         *
 *       vector = 3 * vector;                                                                              *
 *                                                                                                         *
 *       Esto se debe a que el compilador analiza la sentencia de izquierda a derecha y, al encontrar un   *
 *       elemento distinto al tipo del objeto (en el lado izquierdo a la igualdad), indicara que no son    *
 *       del mismo tipo. Lo correcto es colocar primero el operando del mismo tipo del resultado,          *
 *                                                                                                         *
 *       vector = vector * 3;                                                                              *
 *                                                                                                         *
 * NOTA: La notacion de Templates Class en C++ puede ser algo engorrosa. En este ejemplo, cuando la clase  *
 *       matrix hereda la clase parOr; dado que la clase parOr es Template Class, la clase matrix tambien  *
 *       debe ser una Template Class e incluir el tipo template T y hacer template sus tipos internos.     *
 *       Este es un tema de investigacion y lo tengo en curso.                                             *
 * ------------------------------------------------------------------------------------------------------- */
#include<iostream>
#include<vector>

using namespace std;

/* ----------------------------------------------------------------------------------- *
 * Vector 2-dimensional                                                                *
 *                                                                                     *
 * Cumple con las reglas de suma de vectores y producto de un escalar por un vector,   *
 * (x1,y1) + (x2,y2) = (x1+x2,y1+y2)                                                   *
 * c(x1,x2) = (cx1,cx2)                                                                *
 *                                                                                     *
 * Tambien aplican las propiedades del algebra vectorial,                              *
 * α + β = β + α , α + (β + ϒ) = (α + β) + ϒ                                           *
 * c(α + β) = cα + cβ , 1α = α                                                         *
 * ----------------------------------------------------------------------------------- */
template <typename T> class parOr
{
	private:
		// Atributos.
		T dummx;   // Atributos dummy para la suma de vectores. Evitan que las componentes del vector sean alteradas.
		T dummy;
		T x;       // Componente x.
		T y;       // Componente y.
	public:
		// Constructores.
		parOr() : x(0), y(0), dummx(0), dummy(0) {}                          // Usado cuando no se especifican parametros.
		parOr(T inix, T iniy) : x(inix), y(iniy), dummx(0), dummy(0) {}  // Usado cuando se especifican parametros.

		// Funciones miembro.
		void setPar(T valx, T valy) { x = valx; y = valy; }                   // Nuevos valores para las componentes.
		void showPar() { cout << "(x,y) = (" << x << "," << y << ")" << endl; }   // Muestra el par ordenado.
		T getx() { return(x); }                                                 // Obtiene componente x.
		T gety() { return(y); }                                                 // Obtiene componente y.

		// Suma de vectores y producto de un escalar por un vector.
    	parOr operator + (parOr oper) { dummx = x + oper.x; dummy = y + oper.y; return(parOr(dummx, dummy)); }
    	parOr operator * (T scalar) { x *= scalar; y *= scalar; return(parOr(x, y)); }
};

/* ----------------------------------------------- *
 * Matriz 2x2 basada en la clase Vector parOr.     *
 *                                                 *
 * Cada fila corresponde a un elemento tipo parOr  *
 * que se indica en la instanciacion.              *
 * ----------------------------------------------- */
template <typename T, typename P> class matrix : public parOr<T>
{
	private:
		// Atributos.
		vector<P> row1;   // Primera fila [a11 a12].
		vector<P> row2;   // Segunda fila [a21 a22].
	public:
        // Constructores.

		// Funciones miembro.
        void setMat(P row1In, P row2In) { row1.push_back(row1In); row2.push_back(row2In); }
        void showMat() { cout << "= [" << row1[0].getx() << " " << row1[0].gety() << "]" << endl; cout << "  [" << row2[0].getx() << " " << row2[0].gety() << "]" << endl; }
};

int main()
{
	// Cuatro vectores de ejemplo.
	parOr<double> vec1;
	parOr<double> vec2(2.3, 3.5);
	parOr<double> vec3(5.0, 5.6);
	parOr<double> vec4(8.2, 4.8);

	// Matriz de ejemplo.
	matrix<double, parOr<double>> matriz;

	matriz.setMat(vec2, vec3);
	matriz.showMat();

	cout << "Al inicio:" << endl << "---------" << endl; 
	cout << "vec1 ---> "; vec1.showPar(); cout << endl; 
	cout << "vec2 ---> "; vec2.showPar(); cout << endl;
	cout << "vec3 ---> "; vec3.showPar(); cout << endl;
	cout << "vec4 ---> "; vec4.showPar(); cout << endl;

	vec1 = (vec2 + vec4) + vec3;   // Asociativa de la adicion.

	cout << "Luego de vec1 = (vec2 + vec4) + vec3: " << endl << "---------------------------" << endl; 
	cout << "vec1 ---> "; vec1.showPar(); cout << endl; 
	cout << "vec2 ---> "; vec2.showPar(); cout << endl;
	cout << "vec3 ---> "; vec3.showPar(); cout << endl;
	cout << "vec4 ---> "; vec4.showPar(); cout << endl;

	vec3 = vec3 * 1;   // Elemento neutro de la multiplicacion.

	cout << "Luego de vec3 = 1 * vec3: " << endl << "---------------------------" << endl; 
	cout << "vec1 ---> "; vec1.showPar(); cout << endl; 
	cout << "vec2 ---> "; vec2.showPar(); cout << endl;
	cout << "vec3 ---> "; vec3.showPar(); cout << endl;

	vec1 = vec2 + vec3;

	cout << "Luego de vec1 = vec2 + vec3: " << endl << "---------------------------" << endl; 
	cout << "vec1 ---> "; vec1.showPar(); cout << endl; 
	cout << "vec2 ---> "; vec2.showPar(); cout << endl;
	cout << "vec3 ---> "; vec3.showPar(); cout << endl;

	vec2 = vec2 + vec3;

	cout << "Luego de vec2 = vec2 + vec3: " << endl << "---------------------------" << endl; 
	cout << "vec1 ---> "; vec1.showPar(); cout << endl; 
	cout << "vec2 ---> "; vec2.showPar(); cout << endl;
	cout << "vec3 ---> "; vec3.showPar(); cout << endl;

	return(0);
}



/* ------------------------------------------------------- *
 * Ejemplo de uso de dos iteradores sobre un mismo vector. *
 * ------------------------------------------------------- */
typedef vector<contrato>::iterator IterSIX;

IterSIX k = vecSIX.begin();
IterSIX m = vecSIX.begin();

for(; k != vecSIX.end(); k++, m++) { // bloque de sentencias. }




/* ----------------------------------------------------------------------------------- *
 * C++ permite la sobrecarga de funciones (no confundir con sobrecarga de operadores). *
 * Con esta facilidad varias funciones pueden tener el mismo nombre. Hay que tener     *
 * cuidado con esto porque un programador desordenado puede darle un mismo nombre      *
 * a varias funciones y luego no informar a su equipo de trabajo. En aplicaciones muy  *
 * grandes un programador pudiera usar una funcion equivocada si solo se guia por el   *
 * nombre de la funcion.                                                               *
 * ----------------------------------------------------------------------------------- */
int plusFunc(int x, int y) {
  return x + y;
}

double plusFunc(double x, double y) {
  return x + y;
}

int main()
{

  int myNum1 = plusFunc(8, 5);
  double myNum2 = plusFunc(4.3, 6.26);
  cout << "Int: " << myNum1 << "\n";
  cout << "Double: " << myNum2;
  return(0);
}



/* ---------------------------------------------------------- *
 * Ejemplo de uso de la libreria rapidJson en un programa C++ *
 * para el procesamiento de streams JSON.                     *
 * Tomada de:                                                 *
 *            https://github.com/Tencent/rapidjson/           *
 *                                                            *
 * NOTA: La carpeta rapidjason (conteniendo todos los .h) se  *
 *       se debe colocar en el mismo directorio del fuente o  *
 *       incluirla en el PATH.                                *
 * ---------------------------------------------------------- */
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>

using namespace rapidjson;

int main() 
{
    // 1. Parse a JSON string into DOM.
    const char* json = "{\"project\":\"rapidjson\",\"stars\":10}";

    Document d;

    d.Parse(json);

    // 2. Modify it by DOM.
    Value& s = d["stars"];

    s.SetInt(s.GetInt() + 1);

    // 3. Stringify the DOM
    StringBuffer buffer;

    Writer<StringBuffer> writer(buffer);

    d.Accept(writer);

    // Output {"project":"rapidjson","stars":11}
    std::cout << buffer.GetString() << std::endl;

    return 0;
}



/* ------------------------------------------------------- *
 * Ejemplo de lanzamiento de una pagina WEB HTML desde C++ *
 * ------------------------------------------------------- */
int comando = system("start firefox jsontest.html");





# ---------------------------------------------------------- #
# Programa que muestra como usar un apuntador a una funcion. #
# ---------------------------------------------------------- #
#include<iostream>

// Al incluir la siguiente sentencia se evita tener que colocar el prefijo "std::..." en los metodos "cout" y "cin".
use namespace std;

/* ----------------------------------------------------------------------------------- */
/* Calcula el numero Fibonnaci correspondiente a un numero introducido por el usuario. */
/*                                                                                     */
/* La formula de recurrencia es:                                                       */
/*                               F  =  0                ,  n = 0                       */
/*                                0                                                    */
/*                               F  =  1                ,  n = 1                       */
/*                                1                                                    */
/*                               F  =  F    +   F       , n >= 2                       */
/*                                n     n-1      n-2                                   */
/* ----------------------------------------------------------------------------------- */
int fib(int n) { if(n == 0 || n == 1) return(n); return(fib(n - 1) + fib(n - 2)); }


int prueba_case(int valor)
{
	int salida = 1;

	switch(valor)
	{
		case 2:
				salida *= valor;
				break;
		case 4:
				salida = valor * 500;
				break;
		case 7:
				salida += valor;
				break;
		case 10:
				salida = valor / 2;
				break;
		default:
				salida = 1;
	}

	return(salida);
}


int main()
{
    int opcion  = 0;
	int valorIn = 0;
	int fibIn   = 0;

	// Se declara un apuntador a un objeto tipo funcion.
	int (* funcion) (int);

	while(opcion != 3)
	{
		cout << "\n\n          PRUEBAS CON C++\n" <<               \
		        "-------------------------------------------\n"    \
		        "1.- Prueba de switch...case\n" <<                 \
		        "2.- Genera el Fibonnaci de cualquier numero\n" << \
		        "3.- Salir\n\n" <<                                 \
		        "Indique el numero de su eleccion: "; cin >> opcion;

		switch(opcion)
		{
			case 1:   funcion = prueba_case;   // Asigna la direccion de la funcion "prueba_case".
			          cout << "\n\nIntroduzca el valor del case: "; cin >> valorIn;
	                  cout << "\n\n Valor devuelto: " << funcion(valorIn);  // Invoca usando el apuntador a funcion.
			          break;

			case 2:   funcion = fib;           // Asigna la direccion de la funcion "fib".
				      cout << "\n\nIntroduzca el numero: "; cin >> fibIn;
		              cout << "\n\n El fibonaci correspondiente es:" << funcion(fibIn);  // Invoca usando el apuntador a funcion.
	                  break;

	        case 3:
	                  break;
			default:
	                  break;
		}
    }

	return(0);
}









/* ------------------------------------------------------------------------------------------------------------- *
 * Ejemplos de operaciones en BINARIO y el uso de la libreria "bitset* para imprimir valores en formato binario! *
 * ------------------------------------------------------------------------------------------------------------- */
#include <bitset>

#define c 5

int main() {
   unsigned int N = 2;

   std::cout << "\nN = " << N << "\n";
   N = N << 1;
   std::cout << "\nN = " << N << "\n";

   // Ejemplo de and binario!
   if(N & c) std::cout << "\nEs distinto de cero!\n"; else std::cout << "\nEs cero!\n";

   // Ejemplo de uso de la libreria "bitset" de C++.
   std::cout << "N en binario: " << std::bitset<8>(N) << " y c en binario: " << std::bitset<8>(c) << "\n";

   return 0;
}

// Salida:
N = 2

N = 4

Es distinto de cero!
N en binario: 00000100 y c en binario: 00000101



// Otro ejemplo:
std::bitset<4> b1(std::string("0001"));
std::cout << "\nb1 = " << b1 << "\n";

// Salida:
b1 = 0001

// OBSERVAR como bitset acepta un valor en formato string
bitset<4> b1 (string("0101"));
bitset<4> b2 (string("0011"));
bitset<4> b3 = b1 & b2;        // <---- Operacion binaria AND!!

std::cout << "bitset 1: " << b1;
std::cout << "bitset 2: " << b2;
std::cout << "bitset 3: " << b3;


# --------------------------------------------------------------------------- #
# Uso de INLINE ASSEMBLY dentro de un programa C++                            #
#                                                                             #
# Es posible incluir instrucciones en ASSEMBLER dentro de un programa usando  #
# la sentancia asm(...). Incluso, es posible leer y escribir en variables de  #
# programa C++ en el assembler. A continuacion un ejemplo de uso:             #
# --------------------------------------------------------------------------- #

// Ejemplo de uso de la instruccion ADDL:
 int unidad = 1, z = 50;
 38         __asm__ ("ADDL %%EBX, %%EAX" : "=a" (z) : "a" (unidad), "b" (z));
 39         std::cout << "\nLuego del inline assembly Z = " << z << "\n";


// Otro ejemplo:
#include <stdio.h>

//
// En este ejemplo esta escrito en C standard (no en C++), pero pudiera escribirse en C++ sin mayor esfuerzo.
//

int gcd( int a, int b ) 
{
    int result;

    /* Compute Greatest Common Divisor using Euclid's Algorithm */
    __asm__ __volatile__ ( "MOVL   %1, %%EAX;"
                           "MOVL   %2, %%EBX;"
                    "CONTD: CMPL   $0, %%EBX;"
                           "JE     DONE;"
                           "XORL   %%EDX, %%EDX;"
                           "IDIVL  %%EBX;"
                           "MOVL   %%EBX, %%EAX;"
                           "MOVL   %%EDX, %%EBX;"
                           "JMP    CONTD;"
                    "DONE:  MOVL   %%EAX, %0;" : "=g" (result) : "g" (a), "g" (b)
    );

    /*
     * En la sentencia anterior (la cual pudiera escribirse tambien como as(...)) los parametros a la funcion gcd y las variables 
     * locales pueden usarse dentro de la pieza de codigo assembler usando "=g" (que significa llenar la variable con el valor...)
     * y "g" (que significa llenar algun registro de la CPU con el contenido de las variables...). Notar que, incluso, pueden usarse 
     * etiquetas para las instrucciones condicionales y de salto. El nombre de los registros deben contener el prefijo "%%". Los 
     * indicadores "%1", "%2", etc. son los registros intermedios que utiliza "asm" para cargar valores que vienen desde las variables 
     * del programa C++.
     */

    return result;
}

int main()
{
    int first, second;


    printf("Enter two integers: ");
    scanf("%d%d", &first, &second);
    printf("GCD of %d & %d is %d\n", first, second, gcd(first, second));

    return 0;
}

#
# Y aqui esta el codigo assembler generado por el compilador C++ (de la funcion gcd):
#
_Z3gcdii:
.LFB15:
        PUSHQ	%RBP
        MOVQ    %RSP, %RBP
        SUBQ    $16, %RSP
        MOVL    %ECX, 16(%RBP)
        MOVL    %EDX, 24(%RBP)
/APP
 # 22 "EUCLID.CPP" 1
        MOVL   16(%RBP), %EAX;
        MOVL   24(%RBP), %EBX;
 CONTD: CMPL   $0, %EBX;
        JE     DONE;
        XORL   %EDX, %EDX;
        IDIVL  %EBX;
        MOVL   %EBX, %EAX;
        MOVL   %EDX, %EBX;
        JMP    CONTD;
 DONE:  MOVL   %EAX, %EAX;
 # 0 "" 2
/NO_APP
        MOVL    %EAX, -4(%RBP)
        MOVL    -4(%RBP), %EAX
        ADDQ    $16, %RSP
        POPQ    %RBP
        RET


/* ---------------------------------------------------------------------- *
 * Funciones de comparacion, copia y longitud de strings en C estandard.  *
 *                                                                        *
 * NOTA: Estas funciones fueron escritas en 1992-93 y corregidas en 2020. *
 * ---------------------------------------------------------------------- */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Copia un string origen sobre otro destino.
//
// NOTA: Tiene un detalle: ejecutar este programa y ver el detalle. Pendiente por resolver!
void s_copy(const char *origen, char *destino) 
{ 
   while((*destino++ = *origen++) != 0) { ; }
}

// Determina la longitud de un string.
int s_leng(char *str)
{
   register int indice = 0;

   for(; str[indice]; indice++); return indice;
}

// Compara dos strings.
//
// Salida: 0 ---> son iguales
//         1 ---> son diferentes
//
int s_comp(register char *a,register char *b) 
{
   int i = 0, j = 0, a_leng = s_leng(a), b_leng = s_leng(b);

   for(; *a++ == *b++; i++, j++); if(i >= a_leng && j >= b_leng) return 0; return 1;
}

int main()
{
    char nombre[]  = "Jose Maria";
    char destino[] = "Jose";

    s_copy(nombre, destino);   // Copia el string nombre hacia el string destino.

    //nombre = (char *) malloc(15);   // Prueba de malloc.

    //strcpy(nombre, "Jose Maria");   // Prueba de string copy usando la libreria standard de C.

    printf("Nombre: %s y destino: %s , longitud de Nombre: %u , igualdad: %s\n", nombre, destino, s_leng(nombre), (!s_comp(nombre, destino)? "son iguales" : "son diferentes"));
}



/* -------------------------------------------------- *
 * Ejemplo de calculo de DIFERENCIA entre dos FECHAS. *
 * Muy util para calcular el TIEMPO DE EJECUCION.     *
 * -------------------------------------------------- */
#include<iostream>
#include<ctime>

using namespace std;

// Crea una estructura tm representando una fecha especifica.
tm make_tm(int year, int month, int day)
{
    tm tm = {0};
    tm.tm_year = year - 1900; // contador desde el agno 1900.
    tm.tm_mon = month - 1;    // Contador de meses desde Enero = 0.
    tm.tm_mday = day;         // Contador de dias desde 1.
    return tm;
}

int main()
{
	/* -------------------------------------------------- *
	 * Prueba de diferencia entre dos fechas especificas. *
	 * -------------------------------------------------- */

	// Fecha inicio y Fecha fin para comparar.
	tm fecini = make_tm(2020,11,30);
	tm fecfin = make_tm(2020,12,02);

	// En un sistema POSIX, devuelve el conteo de segundos desde el dia 1ro de Enero de 1970 - 00:00:00 UTC.
	time_t time1 = mktime(&fecini);
	time_t time2 = mktime(&fecfin);

	// Divide entre un dia (expresado en segundos).
	const int seconds_per_day = 60*60*24;
	time_t fecdif = (time2 - time1) / seconds_per_day;

	// Muestra diferencia en # de dias.
	cout << "La diferencia (en dias) fecfin - fecini = " << fecdif << endl;

	// To be fully portable, we shouldn't assume that these are Unix time;
	// instead, we should use "difftime" to give the difference in seconds:
	double portable_difference = difftime(time1, time2) / seconds_per_day;

	return(0);
}




/* --------------------------------------------------------------------------- */
/* Ejemplo de uso del metodo std::sort para ordenar los elementos de un array. */
/*                                                                             */
/* NOTA IMPORTANTE: Este metodo espera dos parametros como minimo. El primer   */
/*                  parametro indica la posicion del array desde la cual el    */
/*                  el metodo ejecutara su ordenamiento. El segundo parametro  */
/*                  indica la posicion hasta la cual se ejecutara el sort.     */
/*                  Adicionalmente, puede indicar como tercer parametro una    */
/*                  funcion que ejecutara el criterio de ordenacion.           */
/* --------------------------------------------------------------------------- */

// El siguiente caso es un arreglo cuyos elementos son de tipo numerico.
int arr[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };

int n = sizeof(arr) / sizeof(arr[0]);   // Para indicar la ultima posicion a la cual se aplicara el sort.

// En este caso se dan solo dos parametros.  Observar que SORT aplica a otros tipos de objetos de C++ a parte de vector STL.object
// Mas abajo se da otro ejemplo de esto.
sort(arr, arr + n);


// En el siguiente ejemplo ordenaremos un array de objetos de acuerdo a un atributo de la clase base del objeto.
class contrato
{
   private:
      long long int numCon;    // Numero de Contrato.
      long double monto;       // Monto de la transaccion.
      int indCnc;              // Indicador de coincidencia (contrato SIX vs lista de contratos IBS). Leer notas abajo.
   public:
      long long int getNumCon() const { return(numCon); }     // Funcion que devuelve el numero de contrato.
      double getMonto() { return(monto); }                    // Funcion que devuelve el monto asociado al contrato.
      int getInd() { return(indCnc); }                        // Funcion que devuelve el indicador de coincidencia de la primera pasada.
      void setNumCon(long long int contrato) { numCon = contrato; }
      void setMonto(long double imonto) { monto = imonto; }
      void setInd(int indicador) { indCnc = indicador; }
};

typedef vector<contrato> vectorContratos;   // Tipo de dato "Vector de objetos de ejemplo".

// Funcion que implementa el criterio de ordenacion usado por el metodo sort.
bool criteriOrden(const contrato & contra1, const contrato & contra2)
{
   return contra1.getNumCon() < contra2.getNumCon();
}

/* ------------------------------------------------------------------------------------- */
/* Funcion que ordena un vector de objetos por el atributo ejemplo "numero de contrato". */
/* ------------------------------------------------------------------------------------- */
void ordenaContr(vectorContratos & vector)
{
   // IMPORTANTE: Aqui se invoca una funcion de criterio. Sin embargo, puede crear en sitio una LAMBDA function con este criterio!
   sort(vector.begin(), vector.end(), criteriOrden);   // Se utilizan los metodos begin() y end() de los vectores STL.
}



/* -------------------------------------------------------------------------------------- *
 * Los algoritmos como SORT pueden ser aplicados a otros objetos a parte de vectores STL. *
 * A continuacion un ejemplo de SORT aplicado a un array de elementos float.              *
 * -------------------------------------------------------------------------------------- */
float vecFl[4] = {8.5, 3.4, 12.6, 2.2};

cout << "\n\n\n\n ANTES DE ORDENAR vecFl:\n" << endl;
for(int i = 0; i < 4; i++) cout << vecFl[i] << endl;

sort(vecFl, vecFl+4, [](int x, int y) -> bool { return x < y; });

cout << "\n DESPUES DE ORDENAR vecFl:\n" << endl;
for(int i = 0; i < 4; i++) cout << vecFl[i] << endl;




/* -------------------------------------------------------------------------- *
 * Ejemplo de uso de SORT para ordenar de mayor a menor usando "greater<>()"! *
 * Tambien se muestra un ejemplo de for sin declarar iterador a parte!        *
 * -------------------------------------------------------------------------- */
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
        std::vector<int> V({30, 2, 1, 10, 3, 56, 1});
        std::cout << "\nV antes del sort:\n";
        for(auto &i : V) std::cout << i << ", ";
        std::sort(V.begin(), V.end(), std::greater<int>());
        std::cout << "\nV despues del sort:\n";
        for(auto &i : V) std::cout << i << ", ";
        return 0;
}

Resultado:
V antes del sort:
30, 2, 1, 10, 3, 56, 1,
V despues del sort:
56, 30, 10, 3, 2, 1, 1,






/* ------------------------------------------------------------------------------------ *
 * Ejemplo de uso: codigo escrito usando STL pura (Containers, Iterators y Algorithms). *
 * Con los algoritmos de la libreria STL es posible, en pocas lineas de codigo, hacer   *
 * operaciones complejas que llevarian varias lineas de codigo en C standard.           *
 * ------------------------------------------------------------------------------------ */
// #include<sstream>
#include<iostream>
#include<fstream>
#include<iterator>
#include<vector>
#include<algorithm>

using namespace std;

#define NUM_INTS 30

int main() 
{
    vector<int> myVector(NUM_INTS);

    // Llena el Container con numeros random (usando el algoritmo Generate). En una sola linea de codigo!
    generate(myVector.begin(), myVector.end(), rand);
    // Ordena los elementos del Container (usando el algoritmo Sort). En una sola linea de codigo!
    sort(myVector.begin(), myVector.end());
    // Envia a la salida standard (usando un Iterator). En una sola linea de codigo!
    copy(myVector.begin(), myVector.end(), ostream_iterator<int>(cout, "\n"));

    // Ejemplo de lectura de archivo y mostrar su contenido en la salida standard (usando un iterator). En dos lineas de codigo!
    ifstream input("stros.cpp");
    copy(istreambuf_iterator<char>(input), istreambuf_iterator<char>(), ostreambuf_iterator<char>(cout));

    return 0;
}







# HACER LLAMADAS A COMANDOS DEL SISTEMA DESDE UN PROGRAMA C++: Ver ejemplo a continuacion...


/* ------------------------------------------------------------------------------------------------------------------------------------ *
 * IMPORTANTE: En este ejemplo vemos como toda palabra reservada o metodo tipo "string", "ios", "cout" y "system" debe ir precedido por *
               el prefijo "std" cuando no se establece "using namespace std" al inicio del programa.                                    *
 * ------------------------------------------------------------------------------------------------------------------------------------ */
#include <iostream>
#include <fstream>

int main(int argc, char *argv[]) {
        std::string trama = "campo1 campo2 campo3 campo4";
        std::fstream fout;

        fout.open("test.txt", std::ios::out);

        if(fout) {
                std::cout << "\n\n ABRE EL ARCHIVO!\n\n";
                fout << "\n Contenido del archivo:\n\n" << trama << "\n";
                fout.close();
                std::system("cat test.txt");
                std::system("rm test.txt");
        }

        return 0;
}



# Otro ejemplo de manejo de archivos io:


# ----------------------------------------------------------------------------------------------------------------------------------#
# Programa de demostracion en el uso de algoritmos para eliminar espacios blancos en un string, manejo de substrings, leer archivos #
# para extraer de ellos algunos strings por posicion dentro de la fila leida, uso del ::isspace, etc.                               #
# ----------------------------------------------------------------------------------------------------------------------------------#
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


// Objetos archivos de entrada, salida y archivo de parametros.
fstream   finputSIX;
fstream   finputIBS;
fstream   foutputSIX;
fstream   foutputIBS;
fstream   fparam;


// Registros de entrada y salida.
string inputr   = "";
string outptr   = "";


/* ------------------------------------------ */
/* Elimina los espacios blancos de un string. */
/* ------------------------------------------ */
void elimEsp(string & cadena)
{
   cadena.erase(std::remove_if(cadena.begin(), cadena.end(), ::isspace), cadena.end());
}



/* ---------------------------------------------------------------------------------------------------- */
/* Descripticion: Convierte un archivo en formato texto hacia un archivo con caracter separador blanco. */
/* ---------------------------------------------------------------------------------------------------- */
int main()
{
   string contrato = "";
   string monto = "";


   // Archivo conteniendo los contratos en la base de datos de SIX.
   finputSIX.open("sixdata.csv", ios::in);

   // Archivo conteniendo los contratos y sus montos asociados con separador.
   foutputSIX.open("datosSIX.txt", ios::out);

   // Archivo conteniendo los contratos en la base de datos de SIX.
   finputIBS.open("ibsdata.csv", ios::in);

   // Archivo conteniendo los contratos y sus montos asociados con separador.
   foutputIBS.open("datosIBS.txt", ios::out);



   // Valida que el archivo de base de datos SIX contenga registros.
   if (!finputSIX || !finputIBS) {
       cout << "No hay registros contratos desde SIX o desde IBS!" << endl;

      finputSIX.close();
      finputIBS.close();
      foutputSIX.close();
      foutputIBS.close();

      // Elimina los archivos creados.
      system("del datosIBS.txt datosSIX.txt");

       return 0;
   }else {
      // Descarta la primera linea de titulos de las columnas del archivo de datos SIX.
      // getline(finputSIX, inputr);
   }


   // Ciclo de lectura de contratos SIX.
   while(getline(finputSIX, inputr))
   {
      if(inputr.substr(0, 2) == "0 ") inputr = "         " + inputr;

      outptr = inputr;

      foutputSIX << outptr << endl;   // Escribe en el archivo de salida.

      // Limpiamos los registros de entrada y salida para una nueva lectura.
      inputr = ""; outptr = ""; contrato = ""; monto = "";
   }


   // Limpiamos los registros de entrada y salida para una nueva lectura.
   inputr = ""; outptr = "";


   string strMonto = "";

   // Ciclo de lectura de contratos IBS.
   while(getline(finputIBS, inputr))
   {
      std::replace(std::begin(inputr),std::end(inputr),'\t',' ');        // Elimina cualquier caracter Tab.

      if(inputr.substr(0, 1) == "0") {
         contrato = "         0";

         strMonto = inputr.substr(2, inputr.find_first_of("\n"));   // Toma el string del monto.
      }
      else{
         contrato = inputr.substr(0, 10);                                   // Toma el string del contrato.
         elimEsp(contrato);                                                 // Elimina cualquier espacio blanco.

         strMonto = inputr.substr(11, inputr.find_first_of("\n"));   // Toma el string del monto.
      }

      outptr = contrato + " " + strMonto;                                // Arma la fila conteniendo el contrato y el monto con separador.

      foutputIBS << outptr << endl;                                      // Escribe en el archivo de salida.

      // Limpiamos los registros de entrada y salida para una nueva lectura.
      inputr = ""; outptr = ""; contrato = ""; monto = "";
   }


/*
   // Ciclo de lectura de contratos.
   while(getline(finput, inputr))
   {
      if(inputr.length() < 120) {
         outptr = string("   ;") + string("   ;") + string("   ;") + inputr;
      }else {
         // Llenamos los datos del registro leido.
         outptr = inputr.substr(11, 6) + " " + inputr.substr(31, 4) + ";" + inputr.substr(18, 12) + ";" + inputr.substr(42, 10) + ";" + inputr.substr(120, inputr.find_first_of("\n"));
      }

      foutput << outptr << endl;   // Escribe una linea en el archivo de salida.

      // Limpiamos los registros de entrada y salida para una nueva lectura de registro desde el log.
      inputr = ""; outptr = "";
   }
*/

   // Cierra los archivos.
   finputSIX.close();
   foutputSIX.close();
   finputIBS.close();
   foutputIBS.close();

   return 0;
}




# ---------------------------------------------------------------------------------------------------------------------------- #
# Ejemplo de programa que lee un archivo con separador, arma un vector de objetos (objeto conteniendo cada elemento de la fila leida     #
# desde el archivo convertido de string al tipo de dato de cada atributo en el objeto), procesa los registros y convierte de regreso cada atributo #
# de cada objeto del vector y (finalmente) graba en un nuevo archivo con separador. Este programa tambien incluye ejemplos de  #
# algoritmo para ordenar un vector de objetos de clase de acuerdo a uno de sus atributos, funciones de convertir un string a numero decimal
# ---------------------------------------------------------------------------------------------------------------------------- #
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


fstream   finSIX;   // Archivo conteniendo los contratos registrados en SIX.
fstream   finIBS;   // Archivo conteniendo los contratos registrados en IBS.
fstream   foutFalt;   // Archivo que contendra el faltante.
fstream   foutSobr;   // Archivo que contendra el sobrante.

char sepdr = ' ';   // Separador de campos en los archivos leidos.
char sepdrS = ',';  // Separador de campos en los archivos de salida.


/* ----------------------------------------------------------------------- *
 * Objeto que representa un contrato con su monto de transaccion asociado. *
 * ----------------------------------------------------------------------- */
class contrato
{
   private:
      long long int numCon;    // Numero de Contrato.
      long double monto;       // Monto de la transaccion.
      int indCnc;              // Indicador de coincidencia (contrato SIX vs lista de contratos IBS). Leer notas abajo.
   public:
      long long int getNumCon() const { return(numCon); }     // Funcion que devuelve el numero de contrato.
      double getMonto() { return(monto); }                    // Funcion que devuelve el monto asociado al contrato.
      int getInd() { return(indCnc); }                        // Funcion que devuelve el indicador de coincidencia de la primera pasada.
      void setNumCon(long long int contrato) { numCon = contrato; }
      void setMonto(long double imonto) { monto = imonto; }
      void setInd(int indicador) { indCnc = indicador; }
};


typedef vector<contrato> vectorContratos;   // Tipo de dato "Vector de contratos".



// string patron   = "";   // Patron de busqueda.
/*
void imprimeOcurrencias(string txt, string pat)
{
   int found = txt.find(pat);

   while (found != string::npos) {
      cout << "Patron encontrado en la posicion: " << found << endl;

      found = txt.find(pat, found + 1);
   }
}
*/


bool mifuncion(const contrato & contra1, const contrato & contra2)
{
   return contra1.getNumCon() < contra2.getNumCon();
}

/* ----------------------------------------------------------------- */
/* Funcion que ordena un vector de contratos por numero de contrato. */
/* ----------------------------------------------------------------- */
void ordenaContr(vectorContratos & vector)
{
   sort(vector.begin(), vector.end(), mifuncion);

   /* Esta forma de realizar el sort (usando una Lambda function) no es soportada por algunos compiladores.
   std::sort(vector.begin(), vector.end(), [](contrato & contra1, contrato & contra2)
   {
      return contra1.getNumCon() < contra2.getNumCon();
   });
   */
}


/* --------------------------------------------------------------------------------------------------- *
 * Funcion que convierte un string de campos con separador y llena un elemento del vector de contratos *
 * --------------------------------------------------------------------------------------------------- */
void llenaContr(const string & str, char separador, vectorContratos & vector)
{
   size_t   posi1 = 0;
   size_t   posi2 = 0;
   contrato   elemento;
   string   montoTemp = "";


   // Busca el caracter separador para obtener el numero de contrato.
   posi2 = str.find(separador, posi1);

   if(posi2 != str.npos) {
      if (posi2 > posi1) {
         // Toma el numero de contrato y lo convierte a numerico.
         elemento.setNumCon(stoll(str.substr(posi1, posi2-posi1)));

         posi1 = posi2 + 1;

         montoTemp = str.substr(posi1, str.find_first_of("\n"));
         montoTemp.erase(remove( montoTemp.begin(), montoTemp.end(), '\"' ), montoTemp.end());   // Elimina cualquier comilla doble.


         replace(montoTemp.begin(), montoTemp.end(), ',', '.');   // Reemplaza la coma por un punto decimal.


         elemento.setMonto(stold(montoTemp));   // Convierte el monto en numero decimal.

         elemento.setInd(0);   // Inicia el indicador de coincidencia de primera pasada con cero (0).

         vector.push_back(elemento);   // Almacena el elemento en el vector de contratos.

         montoTemp = "";
      }
   }
}


/* ------------------------------------------------------------- *
 * Funcion que convierte un contrato en un string con separador. *
 * ------------------------------------------------------------- */
string convSep(contrato & contIn)
{
   string soutput = "";
   string strMont = to_string(contIn.getMonto());

   replace(strMont.begin(), strMont.end(), '.', ',');          // Reemplaza el punto decimal por la coma decimal.
   soutput = to_string(contIn.getNumCon()) + sepdr + strMont;

   return(soutput);
}


/* ------------------------------------------------------ *
 * Funcion que graba un contrato en un archivo de salida. *
 * ------------------------------------------------------ */
void grabaContrato(contrato contSalida, fstream & archivo)
{
   string   outptr = "";   // Almacenara cada string (fila) que se escribira al archivo de salida.

   outptr = convSep(contSalida);   // Convierte el contrato en un string con separador.

   archivo << outptr << endl;   // Graba el string en el archivo de salida.
}



/* ------------------------------------------------------------------------------------------------------ */
/* Para compilar este fuente se utilizó el compilador de C++ del producto MinGW para Windows.             */
/* También puede ser compilado en el sistema operativo Linux y en varios sabores de Unix que soporten     */
/* el estándar ISO C++11:                                                                                 */
/*                                                                                                        */
/* c++ -std=c++11 difSIX_ver5.cpp -o difSIX                                                               */
/*                                                                                                        */
/*                                                                                                        */
/* Descripticion: Lee los archivos de contratos (tanto del IBS como del SIX) e identifica las diferencias */
/*                como sobrantes (SIP/IBS) y faltantes (SIX).                                             */
/*                                                                                                        */
/* NOTAS:                                                                                                 */
/*    - Cada archivo de entrada contiene los contratos y sus montos asociados separados por un caracter   */
/*      blanco.                                                                                           */
/*    - Compara cada contrato SIX (y su monto asociado) contra toda la lista de contratos (y montos) del  */
/*      IBS. Una coincidencia se da cuando los contratos son iguales y la diferencia entre sus montos es  */
/*      cero. Los números de contrato (y su monto) pudieran aparecer repetidos N veces en cada grupo.     */
/*      En casos como este, la primera coincidencia será tomada como no diferencia (no es faltante ni es  */
/*      sobrante). Las siguientes coincidencias serán tomadas, automáticamente, como faltantes (para el   */
/*      caso de SIX) o como sobrantes (para el caso de IBS). El programa utiliza un indicador de          */
/*      coincidencia asociado al contrato, con los siguientes valores posibles:                           */
/*                                                                                                        */
/*                                                        -1 ----> Primera coincidencia                   */
/*                                                         0 ----> No es primera coincidencia             */
/*                                                                                                        */
/*      - En la primera parte, el algoritmo compara cada contrato SIX contra la lista de contratos IBS,   */
/*        detectando todas las primeras coincidencias (coloca los indicadores con valor -1).              */
/*      - Al final, envía al archivo de faltantes todo contrato SIX cuyo indicador tenga valor cero. Y    */
/*        lo mismo hace con los contratos IBS: todo contrato IBS cuyo indicador esté en cero lo envía al  */
/*        archivo de sobrantes.                                                                           */
/*                                                                                                        */
/*      Ejemplo:                                                                                          */
/*                                                                                                        */
/*             SIX                                                            IBS                         */
/*  Ind Contrato       Monto                                      Contrato         Monto     Ind          */
/*  ----------------------------                                  --------------------------------        */
/*  -1  04165736122    5000.00 --- Primera coincidencia   ------->04165736122      5000.00   -1           */
/*                               (no es una diferencia)  |                                                */
/*   0  04165736122    5000.00 --- Segunda coinc. -------|        02887711124   2423848.10                */
/*                               (es un faltante)        |                                                */
/*   0  04165736122    5000.00 --- Tercera coinc. -------     ----02126815363    250727.42   -1           */
/*                               (es un faltante)            |----02126815363    250727.42    0           */
/*                                                           |                                            */
/*  -1  02126815363  250727.42<---- Primera coinc. ----------|    02353418840    910529.66                */
/*                                (no es una diferencia)     |                                            */
/*   0  02126815363  250727.42<---- Segunda coinc. ----------                                             */
/*                                (es un sobrante)                                                        */
/*                                                                                                        */
/*    - Esta aplicación ordena ambas listas de contratos. Este paso pudiera no ser necesario.             */
/*    - Los montos asociados a cada contrato deben tener el siguiente formato (en los archivos entrantes: */
/*                                                                                                        */
/*      xxxxxxxxxxx,xx  o  xxxxxxxxxx.xx                                                                  */
/*                                                                                                        */
/*    - Graba dos archivos: uno con el sobrante (SIP/IBS) y otro con el faltante (SIX).                   */
/*                                                                                                        */
/*                                                                                                        */
/* Analista: José Portillo, Newtechsistemas                                                               */
/* Fecha...: Enero 2022                                                                                   */
/* ------------------------------------------------------------------------------------------------------ */
int main()
{
   string   inputr = "";   // Variable que almacenara cada string (fila) leido desde el archivo de entrada.

   contrato   contSix;   // Representa un contrato registrado en SIX.
   contrato   contIBS;   // Representa un contrato registrado en IBS.

   vectorContratos   vecSIX;       // Vector que contendra los contratos registrados en SIX.
   vectorContratos   vecIBS;       // Vector que contendra los contratos registrados en IBS.


   finSIX.open("datosSIX.txt", ios::in);   // Abre el archivo de contratos SIX.
   foutFalt.open("faltante.csv", ios::out);   // Abre el archivo que contendra el faltante.

   finIBS.open("datosIBS.txt", ios::in);   // Abre el archivo de contratos IBS.
   foutSobr.open("sobrante.csv", ios::out);   // Abre el archivo que contendra el sobrante.


   // Valida que el archivo de contratos SIX contenga registros.
   if (!finSIX) {
       cout << "No hay registros contratos desde SIX!" << endl;
       finSIX.close();
       foutFalt.close();
       finIBS.close();
       foutSobr.close();
       system("del faltante.csv sobrante.csv");   // Elimina los archivos de trabajo.
       return 0;
   }

   // Valida que el archivo de contratos IBS contenga registros.
   if (!finIBS) {
       cout << "No hay registros contratos desde IBS!" << endl;
       finSIX.close();
       foutFalt.close();
       finIBS.close();
       foutSobr.close();
       system("del faltante.csv sobrante.csv");   // Elimina los archivos de trabajo.
       return 0;
   }


   // Ciclo de lectura de contratos SIX.
   while(getline(finSIX, inputr))
   {
      llenaContr(inputr, sepdr, vecSIX);       // Adiciona el contrato leido al vector SIX.

      // Limpia el string de entrada para una nueva lectura.
      inputr = "";
   }

   // Limpia el string de entrada para una nueva lectura.
   inputr = "";

   // Ciclo de lectura de contratos IBS.
   while(getline(finIBS, inputr))
   {
      llenaContr(inputr, sepdr, vecIBS);   // Adiciona el contrato leido al vector IBS.

      // Limpia el string de entrada para una nueva lectura.
      inputr = "";
   }

   ordenaContr(vecSIX);       // Ordena la lista de contratos SIX.
   ordenaContr(vecIBS);       // Ordena la lista de contratos IBS.


   /* ----------------------------------------------------------------------------------------- */
   /* PROCEDE A COMPARAR CADA CONTRATO SIX CONTRA LA LISTA DE CONTRATOS IBS. Leer notas arriba. */
   /* ----------------------------------------------------------------------------------------- */
   // Compara cada contrato SIX contra los contratos en el vector IBS. Leer las notas arriba.
   for(vector<contrato>::iterator i = vecSIX.begin(); i != vecSIX.end(); i++)
   {
      long double montoDif = 0.0;

      // Itera a traves de la lista de contratos IBS en busca de coincidencias con el contrato SIX en curso.
      for(vector<contrato>::iterator j = vecIBS.begin(); j != vecIBS.end(); j++)
      {    
         montoDif = 0.0;
         montoDif = i->getMonto() - j->getMonto();   // Calcula la diferencia entre ambos montos.

         // Verifica si los números de contrato coinciden y si sus montos asociados son iguales.
         if((i->getNumCon() == j->getNumCon()) && !montoDif) { 
            /* -----------------------------------------------------------------------------------------------*/
            /* Si se trata de la primera coincidencia del contrato SIX en curso, entonces activa el indicador */
            /* de primera coincidencia en ambos contratos.                                                    */
            /* -----------------------------------------------------------------------------------------------*/
            if(!i->getInd() && !j->getInd()) { i->setInd(-1); j->setInd(-1); continue; }   // Entonces ambos contratos son primera coincidencia.
         }
      }
   }

   // Itera a traves de la lista de contratos SIX. Todo contrato cuyo indicador tenga valor cero sera declarado como faltante.
   for(vector<contrato>::iterator i = vecSIX.begin(); i != vecSIX.end(); i++) if(!i->getInd()) i->setInd(1);

   // Itera a traves de la lista de contratos IBS. Todo contrato cuyo indicador tenga valor cero sera declarado como sobrante.
   for(vector<contrato>::iterator j = vecIBS.begin(); j != vecIBS.end(); j++) if(!j->getInd()) j->setInd(2);


/*
   cout << "CONTRATOS SIX: " << endl;
   for(vector<contrato>::iterator i = vecSIX.begin(); i != vecSIX.end(); i++)
   {
      cout << i->getNumCon() << "   Monto SIX: " << i->getMonto() << "   Indicador: "  << i->getInd() << endl;
   }
   cout << "CONTRATOS IBS: " << endl;
   for(vector<contrato>::iterator j = vecIBS.begin(); j != vecIBS.end(); j++)
   {
      cout << j->getNumCon() << "   Monto SIX: " << j->getMonto() << "   Indicador: "  << j->getInd()  << endl;
   }
*/



   /* ---------------------------------------------------------- */
   /* PROCEDE A GRABAR EN LOS ARCHIVOS DE FALTANTES Y SOBRANTES. */
   /* ---------------------------------------------------------- */
   for(vector<contrato>::iterator i = vecSIX.begin(); i != vecSIX.end(); i++)
   {
      // Graba el contrato con indicador "1" en el archivo de faltantes.
      if(i->getInd() == 1) grabaContrato(*i, foutFalt);
   }


   for(vector<contrato>::iterator j = vecIBS.begin(); j != vecIBS.end(); j++)
   {
      // Graba el contrato con indicador "2" en el archivo de sobrantes.
      if(j->getInd() == 2) grabaContrato(*j, foutSobr);
   }


   // Cierra los archivos.
   finSIX.close();
   foutFalt.close();
   finIBS.close();
   foutSobr.close();

   return 0;
}







# ------------------------------------------------------------------------------------------------------------------------------#
# Otro rograma de demostracion en el uso de vectores, iteradores, templates, sobrecarga de operadores y manejo de archivos CSV. #
# ------------------------------------------------------------------------------------------------------------------------------#

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


struct elemento
{
    int     atributo1 = 0;
    double  atributo2 = 0.0;
    string  atributo3 = "Prueba de string";
};


// Ejemplo de Template class con sobre carga de operador +.
template <class T> class objeto
{
    private:
        T atributo1;
        T atributo2;
        T atributo3;
        T atributo4;
    public:
        objeto (T parm1, T parm2, T parm3, T parm4) { atributo1 = parm1; atributo2 = parm2; atributo3 = parm3; atributo4 = parm4; }
        const objeto operator + (const objeto<T> t1);
        void mostrar_objeto() { cout << "atributo1 es: " << atributo1 << " atributo2 es: " << atributo2 << " atributo3 es: " << atributo3 << " atributo4 es: " << atributo4 << endl; }
};

template <class T> const objeto<T> objeto<T>::operator + (const objeto<T> t1)
{
    objeto<T> temp(0, 0, 0, 0);

    temp.atributo1 = atributo1 - t1.atributo1;
    temp.atributo2 = atributo2 + t1.atributo2;
    temp.atributo3 = atributo3 - t1.atributo3;
    temp.atributo4 = atributo4 * t1.atributo4;

    return temp;
}


/* ------------------------------------------------------------------------------------------------------- *
 * La siguiente funcion lee un string con separador (pudiera ser un CSV) y llena un vector de tipo string. *
 * ------------------------------------------------------------------------------------------------------- */
typedef vector<string> StringVector;

StringVector Explode(const string & str, char separator)
{
    StringVector result;
    size_t pos1 = 0;
    size_t pos2 = 0;


    while (pos2 != str.npos) {
        pos2 = str.find(separator, pos1);

        if (pos2 != str.npos) {
            if (pos2 > pos1) result.push_back(str.substr(pos1, pos2-pos1));

            pos1 = pos2 + 1;
        }
    }

    result.push_back(str.substr(pos1, str.size() - pos1));

    return result;
}


int main()
{
    vector<elemento> eleContainer;
    elemento var_ele;


    var_ele.atributo1 = 5;
    var_ele.atributo2 = 2.3;
    var_ele.atributo3 = "Primer String de Prueba";


    // Prueba de llenado del vector.
    try {
        eleContainer.push_back(var_ele);
    }
    catch (int n)       { cout << "int exception!" << endl; }
    catch (char cexc)   { cout << "char exception!" << endl; }
    catch (...)         { cout << "default exception!" << endl; }

    // Prueba de iterator sobre un vector.
    for (vector <elemento>::iterator i = eleContainer.begin(); i != eleContainer.end(); i++) {
        cout << "Valor del atributo1: " << i->atributo1 << endl;
        cout << "Valor del atributo2: " << i->atributo2 << endl;
        cout << "Valor del atributo3: " << i->atributo3 << endl;
    }


    // Prueba de manejo de archivo CSV.
    string cadenaCSV = "";
    ifstream input("archivo.csv");
    StringVector vecCSV;
    char sepCSV = ',';


    if (!input) {
        cout << "Fallo abriendo archivo.csv!" << endl;
    }else {
        getline(input, cadenaCSV);

        cout << "Contenido del archivo es: " << cadenaCSV << endl;

        vecCSV = Explode(cadenaCSV, sepCSV);    // Prueba la funcion que lee un string con separadores y llena un vector tipo string.

        for (vector <string>::iterator i = vecCSV.begin(); i != vecCSV.end(); i++) cout << "vector: " << *i << endl;
    }


    // Ejemplo de uso de funciones de manejo string.
    string str = "We think in generalities, but we live in details.";
                                           // (quoting Alfred N. Whitehead)

    string str2 = str.substr(3,5);     // "think"

    size_t pos = str.find("live");      // position of "live" in str

    string str3 = str.substr(pos);     // get from "live" to the end

    cout << "str es: " << str << endl;
    cout << "str2 es: " << str2 << endl;
    cout << "pos es: " << pos << endl;
    cout << "str3 es: " << str3 << endl;

    // Ejemplo de concatenacion de strings (tanto variables tipo string como constantes string). En la concatenacion de objetos 
       tipo String se utiliza el operador "+" y las constantes deben pasarse como argumento a la funcion string():
    string inputr   = "";         // Registro de entrada.
    string outptr   = "";         // Registro de salida.

    // Aqui se coloca una cabecera con strings constantes.
    outptr = string("Fecha;") + string("Hora;") + string("Proceso;") + string("Programa y log");

    // Luego, se coloca la fila con datos tipo string.
    outptr = inputr.substr(11,6) + " " + inputr.substr(31,4) + ";" + inputr.substr(18,12)


    // Ejemplo de uso de Template class con sobrecarga de operador +.
    objeto<int> obj1(2, 5, 6, 8), obj2(1, 4, 3, 2), obj3(0, 0, 0, 0);

    obj3.mostrar_objeto();

    obj3 = obj1 + obj2;

    obj3.mostrar_objeto();

    return 0;
}



/* ---------------------------------------------------------------------------------------------------------------------------------- */
/* Ejemplo de lectura y escritura de archivos TXT y CSV.                                                                              */
/*                                                                                                                                    */
/* NOTA IMPORTANTE: Todas las palabras como "string" y "ios" deben tener el prefijo std:: cuando no se ha indicado el namespace std!! */
/*                  Ejemplo,                                                                                                          */
#include<iostream>
#include<fstream>

int main() {
        std::string entrada = "";
        std::string salida  = "Esta es una prueba de escritura";
        std::fstream oFile;

        oFile.open("test.txt", std::ios::out);
        oFile << "\n\n" << salida << "\n\n" << std::endl;
        oFile.close();

        return 0;
}

/*                                                        */
/* Este programa lee un archivo texto conteniendo un log  */
/* de una aplicacion y arma un archivo CSV listo para     */
/* para el Excel.                                         */
/* ------------------------------------------------------ */
#include <iostream>
#include <fstream>

using namespace std;

/* ----------------------------------------------------------------------------------------- */
/* NOTAS:                                                                                    */
/*    - No hace falta convertir la hora leida en un tipo fecha (el excel lo interpreta).     */
/*    - La fecha (en formato "Mes DD") empieza en la columna 11 y mide 6 posiciones.         */
/*    - El año empieza en la columna 31 y mide 4 posiciones.                                 */
/*    - La hora empieza en la columna 18 y mide 12 posiciones.                               */
/*    - El nombre del proceso empieza en la columna 42 y mide 10 posiciones (just. izqui).   */
/*    - El nombre del programa y el log comienzan en la columna 120 hasta el fin de linea.   */
/*    - Todas las filas finalizan con el caracter punto "."                                  */
/*    - Las transacciones terminan con lineas (ejemplo),                                     */
/*                 diagnosis: [successful operation executed].                               */
/*                 diagnosis: [application response timeout].                                */
/* ----------------------------------------------------------------------------------------- */
int main()
{
   string inputr   = "";      // Registro de entrada.
   string outptr   = "";      // Registro de salida.
   // string patron   = "";   // Patron de busqueda.
   fstream foutput;           // Archivo de entrada.
   fstream finput;            // Archivo de salida.


   // Abre el log. Este archivo es de texto.
   finput.open("sixbasev20210728.log", ios::in);

   // Abre el archivo de salida.
   foutput.open("salida.csv", ios::out);


   // Valida que el log contenga registros.
   if (!finput) {
       cout << "Fallo abriendo el log!" << endl;
       return 0;
   }else {
      // Arma la primera fila con titulos para cada campo.
      outptr = string("Fecha;") + string("Hora;") + string("Proceso;") + string("Programa y log");

      foutput << outptr << endl;   // Escribe primera linea en el archivo de salida.
   }

   // Ciclo de lectura del log.
   while(getline(finput, inputr))
   {
      if(inputr.length() < 120) {
         outptr = string(";") + string(";") + string(";") + inputr;
      }else {
         // Llenamos los datos del registro leido.
         outptr = inputr.substr(11,6) + " " + inputr.substr(31,4) + ";" + inputr.substr(18,12) + ";" + inputr.substr(42,10) + ";" + inputr.substr(120, inputr.find_first_of("\n"));
      }

      foutput << outptr << endl;   // Escribe una linea en el archivo de salida.

      // Limpiamos los registros de entrada y salida para una nueva lectura de registro desde el log.
      inputr = ""; outptr = "";
   }

   // Cierra los archivos.
   finput.close();
   foutput.close();

   return 0;
}





/* ------------------------------------------------------------------------------------------------------------------- */
/* Ejemplo del codigo de maquina generado por el compilador C++ de manejo de arreglos a traves de apuntadores basicos. */
/*                                                                                                                     */
/* NOTA: El codigo generado es para un procesador Intel Core(TM) i5-3210M CPU 2.50GHz                                  */
/*       y la invocacion al compilador fue la siguiente:                                                               */
/*                                                       c++ -S -std=c++14 apuntadores.cpp                             */ 
/* ------------------------------------------------------------------------------------------------------------------- */

//
// funcion ejemplo: se maneja un arreglo 4-dimensional a traves de apuntadores basicos del C++.
//
void cargar_arreglo_2(char array[dimension1][dimension2][dimension3][dimension4])
{
	char *base = &array[0][0][0][0];

	for(int j = 0;j < dimension1;j++)
		for(int z = 0;z < dimension2;z++)
			for(int y = 0;y < dimension3;y++)
				for(int x = 0;x < dimension4;x++)
					*((char *) base + (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4) + (y*dimension4) + x) = 3;
}

//
// Codigo assembler generado por el compilador usando la opcion "c++ -S ..." (solo se incluye la funcion, no el main):
//
_Z16CARGAR_ARREGLO_2PA2_A2_A4_C:
.LFB0:
	PUSHQ	%RBP
	MOVQ	%RSP, %RBP
	SUBQ	$32, %RSP
	MOVQ	%RCX, 16(%RBP)   <-- desde el main viene la direccion del arreglo dentro del registro CX del Intel x62.
	MOVQ	16(%RBP), %RAX
	MOVQ	%RAX, -24(%RBP)  <-- ahora la posicion -24 del buffer BP contiene la direccion del arreglo.
	MOVL	$0, -4(%RBP)     <-- int j = 0  (del for mas externo).
	JMP		.L2

.L9:
	MOVL	$0, -8(%RBP)     <-- int z = 0 
	JMP		.L3

.L8:
	MOVL	$0, -12(%RBP)    <-- int y = 0
	JMP		.L4

.L7:
	MOVL	$0, -16(%RBP)    <-- int x = 0
	JMP		.L5

.L6:

#define dimension1   2
#define dimension2   2
#define dimension3   2
#define dimension4   4
-24(%BP) -----> base   (apuntador al array que viene como parametro).
-4(%BP)  -----> j
-8(%BP)  -----> z
-12(%BP) -----> y
-16(%BP) -----> x

// El siguiente es el codigo que ejecuta la sentencia que asigna el valor 3 a cada elemento del arreglo 4-dimensional: 
// *(base + (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4) + (y*dimension4) + x) = 3;
//
// NOTA: Observar que el generador de codigo no utiliza la operacion MULT del Intel x64 (Intel Core(TM) i5-3210M CPU 2.50GHz)
//       En su lugar usa la operacion SALL (Shift Arithmetic Left) que respeta el bit del signo (complemento-2).

	MOVL	-4(%RBP), %EAX    <-- j
	SALL	$4, %EAX          <-- (j*dimension2*dimension3*dimension4)
	MOVSLQ	%EAX, %RDX
	MOVL	-8(%RBP), %EAX    <-- z
	SALL	$3, %EAX          <-- (z*dimension3*dimension4)
	CLTQ                      <-- convierte el contenido del registro AX de double-word a quad-word
	ADDQ	%RAX, %RDX        <-- (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4)
	MOVL	-12(%RBP), %EAX   <-- y
	SALL	$2, %EAX          <-- (y*dimension4)
	CLTQ                      <-- convierte el contenido del registro AX de double-word a quad-word
	ADDQ	%RAX, %RDX        <-- (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4) + (y*dimension4)
	MOVL	-16(%RBP), %EAX   <-- x
	CLTQ                      <-- convierte el contenido del registro AX de double-word a quad-word
	ADDQ	%RAX, %RDX        <-- (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4) + (y*dimension4) + x
	MOVQ	-24(%RBP), %RAX   <-- base
	ADDQ	%RDX, %RAX        <-- base + (j*dimension2*dimension3*dimension4) + (z*dimension3*dimension4) + (y*dimension4) + x
	MOVB	$3, (%RAX)        <-- *(...) = 3 , es decir: asigna el valor 3 a lo apuntado.
	ADDL	$1, -16(%RBP)     <-- x++

//
// NOTA: Asumiendo un modelo de programacion de 64 bits, veamos lo que hace la operacion SALL:
//
// 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0001  <-- valor inicial (asumiendo valor 1)
// 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0100  <-- SALL $2, %EAX (multiplica por 4 el valor)
// 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 1000  <-- SALL $3, %EAX (multiplica por 8 el valor)
// 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0001 0000  <-- SALL $4, %EAX (multiplica por 16 el valor)
//

.L5:
	CMPL	$3, -16(%RBP)            <-- como la dimension4 es 4 el for compara x < 4 (es decir 3).
	JLE		.L6
	ADDL	$1, -12(%RBP)     <-- y++

.L4:
	CMPL	$1, -12(%RBP)
	JLE		.L7
	ADDL	$1, -8(%RBP)      <-- z++

.L3:
	CMPL	$1, -8(%RBP)
	JLE		.L8
	ADDL	$1, -4(%RBP)      <-- j++

.L2:
	CMPL	$1, -4(%RBP)      <-- como la dimension1 es 2 el primer for compara j < 2 (es decir 1).
	JLE		.L9
	ADDQ	$32, %RSP
	POPQ	%RBP
	RET

/* --------------------------------------------------------------- */
/* Ejemplo de generacion de codigo de una sentencia switch...case: */
/* --------------------------------------------------------------- */
void prueba_case()
{
	int valor = 10;
	int salida = 0;

	switch(valor)
	{
		case 2:
				salida *= valor;
				break;
		case 4:
				salida = (valor * 500) / 100;
				break;
		case 7:
				salida += valor;
				break;
		case 10:
				salida = valor / 2;
				break;
		default:
				salida = 1;
	}
}

_Z11prueba_casev:

.LFB1:
	PUSHQ	%RBP
	MOVQ	%RSP, %RBP
	SUBQ	$16, %RSP
	MOVL	$10, -4(%RBP)
	MOVL	$0, -8(%RBP)
	MOVL	-4(%RBP), %EAX
	CMPL	$4, %EAX
	JE		.L12
	CMPL	$4, %EAX
	JG		.L13
	CMPL	$2, %EAX
	JE		.L14
	JMP		.L11

.L13:
	CMPL	$7, %EAX
	JE		.L15
	CMPL	$10, %EAX
	JE		.L16
	JMP		.L11

.L14:
		case 2:
				salida *= valor;
				break;

	MOVL	-8(%RBP), %EAX
	IMULL	-4(%RBP), %EAX
	MOVL	%EAX, -8(%RBP)
	JMP		.L10

.L12:
		case 4:
				salida = (valor * 500) / 100;
				break;

	MOVL	-4(%RBP), %EAX
	IMULL	$500, %EAX, %ECX
	MOVL	$1374389535, %EDX   <-- el algoritmo usado por el compilador c++ no utiliza la operacion DIV del Intel x64.
	MOVL	%ECX, %EAX              En su lugar utiliza un algoritmo basado en desplazamientos y escalamiento.
	IMULL	%EDX
	SARL	$5, %EDX
	MOVL	%ECX, %EAX
	SARL	$31, %EAX
	SUBL	%EAX, %EDX
	MOVL	%EDX, %EAX
	MOVL	%EAX, -8(%RBP)
	JMP		.L10

.L15:
		case 7:
				salida += valor;
				break;

	MOVL	-4(%RBP), %EAX
	ADDL	%EAX, -8(%RBP)
	JMP		.L10

.L16:
		case 10:
				salida = valor / 2;
				break;

	MOVL	-4(%RBP), %EAX
	MOVL	%EAX, %EDX
	SHRL	$31, %EDX
	ADDL	%EDX, %EAX
	SARL	%EAX
	MOVL	%EAX, -8(%RBP)
	JMP		.L10

.L11:
		default:
				salida = 1;

	MOVL	$1, -8(%RBP)

.L10:
	ADDQ	$16, %RSP
	POPQ	%RBP
	RET

#
# Ejemplo de codigo assembler generado para la siguiente funcion Fibonnaci:
int fib(int n) { if(n == 0 || n == 1) return(n); return(fib(n - 1) + fib(n - 2)); }

_Z3FIBI:
	PUSHQ	%RBP
	PUSHQ	%RBX
	SUBQ	$40, %RSP
	LEAQ	128(%RSP), %RBP
	MOVL	%ECX, -64(%RBP)
	MOVL	-64(%RBP), %EAX
	TESTL	%EAX, %EAX
	JE		.L2
	MOVL	-64(%RBP), %EAX
	CMPL	$1, %EAX
	JNE		.L3

.L2:
	MOVL	-64(%RBP), %EAX
	JMP		.L4

.L3:
	MOVL	-64(%RBP), %EAX
	SUBL	$1, %EAX
	MOVL	%EAX, %ECX
	CALL	_Z3FIBI
	MOVL	%EAX, %EBX
	MOVL	-64(%RBP), %EAX
	SUBL	$2, %EAX
	MOVL	%EAX, %ECX
	CALL	_Z3FIBI
	ADDL	%EBX, %EAX

.L4:
	ADDQ	$40, %RSP
	POPQ	%RBX
	POPQ	%RBP
	RET












#
#
#                                        SECCION DE EJEMPLOS BASH Shell Script                                          #
#
#
# NOTA IMPORTANTE: Cualquier sentencia contenida en un archivo .sh puede ser escrita manualmente en la linea de comandos BASH!
#

# El comando "id" muestra informacion sobre el usuario actual:
$ id
uid=3000(tradel) gid=3000(tradel) groups=3000(tradel),0(root),100(users),545(builtin_users),999(docker)








#
# En BASH la variable de script "$?" contiene el valor retornado por el comando ejecutado mas recientemente.
#
# Para BASH, un valor 0 retornado por un comando ejecutado significa exito en la ejecucion. 1 significa que el comando 
# recien ejecutado termino mal. Por tal motivo, en los scripts debemos consultar por el valor 0 para saber si el comando 
# anterior se ejecuto correctamente.
#








#
# Sobre el uso de los wildcards "*" y "?".
#
# NOTA: "?" representa un solo caracter mientras que "*" representa muchos caracteres.
#
# NOTA: Al colocar dichos wildcard en una linea de comandos del SHELL o a traves del comando "echo" dichos 
#       wildcard se expanden a lo representado. Por ejemplo, cuando queremos consultar por todos los archivos 
#       que tengan la extension .py podemos hacerlo asi,
echo *.py
PYTHON_LINUX_COMMANDS_AND_SCRIPTS.py SPECTRE.py

# O si queremos consultar por un archivo cuyo nombre contenga 7 caracteres y con extension.py:
$ echo ???????.py
SPECTRE.py

# Este tipo de expansiones son utiles en sentencias como la siguiente,
for file in *.HTM; do
.......
....





#
# 
#







#
# Sobre el comando GREP en BASH.
#
# NOTA: Para que el comando "grep" acepte todas las formas de expresion regular REGEX, hay que indicarle la opcion "-E".
#       Tambien, para que GREP devuelva el string que coincide con el patron buscado (no toda la fila!!) le indicamos "-o".
#       Ejemplo: Supongamos que queremos saber si la linea contiene un numero de telefono con un formato especifico y 
#                queremos que GREP nos devuelva el numero y solo el numero (no la linea completa leida),
#
$ echo "El numero es +34-618675423" | grep -E "\+[0-9]{2}\-[0-9]{9}" -o
+34-618675423







#
# Sobre la REDIRECCION usando STREAMS y PIPES.
#
# NOTA: En BASH (al igual que en otros shells de UNIX) existe la redireccion de STREAMS que se indica con ">", ">>", "<", "2>"
#       ">>" es append una salida hacia un archivo ya existente. ">" sobre escribe un archivo (elimina su contenido anterior). 
#       "2>" es la redireccion de la STDERR hacia un archivo (el "2" representa el File Descriptor de la salida de error estandar STDERR, 
#       siendo "0" la entrada estandar STDIN y "1" la salida estandar STDOUT).
#
# NOTA: Tambien existe la redireccion a traves de PIPES que involucra la comunicacion entre programas (PYTHON en el siguiente ejemplo 
#       pero pudiera ser con C, C++, etc). El "|" se utiliza para conectar la salida estandar STDOUT de un programa con la 
#       entrada estandar STDIN de otro programa.
#
# IMPORTANTE: PIPES permiten crear nuevos comandos a partir de comandos o programas individuales a traves de la conexion de 
#             la salida estandar STDOUT de programas con la entrada estandar STDIN de otros programas. Esta es la filosofia de trabajo 
#             originaria de UNIX!!!
#
$ cat archivo.txt | ./script.py   # <---- El contenido del archivo.txt es redireccionado desde la STDOUT hacia el script PYTHON.

# El script PYTHON de este ejemplo tiene el siguiente contenido:
#!/usr/bin/env python3

import sys

# En PYTHON podemos leer todas las filas del archivo.txt que provienen desde el comando "cat archivo.txt" a traves de un PIPE 
# usando el atributo "sys.stdin"!!
for line in sys.stdin:
    print(line.strip().capitalize())   # ".capitalize()" es un metodo de string que coloca en mayuscula la primera letra de la palabra.

# La operacion anterior tambien pudo haberse realizado con redireccion de STREAMS de la entrada estandar STDIN:
$ ./script.py < archivo.txt

# IMPORTANTE: Aqui es importante recordar que la redireccion de STREAMS es entre una fuente de datos (como ejemplo un archivo) y 
#             un comando, a diferencia de los PIPES que son la conexion entre la salida de un comando y la entrada a otro comando!!!

#
# IMPORTANTE: Como se dijo anteriormente BASH sigue la filosofia de UNIX sobre el armado de comandos complejos a partir 
#             de comandos y programas que realizan acciones simples. Veamos el siguiente ejemplo:
#
$ cat test.txt   # <---- El contenido de un archivo TXT cualquiera:
Esta es una prueba de linea de archivo

# Ahora armamos todo un "super comando" que hara varias cosas sobre la salida estandar STDOUT del comando "cat":
$ cat test.txt | tr ' ' '\n' | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head
      2 de
      1 una
      1 prueba
      1 linea
      1 esta
      1 es
      1 archivo

# Supongamos que queremos desarrollar un programa nativo (.exe, no script PYTHON) que lea desde una PIPE de salida de otro
# programa (como en el ejemplo anterior). Para esto creamos un fuente en lenguaje C o C++:

#include <iostream>

int main() {
        std::string linea = "";
        std::getline(std::cin, linea);   // La funcion "getline" puede leer la STDIN para recibir el mensaje enviado via PIPE.
        std::cout << linea;              // Luego, enviamos al STDOUT el mismo mensaje para que, via PIPE, lo lea otro programa.
        return 0;
}

# Compilamos este programa para crear el ejecutable que pudieramos llamar "test.exe". Ahora incluimos este programa dentro de 
# la secuencia de PIPES en el ejemplo anterior:
$ g++ -std=c++17 test.cpp -o test

# Repetimos el "super comando" incluyendo el programa nuevo:
$ cat test.txt | ./test | tr ' ' '\n' | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head
      2 de
      1 una
      1 prueba
      1 linea
      1 esta
      1 es
      1 archivo

# Esto mismo lo hubiesemos hecho usando un script PYTHON (no ejecutable .exe). El modulo SYS permite a un script PYTHON
# acceder la entrada estandar. La funcion "print()" permite enviar a la salida estandar STDOUT:
import sys

for line in sys.stdin:
   print(line.strip())   # <---- Usamos el metodo "strip()" para eliminar cualquier espacio blanco en los extremos del mensaje.

# Ahora ejecutamos igual que en el ejemplo anterior pero ahora invocando el script PYTHON:
$ cat test.txt | python test.py | tr ' ' '\n' | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head
      2 de
      1 una
      1 prueba
      1 linea
      1 esta
      1 es
      1 archivo


# Aqui hay otro ejemplo. Imaginemos que queremos obtener el nombre del proceso "ping" de la lista de procesos en curso:
$ ps ax
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     1886       1    1886      12836  ?         197609 21:11:24 /usr/bin/mintty
     1953    1952    1953      12452  pty1      197609 21:16:00 /usr/bin/bash
     2009    1887    2009       3132  pty0      197609 21:17:01 /usr/bin/ps
     1887    1886    1887        708  pty0      197609 21:11:25 /usr/bin/bash
     1994    1953    1994       7956  pty1      197609 21:16:43 /c/Windows/system32/ping
     1952       1    1952       2008  ?         197609 21:16:00 /usr/bin/mintty

# Ejecutamos el siguiente "super comando":
$ ps ax | awk '{print $8}' | tr '/' ' ' | awk '{print $4}' | grep -E 'ping'
ping

# Sobre el comando CUT.
#
# Otra manera de expresar la misma operacion anterior seria a traves del comando "cut". El comando CUT permite separar 
# un string en campos (dado un caracter separador que se repite en el string de entrada al comando) y devolver los campos 
# solicitados. En este ejemplo, CUT toma el string "/c/Windows/system32/ping". Como para metro le indicamos que el caracter separador 
# es "/". Entonces, CUT separa el string en: ' ' 'Windows' 'system32 y 'ping'. Con otro parametro le indicamos que queremos 
# el campo 5, es decir: el nombre de la aplicacion.
$ ps ax | grep -E "mintty" | awk '{print $8}' | cut -f5 -d"/"
ping



# Otro ejemplo de "super comando" BASH. Imaginemos que queremos buscar el process ID de un proceso especifico:
$ ps ax
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     1095       1    1095       7260  ?         197609 10:59:52 /usr/bin/mintty
     1195    1096    1195       5820  pty0      197609 11:03:34 /usr/bin/ps
     1096    1095    1096      11140  pty0      197609 10:59:52 /usr/bin/bash

user@DESKTOP-UGV9SAM MINGW64 ~/DEsktop
$ ps ax | grep -E "mintty" | awk '{print $1}'
1095


# En estos ejemplos anteriores vemos como en una sola linea de comando invocamos varios "mini comandos" para crear un "super comando".
# El comando "tr" traslada o transforma un caracter en otro. En este ejemplo "tr" toma la salida estandar STDOUT de "cat" y 
# reemplaza todos los espacios blancos por el caracter de nueva linea "\n". Luego, la salida estandar de "tr" es enviada a 
# otra invocacion del mismo comando "tr" ahora para reemplazar las mayusculas por minusculas. Esto se conecta con la entrada 
# estandar del comando "sort" que ordena alfabeticamente las palabras recibidas. Despues, se envia al comando "uniq -c" que 
# tomara sin duplicados cada palabra y las cuenta dando como resultado cada palabra acompanada de el numero de veces que aparece. 
# Esto ultimo se envia esto al comando "sort -nr" que ordena en reverso numericamente y alfanumericamente lo que recibe. Al final 
# se envia el resultado hacia el comando "head" que imprime las primeras lineas de todo lo que recibe. Esta es la filosofia de 
# UNIX!!!!



#
# El comando "less" permite navegar a traves de un listado de directorio o de archivo, una pagina a la vez.
#
# NOTA: Para navegar usamos las teclas PageUp, PageDown o las flechas. Tambien podemos hacer busquedas con "/<string>"
#
# Ejemplos:
cat archivo.txt | less

# Con este comando podemos revisar el contenido del archivo.txt. Inclusive, podemos buscar palabras o strings especificos:
:/<alguna secuencia de caracteres a buscar>

# Tambien podemos aplicar "less" a comandos como "ls -l" para revisar y buscar secuencias de caracteres dentro de un listado 
# de un directorio.
ls -l | less

# Para salir de "less" ejecutamos el comando "q":
:q





#
# Ejemplo de command substitution. Con esta tecnica es posible invocar un comando del Shell y que el resultado quede en el 
# mismo sitio donde aparece la invocacion. Tradicionalmente esto se hacia con `...`. Ahora en BASH puede hacerse con $(...).
#
# Primero lo hacemos con $(...).
~/bashWorks$ echo "Hoy $(date) es un dia nublado"
Hoy Wed 11 Oct 2023 05:39:34 PM UTC es un dia nublado

# Ahora en la manera tradicional `...`
~/bashWorks$ echo "Hoy `date` es un dia nublado"
Hoy Wed 11 Oct 2023 05:39:51 PM UTC es un dia nublado





#
# Ejemplo de uso de find y xargs para mover un archivo desde una carpeta hacia otra.
# funciona igual para el comando copy (cp).
#
# NOTA: El comando find tiene una opcion "-exec" que hace lo mismo que xargs como se muestra aqui:
#
#       find ./test -name "test.*" -exec mv {} . \;
#
find -name "test.cpp" | xargs -I {} mv {} ./test

find -name "test.cpp" | xargs -I {} cp {} ./test

# Ahora usando la opcion "-exec" de find:
find ./test -name "test.*" -exec mv {} . \;





#
# Como eliminar el historial del Shell?
#
~/bashWorks$ history -c





#
# Ejemplo de uso de los comandos find y xargs.
#
# IMPORTANTE: El comando find permite indicar varias condiciones de busqueda a traves de las opciones -and y -or!!
#

# Primero listamos el contenido del directorio de ejemplo.
~/bashWorks$ ls -la
total 16
drwxr-xr-x 1 runner runner   90 Oct 11 17:29 .
drwxrwxrwx 1 runner runner   70 Oct 11 17:38 ..
-rw-r--r-- 1 runner runner    0 Sep 12 16:35 3]
drwxr-xr-x 1 runner runner   12 Oct 12  2021 .cache
-rw-r--r-- 1 runner runner 1314 Oct 11 17:29 calculator.sh
-rw-r--r-- 1 runner runner 1411 Oct  8 05:45 main.sh
-rw-r--r-- 1 runner runner  260 Apr  7  2023 .replit
-rw-r--r-- 1 runner runner   56 Oct  8 11:04 replit.nix
~/bashWorks$ 

# Buscamos todos los archivos que ocupen mas de 1K y cuyo nombre tenga extension .sh. La salida del comando find se la aplicamos 
# al comando "ls -l" a traves del comando xargs!
#
~/bashWorks$ find . -size +1000c -and  -name "*.sh" | xargs ls -l
-rw-r--r-- 1 runner runner 1314 Oct 11 17:29 ./calculator.sh
-rw-r--r-- 1 runner runner 1411 Oct  8 05:45 ./main.sh










#
# Sobre los condicionales en BASH: TEST, "[]" e IF.
#
# NOTA: El comando "test" se ha utilizado en los SHELLs (desde 1981) para comprobar una condicion. "test" retorna 0 si 
#       la condicion se cumple y retorna 1 si no se cumple. Esto podemos ejemplificarlo a traves de "$?":
$ test 1 -eq 1

# Ahora comprobamos el valor de retorno del comando "test":
$ $?
bash: 0: command not found   # Retorno 0 ----> la condicion es verdadera!

# Hagamos una que es falsa:
$ test 1 -eq 2

# Comprobamos el valor de retorno:
$ $?
bash: 1: command not found   # Retorno 1 ----> la condicion es falsa!

#
# NOTA: Con el tiempo se incluyo en BASH la sintaxis "[]" que es equivalente a "test". El corchete que abre "[" es 
#       en realidad un comando en si mismo. Por este motivo es que, como regla sintactica, BASH exige rodear "[" y "]" 
#       con espacio blanco, tal y como ocurre con la sintaxis de un comando cualquiera.
#
$ [ 1 -eq 1 ]   # <---- Aqui el comando es "[" y sus argumentos son "1 -eq 1"
$ $?
bash: 0: command not found

$ [ 1 -eq 2 ]
$ $?
bash: 1: command not found

#
# NOTA: El comando "test" y su equivalente "[]" pueden usarse como argumento para el comando IF:
if test 1 -eq 1
o
if [ 1 -eq 1 ]

#
# NOTA: Sobre el IF en BASH. Como podemos ver, el IF acepta formato POSIX y no-POSIX (o viejo).
#       El siguiente es un ejemplo de formato no=POSIX pero que aun se usa mucho:
if [ -n "$PATH" ]; then 
   echo "Your path is not empty" 
fi

# NOTA: La opcion "-n" verifica que lo que viene a continuacion es no vacio!

# NOTA: Si queremos incluir una variable de ambiente en una condicion IF de BASH debemos encerrarla entre comillas para 
#       que el interprete pueda reconocerla como tal.

# NOTA: Otra manera de expresar la condicion de la sentencia IF anterior seria con el comando test:
if test -n "$PATH"......

# Mas adelante veremos ejemplos de IF mas complejos.


#
# NOTA: Tambien existe el operador de negacion "!" como en lenguaje C.
#
# Ejemplo: Supongamos que queremos consultar si existe un archivo en el directorio y mostrar mensaje si no existe. El 
#          archivo "test.py" no existe en el directorio para efectos de este ejemplo,
#
$ [ -f ./test.py ] && echo "Archivo no existe!"   # <---- La ejecucion de esta sentencia no devuelve valor alguno porque 
                                                  #       aqui estamos consultando si existe el archivo.
                                                  #       Observar que se utiliza el operador "&&" que condiciona la 
                                                  #       ejecucion del segundo comando a la ejecucion existosa del primero,
                                                  #       esto es: si se cumple [....] entonces ejecuta el comando "echo"!!!!

# Ahora ejecutamos la misma sentencia pero negando la condicion, es decir: que muestre mensaje si NO existe el archivo:
$ [ ! -f ./test.py ] && echo "Archivo no existe!"
Archivo no existe!


#
# NOTA: Dentro de un condicional es posible incluir la invocacion a un comando. En casos como esos, el comando invocado
#       retorna un valor como el "exit(x)" en languaje C/C++ o como el "sys.exit(x)" en PYTHON.
#
# Ejemplo: imaginemos que tenemos un SHELL script que recibe como argumento el nombre de un ejecutable (o script PYTHON),
$ ./el_shell_script.sh el_ejecutable

# Dentro del SHELL script tenemos lo siguiente:
comando=$1

if ! $comando; then ....   # <---- En este caso, "$comando" representa el parametro $1 pasado al script en curso, es decir
                           #       el ejecutable. Esta sentencia IF expande la variable "$comando" y el SHELL ejecuta el
                           #       programa para, luego, hacer la evaluacion del condicional.










# Sobre la diferencia entre la salida estandar (STDOUT) producida por un comando y el valor retornado por el comando.
#
# NOTA IMPORTANTE: En BASH los comandos producen dos cosas:
#
#                  1.- Una salida estandar (STDOUT)
#                  2.- Un valor de retorno que puede ser consultado a traves de la marca o variable de script "$?".
#
#
# IMPORTANTE: Hay una variante del IF en BASH: cuando el IF se escribe sin operadores de sustitucion [] y (), el IF verifica 
#             que el valor retornado existe o no. Esto es muy util para comprobar si un comando devuelve a traves de la STDOUT.
# Ejemplo:
#
$ if ls -l | grep -E "\w+\.py"; then echo "Consiguio"; else echo "NO consiguio"; fi

-rw-r--r-- 1 user 197121    6813 Jul 21 12:06 PYTHON_LINUX_COMMANDS_AND_SCRIPTS.py
-rw-r--r-- 1 user 197121  560574 Jul 21 12:24 SPECTRE.py
Consiguio

# MUY IMPORTANTE: En este ejemplo, BASH verifica si el "super comando" invocado produce una salida en STDOUT. Tambien pudiera 
#                 consultarse por el valor devuelto por el comando (que es diferente a la salida estandar STDOUT del comando) a traves 
#                 de la marca o variable de script "$?".












#
# Sobre los comandos "basename", "dirname" y la Parameter Expansion aplicada a nombres de archivos y directorios ${variable%pattern},
# ${variable##pattern}, ${variable%%pattern} y ${variable#pattern}.
#
# NOTA: "basename" y "dirname" vienen desde la epoca del BurnShell. Permiten, dada una ruta hacia un archivo, extraer la ruta 
#       de los directorios O el nombre del archivo con o sin su extension.
#
# Ejemplos:
$ basename nombre.html .html
nombre

$ dirname /the/path/foo.txt
/the/path

# Luego, tenemos la llamada Pattern Substitution a traves de la cual obtenemos mismo resultado que en los comandos anteriores:
$ s=/the/path/foo.txt   # <---- Definimos una variable SHELL con la ruta completa hacia un archivo.

$ echo "${s##*/}"       # <---- Esta Parameter Espansion hace un trim desde el comienzo del string hasta el ultimo "/"
foo.txt                 # <---- Obtenemos el nombre del archivo!

# NOTA: La siguiente descripcion es tomada de: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02
#
# Those are the # and the % operators. We also see them used as single characters and in pairs. This gives us four 
# combinations for trimming patterns off the beginning or end of a string:
#
# ${variable%pattern}     Trim the shortest match from the end 
# ${variable##pattern}    Trim the longest match from the beginning 
# ${variable%%pattern}    Trim the shortest match from the end 
# ${variable#pattern}     Trim the shortest match from the beginning 
#
# It's important to understand that these use shell "globbing" rather than "regular expressions" to match these patterns.











#
# Ejemplo de una funcion recursiva en BASH. En este ejemplo se puede ver el uso de if else fi con condicion compuesta. 
# Tambien puede verse un ejemplo de command substitution $(...) la cual pudiera hacerse del modo tradicional `...`.
#
# IMPORTANTE: Declaraciones de funciones como esta pueden hacerse DIRECTAMENTE en la linea de comandos BASH.
#

# Primero expresamos la sentencia if con las condiciones al viejo estilo (no POSIX).
function fib() {
    if [ $1 -eq 0 -o $1 -eq 1 ]; then
        echo $1
    else
        echo $[ `fib $[$1-2]` + `fib $[$1 - 1]` ]
    fi
}


# Ahora expresamos al estilo POSIX actual. La palabra "function" puede omitirse.
fib() {
    if [[ $1 == 0 ]] || [[ $1 == 1 ]]; then
        echo $1
    else
        echo $[ $(fib $[$1-2]) + $(fib $[$1 - 1]) ]
    fi
}

# Veamos ahora como invocar esta funcion desde la linea de comandos
~/bashWorks$ fib 7
13








#
# NOTA IMPORTANTE: SOBRE LOS OPERADORES DE SUSTITUCION ARITMETICA.
#
# En el ejemplo de funcion anterior se utiliza el operador de expansion aritmetica viejo (no POSIX) $[...].
#
# A continuacion una explicacion de dicho operador y otros operadores de sustitucion y comparacion.
#
# Tomado de https://askubuntu.com/questions/939294/difference-between-let-expr-and
#
# $((...)) is called arithmetic expansion, which is typical of the bash and ksh shells. This allows doing simple integer arithmetic, 
# no floating point stuff though. The result of the expression replaces the expression, as in echo $((1+1)) would become echo 2
#
# ((...)) is referred to as arithmetic evaluation and can be used as part of if ((...)); then or while ((...)) ; do statements. 
# Arithmetic expansion $((..)) substitutes the output of the operation and can be used to assign variables as in i=$((i+1)) 
# but cannot be used in conditional statements.
# IMPORTANTE: En el arithmetic evaluation (()) las variables (creadas dentro del script o linea de comandos BASH) se escriben SIN el
#             caracter "$"!!!!
#             Ejemplo: ((n+=1))
#
# $[...] is the old syntax for arithmetic expansion which is deprecated. See also. This was likely kept so that old bash scripts don't break. 
# This didn't work in ksh93, so my guess is that this syntax is bash-specific. 
# NOTE: spaces are very important here; don't confuse $[1+1] with stuff like [ $a -eq $b ]. 
# The [ with spaces is known as the test command, and you typically see it in decision-making parts. It is very different in behavior and purpose.
#
# let is a bash and ksh keyword which allows for variable creation with simple arithmetic evaluation. 
# If you try to assign a string there like let a="hello world" you'll get a syntax error. Works in bash and ksh93.
#
# $(...) is command substitution, where you literally take the output of a command and assign to a variable. 
# Your command here is expr, which takes positional arguments, like expr arg1 arg2 arg3, so spaces are important. 
# It's sort of like a small command-line calculator for integer arithmetic, plus some true/false and regex type of stuff. This is a shell-neutral command.
#
# IMPORTANTE: Ver el estandar POSIX:
# https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html
#
# Ahora expresamos la funcion del ejemplo anterior usando el operador de expansion aritmetico POSIX $((...)):

function fib() {
    if [ $1 == 0 ] || [ $1 == 1 ]; then
        echo $1
    else
        # Se reemplaza el operador antiguo $[...] por el POSIX $((...)).
        echo $(( $(fib $(($1-2))) + $(fib $(($1-1))) ))
    fi
}

#!/bin/bash

fib() {
        if (( $1 == 0 || $1 == 1 )); then
        echo "$1"
        else
        echo $(( $(fib $(($1-2))) + $(fib $(($1-1))) ))
        fi
}





#
# Ejemplo de ciclo WHILE en BASH.
#
$ f() { if(($1 == 0 || $1 == 1)); then echo $1; else echo $(($(f $(($1-2))) + $(f $(($1-1))))); fi }

$ n=1 && while((n < 8)); do echo "Fibonacci de $n = $(f $n)"; ((n+=1)); done
Fibonacci de 1 = 1
Fibonacci de 2 = 1
Fibonacci de 3 = 2
Fibonacci de 4 = 3
Fibonacci de 5 = 5
Fibonacci de 6 = 8
Fibonacci de 7 = 13








#
# Ejemplo de ciclo FOR en BASH.
#
# NOTA IMPORTANTE: El ciclo FOR en BASH tiene dos variantes,
#
#                  for ((........)); do ....; done
#
#                  for i in xxx yyy zzz; do ....; done    <---- En esta variante los elementos deben ir separados por espacio!!!
#
# Veamos un ejemplo de la primera forma del FOR:
#
# Vamos a definir una funcion Fibonacci. Usamos (como ejemplo) la sintaxis no-POSIX vieja, solo como ejemplo...
f() {
   if [ $1 -eq 0 -o $1 -eq 1 ]; then
      echo $1
   else
      echo $[ `f $[ $1-2 ]` + `f $[ $1-1 ]` ]
   fi
}

# Ahora iteramos entre los primeros nueve numeros naturales para mostrar su Fibonacci.
$ for ((i=1; i < 9; i++))
> do
> echo $(f $i)
> done

# Resultado,
1
1
2
3
5
8
13
21

#
# Veamos ahora un ejemplo de la segunda forma del FOR:
#
$ for fruta in peach orange pear; do
> echo "Me gusta la $fruta"
> done
Me gusta la peach
Me gusta la orange
Me gusta la pear

# Otro ejemplo de esta segunda variante:
for file in *.HTM; do
        name=$(basename "$file" .HTM)
        mv "$file" "$name.html" 
done

# Otro ejemplo de esta segunda variante. Esta vez, supongamos que los elementos a iterar no vienen separados por espacio:
$ lista="uno/dos/tres/cuatro/cinco"   # <---- Elementos separados por "/". Hay que convertir ese separador en " ".

# Utilizamos el comando "tr" para transformar el separador "/" en " ".
$ for nombre in $(echo $lista | tr '/' ' '); do echo $nombre; done   # <---- Observar que la sentencia FOR puede contener la
                                                                     #       ejecucion de un comando SHELL, en este caso el 
                                                                     #       "super comando": echo $lista | tr '/' ' '
uno
dos
tres
cuatro
cinco












#
# BASH permite el uso de PRINTF. Veamos un ejemplo.
#
i=2

printf "i = %d" $i

# resultado:
i = 2







#
# Ejemplo de uso de AWK para imprimir lista de campos del comando "ls -l" pero con un separador indicado con Output Field Separator (OFS).
#
ls -l | awk 'OFS="  -+-  " {print $1,$6,$9}'

Resultado,

-rw-r--r--  -+-  Sep  -+-  hilos.cs
drwxr-xr-x  -+-  Nov  -+-  javaGit/
-rw-r--r--  -+-  Dec  -+-  javascript.html
-rw-r--r--  -+-  Aug  -+-  jsonEjercicio.json
-rw-r--r--  -+-  Aug  -+-  jsonTest.json
-rw-r--r--  -+-  Aug  -+-  jsontest.html
-rw-r--r--  -+-  Feb  -+-  lambda.cpp
drwxr-xr-x  -+-  Nov  -+-  lisp/
-rw-r--r--  -+-  Oct  -+-  lispy.cpp
-rw-r--r--  -+-  Nov  -+-  nodef.js
-rw-r--r--  -+-  Nov  -+-  numeros.h












#
# Ejemplo de impresion de un subconjunto de "ls -l" cuyos elementos tengan un tamano mayor que 3000.
#
ls -l | awk '($5 > 3000) {print $0}'







#
# Ejemplo de impresion del contenido de un archivo CSV indicandole a AWK que el caracter separador es ";".
#
# IMPORTANTE: Observar que el caracter ";" tambien es el separador de comandos en BASH. Por tal motivo hay que usar el 
#             el caracter de escape:
#
$ awk -F\; '{print $1,$2}' test.csv

Salida,

campo1 campo2
00001 00002










#
# Como formatear la salida del comando DATE.
#
$ date +"%d-%m-%Y"   # <---- Aqui la letra "Y" en mayuscula muestra el ano con 4 caracteres (XXXX)!!
22-07-2024

$ date +"%d-%m-%y"   # <---- Aqui la letra "y" en minuscula muestra el ano con 2 caracteres (XX)!!
22-07-24


# NOTA: La sentencia anterior pudiera usarse dentro de un script BASH:
FECHA=$(date +"%d-%m-%Y")








#
# Script con ejemplos BASH.
#
#!/bin/bash
echo ""
echo "Ejemplos de BASH:"
echo "----------------"
age=56

if [ "$age" -eq 56 ]
then
   echo "Es igual!"
else
   echo "No es igual!"
fi

echo ""

ps -l | awk '{print $1 "-" $3}'

echo""

cat /etc/shells | awk -F "/" '{print $NF}'

if [ "$age" -gt 60 ]; then
   echo "Mayor que 60!"
else
   echo "No es mayor que 60!"
fi

# Ejemplo de calculo aritmetico.
x=16
y=10

let z=$(($x+$y))

printf '\n\nResultado z: %d\n\n' $z


if (( $# < 3 )) 
then
   printf 'argumentos son: %d %d\n\n' $1 $2
fi

# Ejemplo de case.
case $1 in
   10) echo "Es diez!"
       ;;
   20) echo "Es veinte!"
       ;;
   30) echo "Es treinta!"
       ;;
esac

echo ""

# Ejemplo de manejo de archivos desde Bash.
echo "ESTE ES UN TEXTO DE PRUEBA" > /home/runner/bashWorks/prueba.txt

ARCH=/home/runner/bashWorks/prueba.txt

if [ -e "$ARCH" ]
then
   echo "Existe el archivo prueba.txt y su contenido es: "
   echo ""
   cat ./prueba.txt
   rm /home/runner/bashWorks/prueba.txt
fi


printf '\n\n\n\n'

#
# Tambien puede expresar la siguiente sentencia como: awk 'BEGIN { x = 2; y = 3; print "x + y = "(x+y) }'.
#
awk 'BEGIN { 
        x = 2; 
        y = 3; 

        print "x + y = "(x+y) 
     }'


#
# Ejemplo de paso de argumentos a AWK. ARGV[0] es la palabra awk, ARGV[1] seria el primer argumento 2, etc.
#
awk 'BEGIN { print ARGV[1] + ARGV[2] }' 2 3


#
# Otro ejemplo de manejo de argumentos en AWK. La variable ARGC contiene el conteo de argumentos.
BEGIN {
    printf "A=%d, B=%d\n", A, B
    for (i = 0; i < ARGC; i++)
        printf "\tARGV[%d] = %s\n", i, ARGV[i]
}
END   { printf "A=%d, B=%d\n", A, B }


Running it produces the following:

$ awk -v A=1 -f showargs.awk B=2 /dev/null
-| A=1, B=0
-|        ARGV[0] = awk
-|        ARGV[1] = B=2
-|        ARGV[2] = /dev/null
-| A=1, B=2






/* ----------------------------------------------------------------------------- *
 * Ejemplo de ejecucion del Bash script anterior desde un programa C++ en Linux. *
 * ----------------------------------------------------------------------------- */
#include<stdlib.h>
.....
...
..

  int resp = system("bash script.sh 2 3");






#
# Otro ejemplo de case.
#
echo "Welcome to the Calculator in BASH"
echo "================================="
echo " "

PS3="Enter your choice:"

options=("float" "trig" "log" "exp" "exit")

select choice in "${options[@]}"
do
   case $choice in
      "float") echo "Enter expression: "
		     read exp	
		     #cal()
			   awk "BEGIN{print $*}";	 
		     #echo "Answer: " `cal $exp`
		     ;;

	    "trig") echo "Enter Trigonometric function : "
			   read exp
			   echo "Degree: "
			   read degree 
         e=$(awk "BEGIN{print $exp($degree*atan2(0,-1)/180)}") 
			   echo "$exp($degree)= $e"
			   ;;

      "log") echo "Enter the logarithmic value: "
			   read value 
			   echo $value | awk '{printf "%11.9f\n",log($1)/log(10)}'
			   ;;

      "exp") echo "Enter the base number x: "	
         read x 
         echo "Enter exponent number y: "
         read y 
         E=$(echo "$x 1" | awk "{print (($x/1)^$y)}") 
         echo "$x^$y = $E"
         ;;
      "exit") break 2
         ;;
      *) echo "Invalid option"
   esac
done









#
# USar AWK para encontrar algun string dentro de un archivo.
#
# IMPORTANTE: El caracter "~" significa que tal cosa es equivalente a otra cosa como se ve en el ejemplo.
#
# Este ejemplo busca el string "prueba" en todas las filas dentro de un archivo y muestra las filas.
awk '$0 ~ /prueba/' vectores.cpp

Resultado:

} prueba;
   prueba estPrueba;
   prueba *apuntador;

# El comando anterior es equivalente a,
awk '{ if ($0 ~ /prueba/) print }' vectores.cpp








#
# Mas ejemplos AWK tomados de,
# https://www.math.utah.edu/docs/info/gawk_4.html#SEC24
#
Many useful awk programs are short, just a line or two. Here is a collection of useful, short programs to get you started. 
Some of these programs contain constructs that haven't been covered yet. The description of the program will give you a good idea of what is going on, 
but please read the rest of the book to become an awk expert!

Most of the examples use a data file named `data'. This is just a placeholder; if you were to use these programs yourself, 
you would substitute your own file names for `data'.

awk '{ if (length($0) > max) max = length($0) }
END { print max }' data
    This program prints the length of the longest input line. 

awk 'length($0) > 80' data
    This program prints every line that is longer than 80 characters. The sole rule has a relational expression as its pattern, 
    and has no action (so the default action, printing the record, is used). 

expand data | awk '{ if (x < length()) x = length() }
END { print "maximum line length is " x }'
    This program prints the length of the longest line in `data'. The input is processed by the expand program to change tabs into spaces, 
    so the widths compared are actually the right-margin columns. 

awk 'NF > 0' data
    This program prints every line that has at least one field. This is an easy way to delete blank lines from a file 
    (or rather, to create a new file similar to the old file but from which the blank lines have been deleted). 

awk 'BEGIN { for (i = 1; i <= 7; i++)
print int(101 * rand()) }'
    This program prints seven random numbers from zero to 100, inclusive. 

ls -lg files | awk '{ x += $5 } ; END { print "total bytes: " x }'
    This program prints the total number of bytes used by files. 

ls -lg files | awk '{ x += $5 }
END { print "total K-bytes: " (x + 1023)/1024 }'
    This program prints the total number of kilobytes used by files. 

awk -F: '{ print $1 }' /etc/passwd | sort
    This program prints a sorted list of the login names of all users. 

awk 'END { print NR }' data
    This program counts lines in a file. 

awk 'NR % 2' data
    This program prints the even numbered lines in the data file. If you were to use the expression `NR % 2 == 1' instead, it would print the odd number lines. 














#
#
#                                        SECCION DE EJEMPLOS C# .NET                                             #
#
#
# NOTA: Debe incluir en la variable PATH del ambiente la ruta hacia el .NET Framework. Ejemplo,
#       C:\Windows\Microsoft.NET\Framework64\v4.0.30319
#
#       Debe reinicar el sistema.
#
# NOTA: Para compilar un programa C# debe usar el comando,
#
#       csc nombreDelPrograma.cs
#
#       La compilacion generara un ejecutable (.exe) a diferencia de la compilacion en JAVA el cual genera un archivo conteniendo
#       pcodes o bytecodes.
#
# NOTA: Existe tambien el comando dotnet con varias opciones como "run".
#
# NOTA: Puede instalar un REPL de C# con el siguiente comando:
#
#       dotnet tool install -g csharprepl
#
#       Luego, para invocar el REPL,
#
#       csharprepl
#

/* ------------------------------------------- *
 * Ejemplo de LAMBDA function recursiva en C#. *
 * ------------------------------------------- */
using System;

class Program {
  public static void Main (string[] args) {
    // Declaracion de una funcion con un parametro y una salida int.
    Func<int, int> genFun = null;

    // Definicion de la funcion generica como fibonacci.
    genFun = (x) => x == 0 || x == 1? x : genFun(x - 1) + genFun(x - 2);
    Console.WriteLine(genFun(7));

    // Redefinicion de la funcion generica de ejemplo.
    genFun = (x) => x*x;
    Console.WriteLine(genFun(4));

    // Declaracion de una funcion con dos parametros y una salida int.
    Func<int, int, int> genFunS = null;

    // Definicion de la funcion generica segunda como suma de dos enteros.
    genFunS = (x, y) => x+y;

    Console.WriteLine(genFunS(3, 2));
  }
}




/* -------------------------------------------------------------------------------------------------------------- *
 * Ejemplo de codigo IL generado por el Visual Studio 2022 de un ejemplo de la funcion generica recursiva genFun, *
 *                                                                                                                *
 * internal class Program                                                                                         *
 * {                                                                                                              *
 *    private static void Main(string[] args)                                                                     *
 *    {                                                                                                           *
 *       Func<int, int> genFun = null;                                                                            *
 *                                                                                                                *
 *       genFun = (x) => x == 0 || x == 1 ? x : genFun(x - 1) + genFun(x - 2);                                    *
 *    }                                                                                                           *
 * }                                                                                                              *
 * -------------------------------------------------------------------------------------------------------------- */
// =============== CLASS MEMBERS DECLARATION ===================

.class private auto ansi sealed beforefieldinit Microsoft.CodeAnalysis.EmbeddedAttribute extends [System.Runtime]System.Attribute
{
  .custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = ( 01 00 00 00 ) 
  .method public hidebysig specialname rtspecialname instance void  .ctor() cil managed
  {
    // Code size       8 (0x8)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [System.Runtime]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ret
  } // end of method EmbeddedAttribute::.ctor

} // end of class Microsoft.CodeAnalysis.EmbeddedAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.NullableAttribute extends [System.Runtime]System.Attribute
{
  .custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void [System.Runtime]System.AttributeUsageAttribute::.ctor(valuetype [System.Runtime]System.AttributeTargets) = ( 01 00 84 6B 00 00 02 00 54 02 0D 41 6C 6C 6F 77   // ...k....T..Allow
                                                                                                                                     4D 75 6C 74 69 70 6C 65 00 54 02 09 49 6E 68 65   // Multiple.T..Inhe
                                                                                                                                     72 69 74 65 64 00 )                               // rited.
  .field public initonly uint8[] NullableFlags
  .method public hidebysig specialname rtspecialname instance void  .ctor(uint8 A_1) cil managed
  {
    // Code size       24 (0x18)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [System.Runtime]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ldarg.0
    IL_0008:  ldc.i4.1
    IL_0009:  newarr     [System.Runtime]System.Byte
    IL_000e:  dup
    IL_000f:  ldc.i4.0
    IL_0010:  ldarg.1
    IL_0011:  stelem.i1
    IL_0012:  stfld      uint8[] System.Runtime.CompilerServices.NullableAttribute::NullableFlags
    IL_0017:  ret
  } // end of method NullableAttribute::.ctor

  .method public hidebysig specialname rtspecialname instance void  .ctor(uint8[] A_1) cil managed
  {
    // Code size       15 (0xf)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [System.Runtime]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ldarg.0
    IL_0008:  ldarg.1
    IL_0009:  stfld      uint8[] System.Runtime.CompilerServices.NullableAttribute::NullableFlags
    IL_000e:  ret
  } // end of method NullableAttribute::.ctor

} // end of class System.Runtime.CompilerServices.NullableAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.NullableContextAttribute extends [System.Runtime]System.Attribute
{
  .custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void [System.Runtime]System.AttributeUsageAttribute::.ctor(valuetype [System.Runtime]System.AttributeTargets) = ( 01 00 4C 14 00 00 02 00 54 02 0D 41 6C 6C 6F 77   // ..L.....T..Allow
                                                                                                                                     4D 75 6C 74 69 70 6C 65 00 54 02 09 49 6E 68 65   // Multiple.T..Inhe
                                                                                                                                     72 69 74 65 64 00 )                               // rited.
  .field public initonly uint8 Flag
  .method public hidebysig specialname rtspecialname instance void  .ctor(uint8 A_1) cil managed
  {
    // Code size       15 (0xf)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [System.Runtime]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ldarg.0
    IL_0008:  ldarg.1
    IL_0009:  stfld      uint8 System.Runtime.CompilerServices.NullableContextAttribute::Flag
    IL_000e:  ret
  } // end of method NullableContextAttribute::.ctor

} // end of class System.Runtime.CompilerServices.NullableContextAttribute

.class private auto ansi beforefieldinit Program extends [System.Runtime]System.Object
{
  .class auto ansi sealed nested private beforefieldinit '<>c__DisplayClass0_0' extends [System.Runtime]System.Object
  {
    .custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
    .field public class [System.Runtime]System.Func`2<int32,int32> genFun
    .method public hidebysig specialname rtspecialname instance void  .ctor() cil managed
    {
      // Code size       8 (0x8)
      .maxstack  8
      IL_0000:  ldarg.0
      IL_0001:  call       instance void [System.Runtime]System.Object::.ctor()
      IL_0006:  nop
      IL_0007:  ret
    } // end of method '<>c__DisplayClass0_0'::.ctor

    .method assembly hidebysig instance int32 '<Main>b__0'(int32 x) cil managed
    {
      // Code size       40 (0x28)
      .maxstack  8
      IL_0000:  ldarg.1
      IL_0001:  brfalse.s  IL_0026
      IL_0003:  ldarg.1
      IL_0004:  ldc.i4.1
      IL_0005:  beq.s      IL_0026
      IL_0007:  ldarg.0
      IL_0008:  ldfld      class [System.Runtime]System.Func`2<int32,int32> Program/'<>c__DisplayClass0_0'::genFun
      IL_000d:  ldarg.1
      IL_000e:  ldc.i4.1
      IL_000f:  sub
      IL_0010:  callvirt   instance !1 class [System.Runtime]System.Func`2<int32,int32>::Invoke(!0)
      IL_0015:  ldarg.0
      IL_0016:  ldfld      class [System.Runtime]System.Func`2<int32,int32> Program/'<>c__DisplayClass0_0'::genFun
      IL_001b:  ldarg.1
      IL_001c:  ldc.i4.2
      IL_001d:  sub
      IL_001e:  callvirt   instance !1 class [System.Runtime]System.Func`2<int32,int32>::Invoke(!0)
      IL_0023:  add
      IL_0024:  br.s       IL_0027
      IL_0026:  ldarg.1
      IL_0027:  ret
    } // end of method '<>c__DisplayClass0_0'::'<Main>b__0'

  } // end of class '<>c__DisplayClass0_0'

  .method private hidebysig static void  Main(string[] args) cil managed
  {
    .entrypoint
    .custom instance void System.Runtime.CompilerServices.NullableContextAttribute::.ctor(uint8) = ( 01 00 01 00 00 ) 
    // Code size       33 (0x21)
    .maxstack  3
    .locals init (class Program/'<>c__DisplayClass0_0' V_0)
    IL_0000:  newobj     instance void Program/'<>c__DisplayClass0_0'::.ctor()
    IL_0005:  stloc.0
    IL_0006:  nop
    IL_0007:  ldloc.0
    IL_0008:  ldnull
    IL_0009:  stfld      class [System.Runtime]System.Func`2<int32,int32> Program/'<>c__DisplayClass0_0'::genFun
    IL_000e:  ldloc.0
    IL_000f:  ldloc.0
    IL_0010:  ldftn      instance int32 Program/'<>c__DisplayClass0_0'::'<Main>b__0'(int32)
    IL_0016:  newobj     instance void class [System.Runtime]System.Func`2<int32,int32>::.ctor(object, native int)
    IL_001b:  stfld      class [System.Runtime]System.Func`2<int32,int32> Program/'<>c__DisplayClass0_0'::genFun
    IL_0020:  ret
  } // end of method Program::Main

  .method public hidebysig specialname rtspecialname instance void  .ctor() cil managed
  {
    // Code size       8 (0x8)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [System.Runtime]System.Object::.ctor()
    IL_0006:  nop
    IL_0007:  ret
  } // end of method Program::.ctor
} // end of class Program








/* ----------------------------------------------------------------- *
 * Ejemplo de creacion y uso de una lista (vector) de objetos en C#. *
 * ----------------------------------------------------------------- */
using System;
using System.Collections.Generic;

namespace fib {
    // Clase ejemplo.
    class punto {
        public punto() {}
        public int getX() { return(this.x); }
        public int getY() { return(this.y); }

        public int x;
		public int y;
	}

	// Class declaration
	class fibonacci {
        /* ------------------------------------------------- *
         * Funcion que devuelve el fibonacci de un entero x. *
         * ------------------------------------------------- */
        static int fib(int x) {
           if(x == 0 || x == 1) return(x);
           return(fib(x - 1) + fib(x - 2));
        }

		// Main Method
		static void Main(string[] args) {
            //punto miPunto = new punto(3, 2);

            // Definicion de una lista (vector) cuyos elementos son instancias de la clase de ejemplo.
            List<punto> miLista = new List<punto>() 
            {
                new punto{x=1, y=2},
                new punto{x=3, y=4},
                new punto{x=5, y=6}
			   };

            // Ejemplo de iteracion a traves de la lista (vector).
            foreach (var i in miLista)
			   {
                Console.WriteLine("X:" + i.getX() + ", Y: " + i.getY());
			   }

			Console.WriteLine("El Fibonacci de 7 es " + fib(7));
			
			// Console.ReadKey();
		}
	}
}


/* ----------------------------------- *
 * Ejemplo de creacion de hilos en C#. *
 * ----------------------------------- */
using System;
using System.Threading;

class Program
{
	static void Main()
	{
		// create a new thread
		Thread t = new Thread(Worker);

		// start the thread
		t.Start();

		// do some other work in the main thread
		for (int i = 0; i < 10; i++)
		{
			Console.WriteLine("Main thread doing some work");
			Thread.Sleep(100);
		}

		// wait for the worker thread to complete
		t.Join();

		Console.WriteLine("Done");
	}

	static void Worker()
	{
		for (int i = 0; i < 10; i++)
		{
			Console.WriteLine("Worker thread doing some work");
			Thread.Sleep(100);
		}
	}
}










/* ------------------------------------------------------------------------------------------------------------------------ *
 *                                                SECCION DE EJEMPLOS EN RUST                                               *
 *                                                                                                                          *
 * Para compilar se utiliza el comando "rustc" seguido del nombre del fuente .rs                                            *
 * ------------------------------------------------------------------------------------------------------------------------ */

/* ------------------------------------- *
 * Ejemplo de funcion recursiva en RUST. *
 * ------------------------------------- */
pub fn fib(x: u32) -> u32 {
    if x == 0 || x == 1 { return x; } else { return fib(x - 1) + fib(x - 2); }
}

fn main() {
    println!("El fibonacci de 7 es: {}", fib(7));
}








/* ------------------------------------------------------------------------------------------------------------------------ *
 *                                              SECCION DE EJEMPLOS EN KOTLIN                                               *
 *                                                                                                                          *
 * NOTA: Para compilar el fuente (en UBUNTU) de este ejemplo debe usar el siguiente comando,                                *
 *                                                                                                                          *
 *       kotlinc main.kt -include-runtime -d main.jar                                                                       *
 *                                                                                                                          *
 *       El resultado es un archivo main.jar listo para poder ejecutarse con el Java Virtual Machine con el siguiente,      *
 *                                                                                                                          *
 *       java -jar main.jar                                                                                                 *
 *                                                                                                                          *
 * IMPORTANTE: Es de hacer notar que el archivo .jar generado con kotlinc es grande en tamano porque incluye el runtime     *
 *             de Kotlin. Existe otra forma de compilacion que genera un .jar mas pequeno,                                  *
 *                                                                                                                          *
 *             kotlinc -d main.jar main.kt                                                                                  *
 *                                                                                                                          *
 *             Ahora puede ejecutar con el comando,                                                                         *
 *             kotlin -classpath main.jar MainKt                                                   *
 *                                                                                                                          *
 * NOTA: Kotlin tambien tiene un REPL que se ejecuta con el siguiente comando,                                              *
 *                                                                                                                          *
 *       kotlinc-jvm                                                                                                        *
 *       Welcome to Kotlin version 1.7.20 (JRE 17.0.4+8-nixos)                                                              *
 *       Type :help for help, :quit for quit                                                                                *
 *       >>> 3+2                                                                                                            *
 *       res0: kotlin.Int = 5                                                                                               *
 *       >>> :quit                                                                                                          *
 * ------------------------------------------------------------------------------------------------------------------------ */

/* ---------------------------------------------------- *
 * Ejemplo de LAMBDA expressions y funciones en Kotlin. *
 * ---------------------------------------------------- */
fun main() {
    //fun pow(x: Int) : Int =  x*x
    lateinit var funVar : (Int) -> Int
    funVar = { if (it == 0 || it == 1) it else funVar(it-1) + funVar(it-2) }

    (1..7).map(funVar).forEach(::println)

    //println("fib(7)= " + funVar(7) + " y pow(2)= " + pow(2))
}











#
#
#                                        SECCION DE EJEMPLOS R Language                                           #
#
#
# NOTA: Para ejecutar un script R desde la linea de comandos Linux,
#
#       R -f main.r
#

##
## Ejemplo de una funcion recursiva en R.
##
recursive.fib <- function(x) { if(x == 0 || x == 1) return(x); return(recursive.fib(x - 1) + recursive.fib(x - 2)) }

## Invocacion,
> recursive.fib(7)
[1] 13




##
## Ejemplo de vectores en R.
##
> A <- c(2.3, 5.4, 3.0)
> A
[1] 2.3 5.4 3.0
> B <- c(1.0, 2.0, 3.0)
> C <- 2 * A
> C
[1]  4.6 10.8  6.0
> 
> D <- A + B
> D
[1] 3.3 7.4 6.0

## Ejemplo de una funcion recursiva.
recursive.fib <- function(x) { if(x == 0 || x == 1) return(x); return(recursive.fib(x - 1) + recursive.fib(x - 2)) }

# Ejemplo de imprimir mensajes y resultados.
sprintf("fib(7) = %d", recursive.fib(7))


##
## Creacion de arreglos multidimensionales.
## Create two vectors of different lengths. 
##
vector1 <- c(5, 9, 3) 
vector2 <- c(10, 11, 12, 13, 14, 15) 

## Aqui se creara un array de 2 matrices cada una de tres 
## filas y tres columnas.
# Take these vectors as input to the array. 
result <- array(c(vector1, vector2), dim = c(3, 3, 2)) 
print(result) 

## Otro ejemplo:
## Create two vectors of different lengths. 
##
vector1 <- c(5, 9, 3) 
vector2 <- c(10, 11, 12, 13, 14, 15) 
column.names <- c("COL1", "COL2", "COL3") 
row.names <- c("ROW1", "ROW2", "ROW3") 
matrix.names <- c("Matrix1", "Matrix2") 

# Take these vectors as input to the array. 
result <- array(c(vector1, vector2), dim = c(3, 3, 2), 
				dimnames = list(row.names, column.names, 
				matrix.names)) 
print(result) 


# Histogram for Maximum Daily Temperature 
data(airquality) 

hist(airquality$Temp, main ="La Guardia Airport's\ 
Maximum Temperature(Daily)", 
  xlab ="Temperature(Fahrenheit)", 
  xlim = c(50, 125), col ="yellow", 
  freq = TRUE) 


# Adding Titles and Labeling Axes to Plot 
cone <- function(x, y){ 
sqrt(x ^ 2 + y ^ 2) 
} 

# prepare variables. 
x <- y <- seq(-1, 1, length = 30) 
z <- outer(x, y, cone) 

# plot the 3D surface 
# Adding Titles and Labeling Axes to Plot 
persp(x, y, z, 
main="Perspective Plot of a Cone", 
zlab = "Height", 
theta = 30, phi = 15, 
col = "orange", shade = 0.4)










#
#
#                                        SECCION DE EJEMPLOS WOLFRAM Language                                           #
#
# NOTA: Esta prueba se ha hecho con WOLFRAM CLOUD
#
#       Para ejecutar un programa WOLFRAM Language debe presionar Shift + Enter
#
"Esta es una prueba de numeros complejos:"
z =Complex[3, 2]
t = Complex[4, 4]
r = z + t
Print[r]

"Esta es una prueba de funcion recursiva que devuelve el Fibonacci de un numero x:"
f[x_] = If[x == 0 || x == 1, x, f[x-1] + f[x-2]]

"La funcion Fibonacci aplicada a una lista de numeros:"
Map[f,{0, 1, 2, 3, 4, 5, 6, 7,8, 9}]

"Prueba de For y Print:"
For[i = 1; t = x, i^2 < 10, i++, t = t^2 + i; Print[t]]
For[i = 0, i < 10, i++, Print[f[i]]]

"Prueba de grafico:"
q[x_] = x^2
Plot[q[x], {x,0, 10}]

Plot3D[Sin[x + y^2], {x, -3, 3}, {y, -2, 2}]

RevolutionPlot3D[{2 + Cos[t], Sin[t]}, {t, 0, 2 Pi}]

ParametricPlot3D[{{4 + (3 + Cos[v]) Sin[u], 4 + (3 + Cos[v]) Cos[u], 4 + Sin[v]}, {8 + (3 + Cos[v]) Cos[u], 3 + Sin[v], 4 + (3 + Cos[v]) Sin[u]}}, {u, 0, 2 Pi}, {v, 0, 2 Pi}, PlotStyle -> {Red, Green}]

Plot3D[{x^2 + y^2, -x^2 - y^2}, {x, -2, 2}, {y, -2, 2}, ColorFunction -> "RustTones"]

StreamPlot[{-1 - x^2 + y, 1 + x - y^2}, {x, -3, 3}, {y, -3, 3}, PlotLegends -> Automatic]

Histogram[Table[StringLength[RomanNumeral[n]] / IntegerLength[n], {n, 1000}]]

"Ejemplo de geometria: poligonos."
ngon[p_, q_] := Polygon[Table[{Cos[2 Pi k q/p], Sin[2 Pi k q/p]}, {k, p}]]
Row[Table[ Graphics[{EdgeForm[Black], LightRed, ngon[n, 1]}, ImageSize -> 70], {n, 3, 14}]]

h[x_, y_] := Polygon[Table[{Cos[2 Pi k/6] + x, Sin[2 Pi k/6] + y}, {k, 6}]]
Graphics[{EdgeForm[Opacity[.7]], LightBlue, Table[h[3 i + 3 ((-1)^j + 1)/4, Sqrt[3]/2 j], {i, 5}, {j, 10}]}]

p = N[PolyhedronData["TruncatedIcosahedron", "Faces", "Polygon"]];
shrink[t_, Polygon[x_List, opts___]] := Module[{c = Plus @@ x/Length[x]}, Polygon[Map[(c + (1 - t) (# - c)) &, x], opts]]
Animate[Graphics3D[{FaceForm[Yellow, Green], p /. y_Polygon :> shrink[s, y]}, PlotRange -> 2.5], {s, 0, .8}, SaveDefinitions -> True, AnimationRunning -> False, AnimationDirection -> ForwardBackward, DefaultDuration -> 1]

rcoord := RandomReal[1., {3}]
rantricoords := Table[rcoord, {3}]
Graphics3D[Polygon[Table[rantricoords, {10000}]]]

Graphics3D[Table[{Cuboid[10 rcoord], Sphere[10 rcoord]}, {10}]]

Graphics3D[PolyhedronData["Dodecahedron", "GraphicsComplex"]]; Show[%, Axes -> True]
pts = Table[Point[Table[RandomReal[], {3}]], {20}]; Show[%, Axes -> True]; Show[%, FaceGrids -> All]

Graphics3D[Ellipsoid[{0, 0, 0}, {4, 3, 2}]]

"Ejemplo de Solve Linear system."
m = {{1, 5}, {2, 1}}
m . {x, y} == {a, b}
m . {x, y} == {a, b}; Solve[%, {x, y}]

"Ejemplo de Tensor."
t = Table[i1 + i2 i3, {i1, 2}, {i2, 3}, {i3, 2}]
Array[(#1 + #2 #3) &, {2, 3, 2}]
MatrixForm[t]

"Ejemplo de calculo de PI con 707 digitos."
N[Pi, 707]

"Ejemplo de calculo de numero primo."
Prime[100000000]

"Ejemplo de factorizacion."
Factor[x^4-10x^2+9]

"Geolocalizacion."
GeoNearest["City", Here, 10]












#
#
#                                        SECCION DE EJEMPLOS SCHEME y COMMON LISP                                           #
#
#

# Expresar una funcion usando una expresion lambda:

(define fib (lambda (n) (cond ((= n 0) 0) ((= n 1) 1) (else (+ (fib (- n 1)) (fib (- n 2)))))))
#        |  |                                                                                 |
#        |   ---------------------------------------------------------------------------------
#        |                                          |
#      nombre                               expresion lambda
#

# NOTA: Este es solo un ejercicio en el uso de expresion lambda (y es como el interprete LISP traduce una definicion). En la practica, 
#       el programador definira esta misma funcion de la siguiente manera:

(define (fib n)
	    (cond ((= n 0) 0)
	    	  ((= n 1) 1)
	    	  (else (+ (fib (- n 1)) (fib (- n 2))))))

(define fib (lambda (x)
                    (cond ((= x 0) 0)
                    ((= x 1) 1)
                    ((> x 1) (+ (fib (- x 1)) (fib (- x 2)))))))

(display (fib 8))
21


(define (fact x) (cond ((= x 0) 1) ((= x 1) 1) else (* x fact(- x 1))))



#
# Ejemplo en Common LISP (misma sintaxis de Emacs LISP).
#
(defun fib (x) 
           (cond ((= x 0) 0)
           ((= x 1) 1)
           ((> x 1) (+ (fib (- x 1)) (fib (- x 2))))))

(print (fib 7))
13

(defun fibonacci (x)
                 (if (<= x 2) 1
                 (+ (fibonacci (- x 1)) (fibonacci (- x 2)))))

(print (fibonacci 8))
21


(print ((lambda (x y) (+ x y)) 2 3))
5


#
# IMPORTANTE: En LISP una function LAMBDA puede ser retornada desde una funcion. A su vez, se puede pasar como argumento una 
#             funcion LAMBDA durante la invocacion de una funcion. A continuacion dos ejemplos de ambas situaciones:
#

;
; Ejemplo de paso de una LAMBDA function como argumento a una 
; funcion.
;
(defun pow (n) (* n n))

(write "Ejemplo de una funcion que recibe como argumento LAMBDA ")
(write (pow ((lambda (x y) (+ x y)) 3 2)))

Salida:
"Ejemplo de una funcion que recibe como argumento LAMBDA "25


;
; Ejemplo de una funcion cuyo valor de retorno es una LAMBDA function.
;
(defun add (x y)
           ((lambda (o1 o2) (+ o1 o2)) x y))

(write "Ejemplo de una funcion que retorna LAMBDA ")
(write (add 5 6))

Salida:
"Ejemplo de una funcion que retorna LAMBDA "11





;
; IMPORTANTE: Un programa en LISP puede generar (escribir) programas LISP!
;             A continuacion un ejemplo de esta capacidad:
;
[1]> (defun makes (x) (list '+ x 2))
MAKES

;
; aqui vemos como al invocar la funcion esta devuelve una combination LISP que representa la suma de x + 2!!
;
[2]> (makes 5)
(+ 5 2)












#
#
#                                        SECCION DE EJEMPLOS Oracle PL/SQL                                        #
#
#
# IMPORTANTE: En SQL*Plus, para ejecutar una sentencia SQL o bloque existe el comando "RUN". Dicho comando primero muestra el comando SQL 
#             a ejecutar y luego ejecuta el comando y muestra el resultado.
#
#             Otra forma de ejecutar una sentencia SQL o bloque es usando el slash "/". Este no muestra el comando a ejecutar sino que muestra 
#             el resultado.
#
#             Tanto "RUN" como "/" ejecutan el comando SQL o bloque mas recientemente ejecutado (el mas reciente en el SQL buffer).
#

#
# Prueba de cursor en esquema con FOR.
#
BEGIN
   FOR curolc IN
   (
      SELECT * FROM TP_OLC_LOG WHERE FECHATRANSACCION = '20210625'
   )
   LOOP
      DBMS_OUTPUT.PUT_LINE('Transacción: ' || curolc.CODIGOTRANSACCION || 
                               ',  Fecha: ' || TO_CHAR(TO_DATE(curolc.FECHATRANSACCION, 'YYYYMMDD'), 'DD/MM/YYYY'));
   END LOOP;
END;
/


#
# Ejemplo de cursor en esquema declarando un cursor y su variable tipo ROW (sin usar FOR LOOP).
# Ejemplo de uso de funcion TO_DATE para convertir un campo VARCHAR2 a DATE (indicando un formato de fecha).
# Ejemplo de uso de funcion TO_CHAR (indicando un formato de salida).
#
DECLARE
   -- Prueba de cursor sobre la tabla OLC Log.
   CURSOR curlog
   IS
      SELECT * FROM TP_OLC_LOG WHERE FECHATRANSACCION = '20210625';
   
   -- Variable que contendrá una fila de la tabla OLC Log.
   olcrow   TP_OLC_LOG%ROWTYPE;
BEGIN
   -- Abrimos el cursor.
   OPEN curlog;

   -- Itera a través del cursor.   
   LOOP
      FETCH curlog INTO olcrow;
      
      EXIT WHEN curlog%NOTFOUND;
      
      DBMS_OUTPUT.PUT_LINE('Transacción: ' || olcrow.CODIGOTRANSACCION || 
                               ',  Fecha: ' || TO_CHAR(TO_DATE(olcrow.FECHATRANSACCION, 'YYYYMMDD'), 'DD/MM/YYYY'));
   END LOOP;
   
   CLOSE curlog;
END;
/



# Otro ejemplo
DECLARE
   varcomer   VARCHAR2(15);
BEGIN
   /*
   * Consulta el código de comercio.
   */
   SELECT COMERCIO INTO varcomer FROM TP_OLC_LOG
   WHERE CODIGOTRANSACCION = '350000' AND FECHATRANSACCION = '20210712';

   -- Imprime el código de comercio.
   DBMS_OUTPUT.PUT_LINE('El código del comercio es: ' || varcomer);
END;
/


# Otro ejemplo
DECLARE
   varmonto   NUMBER(12,2);
BEGIN
   -- Captura el monto.
   SELECT monto INTO varmonto FROM TP_OLC_LOG
   WHERE FECHATRANSACCION = '20210712' AND HORATRANSACCION = '134230';
   
   -- Muestra el monto de la transacción.
   DBMS_OUTPUT.PUT_LINE('El monto de la transacción es: ' || varmonto);
END;
/


# Otro ejemplo
SELECT COUNT(*) TOTAL_TRX, SUM(MONTO) FROM TP_OLC_LOG
                                      WHERE TIPOMENSAJE = '200' AND CODIGORESPUESTA = '00' AND REVERSAL = 0 AND 
                                            (CODIGOTRANSACCION >= '940000' AND CODIGOTRANSACCION <= '959999') AND 
                                            (FECHATRANSACCION BETWEEN '20210625' AND '20210625') AND 
                                            BIN_ACREEDOR IN (0009);



#
# Ejemplo de uso de funcion de agregado y GROUP BY
#
SELECT FECHATRANSACCION, SUM(MONTO) SubTotal FROM TP_OLC_LOG GROUP BY FECHATRANSACCION ORDER BY FECHATRANSACCION DESC;


#
# Ejemplo de una variable consecutivo con relleno de ceros a la izquierda a traves de la funcion TO_CHAR.
# Ejemplo de uso de sentencia CASE WHEN en una consulta SQL y dentro de un bloque PL/SQL.
#
DECLARE
   secuencia   NUMBER := 1;
BEGIN
   FOR curOlc IN (SELECT FECHATRANSACCION, CODIGOTRANSACCION, 
                         (CASE CODIGO_RESPUESTA_EXT 
                          WHEN '56' THEN 'ES RECHAZO'
                          WHEN '402' THEN 'TIMEOUT'
                          ELSE 'NO IDENTIFICADO'
                          END) RESPUESTA
                  FROM TP_OLC_LOG)
   LOOP
      BEGIN
         CASE
         WHEN curOlc.FECHATRANSACCION = '20210615' THEN
            -- Usa la funcion TO_CHAR para rellenar con ceros a la izquierda de forma automatica.
            DBMS_OUTPUT.PUT_LINE('Secuencia: ' || TO_CHAR(secuencia, '00000000') || 
                                     ',   Transacción: ' || curOlc.CODIGOTRANSACCION || 
                                     ',   Fecha: ' || TO_DATE(curOlc.FECHATRANSACCION, 'YYYYMMDD') || 
                                     ',   Respuesta: ' || curOlc.RESPUESTA);
            secuencia := secuencia + 1;
         ELSE
            NULL;
         END CASE;
      EXCEPTION
         WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('ERROR!');
      END;
   END LOOP;
END;


#
# Ejemplo de funcion DECODE (tiene la misma funcionalidad del IF ELSE IF y ELSE)
#
SELECT CODIGOTRANSACCION, 
       FECHATRANSACCION, 
       HORATRANSACCION, 
       DECODE(CODIGOTRANSACCION,940000, 'PAGO', 
                                350000, 'CONSULTA', 
                                'NO EXISTE') TIPO 
FROM TP_OLC_LOG;


## Ejemplo de uso de Oracle SQL como calculadora (a través de la tabla dummy DUAL).
SELECT ((200 * 4) / 10) FROM DUAL;


## Ejemplo de la función Módulo de la división.
SELECT MOD(10, 4) FROM DUAL;


## Ejemplo de la función Potencia.
SELECT POWER(2,10) kilobyte, POWER(2,20) megabyte, POWER(2,30) gigabyte, POWER(2,40) terabyte FROM DUAL;


## Ejemplo de la función Logarítmo: LOG(m, n) donde m es la base y n el exponente.
SELECT LOG(10, 100) FROM DUAL;


## Ejemplo de la función trigonométrica SENO (las funciones trigonométricas asumen que el valor está en radianes!).
## Por tal motivo,primero hay que convertirlo a grados usando la relación,
##
##                                                                        Radianes = Grados * (Pi / 180)
## Oracle no posee una función que devuelva el valor de Pi.
## Pero podemos simularlo usando la función Arco-coseno pasandole como argumento -1. 
SELECT SIN(30 * (ACOS(-1) / 180)) FROM DUAL;


## Ejemplo de las funciones de redondeo (por arriba y por abajo) y de Truncamiento.
SELECT CEIL(72.445), FLOOR(72.445), ROUND(72.49999), ROUND(72.5), ROUND(72.50001), TRUNC(72.0909, 1), TRUNC(72.0909, 2) FROM DUAL;


## Ejemplo de cálculo de funciones Promedio, Media, Moda y Desviación Estándar.
SELECT AVG(MONTO) AS PROMEDIO, MEDIAN(MONTO) AS MEDIA, STATS_MODE(MONTO) AS MODA, STDDEV(MONTO) AS DESV_ESTANDAR FROM TP_OLC_LOG;


## Simulando la función Promedio usando solo las funciones SUM y COUNT.
SELECT AVG(MONTO) AS PROMEDIO_1, (SUM(MONTO) / COUNT(*)) AS PROMEDIO_2 FROM TP_OLC_LOG;


## Dos formas de hacer una concatenación: usando la función CONCAT y luego usando '||'.
SELECT CONCAT(CONCAT(NOM_CONEXION, ' '), HOST_NAME) AS FULL_NAME FROM CIERREADM.TP_CONEXION;

SELECT (NOM_CONEXION || ' ' || HOST_NAME) AS FULL_NAME FROM CIERREADM.TP_CONEXION;


-- Extraer un substring de un string.
SUBSTR(<variable o nombre de columna de una tabla>, 5, 2)


/*
 * Ejemplo de uso de la función SUBSTR para extraer una parte de un string (en este caso se usa para añadir los ":" a la hora.
 */
DECLARE
   conta DECIMAL(10) := 1;
BEGIN
   FOR curOlc IN (SELECT * FROM TP_OLC_LOG WHERE FECHATRANSACCION = '20210625' ORDER BY FECHATRANSACCION ASC, HORATRANSACCION ASC)
   LOOP
      DBMS_OUTPUT.PUT_LINE(TO_CHAR(conta, '0000000000') || ',   ' || curOlc.CODIGOTRANSACCION || ',   ' || TO_CHAR(TO_DATE(curOlc.FECHATRANSACCION, 'YYYYMMDD'), 'DD-MM-YYYY') || ',   ' || SUBSTR(curOlc.HORATRANSACCION, 1, 2) || ':' || SUBSTR(curOlc.HORATRANSACCION, 3, 2) || ':' || SUBSTR(curOlc.HORATRANSACCION, 5, 2));

      conta := conta + 1;
   END LOOP;
END;


#
# Otro ejemplo de cursor incluyendo las funciones DECODE y TO_DATE dentro de la consulta.
#
DECLARE
   CURSOR   curOlc IS SELECT CODIGOTRANSACCION, TO_DATE(FECHATRANSACCION, 'YYYYMMDD') AS FECHA, DECODE(CODIGOTRANSACCION, 940000, 'PAGO', 350000, 'CONSULTA', 'ERROR') AS OPERACION FROM TP_OLC_LOG ORDER BY FECHA DESC;
   
   curRow   curOlc%ROWTYPE;
BEGIN
   OPEN curOlc;
   
   LOOP
      FETCH curOlc INTO curRow;
      
      EXIT WHEN curOlc%NOTFOUND;
      
      DBMS_OUTPUT.PUT_LINE('Transacción: ' || curRow.CODIGOTRANSACCION || ',   Fecha: ' || TO_CHAR(curRow.FECHA, 'DD-MM-YYYY') || ',   Tipo de operación: ' || curRow.OPERACION);
   END LOOP;
   
   CLOSE curOlc;
END;


/*
 * Ejemplo de manejo de tipo de datos TIMESTAMP. Ejemplo de uso de la función EXTRACT para extraer componentes 
 * de la Fecha Hora.
 */
DECLARE
   finici  NUMBER(10,2);
   ffinal  NUMBER(10,2);
   difere  NUMBER(10,2);
   fecha   TIMESTAMP := SYSDATE;
BEGIN
   finici := EXTRACT(SECOND FROM SYSTIMESTAMP);
   FOR contador IN 1..1000
   LOOP
      DBMS_OUTPUT.PUT_LINE(' ');
      DBMS_OUTPUT.PUT_LINE('Fecha: ' || TO_CHAR(fecha, 'DD') || ' de ' || TO_CHAR(fecha, 'Month') || TO_CHAR(fecha, 'YYYY'));
      DBMS_OUTPUT.PUT_LINE('Hora: ' || TO_CHAR(fecha, 'HH:MM:SSSSSSS'));
   END LOOP;

   ffinal:= EXTRACT(SECOND FROM SYSTIMESTAMP);
   difere := ffinal - finici;

   DBMS_OUTPUT.PUT_LINE('finici: ' || finici);
   DBMS_OUTPUT.PUT_LINE('ffinal: ' || ffinal);
   DBMS_OUTPUT.PUT_LINE('Diferencia: ' || difere);
END;








#
#
#                                        SECCION DE GIT                                        #
#
#

#
# Para conocer, en todo momento, que hace un comando de GIT podemos ejecutar lo siguiente.
#
git help config

# Esto abrira una pagina HTML de ayuda (estas paginas estan incluidas en el GIT).

#
# EJEMPLO COMPLETO: Imagina que tienes un repositorio en github llamado Java-development. 
#                   Imaginemos que hemos sido incorporados a un proyecto.
#                   La primera actividad es clonar ese repositorio para hacer las modificaciones a un fuente 
#                   ejemplo llamado multithread.java
#
#Paso 1. Clonar el repositorio usando la URL que nos den
#
# NOTA IMPORTANTE: GIT crea la carpeta conteniendo todo lo necesario, incluidos los fuentes. NO ES NECESARIO crear una carpeta!
$ git clone https://github.com/jportillo34/Java-development.git

#Paso 2.
$ cd Java-development
$ ls -la
total 17
drwxr-xr-x 1 user 197121    0 Apr  1 14:14 ./
drwxr-xr-x 1 user 197121    0 Apr  1 14:14 ../
drwxr-xr-x 1 user 197121    0 Apr  1 14:14 .git/
-rw-r--r-- 1 user 197121 2759 Apr  1 14:14 Java-PostgreSQL
-rw-r--r-- 1 user 197121  644 Apr  1 14:14 Multithread.java
-rw-r--r-- 1 user 197121  455 Apr  1 14:14 README.md

# Paso 3. Modificamos
$ vi Multithread.java

#Paso 4. Consultar status
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Multithread.java

no changes added to commit (use "git add" and/or "git commit -a")

#Paso 5. Registramos los cambios
$ git add .

#Paso 6. Consultamos
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   Multithread.java

#Paso 7. Antes de hacer commit vamos a identificarnos con nuestro email y nombre.
#
# NOTA IMPORTANTE: Este paso se hace una sola vez (cuando se es un usuario nuevo en el proyecto y una vez clonado el repositorio).
$ git config --global user.email "jportillo34@gmail.com"
$ git config --global user.name "Jose Portillo"

#Paso 8.
$ git commit -m "Nuevo cambio"
[master 751dfe0] Nuevo cambio
 1 file changed, 2 insertions(+)

#Paso 9. Consultamos status
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

#Paso 10. Subimos los cambios
#
# NOTA IMPORTANTE: Con este comando GIT actualiza el repositorio remoto (github en este ejemplo). El PUSH se hace SIN argumentos.
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 400 bytes | 400.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jportillo34/Java-development.git
   60fa9d9..751dfe0  master -> master

#
# En este punto el repositorio remoto contiene los cambios realizados!
#
# Si algun usuario hace un cambio es preciso hacer PULL para que dicho cambio se vea en mi repositorio local:
#
# Con el siguiente comando puede actualizar el local con los cambios en el remoto github.
#
git pull

# Tambien puede...
git fetch
git merge --ff-only


#
# IMPORTANTE: Es posible indicar al GIT que ignore algunos archivos contenidos en la carpeta repositorio. Ejemplo, si tenemos algun 
#             archivo con anotaciones que queremos mantener oculto en el repositorio.
#
#             Para esto creamos un archivo llamado ".gitignore". Luego, incluimos dentro del archivo el nombre o extension de todos 
#             los archivos que deseamos que GIT ignore en sus operaciones con el repositorio.
#
# Por ejemplo: ignorar todos los archivos con extension .txt
*.txt

#
# GIT lleva un log de cambios el cual es posible visualizar con el siguiente comando:
git log

# Para obtener una salida mejor del log:
git log --pretty=format:"%h - %an, %ar : %s"

ca82a6d - Scott Chacon, 6 years ago : changed the version number
085bb3b - Scott Chacon, 6 years ago : removed unnecessary test
a11bef0 - Scott Chacon, 6 years ago : first commit

# Opciones útiles de git log --pretty=format Opción 	Descripción de la salida
#
# %an
# Nombre del autor
#
# %ae
# Dirección de correo del autor
#
# %ad
# Fecha de autoría (el formato respeta la opción -–date)
#
# %ar
# Fecha de autoría, relativa
#
# %s
# Asunto


#
# Pasos para eliminar un fuente creado en el repositorio.
#
# IMPORTANTE: Se trata de eliminar un fuente que este manejado por GIT. Es decir: que existe tanto en el repositorio local como en el 
#             remoto (github por ejemplo).
#
#Paso 1. Eliminamos el fuente en el repositorio local
git rm <nombre del fuente, ejemplo index.html>

#Paso 2. Comprobamos que esta en status eliminado para GIT
git status

On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    index.html

#Paso 3. Confirmamos el cambio
git commit -m "elimina el HTML"

[master 5e5ba31] elimina el HTML
 1 file changed, 11 deletions(-)
 delete mode 100644 index.html

#Paso 4. Avisamos al repositorio remoto (github en este ejemplo) sobre el cambio
 git push

Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 227 bytes | 227.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jportillo34/Java-development.git
   886710c..5e5ba31  master -> master




#
# Para crear un BRACH nuevo:
git branch pruebas

# Para visualizar todas las ramas en el proyecto:
 git branch

* master
  pruebas
#
# NOTA IMPORTANTE: El '*' indica el BRACH en el que estamos hubicados!
#
# Para cambiar de BRACH usamos el comando:
git switch pruebas

Switched to branch 'pruebas'

# Consultamos de nuevo:
git branch

  master
* pruebas

# En este punto cualquier cambio que hagamos a algun fuente, dicho cambio se hace en el BRANCH 'pruebas'. Es decir, 
# si vemos el contenido del fuente modificado en la carpeta, no veremos cambio alguno.
# Luego, para que dichos cambios se reflejen en el BRACH 'master' principal ejecutamos el comando:
git merge -m "Nuevos cambios adicionados al master"


# Ahora, imaginemos que ya hemos finalizado los cambios y hemos hecho el MERGE en la rama principal del proyecto.
# Para eliminar el BRANCH creado (dado que ya no hace falta mas) primero nos cambiamos de regreso al branch principal:
git switch master

Switched to branch 'master'
Your branch is up to date with 'origin/master'.

# Luego, eliminamos el branch:
git branch -d pruebas

Deleted branch pruebas (was 530a891).

# Verificamos de nuevo la lista de branches y vemos como ya no existe el branch 'prueba':
git branch

* master




# Aqui van mas ejemplos e informacion adicional:
#
# Configurar usuario e email.
#
git config --global user.name "Jose Portillo"
git config --global user.email jportillo34@gmail.com


#
# Ahora configuramos el default branch name.
#
git config --global init.default branch main

#
# Nos movemos al directorio que contiene los fuentes a usar con GIT.
#
cd javaRep


#
# Ahora iniciamos el GIT
#
git init 
Initialized empty Git repository in C:/Users/user/Desktop/javaGit/javaRep/.git/

# Al mostrar el contenido de dicha carpeta esta incluira una carpeta oculta llamada .git
 ls -la
total 8
drwxr-xr-x 1 user 197121   0 Nov 22 17:52 ./
drwxr-xr-x 1 user 197121   0 Nov 22 17:51 ../
drwxr-xr-x 1 user 197121   0 Nov 22 17:52 .git/
-rw-r--r-- 1 user 197121 642 Aug  7 19:03 Multithread.java


#
# Ahora podemos consultar el status del repositorio actual.
#
git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Multithread.java

nothing added to commit but untracked files present (use "git add" to track)

# IMPORTANTE: Observar que GIT muestra el fuente "Multithread.java" con status "untracked". Esto es porque GIT aun no tiene registrado
#             dicho fuente, mucho menos puede llevar un track de cambios aplicados a dicho fuente. Si hacemos algun cambio a este fuente 
#             en este momento GIT no toma en cuenta esos cambios hasta que el fuente este registrado en GIT.
#
# Para que GIT lleve el track del fuente ejecutamos:
git add Multithread.java


# IMPORTANTE: Es posible indicar a GIT que haga track de todos los fuentes contenidos en el repositorio. Los comandos siguientes son equivalentes:
git add --all 
git add .


#
# Ahora podemos consultar de nuevo el status y SI muestra el fuente ya registrado en GIT.
#
git status 
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   Multithread.java

# OBSERVAR que el mismo comando muestra el comando para remover dicho fuente de la memoria de GIT!


#
# Primero debe clonar un repositorio desde su github.
#
git clone https://github.com/jportillo34/Java-development.git

Cloning into 'Java-development'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 16 (delta 0), reused 0 (delta 0), pack-reused 12
Receiving objects: 100% (16/16), 6.73 KiB | 3.36 MiB/s, done.
Resolving deltas: 100% (2/2), done.

user@DESKTOP-UGV9SAM MINGW64 ~/DEsktop/javaGit

$ ls -la
total 48
drwxr-xr-x 1 user 197121 0 Nov 22 12:10 ./
drwxr-xr-x 1 user 197121 0 Nov 22 12:08 ../
drwxr-xr-x 1 user 197121 0 Nov 22 12:10 Java-development/


#
# Copie un fuente que desee hacia su directorio de trabajo local.
#
cp Multithread.java ./javaGit/Java-development/Mutithread.java


#
# Ejecute el commit de los cambios en el fuente que desea incorporar.
#
$ git add .


$ git commit -m "actualiza el fuente Multithread.java"
[master 4f8fae7] actualiza el fuente Multithread.java
 1 file changed, 26 insertions(+)
 create mode 100644 Multithread.java


#
# Envie o sincronice el repositorio en github con los cambios hechos en el local.
#
$ git push -u origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 980 bytes | 980.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/jportillo34/Java-development.git
   dfe0bf7..b507dfe  master -> master
branch 'master' set up to track 'origin/master'.



#
# Con el siguiente comando puede actualizar el local con los cambios en el remoto github.
#
git pull

# Tambien puede...
git fetch
git merge --ff-only














#
#
#                                        SECCION DE ARITMETICA                                        #
#
#
NOTA SOBRE LA RESTA DE NUMEROS DECIMALES:
----------------------------------------
Existen varios algoritmos para realizar esta operacion (ver "An Investigation of Subtraction Algorithms from the 18th and 19th Centuries", Enzinger).

El algoritmo clasico que aprendimos en la escuela es el de Descomposicion. En su base teorica, este algoritmo descompone minuendo y sustraendo en unidades, 
decenas, centenas, etc. Ejemplo,

   940   ----> 900 + 40 + 0   ----> 800 + 30 + 10   (ver como el algoritmo convierte en diez en cero "tomando prestado")
 - 586   -------------------------> 500 + 80 +  6
 ------                           ----------------
   354   <------------------------  300 + 50 +  4

En el ejemplo arriba vemos como la unidad del minuendo es cero (0). En este caso, el algoritmo, debe implementar un procedimiento de "tomar prestado" 
a las decenas una unidad superior (10) para transformar el cero en diez. Luego, la decena debe "tomar prestado" a las centenas, etc.

En este otro ejemplo podemos ver como se interpreta cada paso (restando de forma vertical de arriba hacia abajo y comenzando por las unidades),

   13   ----> 10 + 3
 - 25   ----> 20 + 5
 -----       -------
 - 12   <--- -10 + (-2) 

Hay una excepcion: cuando el minuendo es menor que el sustraendo (en este caso el algoritmo debe hacer un paso previo de comparacion para 
conocer cual de los dos numeros es el menor). Si el caso es que el minuendo es el menor, entonces se invierte el papel de cada numero y 
se hace la resta cuidando, al final, de colocar signo menos. Ejemplo,

   654   ----> 928
 - 928       - 654
 ------      ------
 - 274   <---- 274


Este metodo por Descomposicion podemos formularlo (muy generalmente) como,

(10 + m) - s = r

Ejemplo,

   16    ----> (10 + 6) - 9 = 7
  - 9
  ----


El otro metodo (utilizado tambien en el sistema Binario) es el de los Complementos,

(10 - s) + m = r

es decir, se representa el sustraendo por su complemento aritmetico. Esto es lo que se hace en la representacion de 2's Complement.

Vamos a hacer una resta, primero por el metodo de Descomposicion y luego usando el metodo de los Complementos,

   873   ------------>   8   7   3
 - 218                 - 2   1   8
 ------                ------------
                        +6  +6  -5    Luego ------> (+600) + (+60) + (-5) = 655

Ahora vamos a hacer la resta por Complementos

1.- Complemento del sustraendo: 1000 - 218 = 782

2.- Sumamos minuendo mas el complemento del sustraendo    873
                                                        + 782
                                                        ------
                                                         1655

3.- Del resultado de la suma anterior descartamos el 1 de los miles. El resultado de la resta es: 655

NOTA: Como comentamos antes, si la resta se hiciera al reves (en el ejemplo anterior), como el minuendo seria menor que el sustraendo, entonces 
      pudieramos usar el mismo procedimiento anterior (cualquiera de dos los metodos de restar) pero colocando signo negativo al resultado (-655).





#
# REGLA DE CALCULOS: Como sumar dos numeros con una regla de calculos?
#
x + y = m * x

m = 1 + y/x

x( 1  +/- y ) = x +/- y
         ---
          x

-------------------------------------------------
x + y = m / x

m = x(x + y)

x + y = x(x + y)
        --------
           x

x + y = x + y*x
            ---
             x








#
#
#                                        SECCION DE ALGEBRA                                        #
#
#
(1) PAR ORDENADO

   Definicion:   (a, b) = {{a}, {a, b}}


   Teorema:   (a, b) = (b, c) => a=c ^ b=d
            |                |
             ----------------
                    |
                    |  Hipotesis
                    |
                    V
              {{a}, {a, b}}   =   {{c}, {c, d}}
             |             |     |             |
              -------------       -------------
                    |                   |
                    |                   |
         Elemento (objeto) comun     Elemento (objeto comun)
         es "a"                      es "c"
             |                           |
              ---------------------------
                         |
                         | Por tanto
                         V
                        a = c

                    Entonces,

            {{a}, {a, b}} = {{a}, {a, d}}

NOTA: Ver Spivak (Calculus), "Apendix: Ordered Pairs".




(2) Conjunto de n-tuplas (Producto Cartesiano o Conjunto Producto)

     n
   -----
    | | A   = A  X  A   X  A   X ... X   A   = {(x , x , ..., x ) | x  E  A  , i E N}   (N = {1, 2, 3, ..., n})
    | |  i     1     2      3             n       1   2        n     i     i
    i=1


   (x  , x  , ..., x ) es una n-tupla
     1    2         n

   El conjunto asi obtenido esta compuesto por n-tuplas ordenadas.


(3) NOTA: En la definicion anterior el producto "X" tiene su origen en el concepto de interseccion presente en la Teoria de Conjuntos,

    Para toda coleccion de Conjuntos A  , A  , ..., A   la interseccion se representa como
                                      1    2         n
    n
    -
   | |                                -       -        -
   | | A    o lo que es lo mismo  A  | |  A  | |  ... | |  A
   i=1  i                          1       2                n



(4) Ejemplo de Espacio Vectorial (basado en la definicion (2))

   Dado el Conjunto Producto (2), un Espacio Vectorial comprenderia las siguientes Aplicaciones (Maps) que designamos por + y .

   (x , x , ..., x ) + (y , y , ..., y ) = (x  +  y  , x  +  y  , ..., x  + y )
     1   2        n      1   2        n      1     1    2     2         n    n

   y

   q . (x  , x  , ..., x ) = (q.x  , q.x  , ..., q.x )   ,  q E N
         1    2         n        1      2           n



(5) Definicion de Funcion ("Calculus", Apostol)

   Una Funcion f es un Conjunto de Pares Ordenados (x, y) ninguno de los cuales tiene el mismo primer elemento.




(6) Sobre los terminos Punto, Recta y Plano (respuesta del prof. Iribarren, 29 de Agosto de 2016)

 En la definicion axiomatica depurada de la Geometria Euclidiana -tomemos la de Gilbert- los terminos no definidos (primitivos) 
 son "Punto", "Recta" y "Plano", y ademas "Incidencia" (mas dos o tres terminos primitivos adicionales). No debe entenderse que la 
 Recta sea un Conjunto de Puntos o que este constituida por Puntos; solo que un Punto y una Recta son o no son "Incidentes"; igual 
 que una Recta (o Punto) "incide" en un Plano. Uno de los axiomas dice que dos Puntos distintos "inciden" en una Recta. Enfatizo que 
 "incidir" es un termino primitivo, carece de definicion. De esto no se infiere logicamente que la Recta sea un Conjunto de Puntos.

 Cuando partimos del Cuerpo de los numeros Reales (R), fijamos ejes de Coordenadas y llamamos Punto a un Par Ordenado de numeros Reales. 
 En este caso SI podemos DEFINIR Recta como el Lugar Geometrico de Puntos cuyas Coordenadas satisfacen una ecuacion de primer grado!
 Lo que tenemos, en esta ultima interpretacion, es un Modelo de la Geometria Euclidiana Plana; vale decir, se cumplen todos los axiomas 
 (con "incidir" interpretado en sentido conjuntista). En este modelo una Recta es ciertamente un conjunto de Puntos (un nivel de abstraccion superior 
 al de la Geometria Euclidiana basica primitiva).




(7) Computational Method (ver "Fundamental Algorithms" en TAOCP de Knuth)

(A procedure that has all of the characteristics of an algorithm except that it
possibly lacks finiteness may be called a computational method. Euclid originally
presented not only an algorithm for the greatest common divisor of numbers, but
also a very similar geometrical construction for the “greatest common measure”
of the lengths of two line segments; this is a computational method that does
not terminate if the given lengths are incommensurable. Another example of a
nonterminating computational method is a reactive process, which continually
interacts with its environment.)


So far our discussion of algorithms has been rather imprecise, and a mathematically
oriented reader is justified in thinking that the preceding commentary
makes a very shaky foundation on which to erect any theory about algorithms.
We therefore close this section with a brief indication of one method by which the
concept of algorithm can be firmly grounded in terms of mathematical set theory.
Let us formally define a computational method to be a quadruple (Q, I, Ω, f),
in which Q is a set containing subsets I and Ω, and f is a function from Q
into itself. Furthermore f should leave Ω pointwise fixed; that is, f(q) should
equal q for all elements q of Ω. The four quantities Q, I, Ω, f are intended
to represent respectively the states of the computation, the input, the output,
and the computational rule. Each input x in the set I defines a computational
sequence, x0, x1, x2, . . . , as follows:

x0 = x and xk+1 = f(xk) for k ≥ 0.                                           (1)

The computational sequence is said to terminate in k steps if k is the smallest
integer for which xk is in Ω, and in this case it is said to produce the output
xk from x. (Notice that if xk is in Ω, so is xk+1, because xk+1 = xk in such
a case.) Some computational sequences may never terminate; an algorithm is a
computational method that terminates in finitely many steps for all x in I.
Algorithm E may, for example, be formalized in these terms as follows: Let Q
be the set of all singletons (n), all ordered pairs (m, n), and all ordered quadruples
(m, n, r, 1), (m, n, r, 2), and (m, n, p, 3), where m, n, and p are positive integers
and r is a nonnegative integer. Let I be the subset of all pairs (m, n) and let Ω
be the subset of all singletons (n). Let f be defined as follows:

f((m, n)) = (m, n, 0, 1); 

f((n)) = (n);

f((m, n, r, 1)) = (m, n, remainder of m divided by n, 2);
                                                                            (2)
f((m, n, r, 2)) = (n)   if r = 0,     (m, n, r, 3) otherwise;

f((m, n, p, 3)) = (n, p, p, 1).



The correspondence between this notation and Algorithm E is evident.
This formulation of the concept of an algorithm does not include the restriction
of effectiveness mentioned earlier. For example, Q might denote infinite
sequences that are not computable by pencil and paper methods, or f might
involve operations that mere mortals cannot always perform. If we wish to
restrict the notion of algorithm so that only elementary operations are involved,
we can place restrictions on Q, I, Ω, and f, for example as follows: Let A be
a finite set of letters, and let A∗ be the set of all strings on A (the set of all
ordered sequences x1x2 . . . xn, where n ≥ 0 and xj is in A for 1 ≤ j ≤ n). The
idea is to encode the states of the computation so that they are represented by
strings of A∗. Now let N be a nonnegative integer and let Q be the set of all
(σ, j), where σ is in A∗ and j is an integer, 0 ≤ j ≤ N; let I be the subset of Q
with j = 0 and let Ω be the subset with j = N. If θ and σ are strings in A∗, we
say that θ occurs in σ if σ has the form αθω for strings α and ω. To complete
our definition, let f be a function of the following type, defined by the strings
θj , ϕj and the integers aj , bj for 0 ≤ j < N:


f((σ, j)) = (σ, aj)  if θj does not occur in σ;

f((σ, j)) = (αϕjω, bj)   if α is the shortest possible string for which σ=αθjω;

f((σ,N)) = (σ,N).                                                           (3)


Every step of such a computational method is clearly effective, and experience
shows that pattern-matching rules of this kind are also powerful enough
to do anything we can do by hand. There are many other essentially equivalent
ways to formulate the concept of an effective computational method (for example,
using Turing machines). The formulation above is virtually the same as that
given by A. A. Markov in his book The Theory of Algorithms [Trudy Mat. Inst.
Akad. Nauk 42 (1954), 1–376], later revised and enlarged by N. M. Nagorny
(Moscow: Nauka, 1984; English edition, Dordrecht: Kluwer, 1988).









#
# Sobre el tiempo de ejecucion de los algoritmos
#
The most common attributes of logarithmic running-time function are that:

    the choice of the next element on which to perform some action is one of several possibilities, and
    only one will need to be chosen.

or

    the elements on which the action is performed are digits of n

This is why, for example, looking up people in a phone book is O(log n). You don't need to check every person in the phone book to find the right one; 
instead, you can simply divide-and-conquer by looking based on where their name is alphabetically, and in every section 
you only need to explore a subset of each section before you eventually find someone's phone number.

Of course, a bigger phone book will still take you a longer time, but it won't grow as quickly as the proportional increase in the additional size.

We can expand the phone book example to compare other kinds of operations and their running time. 
We will assume our phone book has businesses (the "Yellow Pages") which have unique names and people (the "White Pages") which may not have unique names. 
A phone number is assigned to at most one person or business. We will also assume that it takes constant time to flip to a specific page.

Here are the running times of some operations we might perform on the phone book, from fastest to slowest:

    O(1) (in the worst case): Given the page that a business's name is on and the business name, find the phone number.

    O(1) (in the average case): Given the page that a person's name is on and their name, find the phone number.

    O(log n): Given a person's name, find the phone number by picking a random point about halfway through the part of the book you haven't searched yet, 
              then checking to see whether the person's name is at that point. Then repeat the process about halfway through the part of the book where 
              the person's name lies. (This is a binary search for a person's name.)

    O(n): Find all people whose phone numbers contain the digit "5".

    O(n): Given a phone number, find the person or business with that number.

    O(n log n): There was a mix-up at the printer's office, and our phone book had all its pages inserted in a random order. 
                Fix the ordering so that it's correct by looking at the first name on each page and then putting that page in the appropriate spot 
                in a new, empty phone book.

For the below examples, we're now at the printer's office. Phone books are waiting to be mailed to each resident or business, 
and there's a sticker on each phone book identifying where it should be mailed to. Every person or business gets one phone book.

    O(n log n): We want to personalize the phone book, so we're going to find each person or business's name in their designated copy, 
                then circle their name in the book and write a short thank-you note for their patronage.

    O(n2): A mistake occurred at the office, and every entry in each of the phone books has an extra "0" at the end of the phone number. 
           Take some white-out and remove each zero.

    O(n · n!): We're ready to load the phonebooks onto the shipping dock. Unfortunately, the robot that was supposed to load the books has gone haywire: 
               it's putting the books onto the truck in a random order! Even worse, it loads all the books onto the truck, then checks to see if they're 
               in the right order, and if not, it unloads them and starts over. (This is the dreaded bogo sort.)

    O(nn): You fix the robot so that it's loading things correctly. The next day, one of your co-workers plays a prank on you and wires the loading 
           dock robot to the automated printing systems. Every time the robot goes to load an original book, the factory printer makes a duplicate run 
           of all the phonebooks! Fortunately, the robot's bug-detection systems are sophisticated enough that the robot doesn't try printing even 
           more copies when it encounters a duplicate book for loading, but it still has to load every original and duplicate book that's been printed.








#
# Convertir un numero decimal fraccionario en binario (tomado de geeksforgeeks):
#

Let's take an example for n = 4.47 k = 3

Step 1: Conversion of 4 to binary
1. 4/2 : Remainder = 0 : Quotient = 2
2. 2/2 : Remainder = 0 : Quotient = 1
3. 1/2 : Remainder = 1 : Quotient = 0

So equivalent binary of integral part of decimal is 100.

Step 2: Conversion of .47 to binary
1. 0.47 * 2 = 0.94, Integral part: 0
2. 0.94 * 2 = 1.88, Integral part: 1
3. 0.88 * 2 = 1.76, Integral part: 1

So equivalent binary of fractional part of decimal is .011

Step 3: Combined the result of step 1 and 2.

Final answer can be written as:
100 + .011 = 100.011



# Tomado de https://www.quora.com/Why-is-it-important-to-know-the-conversion-of-decimal-to-binary
Before we convert a decimal number into binary let’s make sure we understand how regular decimal numbers work. 

We can use the decimal number 1337 as a random number to work through an example.

When we write the decimal number 1337 we are actually using a form of shorthand. What we really mean when we say 1337 is 1×1000 + 3×100 + 3×10 + 7×1

In words, “1337 is 1 thousands, 3 hundreds, 3 tens, and 7 ones”. But notice that thousands, hundreds, tens, and ones, are just powers of 10.

So 1337 = 1×10^3 + 3×10^2 + 3×10^1 + 7×10^0

If we weren’t already so used to decimal numbers and we wanted to ‘build’ this decimal number from scratch, we could ask ourselves, 
“how many 10^3s will take to build that number? How many 10^2s?” And so on.

Now let’s move into the binary world.

In the binary world we will use powers of 2 instead of powers and 10 as our basic building blocks. That being the case let’s get familiar with the powers of 2:

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10= 1024
2^11= 2048

We could do that for a long time so let’s stop there. : ) These are enough building blocks to remake the decimal number 1337 in binary.

So how many 2^11s do we need to build 1337? The answer is none at all. So that is 0×2^11

How many 2^10s are needed to build 1337? We can use one of those. So that is 1×2^10. When we use the 2^10 building block we still have 
313 left to build (Because 1337 - 10^24 = 313). So let’s keep going.

How many 2^9s can be used to build 313? The answer is none. It is too big. So that is 0×2^9

How many 2^8s can be used to build 313? We can use one of these. So the answer is 1×2^8. When we use the 2^8 building block we still have 
57 left to build (because 313 - 256 = 57). So let’s keep going.

How many 2^7s can be used to build 57? The answer is none. It is too big. So that is 0×2^7

How many 2^6s can be used to build 57? The answer is none. It’s also too big. So that is 0×2^6

How many 2^5s can be used to build 57? We can use one of these. So the answer is 1×2^5. When we use this 2^5 building block we still have 
25 left to build (because 57 - 32 = 25). So let’s keep going.

How many 2^4s can be used to build 25? We can use one of these. So the answer is 1×2^4. When we use this 2^4 building block we still have 
9 left to build (because 25 - 16 = 9). So let’s keep going.

How many 2^3s can be used to build 9? We can use one of these. So the answer is 1×2^3. When we use this 2^3 building block we still have 
1 left to build (because 9 - 8 = 1). So let’s keep going.

How many 2^2s can be used to build 1? The answer is none. It’s too big. So that is 0×2^2

How many 2^1s can be used to build 1? The answer is none. It’s also too big. So that is 0×2^1

How many 2^0s can be used to build 1? The answer is one. So that is 1×2^0

Now let’s put this all together and add up all the blocks to get 1337.

1337 = 0×2^11 + 1×2^10 + 0×2^9 + 1×2^8 + 0×2^7 + 0×2^6 + 1×2^5 + 1×2^4 + 1×2^3 + 0×2^2 + 0×2^1 + 1×2^0

.

Wow! Okay so that is a rather unwieldy way of expressing 1337. That’s why we just write the number of times each block is used 
as we go from left to right and this becomes:

1337 (in decimal) = 010100111001 (in binary)

The 0 that is out in front on the left isn’t necessary. It came from the fact that 2^11 was already larger than 1337 to begin with. 
The same will be true of any larger power of two as well. 

Any number of zeros on the left would produce the same number since they only indicate that blocks that large 
are already too big to contribute to our number. So we can drop any zeros from the left and arrive at our final answer:

1337 (in decimal) = 10100111001 (in binary).

So what about numbers less than 1?

When we write the (decimal) number 0.375 we are using the same shorthand described above. We are writing out the number of 
each power of ten block needed to build up the desired number. The only difference is that now the powers of ten require negative exponents.

Here’s what 0.375 really means: 0×10^0 + 3×10^−1 + 7×10^−2 + 5×10^−3

.

Let’s use the same idea to write 0.375 in binary form. To do that we need to know our negative powers of 2:

2^−1 = 1/2 = .5
(as a decimal)

2^−2 = 1/4 = .25
(as a decimal)

2^−3 = 1/8 = .125
(as a decimal)

Notice that 0.375 = 0×2^−1 + 1×2^−2 + 1×2^−3

.

So 0.375 (in decimal) = 0.011 (in binary). And bringing our two examples together we may say that 1337.375 (in decimal) = 10100111001.011 (in binary).
