def operation_logger(func):
    def wrapper(operation, *args, **kwargs):
        try:
            result=func(operation, *args, **kwargs)
            print(f"Resultado: {result}")
            return result
        except ZeroDivisionError:
            print("No se pueden realizar divisiones entre cero")
            return None
    return wrapper


add = lambda *args: sum(args)
substract = lambda *args: args[0] - sum(args[1:])
multiply = lambda *args: 1 if not args else args[0] * multiply(*args[1:])
divide = lambda *args: args[0] if len(args) == 1 else args[0] / divide(*args[1:]) if all(args[1:]) else None


@operation_logger
def math_operation(operation, *args):
    return operation(*args)

math_operation(add, 5, 3)                       # Resultado 8
math_operation(substract, 10, 4)                # Resultado 6
math_operation(multiply, 2, 6)                  # Resultado 12
math_operation(divide, 15, 3)                   # Resultado 5.0
math_operation(divide, 10, 0)                   # Resultado None
math_operation(add, 1, 2, 3, 4, 5)              # Resultado 15