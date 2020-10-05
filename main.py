class WasRun:
    def __init__(self, name):
        self.wasRun = None


if __name__ == '__main__':
    test = WasRun("testMethod")
    print test.wasRun
    test.testMethod()
    print test.wasRun
