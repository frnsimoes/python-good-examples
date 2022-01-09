# brandon rhodes, when python practices go wrong

class Mock:
    def __init__(self):
        self.calls = []

    def __getattr__(self, name):
        def fake_method(*args):
            self.calls.append((name, args))
        return fake_method


"""

Problems:
- Mock encourages tests that are not really tests.
    The ideal is to have unit tests and integration tests.
    Mocks encourages tests in cenaries that can't exists.
- Tests start to lose signal when Mock becomes routine instead of a reluctant workaround.
    The problem is that we know how to use it, but don't know when to use it. 

"""
