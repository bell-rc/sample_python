import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test1(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)
    
    def test2(self):
        app = App()
        app.calculate2()
        self.failIf(app.retrieve2() != 58)

    def test3(self):
        app = App()
        app.calculate3()
        self.failIf(app.retrieve3() != 64)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
