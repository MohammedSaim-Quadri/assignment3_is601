# Convert function based code to Object Oriented Programming style using classes and methods.

class Operations:
    # we use static methods so that we can use them without having to create instance of the class.
    """
    A class to encapsulate static methods for basic arithmetic operations.
    Using static methods allows these functions to be called without creating an instance of the class.
    """
    @staticmethod
    def addition(a:float, b:float) -> float:
        """
        Calculates the sum of two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a+b
    
    @staticmethod
    def subtraction(a:float, b:float) -> float:
        """
        Subtracts the second number from the first.
        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of a - b.
        """
        return a-b
    
    @staticmethod
    def multiplication(a:float, b:float) -> float:
        """
        Multiplies two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The product of a and b.
        
        """
        return a*b
    
    @staticmethod
    def division(a:float, b:float) -> float:
        """
        Divides the first number by the second.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If the divisor 'b' is zero.
        """
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