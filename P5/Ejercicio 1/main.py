def operation_logger(math_operation):
    def wrapper(op, *args, **kwargs):
        try:
            resultado = math_operation(op, *args, **kwargs)
            print(f"Operacion: {op.__name__}, Argumentos {args}, Resultado: {resultado}")
        except ZeroDivisionError:
            print(f"Operacion {op.__name__} no se puede realizar entre 0")
        except Exception as e:
            print(f"Operacion {op.__name__} hay un error inesperado.")
    return wrapper

@operation_logger
def math_operation(op, *args, **kwargs):
    return op(*args, **kwargs)

add = lambda *args: sum(args)
subtract = lambda x, y: x - y
multiply = lambda *args: __import__('functools').reduce(lambda a, b: a * b, args)
divide = lambda x, y: x / y


math_operation(add, 5, 3)
math_operation(subtract, 10, 4)
math_operation(multiply, 2, 6)
math_operation(divide, 15, 3)
math_operation(divide, 10, 0)
math_operation(add, 1, 2, 3, 4, 5)