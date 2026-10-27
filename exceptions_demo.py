
import time
def safe_div(a: int, b: int) :
    try:
        return a / b
    except ZeroDivisionError:
        return "division by zero"
    except Exception as exp:
        return "unhandled exception: " + str(exp)
    

def get_exception(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        print ("divide by zero")


def get_else_after_exception(a: int, b: int):   

    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        print("divide by zero")
    else:
        print("divide a/b was successfull")

    return result

def get_finally(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("divide by zero")
    finally:
        print("divide call", time.time())

a, b = 10, 2
delimeter = "-" * 40
print("normal safe divide")
print(safe_div(a, b))
print(delimeter)
print("safe divide by zero")
print(safe_div(a, 0))
print(delimeter)
print("get exception of divide by zero")
print(get_exception(a, 0))
print(delimeter)
print("get else after exception")
print(get_else_after_exception(a, b))
print(delimeter)
print("get else after exception divide by zero")
print(get_else_after_exception(a, 0))
print(delimeter)
print("get finally with normal divide")
print(get_finally(a, b))
print(delimeter)
print("get finally with divide by zero")
print(get_finally(a, 0))



    