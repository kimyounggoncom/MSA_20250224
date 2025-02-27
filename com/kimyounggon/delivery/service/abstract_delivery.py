from abc import ABCMeta, abstractmethod


class AbstractDelivery(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, **kwargs):
        pass