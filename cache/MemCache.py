memCache = None


def getMemCache():
    global memCache
    if memCache is None:
        memCache = MemCache()
    return memCache


class MemCache:
    def __init__(self):
        pass

    def getValueByName(self, vName: str, forceCache=False, func=None, *args):
        try:
            v = self.__getattribute__(vName)
        except AttributeError:
            v = None
        if forceCache:
            v = func(args)
            self.setValueByName(vName, v)

        return v

    def setValueByName(self, vName: str, value):
        self.__setattr__(vName, value)
