from threading import Condition, Thread
from typing import Callable

def printFirst():
    print('first', end="")

def printSecond():
    print('second', end="")

def printThird():
    print('third')

class Foo:
    def __init__(self):
        self.condition1 = Condition()
        self.condition2 = Condition()
        self.first_done = False
        self.second_done = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition1:
            printFirst()
            self.first_done = True
            self.condition1.notify()
        


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition1:
            self.condition1.wait_for(lambda: self.first_done)
            with self.condition2:
                printSecond()
                self.second_done = True
                self.condition2.notify()

    def third(self, printThird: Callable[[], None]) -> None:
        with self.condition2:
            self.condition2.wait_for(lambda: self.second_done)
            printThird()


foo = Foo()
thread1 = Thread(target = foo.first, args = (printFirst, ))
thread1.start()
thread3 = Thread(target = foo.third, args = (printThird, ))
thread3.start()
thread2 = Thread(target = foo.second, args = (printSecond, ))
thread2.start()