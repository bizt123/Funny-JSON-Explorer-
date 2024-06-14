# fje/styles/rectangle_style.py
from .style_interface import IStyle


class RectangleStyle(IStyle):
    RectangleLength = 10
    Outstream = []

    def draw(self, container):
        self.Outstream = []
        for ch in container.children:
            self._draw(self,ch, "")
        self.upd_length(self,self.RectangleLength)
        self.Outstream[0] = self.Outstream[0].replace("├", "┌").replace("┤", "┐")
        pos = self.Outstream[-1].find("├")
        self.Outstream[-1] = self.Outstream[-1][:pos].replace(" ", "─").replace(
            "│", "┴"
        ) + self.Outstream[-1][pos:].replace("├", "┴").replace("┤", "┘")
        self.Outstream[-1] = "└" + self.Outstream[-1][1:]
        print("\n".join(self.Outstream))

    def _draw(self, container, prefix):
        self.__append_outstream(self,prefix, container.icon + container.name)
        if container.is_container == True:
            for child in container.children:
                self._draw(self,child, prefix + "│  ")

    def upd_length(self, new_length):
        if self.RectangleLength <= new_length:
            for i, outstr in enumerate(self.Outstream):
                delta = new_length - len(outstr)
                self.Outstream[i] = outstr[:-1] + "─" * delta + outstr[-1]
            self.RectangleLength = new_length

    def __append_outstream(self, prefix: str, middle_str: str):
        front_str = prefix + "├─" + middle_str + " "
        self.RectangleLength = max(len(front_str) + 1 + 5, self.RectangleLength)
        self.Outstream.append(
            front_str + "─" * (self.RectangleLength - len(front_str) - 1) + "┤"
        )
