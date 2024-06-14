# fje/styles/tree_style.py
from .style_interface import IStyle


class TreeStyle(IStyle):
    def draw(self, container):
        length = len(container.children) - 1
        for i in range(length):
            self._draw(self,container.children[i], "├")
        self._draw(self, container.children[length], "└")

    def _draw(self, container, prefix):
        print(prefix + "─" + container.icon + container.name)
        if container.is_container == True:
            if prefix[-1] == "├":
                prefix_child = prefix[:-1] + "|" + "  "
            else:
                prefix_child = prefix[:-1] + " " + "  "
            length = len(container.children) - 1
            for i in range(length):
                self._draw(self, container.children[i], prefix_child + "├")
            self._draw(self, container.children[length], prefix_child + "└")
