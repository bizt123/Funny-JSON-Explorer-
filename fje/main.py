# fje/main.py
from explorer import FunnyJsonExplorer

if __name__ == "__main__":
    json_file = "data/sample.json"
    styles = ["TreeStyle", "RectangleStyle"]
    icon_familys = ["PokerFaceIconFamily", "DefaultIconFamily"]

    for style in styles:
        for icon_family in icon_familys:
            fje = FunnyJsonExplorer(json_file, style, icon_family)
            fje.load()
            fje.show()
