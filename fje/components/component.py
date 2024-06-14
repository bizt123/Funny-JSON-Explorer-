# fje/components/components.py
from abc import ABC, abstractmethod

class Component(ABC):
    icon = ""
    name = ""
    is_container = False
    @abstractmethod
    def draw(self, is_leaf):
        pass
