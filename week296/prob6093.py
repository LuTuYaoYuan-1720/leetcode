# coding:utf-8

class TextEditor:

    def __init__(self):
        self.cursor = 0
        self.text = ''

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor = self.cursor + len(text)

    def deleteText(self, k: int) -> int:
        if k <= self.cursor:
            self.text = self.text[:self.cursor - k] + self.text[self.cursor:]
            self.cursor = self.cursor - k
            return k
        else:
            self.text = self.text[self.cursor:]
            l = self.cursor
            self.cursor = 0
            return l

    def cursorLeft(self, k: int) -> str:
        if k <= self.cursor:
            self.cursor = self.cursor - k

            if self.cursor >= 10:
                idx = self.cursor - 10
            else:
                idx = 0
            res = self.text[idx: self.cursor]

            return res
        # 越界
        else:
            self.cursor = 0
            return ''

    def cursorRight(self, k: int) -> str:
        # 越界
        if k > len(self.text) - self.cursor:
            self.cursor = len(self.text)

            if self.cursor >= 10:
                idx = self.cursor - 10
            else:
                idx = 0

            res = self.text[idx:self.cursor]

            return res
        else:
            self.cursor = self.cursor + k
            if self.cursor >= 10:
                idx = self.cursor - 10
            else:
                idx = 0
            res = self.text[idx:self.cursor]

            return res


s = TextEditor()
s.addText('leetcode')
s.deleteText(4)
s.addText('practice')
s.cursorRight(3)
s.cursorLeft(8)
s.deleteText(10)
s.cursorLeft(2)
s.cursorRight(6)
