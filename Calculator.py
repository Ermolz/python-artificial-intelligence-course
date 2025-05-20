class Calculator:
    a = 0
    b = 0
    result = 0

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        self.result = self.a + self.b
        return self.result

    def subtract(self):
        self.result = self.a - self.b
        return self.result

    def multiply(self):
        self.result = self.a * self.b
        return self.result

    def divide(self):
        if self.b == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result = self.a / self.b
        return self.result

    def update_numbers(self, a: int, b: int):
        self.a = a
        self.b = b
        return self.a, self.b