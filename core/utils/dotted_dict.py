class DottedDict(dict):
    __slots__ = ()

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, name, value):
        self[name] = value
