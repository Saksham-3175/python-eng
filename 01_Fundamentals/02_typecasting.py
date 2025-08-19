#Changing one dtype into another dtype
a = 35
b = "23"

# print(f"{a}, {type(a)}")
# print(f"{b}, {type(b)}")

c = int(b)
# The original version of b is not changed(the copy is changed though)
# print(f"a + b: {a + b}") #error: can't add int and str
# print(f"{a} + {b} = {a+c}")
# print(f"Type of b: {type(b)}")
# print(f"Type of c: {type(c)}")

#Implicit Typecasting-> Python automaticaly does this (int + float -> float)
x = 5
y = 32.3
z = x + y #Python will typecast this
# print(f"{z}, {type(z)}")

def implicit_typecasting():
    """Python's type promotion:
    bool -> int -> float -> complex
    bool+int -> int
    int+float -> float
    int+complex -> complex
    float+complex -> complex
    bool+complex -> complex
    """

    a_int = 4
    b_complex = 8 + 4j
    print(f"Int + Complex = Type({type(a_int + b_complex)}): {a_int + b_complex}")
    
    b_bool = False
    print(f"Int + Bool = Type({type(a_int + b_bool)}): {a_int + b_bool}")

    b_float = 3.14
    print(f"Int + Float = Type({type(a_int + b_float)}): {a_int + b_float}")

    a_float = 42.212
    b_complex = 8 + 32j
    print(f"Float + Complex = Type({type(a_float + b_complex)}): {a_float + b_complex}")

print(implicit_typecasting.__doc__)
implicit_typecasting()

#Explicit Typecasting -> We convert this ourselves
#Above examples.