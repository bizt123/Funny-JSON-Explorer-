# fje/styles/style_interface.py

from abc import ABC, abstractmethod

class IStyle(ABC):
    @abstractmethod
    def draw(self, container):
        pass
