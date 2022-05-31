from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from ast import Try

class IAbiturients(ABC):
    @abstractproperty
    def filename():
        pass

class Abiturients(IAbiturients):
    filename = str("")
    def __init__(self, filename: str) -> None:
        self.filename = filename

class SafeAbiturients(IAbiturients):
    filename = str("")
    def __init__(self, filename: str) -> None:
        try:
            self.filename = Abiturients(filename).filename
        except print(0):
            pass
