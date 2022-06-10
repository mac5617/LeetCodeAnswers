class OrderedStream:

    def __init__(self, n: int):
        self.list = [None]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        ret = []
        while self.pointer < len(self.list) and self.list[self.pointer] is not None:
            ret.append(self.list[self.pointer])
            self.pointer+=1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)