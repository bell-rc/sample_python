class App():
    def __init__(self):
        self.var1 = 15
        self.var2 = 15

    def calculate(self):
        self.result = self.var1 * 4 + 2

    def retrieve(self):
        return self.result

    def calculate2(self):
        self.result2 = self.var2 * 4 - 2
        
    def retrieve2(self):
        return self.result2
        
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
    
    app.calculate2()
    print(app.retrieve2)
