class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        pairs = self.store[key]
        l = 0
        r = len(pairs) - 1
        res = ""
        while l <= r:
            m = (l + r) >> 1
            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m + 1
            else:
                r = m - 1
        return res