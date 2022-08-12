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

