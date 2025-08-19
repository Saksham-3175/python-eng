age = 34
name = "string"
cgpa = 5.23

## Rules
#1 Don't assing variables starting with numbers. Because if you try to name a variable starting with a number, the language thinks it’s a number, not a name. So `2x = 5` is “number 2 times x” to the interpreter, not “variable 2x.”
#2 Var names are case-sensitive (Age, age -> both are diff)
# Variables cannont contain special characer other that (_)


##Data Types:
#Bulit-in
# int, float, str, bool, list, tuple, set, dict

#int:
print(f"Integer: {age}, {type(age)}")

#float:
print(f"Float: {cgpa}, {type(cgpa)}")

#str:
print(f"String: {name}, {type(name)}")

#bool:
is_completed = True
print(is_completed, {type(is_completed)})

