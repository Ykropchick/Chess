class Color:
    def __init__(self):
        self.color = "w"

    def get(self):
        return self.color

    def swap(self):
        if self.color == "w":
            self.color = "b"
        else:
            self.color = "w"
        return self.color
