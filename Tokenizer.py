class Tokenizer:
    def __init__(self, s: str):
        self._s = s
        self._cursor = 0

    def hasMoreToken(self) -> bool:
        return self._cursor < len(self._s)

    def getNextToken(self):
        if not self.hasMoreToken():
            return None

        # Bracket
        

