class WasRun:
    def __init__(self, name):
        self.wasRun = None
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1


if __name__ == '__main__':
    test = WasRun("testMethod")
    print test.wasRun
    test.run()
    print test.wasRun
