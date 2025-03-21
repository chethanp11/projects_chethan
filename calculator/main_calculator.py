class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return a ** 0.5

    def factorial(self, a):
        if a < 0:
            raise ValueError("Cannot take factorial of a negative number")
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result