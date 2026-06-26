class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append( (timestamp, value) )
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        dic = self.timemap[key]
        idx = len(dic)-1
        while dic[idx][0] > timestamp and idx >= 0:
            idx -= 1
        if idx == -1:
            return ""
        return dic[idx][1]
