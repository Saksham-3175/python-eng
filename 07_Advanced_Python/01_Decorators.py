#Decorator -> Takes a function and creates a wrapper(a new function)
#Wrapper -> wraps the original function with the extra code(only if you want)

def decorator(func):
    def wrapper():
        print("func() called in below")
        func()
        print("Func was called in the wrapper")
    return wrapper

@decorator
def a_func():
    print("This function has some code in it.")

# a_func()
# call_decorator = decorator(a_func)  
# call_decorator()

a_func()

#Used for API routes in flas, django, etc.

'''
Decorators let you inject behavior before and after a function runs without editing the function itself. That’s why they’re perfect for:
Logging
Authentication checks
Timing a function’s runtime
Retrying a failed function call'''
