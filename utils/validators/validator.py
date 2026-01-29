from abc import ABCMeta, abstractmethod


class IValidator(metaclass=ABCMeta):
    @abstractmethod
    def isValid(self):
        pass
