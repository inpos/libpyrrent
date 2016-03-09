class AttrDict(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[attr] = value

class Enum(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        pass
    def __setitem__(self, k, v):
        pass
