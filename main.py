from Calculator import Calculator

calc = Calculator(10, 5)
print("Додавання:", calc.add())
print("Віднімання:", calc.subtract())
print("Множення:", calc.multiply())
print("Ділення:", calc.divide())

calc.update_numbers(20, 4)
print("Нове додавання:", calc.add())
