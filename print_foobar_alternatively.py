from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        self.foolock.acquire()

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.barlock.acquire()
            printFoo()
            self.foolock.release()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.foolock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barlock.release()
