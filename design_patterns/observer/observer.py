from abc import ABC, abstractmethod


class AbsObserver(ABC):
    # __metaclass__ = abc.ABCMeta

    @abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass
