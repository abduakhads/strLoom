class Text:
    def __init__(self, input_text: str) -> None:
        self.text = input_text
    
    def replace(self, a: str, b: str) -> None:
        self.text = self.text.replace(a, b)
    
    def remove(self, x: str) -> None:
        self.text = self.text.replace(x, "")
    
    def filtLen(self, n: int, sep: str) -> None:
        if '\\n' in sep:
            sep = sep.replace('\\n', '\n')
        if n > 0:
            filtered = [word for word in self.text.split() if len(word) <= n]
            self.text = sep.join(filtered)
        elif n < 0:
            filtered = [word for word in self.text.split() if len(word) >= (-1 * n)]
            self.text = sep.join(filtered)
        elif n == 0:
            pass

    def getText(self) -> str:
        return self.text