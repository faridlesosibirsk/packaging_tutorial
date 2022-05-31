from abc import abstractmethod
from ast import Break
from fileinput import filename
from sys import argv as arguments
from abc import ABC

class IApplication(ABC):
    @abstractmethod
    def fileName() -> str:
        pass

class Application(IApplication, Exception):
    def fileName() -> str:
        return arguments[1]

class SafeApplication(IApplication):
    def fileName() -> str:
        try:
            return Application.fileName()
        except IndexError as err:
            print("Oops!", err)
        finally:
            Break
