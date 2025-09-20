# Convert function based code to Object Oriented Programming style using classes and methods.

class Operations:
    # we use static methods so that we can use them without having to create instance of the class.
    @staticmethod
    def addition(a:float, b:float) -> float:
        return a+b
    
    @staticmethod
    def subtraction(a:float, b:float) -> float:
        return a-b
    
    @staticmethod
    def multiplication(a:float, b:float) -> float:
        return a*b
    
    @staticmethod
    def division(a:float, b:float) -> float:
        if b == 0:
            # check to see if b is zero to avoid divide by zero error.
            raise ValueError("Division by zero is not allowed.")
        return a/b



# def addition(a: float, b: float) -> float:
#     return a + b

# def subtraction(a: float, b: float) -> float:
#     return a - b

# def multiplication(a: float, b: float) -> float:
#     return a * b

# def division(a: float, b: float) -> float:
#     if b == 0:
#         raise ValueError("Division by zero is not allowed.")
#     return a / b