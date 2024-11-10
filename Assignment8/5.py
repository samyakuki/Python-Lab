class StringProcessor:
    def getString(self):
        self.s = input("write the string")

    def printString(self):
        print(self.s.upper())

def test():
    processor = StringProcessor()
    processor.getString()
    processor.printString()

test()
