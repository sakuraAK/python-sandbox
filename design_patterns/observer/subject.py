from abc import ABC
from observer import AbsObserver


class AbsSubject(object):
    # __metaclass__ = abc.ABCMeta
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Type is not supported')
        self._observers.add(observer)

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self):
        for observer in self._observers:
            observer.update()
            # if value is None:
            #     observer.update()
            # else:
            #     observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()
