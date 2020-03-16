class Add:
    variable_a = 1
    variable_b = 2

    def __init__(self):
        self.a = 5
        self.b = 10

    def calculate(self):
        print("variable_a =", self.a)
        print("variable_b =", self.b)
        init_sum = (self.a + self.b)
        print("sum is", init_sum)
        print("variable_a =", Add. a)
        print("variable_b =", Add.b)
        class_sum = Add.a + Add.b
        print("sum is", class_sum)


al = Add()
al.calculate()
