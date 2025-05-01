class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        var = self.a + self.b
        return var
        
    def subtraction(self):
        var = self.a - self.b
        return var
    
    def multiplication(self):
        var = self.a * self.b
        return var

    def division(self):
        var = self.a / self.b
        return var
        


obj = BasicCalculator(10, 5)
print("{}{}{}{}{}{}".format("Addition: ", 10, " + ", 5, " = ", obj.addition()))
print("{}{}{}{}{}{}".format("Subtraction: ", 10, " - ", 5, " = ", obj.subtraction()))
print("{}{}{}{}{}{}".format("Multiplication: ", 10, " * ", 5, " = ", obj.multiplication()))
print("{}{}{}{}{}{}".format("Division: ", 10, " / ", 5, " = ", obj.division()))
