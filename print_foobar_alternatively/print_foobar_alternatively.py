from threading import Condition, Thread
from typing import Callable, Optional

def printFoo():
    print('foo', end="")

def printBar():
    print('bar', end="")

class FooBar:
    def __init__(self, n: int) -> None:
        self.n = n
        self.condition = Condition()
        self.last_printed: Optional[str] = None

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.last_printed in (None, 'bar'))
                printFoo()
                self.last_printed = 'foo'
                self.condition.notify()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.last_printed == 'foo')
                printBar()
                self.last_printed = 'bar'
                self.condition.notify()


foobar = FooBar(3)
thread1 = Thread(target = foobar.foo, args = (printFoo, ))
thread1.start()
thread2 = Thread(target = foobar.bar, args = (printBar, ))
thread2.start()
